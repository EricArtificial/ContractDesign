"""Compare proposed quotation grids; arithmetic scenarios, not execution estimates."""
from decimal import Decimal
from pathlib import Path
import json

UNIT = Decimal('1000')
REFERENCE = Decimal('74.63')  # historical 2025 year-end price, not current price
rows = []
for value in ['0.001', '0.01', '0.05', '0.10']:
    tick = Decimal(value)
    rows.append({
        'tick_yuan_per_ton': str(tick),
        'tick_value_yuan_per_lot': str(tick * UNIT),
        'tick_as_percent_of_reference_price': str(tick / REFERENCE * 100),
        'nearest_grid_rounding_bound_yuan_per_ton': str(tick / 2),
        'nearest_grid_rounding_bound_yuan_per_lot': str(tick / 2 * UNIT),
    })
result = {
    'contract_unit_ton': str(UNIT),
    'historical_reference_price_yuan_per_ton': str(REFERENCE),
    'reference_source': 'mee2026: 2025 year-end CEA closing price',
    'rounding_assumption': 'Arbitrary continuous target price rounded to nearest grid point; bound is not a realized execution cost, bid-ask spread, or fee.',
    'candidates': rows,
    'selected_tick_yuan_per_ton': '0.01',
}
Path(__file__).with_name('data').joinpath('tick_size_20261008.json').write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(result, ensure_ascii=False, indent=2))
