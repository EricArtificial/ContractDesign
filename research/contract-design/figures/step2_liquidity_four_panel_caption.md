# 第二研究步骤四面板横向图

**中文图题：** CEA 与 CCER 的价格变化及挂牌成交分布，2025 年。

**图注：** 共同观察期为 2025 年 3 月 7 日至 12 月 31 日，共 203 个相同交易日。面板 (a) 上栏为 CEA 已公布的综合收盘价和 CCER 日成交均价，单位为元/吨；下栏为各自相邻观测日的价格差绝对值 |Pₜ−Pₜ₋₁|，单位同为元/吨，每个市场有 202 个差值，首日不填零。周末、休市日期不补值；上栏保留官方已公布的 CEA 价格，包括无挂牌成交日，其价格不能当作该日挂牌成交价格。下栏展示的是价格水平的跨日变化，不是收益率，也不是 CEA 与 CCER 之间的价差。两市场价格定义及资产构成不同，曲线不直接支持同质波动率或保证金的比较。面板 (b)—(d) 分别显示挂牌日量的经验累积分布、高量交易日的累计成交集中度和月度成交量占比，与此前三面板图采用同一数据和口径。面板 (b) 横轴按 ln(1+日量) 变换，刻度为实际吨数，并保留零量日；面板 (c) 从最大日量开始累计，灰色对角线代表均匀成交，标记点为前十个高量日；面板 (d) 的浅灰背景表示第四季度，3 月从 7 日起计算。

**CCER*：** 使用经两条官方单日公告更正的二次整理表，仍存在未定位到具体日期的 9,020 吨、631,490.20 元差额，因此 CCER 相关曲线及分布仍依赖该表，统计为近似值。

**English title:** Prices, absolute price changes, and listed-trading volume: CEA and CCER, 2025.

**English notes:** The common sample covers March 7–December 31, 2025 (203 identical trading dates). The upper row of panel (a) shows the published CEA composite closing price and CCER daily mean transaction price, in CNY per ton. The lower row plots |Pₜ−Pₜ₋₁| within each series, also in CNY per ton (202 differences); the first observation is omitted. Weekends and nontrading dates are not imputed. Published CEA prices are retained on dates without listed trades and should not be interpreted as observed listed-trade prices on those dates. These are absolute price-level changes, not returns or differences between the two markets. Price definitions and asset composition differ between CEA and CCER. Panels (b)–(d) show the empirical distribution of daily listed volume, cumulative volume ranked from largest-volume days to smallest, and monthly shares of sample volume. Panel (b) uses ln(1 + volume in tons), with ticks in actual tons and zero-volume dates retained. Markers in panel (c) identify the ten largest-volume dates; the dotted diagonal represents uniform daily volume. The shading in panel (d) denotes the fourth quarter, and March starts on March 7. CCER* is a corrected secondary compilation with an unresolved difference of 9,020 tons and CNY 631,490.20 relative to official annual totals; its distribution statistics are approximate.

**来源 / Sources：** 上海环境能源交易所 [2025 年每日概况](https://overview.cneeex.com/qgtpfqjy/mrgk/2025n/)；碳中和网 [2025 年 CCER 逐日转载表](https://www.ccn.ac.cn/carbon-market/ccer/ccerdate/219.html)，及研究底稿列出的官方更正公告。图稿直接读取 `../data/cea_daily_2025.csv` 和 `../data/ccer_daily_2025_secondary.csv`；详细核对记录见 `../DAILY_LIQUIDITY_AND_DELIVERABLE_SUPPLY_2025.md`。

**文件：** `step2_liquidity_four_panel.pdf`（矢量图，11.6 × 2.95 英寸，29.464 × 7.493 cm）、同名 400 dpi PNG、`step2_liquidity_four_panel_metrics.json`。新增价格面板上、下栏高度比为 3.1:1；沿用绿/橙配色、细灰全框和嵌入的衬线字体。原三面板 PDF、PNG 保留。四面板图应以足够宽的横向版面使用，避免大幅缩小后文字难以辨认。

**复现：** 使用与三面板图相同的 matplotlib / numpy 环境，在项目根目录执行：

```sh
/private/tmp/contract-design-plot-env/bin/python research/contract-design/figures/plot_step2_liquidity.py --include-prices
```

不加 `--include-prices` 则重绘原三面板图。
