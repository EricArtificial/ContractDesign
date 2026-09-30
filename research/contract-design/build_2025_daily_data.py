"""Rebuild the 2025 CEA/CCER daily research CSVs from cited public pages.

CEA is taken from the Shanghai Environment and Energy Exchange's daily
bulletins. CCER is taken from CCN's transcription of the Beijing Green
Exchange's daily bulletins; the latter is a secondary source and is labelled
accordingly in the output. Run from the project root with network access.
"""

import csv
import html
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from urllib.parse import urljoin

import requests


OUT = Path("research/contract-design/data")
CEA_ROOT = "https://overview.cneeex.com"
CEA_INDEX = CEA_ROOT + "/qgtpfqjy/mrgk/2025n/"
CCER_TABLE = "https://www.ccn.ac.cn/carbon-market/ccer/ccerdate/219.html"
CCER_OFFICIAL_CORRECTIONS = {
    "2025-06-24": {
        "amount_yuan": "54720.20",
        "source_url": "https://www.ccer.com.cn/wcm/ccer/html/2502lshq/20250624/170135985.shtml",
    },
    "2025-07-01": {
        "volume_ton": "601",
        "source_url": "https://www.ccer.com.cn/wcm/ccer/html/2502lshq/20250701/170330466.shtml",
    },
}
SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "Mozilla/5.0 (compatible; academic-research/1.0)"})


def get(url):
    r = SESSION.get(url, timeout=35)
    r.raise_for_status()
    return r.content.decode("utf-8", "replace")


def plain(markup):
    return html.unescape(re.sub(r"<[^>]+>", " ", markup)).replace("\u3000", " ")


def number(s):
    return s.replace(",", "")


def match_number(pattern, s):
    m = re.search(pattern, s)
    return number(m.group(1)) if m else ""


def cea_index_urls():
    rows = {}
    page = 1
    while True:
        if page == 1:
            url = CEA_INDEX
        elif page <= 10:
            url = CEA_INDEX + f"index_{page}.shtml"
        else:
            url = CEA_ROOT + f"/zcms/ui/catalog/15464/pc/index_{page}.shtml"
        try:
            content = get(url)
        except requests.HTTPError as exc:
            if exc.response is not None and exc.response.status_code == 404 and page > 1:
                break
            raise
        links = re.findall(
            r'<a\s+href="((?:https://www\.cneeex\.com)?/c/(2025-\d\d-\d\d)/\d+\.shtml)"[^>]*>'
            r'[^<]*全国碳市场每日综合价格行情及成交信息(2025\d{4})</a>',
            content,
        )
        if not links:
            raise ValueError(f"No CEA daily links on {url}")
        for href, date, title_date in links:
            if date.replace("-", "") != title_date:
                raise ValueError(f"Date mismatch: {href} {title_date}")
            rows[date] = CEA_ROOT + re.sub(r"^https://www\.cneeex\.com", "", href)
        print("CEA index", page, "unique days", len(rows), flush=True)
        if f"index_{page + 1}.shtml" not in content:
            break
        page += 1
    return rows


