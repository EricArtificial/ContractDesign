"""Recheck existing step 1/2 evidence without network access or data edits.

Run from any directory with Python's standard library. Sensitivity scenarios
are hypothetical allocations, not corrections to the CCER source table.
"""
import csv
import hashlib
import json
import math
import statistics
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def read(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def summarize(values, dates):
    ordered = sorted(values)
    total = sum(values)
    return {
        "total_ton": total,
        "median_ton": statistics.median(values),
        "p90_nearest_rank_ton": ordered[math.ceil(len(values) * .9) - 1],
        "top10_share_pct": sum(ordered[-10:]) / total * 100,
        "q4_share_pct": sum(v for d, v in zip(dates, values) if d[5:7] >= "10") / total * 100,
        "days_at_most_1000_ton": sum(v <= 1000 for v in values),
    }


def main():
    cea_path = HERE / "data/cea_daily_2025.csv"
    ccer_path = HERE / "data/ccer_daily_2025_secondary.csv"
    csmar_path = ROOT / "CSMAR中国碳排放权交易信息表（日）/GF_CEMISSRIGHTTRADE.csv"
    cea, ccer = read(cea_path), read(ccer_path)
    assert len(cea) == len({r["date"] for r in cea}) == 243
    assert len(ccer) == len({r["date"] for r in ccer}) == 203
    for r in cea:
        for suffix in ("volume_ton", "amount_yuan"):
            assert sum(Decimal(r[k + "_" + suffix]) for k in ("listed", "block", "auction")) == Decimal(r["total_" + suffix])
    assert sum(Decimal(r["total_volume_ton"]) for r in cea) == Decimal("234597856")
    assert sum(Decimal(r["total_amount_yuan"]) for r in cea) == Decimal("14629891128.06")
    mapping = dict(zip(
        ("total_volume_ton", "total_amount_yuan", "close_yuan_per_ton", "listed_volume_ton", "listed_amount_yuan", "block_volume_ton", "block_amount_yuan", "auction_volume_ton", "auction_amount_yuan"),
        ("Volume", "Amount", "ClosePrice", "ListingVolume", "ListingAmount", "BulkVolume", "BulkAmount", "SingleBidVolume", "SingleBidAmount")))
    local = [r for r in read(csmar_path) if r["CityName"] == "中国" and r["TradingType"] == "CEA" and r["TradingDate"].startswith("2025-")]
    lookup = {r["TradingDate"]: r for r in local}
    assert len(local) == len(lookup) == 233
    blank_fields = {key: 0 for key in mapping.values()}
    for r in cea:
        if int(r["total_volume_ton"]):
            for key, other in mapping.items():
                value = lookup[r["date"]][other]
                if value == "":
                    # The official bulletin, not the CSMAR blank, establishes zero.
                    assert Decimal(r[key]) == 0
                    blank_fields[other] += 1
                else:
                    assert Decimal(r[key]) == Decimal(value)
        else:
            assert r["date"] not in lookup
    valid = [r for r in cea if int(r["listed_volume_ton"]) > 0]
    def median_change(pairs):
        values = [abs(float(b["close_yuan_per_ton"]) / float(a["close_yuan_per_ton"]) - 1) * 100 for a, b in pairs]
        return {"pairs": len(values), "median_absolute_change_pct": statistics.median(values)}
    consecutive = [(a, b) for a, b in zip(cea, cea[1:]) if int(a["listed_volume_ton"]) > 0 and int(b["listed_volume_ton"]) > 0]
    values = [int(r["volume_ton"]) for r in ccer]
    dates = [r["date"] for r in ccer]
    scenarios = []
    for day in ("2025-09-11", "2025-09-12"):
        altered = values.copy()
        altered[dates.index(day)] += 9020
        scenarios.append({"hypothetical_allocation_date": day, **summarize(altered, dates)})
    # All integer splits of the known volume difference across the suspect days.
    p90 = []
    for first in range(9021):
        altered = values.copy()
        altered[dates.index("2025-09-11")] += first
        altered[dates.index("2025-09-12")] += 9020 - first
        p90.append(sorted(altered)[math.ceil(len(values) * .9) - 1])
    result = {
        "date": "2026-10-03", "cea_checks": "PASS",
        "csmar_nonempty_fields_equal_official": "PASS",
        "csmar_blank_fields_corresponding_to_official_zero": blank_fields,
        "cea_zero_total_days": sum(int(r["total_volume_ton"]) == 0 for r in cea),
        "cea_zero_listed_days": sum(int(r["listed_volume_ton"]) == 0 for r in cea),
        "cea_price_changes_not_margin_calibration": {
            "successive_observations_after_dropping_zero_listed_days": median_change(list(zip(valid, valid[1:]))),
            "adjacent_exchange_days_with_listed_trade_on_both_days": median_change(consecutive)},
        "ccer_unallocated_volume_pct_of_official_year": 9020 / 8844114 * 100,
        "ccer_unallocated_amount_pct_of_official_year": 631490.20 / 625801436.80 * 100,
        "ccer_secondary_baseline": summarize(values, dates),
        "ccer_hypothetical_scenarios_not_data_corrections": scenarios,
        "ccer_p90_range_under_all_nonnegative_integer_splits": [min(p90), max(p90)],
        "sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in (cea_path, ccer_path, csmar_path)},
    }
    out = HERE / "data/completed_steps_check_20261003.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
