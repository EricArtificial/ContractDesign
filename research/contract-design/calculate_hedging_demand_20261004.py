"""Reproduce descriptive CEA compliance-demand indicators; no futures forecast."""
import csv
import json
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
rows = list(csv.DictReader((ROOT / 'data/cea_daily_2025.csv').open()))
assert len(rows) == 243 and len({r['date'] for r in rows}) == 243
result = {'observation_year': 2025, 'trading_days': len(rows), 'transaction_metrics': {}}
for field in ['total_volume_ton', 'listed_volume_ton', 'block_volume_ton', 'auction_volume_ton']:
    monthly = {str(m): sum(Decimal(r[field]) for r in rows if int(r['date'][5:7]) == m) for m in range(1, 13)}
    total = sum(monthly.values())
    q4 = sum(monthly[str(m)] for m in [10, 11, 12])
    result['transaction_metrics'][field] = {
        'annual_ton': int(total), 'monthly_ton': {m: int(v) for m, v in monthly.items()},
        'q4_ton': int(q4), 'q4_share': float(q4 / total),
        'nov_dec_share': float((monthly['11'] + monthly['12']) / total),
        'dec_share': float(monthly['12'] / total),
        'interpretation': 'Gross market transactions, not identified deficit-firm procurement.'
    }
assert result['transaction_metrics']['total_volume_ton']['annual_ton'] == 234597856
result['first_compliance_period_2019_2020'] = {
    'deficit_firms': 847, 'listed_firms': 2162, 'actually_allocated_firms': 2011,
    'deficit_share_listed': 847 / 2162, 'deficit_share_actually_allocated': 847 / 2011,
    'gross_deficit_ton_approx': 188000000,
    'mean_gross_deficit_ton_approx': 188000000 / 847,
    'ccer_used_ton_approx': 32730000,
    'gross_deficit_less_all_ccer_ton_illustrative': 188000000 - 32730000,
    'warning': 'Two emission years. CCER recipient overlap, holdings and final settlement adjustments unavailable; residual is not observed procurement.'
}
result['changyuan_announced_20260924'] = {
    'compliance_emission_year': 2025, 'planned_purchase_year': 2026,
    'deficit_after_carryover_ton_approx': 511200,
    'planned_budget_yuan_range': [45000000, 70000000],
    'cost_increase_yuan_if_price_rises_10': 5112000,
    'contracts_at_1000_ton_illustrative': 511.2,
    'warning': 'Company estimate and authorized plan, not completed purchase or futures participation.'
}
output = ROOT / 'data/hedging_demand_20261004.json'
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(output)
print('2025 Q4 share: {:.4%}'.format(result['transaction_metrics']['total_volume_ton']['q4_share']))
