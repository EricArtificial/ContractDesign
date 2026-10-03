"""Reproduce the three-panel 2025 liquidity figure from the research CSVs.

Requires matplotlib==3.10.8 and numpy==2.4.0. No network access is used.
Run with any configured Python containing these packages, from any directory.
"""

from pathlib import Path
import os

os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/contract-design-matplotlib")

import csv
import json
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.lines import Line2D
from matplotlib.ticker import FixedLocator, NullLocator
import numpy as np


HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
START, END = "2025-03-07", "2025-12-31"
COLORS = {"CEA": "#20B795", "CCER": "#EE7B19"}
STYLES = {"CEA": "-", "CCER": (0, (4, 2))}
FIGURE_SIZE = (8.4, 2.8)


def load(file, volume_col):
    with (DATA / file).open(encoding="utf-8-sig", newline="") as stream:
        rows = [r for r in csv.DictReader(stream) if START <= r["date"] <= END]
    dates = [r["date"] for r in rows]
    if dates != sorted(set(dates)):
        raise ValueError("Dates must be unique and increasing")
    return dates, np.array([int(r[volume_col]) for r in rows], dtype=np.int64)


def main():
    cea_dates, cea = load("cea_daily_2025.csv", "listed_volume_ton")
    ccer_dates, ccer = load("ccer_daily_2025_secondary.csv", "volume_ton")
    if cea_dates != ccer_dates or len(cea_dates) != 203:
        raise ValueError("The two samples must have the same 203 dates")
    series = {"CEA": cea, "CCER": ccer}
    metrics = {}
    monthly = {}
    for name, values in series.items():
        totals = defaultdict(int)
        for date, value in zip(cea_dates, values):
            totals[int(date[5:7])] += int(value)
        monthly[name] = np.array([totals[m] for m in range(3, 13)]) / values.sum() * 100
        metrics[name] = {
            "observations": len(values),
            "total_tons": int(values.sum()),
            "median_tons": float(np.median(values)),
            "zero_days": int(np.count_nonzero(values == 0)),
            "top10_share_pct": float(np.sort(values)[-10:].sum() / values.sum() * 100),
            "q4_share_pct": float(monthly[name][-3:].sum()),
            "monthly_share_pct": {str(m): float(x) for m, x in zip(range(3, 13), monthly[name])},
        }
    # These gates refer to the checked research results, not chart coordinates.
    assert metrics["CEA"]["median_tons"] == 288406
    assert metrics["CCER"]["median_tons"] == 2700
    assert metrics["CEA"]["zero_days"] == 3
    assert metrics["CCER"]["zero_days"] == 0

    fonts = {f.name for f in font_manager.fontManager.ttflist}
    font = "Times New Roman" if "Times New Roman" in fonts else "STIXGeneral"
    plt.rcParams.update({
        "font.family": "serif", "font.serif": [font],
        "font.size": 9, "axes.labelsize": 9,
        "axes.labelpad": 2.5,
        "xtick.labelsize": 8, "ytick.labelsize": 8,
        "legend.fontsize": 8.5,
        "axes.edgecolor": "#9C9C9C", "axes.linewidth": 0.65,
        "text.color": "#252525", "axes.labelcolor": "#252525",
        "xtick.color": "#444444", "ytick.color": "#444444",
        "xtick.major.width": 0.6, "ytick.major.width": 0.6,
        "xtick.major.size": 3, "ytick.major.size": 3,
        "lines.linewidth": 1.15, "pdf.fonttype": 42,
        "ps.fonttype": 42, "mathtext.fontset": "stix",
        "savefig.dpi": 400,
    })
    fig, axes = plt.subplots(1, 3, figsize=FIGURE_SIZE)
    fig.subplots_adjust(left=0.058, right=0.994, top=0.89, bottom=0.21, wspace=0.29)
    for ax in axes:
        ax.set_axisbelow(True)
        ax.tick_params(direction="out", pad=2.0)
        # Full, light frames echo the reference screenshot; no decorative grid.
        for spine in ax.spines.values():
            spine.set_visible(True)

    ax = axes[0]
    for name, values in series.items():
        ordered = np.sort(values)
        unique, count = np.unique(ordered, return_counts=True)
        ecdf = np.cumsum(count) / len(values) * 100
        ax.step(np.r_[0, unique], np.r_[0, ecdf], where="post",
                color=COLORS[name], linestyle=STYLES[name])
        median = metrics[name]["median_tons"]
        ax.plot(median, 50, "o" if name == "CEA" else "s", markersize=3.4,
                markerfacecolor="white", markeredgecolor=COLORS[name], markeredgewidth=0.8)
    ax.set_xscale("function", functions=(np.log1p, np.expm1))
    ax.set_xlim(0, max(cea.max(), ccer.max()) * 1.2)
    ax.xaxis.set_major_locator(FixedLocator([0, 100, 1000, 10000, 100000, 1000000]))
    ax.set_xticklabels(["0", r"$10^2$", r"$10^3$", r"$10^4$", r"$10^5$", r"$10^6$"])
    ax.xaxis.set_minor_locator(NullLocator())
    ax.set_ylim(0, 103)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_ylabel("Cumulative share of days (%)")
    ax.set_xlabel("Daily listed volume (tons)")
    ax.text(0.04, 0.96, "Median daily volume", transform=ax.transAxes,
            va="top", fontsize=8.5)
    ax.text(0.04, 0.87, "CEA: 288,406 tons", transform=ax.transAxes,
            va="top", fontsize=8.5, color=COLORS["CEA"])
    ax.text(0.04, 0.79, "CCER: 2,700 tons", transform=ax.transAxes,
            va="top", fontsize=8.5, color=COLORS["CCER"])

    ax = axes[1]
    ax.plot([0, 100], [0, 100], color="#AAAAAA", linewidth=0.8, linestyle=":", zorder=1)
    x = np.arange(0, 204) / 203 * 100
    for name, values in series.items():
        y = np.r_[0, np.cumsum(np.sort(values)[::-1])] / values.sum() * 100
        ax.plot(x, y, color=COLORS[name], linestyle=STYLES[name])
        ax.plot(x[10], y[10], "o" if name == "CEA" else "s", markersize=3.4,
                markerfacecolor="white", markeredgecolor=COLORS[name], markeredgewidth=0.8)
        label_y = 45 if name == "CEA" else 73
        ax.annotate(f"{name}: {y[10]:.2f}%", xy=(x[10], y[10]),
                    xytext=(30, label_y), fontsize=8.5, color=COLORS[name],
                    arrowprops={"arrowstyle": "-", "color": COLORS[name], "lw": 0.65},
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    ax.text(0.42, 0.25, "Top 10 trading days", transform=ax.transAxes, fontsize=8)
    ax.text(0.57, 0.10, "Uniform volume", transform=ax.transAxes, fontsize=7.5, color="#777777")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 103)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_ylabel("Cumulative share of volume (%)")
    ax.set_xlabel("Share of days, largest first (%)")

    ax = axes[2]
    x = np.arange(10)
    ax.axvspan(6.5, 9.5, facecolor="#F2F2F2", edgecolor="none", zorder=0)
    for name, offset in [("CEA", -0.19), ("CCER", 0.19)]:
        ax.bar(x + offset, monthly[name], width=0.34, color=COLORS[name],
               alpha=0.80, edgecolor=COLORS[name], linewidth=0.4,
               hatch="///" if name == "CCER" else None)
    ax.set_xlim(-0.6, 9.6)
    ax.set_ylim(0, max(monthly["CEA"].max(), monthly["CCER"].max()) * 1.52)
    ax.set_xticks(x)
    ax.set_xticklabels(["Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax.set_ylabel("Share of window volume (%)")
    ax.set_xlabel("Month", labelpad=2.5)
    ax.text(0.04, 0.96, "Fourth-quarter share", transform=ax.transAxes,
            va="top", fontsize=8.5)
    for name, ypos in [("CEA", 0.87), ("CCER", 0.79)]:
        ax.text(0.04, ypos, f"{name}: {metrics[name]['q4_share_pct']:.2f}%",
                transform=ax.transAxes, va="top", fontsize=8.5, color=COLORS[name])

    handles = [Line2D([0], [0], color=COLORS[name], linestyle=STYLES[name],
                      marker="o" if name == "CEA" else "s", markersize=3.4,
                      markerfacecolor="white", label="CCER*" if name == "CCER" else name) for name in series]
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.525, 0.995),
               ncol=2, frameon=True, facecolor="white", edgecolor="#D7D7D7",
               handlelength=1.7, columnspacing=1.2, borderpad=0.20,
               handletextpad=0.45, borderaxespad=0.15)
    for ax, title in zip(axes, ["(a) Daily volume distribution", "(b) Volume concentration", "(c) Monthly volume shares"]):
        box = ax.get_position()
        fig.text((box.x0 + box.x1) / 2, 0.02, title, ha="center", va="bottom", fontsize=9.5)

    stem = HERE / "step2_liquidity_three_panel"
    fig.savefig(stem.with_suffix(".pdf"), metadata={"Title": "CEA and CCER listed-trading liquidity, 2025", "Author": "ContractDesign research"})
    fig.savefig(stem.with_suffix(".png"), dpi=400)
    plt.close(fig)
    result = {
        "window": [START, END], "volume_unit": "tons",
        "CEA_source_level": "official_daily_bulletins",
        "CCER_source_level": "secondary_transcription_with_two_official_corrections",
        "unallocated_CCER_difference_tons": 9020,
        "panel_a_x_transform": "log(1 + volume_tons)",
        "font": font, "figure_inches": list(FIGURE_SIZE), "colors": COLORS,
        "matplotlib": matplotlib.__version__, "numpy": np.__version__,
        "metrics": metrics,
    }
    (HERE / "step2_liquidity_metrics.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
