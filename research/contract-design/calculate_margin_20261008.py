"""Historical spot diagnostics and cash ledgers for proposed CEA futures margins."""
import csv, json, math, hashlib
from decimal import Decimal as D
from pathlib import Path
ROOT=Path(__file__).parent
source=ROOT/'data/cea_daily_2025.csv'
rows=list(csv.DictReader(source.open()))
historical={}
for horizon in [1,2,3]:
    windows=[]
    for i in range(horizon,len(rows)):
        w=rows[i-horizon:i+1]
        if all(int(z['listed_volume_ton'])>0 for z in w):
            windows.append({'start':w[0]['date'],'end':w[-1]['date'],
                'return_pct':float((D(w[-1]['close_yuan_per_ton'])/D(w[0]['close_yuan_per_ton'])-1)*100)})
    historical[str(horizon)]={}
    for label,part in [('all',windows),('Q1_Q3',[x for x in windows if x['end']<'2025-10-01']),('Q4',[x for x in windows if x['end']>='2025-10-01'])]:
        absolute=sorted(abs(x['return_pct']) for x in part)
        historical[str(horizon)][label]={'n':len(part),
            'abs_q99_pct_nearest_rank':absolute[math.ceil(.99*len(part))-1],
            'max_abs_window':max(part,key=lambda x:abs(x['return_pct'])),
            'exceedances':{str(k):sum(x>k for x in absolute) for k in [6,8,10,12,15,20]}}

P0,U=D('74.63'),D('1000')
ledgers=[]
for label,base_limit,base_margin in [('ordinary',D('.06'),D('.08')),('Q4',D('.10'),D('.12'))]:
    limits=[base_limit,base_limit+D('.03'),base_limit+D('.05')]
    for side in ['short_rising','long_falling']:
        p=P0; cash=P0*U*base_margin; initial=cash; injections=D(0); loss_total=D(0); daily=[]
        for i,limit in enumerate(limits):
            new_p=p*(1+limit if side=='short_rising' else 1-limit)
            loss=abs(new_p-p)*U
            # At D1/D2 settlement collect the following day's applicable margin.
            # After D3 hold its rate pending the exchange's special action; no assumed release.
            next_limit=limits[min(i+1,2)]
            rate=max(base_margin,next_limit+D('.02'))
            required=new_p*U*rate
            after_loss=cash-loss
            call=max(D(0),required-after_loss)
            cash=after_loss+call
            injections+=call; loss_total+=loss
            daily.append({'day':i+1,'settlement_price':str(new_p),'limit_pct':str(limit*100),
                'loss_yuan':str(loss),'margin_rate_collected_pct':str(rate*100),
                'required_margin_yuan':str(required),'equity_before_call_yuan':str(after_loss),
                'cash_call_yuan':str(call),'equity_after_call_yuan':str(cash)})
            assert cash>=required
            p=new_p
        assert initial+injections==loss_total+cash
        ledgers.append({'case':label+'_'+side,'initial_margin_yuan':str(initial),
            'daily':daily,'cumulative_loss_yuan':str(loss_total),
            'additional_cash_total_yuan':str(injections),'retained_equity_yuan':str(cash),
            'total_initial_and_added_cash_yuan':str(initial+injections),
            'cash_identity_verified':True})

result={'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'price_definition':'2025 aggregate CEA spot close, not futures settlement',
    'window':[rows[0]['date'],rows[-1]['date']],
    'historical_filter':'Consecutive official trading-day rows, all dates with positive listed volume, overlapping windows; group by endpoint date',
    'liquidation_horizon_assumption':'Two trading days for initial comparison; not evidence that liquidation is possible within two days',
    'historical':historical,'proposal':{'base_pct':8,'Q4_pct':12,'T_minus_5_and_later_pct':20,
        'one_lot_amount_at_74_63':{str(k):str(P0*U*D(k)/100) for k in [8,12,20]}},
    'ledger_assumptions':'One lot; no fees, tax, interest or extra cash initially; exact arithmetic without tick rounding; all calls paid before next open; D3 margin held pending special action; no position liquidation assumed',
    'stress_ledgers':ledgers,
    'no_call_short_two_up_limits':[
        {'case':name,'initial_margin_pct':str(m*100),
         'two_day_loss_pct':str(((1+l)*(1+l+D('.03'))-1)*100),
         'equity_after_two_days_yuan':str((m-((1+l)*(1+l+D('.03'))-1))*P0*U)}
        for name,l,m in [('ordinary',D('.06'),D('.08')),('Q4',D('.10'),D('.12')),('Q4_near_expiry',D('.10'),D('.20'))]]
    }
(ROOT/'data/margin_20261008.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'proposal':result['proposal'],'ledgers':[{k:x[k] for k in ['case','initial_margin_yuan','cumulative_loss_yuan','additional_cash_total_yuan','retained_equity_yuan']} for x in ledgers]},ensure_ascii=False,indent=2))
