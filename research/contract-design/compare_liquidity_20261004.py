"""Recompute descriptive liquidity statistics; aggregate-price proxies are not causal impact."""
import csv
import json
from decimal import Decimal as D
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parent


def read(name):
    with (ROOT / 'data' / name).open(newline='') as stream:
        return [r for r in csv.DictReader(stream) if '2025-03-07' <= r['date'] <= '2025-12-31']


def describe(rows, volume, amount, price):
    pairs = [(x, y) for x, y in zip(rows, rows[1:]) if D(x[volume]) > 0 and D(y[volume]) > 0]
    # Simple returns in decimal units; value traded is scaled to RMB one million.
    proxies = [abs(D(y[price]) / D(x[price]) - 1) / (D(y[amount]) / D(1000000)) for x, y in pairs]
    volumes = [D(r[volume]) for r in rows]
    total = sum(volumes)
    return {
        'days': len(rows),
        'volume_tons': str(total),
        'amount_yuan': str(sum(D(r[amount]) for r in rows)),
        'median_volume_tons': str(median(volumes)),
        'zero_volume_days': sum(v == 0 for v in volumes),
        'positive_volume_le_1000_days': sum(0 < v <= 1000 for v in volumes),
        'top10_volume_share_pct': str(sum(sorted(volumes, reverse=True)[:10]) / total * 100),
        'q4_volume_share_pct': str(sum(D(r[volume]) for r in rows if r['date'] >= '2025-10-01') / total * 100),
        'valid_adjacent_trading_day_pairs': len(pairs),
        'zero_return_pairs': sum(D(x[price]) == D(y[price]) for x, y in pairs),
        'zero_return_pct': str(D(sum(D(x[price]) == D(y[price]) for x, y in pairs)) / len(pairs) * 100),
        'mechanical_amihud_proxy_mean_per_million_yuan': str(mean(proxies)),
        'mechanical_amihud_proxy_median_per_million_yuan': str(median(proxies)),
    }


cea = read('cea_daily_2025.csv')
ccer = read('ccer_daily_2025_secondary.csv')
assert [r['date'] for r in cea] == [r['date'] for r in ccer]
result = {
    'window': ['2025-03-07', '2025-12-31'],
    'limitations': [
        'CEA uses aggregate closing price and listed-trading value, not matched annual-grade price/value.',
        'CCER uses rounded cross-project daily mean price, not a homogeneous asset closing price.',
        'CCER secondary daily table remains short by 9020 tons and RMB 631490.20.',
        'Amihud numbers are mechanical diagnostics only; their ratio is not a liquidity ranking.',
        'Zero-return counts exclude pairs with zero listed volume on either day; no forward fill.',
    ],
    'CEA': describe(cea, 'listed_volume_ton', 'listed_amount_yuan', 'close_yuan_per_ton'),
    'CCER_secondary': describe(ccer, 'volume_ton', 'amount_yuan', 'mean_yuan_per_ton'),
}
output = ROOT / 'data' / 'liquidity_comparison_20261004.json'
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(result, ensure_ascii=False, indent=2))
