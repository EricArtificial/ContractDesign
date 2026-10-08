"""CEA spot diagnostic and proposed limit scenarios; no simulated futures order book."""
import csv, json, math, hashlib
from decimal import Decimal as D, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).parent
SOURCE = ROOT / 'data/cea_daily_2025.csv'
rows = list(csv.DictReader(SOURCE.open()))

def pair(a, b):
    return {'previous_date': a['date'], 'date': b['date'],
            'previous_price': a['close_yuan_per_ton'], 'price': b['close_yuan_per_ton'],
            'return_pct': float((D(b['close_yuan_per_ton']) / D(a['close_yuan_per_ton']) - 1) * 100),
            'source_url': b['source_url']}

valid = [pair(a,b) for a,b in zip(rows,rows[1:])
         if int(a['listed_volume_ton']) > 0 and int(b['listed_volume_ton']) > 0]
all_pairs = [pair(a,b) for a,b in zip(rows,rows[1:])]
traded = [r for r in rows if int(r['listed_volume_ton']) > 0]
bridged = [pair(a,b) for a,b in zip(traded,traded[1:])]

def stats(sample):
    absolute = sorted(abs(r['return_pct']) for r in sample)
    return {'n':len(sample), 'abs_return_q95_pct':absolute[math.ceil(.95*len(sample))-1],
            'abs_return_q99_pct':absolute[math.ceil(.99*len(sample))-1],
            'maximum_abs_return':max(sample,key=lambda r:abs(r['return_pct'])),
            'minimum_return_pct':min(r['return_pct'] for r in sample),
            'exceedance_counts': {str(k):sum(x>k for x in absolute) for k in [4,5,6,8,10]},
            'at_or_above_counts': {str(k):sum(x>=k for x in absolute) for k in [4,5,6,8,10]}}

stress=[]
for normal in [D('.06'),D('.10')]:
    limits=[normal,normal+D('.03'),normal+D('.05')]
    up=down=D(1)
    for x in limits:
        up*=1+x
        down*=1-x
    stress.append({'daily_limits_pct':[str(x*100) for x in limits],
                   'three_day_up_pct':str((up-1)*100),
                   'three_day_down_pct':str((down-1)*100),
                   'short_loss_yuan_per_lot_at_74_63':str((up-1)*D('74630')),
                   'long_loss_yuan_per_lot_at_74_63':str((1-down)*D('74630'))})

bounds=[]
for fraction in [D('.06'),D('.10')]:
    price, tick=D('74.63'),D('.01')
    upper=(price*(1+fraction)/tick).to_integral_value(rounding=ROUND_FLOOR)*tick
    lower=(price*(1-fraction)/tick).to_integral_value(rounding=ROUND_CEILING)*tick
    assert upper <= price*(1+fraction) and lower >= price*(1-fraction)
    bounds.append({'limit_pct':str(fraction*100),'reference_price':str(price),
                   'upper':str(upper),'lower':str(lower)})

result={'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'window':[rows[0]['date'],rows[-1]['date']], 'source_rows':len(rows),
        'price_definition':'2025 CEA aggregate spot closing price; not single-vintage futures settlement',
        'percentile_method':'nearest rank ceil(p*n)',
        'main_filter':'Adjacent rows in official trading-day calendar, both with positive listed volume; no filling or bridging',
        'main_all':stats(valid),
        'main_Q1_Q3':stats([r for r in valid if r['date']<'2025-10-01']),
        'main_Q4':stats([r for r in valid if r['date']>='2025-10-01']),
        'sensitivity_including_stale_closes':stats(all_pairs),
        'sensitivity_adjacent_traded_observations_may_bridge_days':stats(bridged),
        'stress_assumption':'Pure hypothetical sequential settlement at upper/lower bands, before tick rounding; no claim of actual limit-hit or close-out feasibility',
        'three_day_stresses':stress,'inward_rounding_examples':bounds}
output=ROOT/'data/price_limits_20261008.json'
output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['main_all','main_Q1_Q3','main_Q4','three_day_stresses','inward_rounding_examples']},ensure_ascii=False,indent=2))
