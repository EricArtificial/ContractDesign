"""Descriptive daily changes and quadratic time-trend residuals, common 2025 window."""
import csv
import json
from pathlib import Path
import numpy as np

DATA = Path(__file__).resolve().parent / 'data'
WINDOW = ('2025-03-07', '2025-12-31')

def calculate(filename, price_key, volume_key):
    with (DATA / filename).open(newline='') as source:
        rows = [r for r in csv.DictReader(source) if WINDOW[0] <= r['date'] <= WINDOW[1]]
    pairs = [(a, b) for a, b in zip(rows, rows[1:])
             if float(a[volume_key]) > 0 and float(b[volume_key]) > 0]
    changes = np.array([float(b[price_key]) - float(a[price_key]) for a, b in pairs])
    # Retain original trading-day indices; exclude zero-volume prices from OLS.
    selected = [(i, float(r[price_key])) for i, r in enumerate(rows)
                if float(r[volume_key]) > 0]
    # Center and scale time for numerical stability; same span as 1,t,t^2.
    time = np.array([i for i, _ in selected], dtype=float)
    center, scale = float(time.mean()), float(time.std())
    z = (time - center) / scale
    prices = np.array([price for _, price in selected])
    design = np.column_stack([np.ones(len(z)), z, z*z])
    coefficients, _, rank, _ = np.linalg.lstsq(design, prices, rcond=None)
    fitted = design @ coefficients
    residuals = prices - fitted
    if rank != 3 or np.any(fitted <= 0):
        raise ValueError('Quadratic trend is rank deficient or has nonpositive fitted prices.')
    return {
        'window_trading_days': len(rows),
        'valid_adjacent_trading_day_pairs': len(pairs),
        'daily_price_change_sd_yuan_per_ton': float(changes.std(ddof=1)),
        'regression_observations': len(prices),
        'time_center': center, 'time_scale': scale,
        'coefficients_in_centered_scaled_time': coefficients.tolist(),
        'minimum_fitted_price': float(fitted.min()),
        'sample_mean_price_yuan_per_ton': float(prices.mean()),
        'residual_sample_sd_yuan_per_ton': float(residuals.std(ddof=1)),
        'sd_residual_over_mean_price_pct': float(residuals.std(ddof=1)/prices.mean()*100),
        'normal_equation_max_absolute_error': float(np.max(np.abs(design.T @ residuals))),
    }

result = {
    'window': WINDOW,
    'regression': 'OLS P_t = alpha + beta*t + gamma*t^2; t is original trading-day index',
    'sample_filter': 'Daily changes require positive volume on both adjacent trading days; regression excludes zero-volume days without renumbering time.',
    'relative_residual_definition': 'User confirmed: SD(residual)/sample mean price, reported in percent.',
    'dispersion_denominator': 'n-1 for descriptive sample standard deviations; not regression standard error n-3',
    'CEA': calculate('cea_daily_2025.csv', 'close_yuan_per_ton', 'listed_volume_ton'),
    'CCER_secondary': calculate('ccer_daily_2025_secondary.csv', 'mean_yuan_per_ton', 'volume_ton'),
    'interpretation': 'Residual level dispersion around a fitted trend, not daily return volatility or risk after hedging. CEA/CCER price definitions differ.',
}
output = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
(DATA / 'detrended_price_risk_20261004.json').write_text(output)
print(output)