def cea_day(item):
    date, url = item
    content = plain(get(url))
    start = content.find("今日全国碳")
    end = content.find("声明", start)
    if start == -1:
        raise ValueError(f"No daily prose: {url}")
    prose = content[start:end if end > start else None]
    prose = re.sub(r"(?<=[\d,.])\s+(?=[\d,.])", "", prose)
    prose = re.sub(r"交易\s+成交量|总\s+成交额", lambda m: m.group().replace(" ", ""), prose)
    p = r"([\d,]+(?:\.\d+)?)"
    fields = {
        "date": date,
        "close_yuan_per_ton": match_number(r"收盘价" + p + r"元/吨", prose),
        "listed_volume_ton": match_number(r"挂牌协议交易成交量" + p + r"吨", prose),
        "listed_amount_yuan": match_number(r"挂牌协议交易成交量[\d,]+吨[，,]\s*成交额" + p + r"元", prose),
        "block_volume_ton": match_number(r"大宗协议交易成交量" + p + r"吨", prose),
        "block_amount_yuan": match_number(r"大宗协议交易成交量[\d,]+吨[，,]\s*成交额" + p + r"元", prose),
        "auction_volume_ton": match_number(r"单向竞价(?:交易)?成交量" + p + r"吨", prose),
        "auction_amount_yuan": match_number(r"单向竞价(?:交易)?成交量[\d,]+吨[，,]\s*成交额" + p + r"元", prose),
        "total_volume_ton": match_number(r"总成交量" + p + r"吨", prose),
        "total_amount_yuan": match_number(r"总成交额" + p + r"元", prose),
        "has_trade": "0" if "今日全国碳市场无成交" in prose else "1",
        "source_url": url,
    }
    if fields["has_trade"] == "0":
        for kind in ("listed", "block", "auction", "total"):
            fields[kind + "_volume_ton"] = "0"
            fields[kind + "_amount_yuan"] = "0"
    for kind in ("listed", "block", "auction"):
        if not fields[kind + "_volume_ton"] and fields["has_trade"] == "1":
            fields[kind + "_volume_ton"] = "0" if kind == "auction" and "无单向竞价" in prose else ""
            if fields[kind + "_volume_ton"] == "0":
                fields[kind + "_amount_yuan"] = "0"
    if any(not fields[k] for k in ("total_volume_ton", "total_amount_yuan", "close_yuan_per_ton")):
        raise ValueError(f"Missing CEA field: {date} {url}")
    for suffix, total in (("volume_ton", "total_volume_ton"), ("amount_yuan", "total_amount_yuan")):
        components = [kind + "_" + suffix for kind in ("listed", "block", "auction")]
        observed = sum(Decimal(fields[k]) for k in components if fields[k])
        if observed != Decimal(fields[total]):
            raise ValueError(f"CEA component sum mismatch: {date} {suffix} {url}")
        for key in components:
            if not fields[key]:
                fields[key] = "0"
    return fields


def ccer_rows():
    content = get(CCER_TABLE)
    table = re.search(r"<table[^>]*><tbody>(.*?)</tbody></table>", content, re.S)
    if not table:
        raise ValueError("CCER table missing")
    output = []
    for row in re.findall(r"<tr>(.*?)</tr>", table.group(1), re.S):
        cells = [plain(c).strip() for c in re.findall(r"<td>(.*?)</td>", row, re.S)]
        if len(cells) < 4 or not cells[0].startswith("2025/"):
            continue
        date = datetime.strptime(cells[0], "%Y/%m/%d").date().isoformat()
        output.append({
            "date": date,
            "volume_ton": number(cells[1]),
            "amount_yuan": number(cells[2]),
            "mean_yuan_per_ton": number(cells[3]),
            "source_url": CCER_TABLE,
            "source_level": "secondary_transcription",
        })
        if date in CCER_OFFICIAL_CORRECTIONS:
            output[-1].update(CCER_OFFICIAL_CORRECTIONS[date])
            output[-1]["source_level"] = "official_correction"
    dates = [r["date"] for r in output]
    if len(dates) != len(set(dates)):
        raise ValueError("Duplicate CCER date")
    return sorted(output, key=lambda x: x["date"])


def write_csv(name, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / name).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    urls = cea_index_urls()
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = [pool.submit(cea_day, item) for item in urls.items()]
        cea = [future.result() for future in as_completed(futures)]
    cea.sort(key=lambda x: x["date"])
    ccer = ccer_rows()
    write_csv("cea_daily_2025.csv", cea)
    write_csv("ccer_daily_2025_secondary.csv", ccer)
    for name, rows, vol, amt in [
        ("CEA", cea, "total_volume_ton", "total_amount_yuan"),
        ("CCER", ccer, "volume_ton", "amount_yuan"),
    ]:
        missing = [r["date"] for r in rows if not r[vol] or not r[amt]]
        print(name, "rows", len(rows), "missing volume/amount", missing)
        print(name, "volume", sum(int(r[vol]) for r in rows if r[vol]))
        print(name, "amount", sum(Decimal(r[amt]) for r in rows if r[amt]))


if __name__ == "__main__":
    main()
