"""Compute CEA price-change SD from adjacent trading days with listed trades."""
import csv
import json
import statistics
from pathlib import Path

DATA = Path(__file__).parent / 'data'
with (DATA / 'cea_daily_2025.csv').open() as source:
    rows = list(csv.DictReader(source))
changes = [
    float(current['close_yuan_per_ton']) - float(previous['close_yuan_per_ton'])
    for previous, current in zip(rows, rows[1:])
    if int(previous['listed_volume_ton']) > 0
    and int(current['listed_volume_ton']) > 0
]
result = {
    'window': [rows[0]['date'], rows[-1]['date']],
    'source_rows': len(rows),
    'valid_adjacent_trading_day_pairs': len(changes),
    'price_definition': 'CEA aggregate closing price',
    'filter': 'Both adjacent trading days have positive listed trading volume; no bridging or filling.',
    'statistic': 'Sample SD of current minus previous closing price, denominator n-1',
    'unit': 'yuan per ton',
    'price_change_sample_sd': statistics.stdev(changes),
}
output = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
(DATA / 'cea_price_risk_20261004.json').write_text(output)
print(output)
