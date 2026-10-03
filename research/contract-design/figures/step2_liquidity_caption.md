# 第二研究步骤横向组合图

**中文图题：** CEA 与 CCER 的挂牌成交规模、集中度及月度分布，2025 年。

**中文图注：** 共同观察期为 2025 年 3 月 7 日至 12 月 31 日，共 203 个相同交易日。两市场均使用挂牌成交量，单位为吨，CEA 不计大宗协议和单向竞价。面板 (a) 为日量的经验累积分布，横轴按 ln(1+日量) 变换，刻度仍显示实际吨数；零量日保留，CEA 为 3 日，CCER 表内为 0 日。面板 (b) 按各市场日量由高到低排序，横轴为累计交易日占比，纵轴为累计成交量占比；灰色对角线表示每个交易日成交量相等，标记点为前 10 个高量日。面板 (c) 以各市场的观察期成交量为分母计算月度占比，3 月仅覆盖 7 日起的观察日期，浅灰背景标识第四季度。CCER* 来自经两条官方公告更正的二次整理表，仍比官方年度累计数少 9,020 吨、631,490.20 元，疑点集中于 9 月 11—12 日，故 CCER 分布统计为近似值。图中显示的成交分布不直接度量可交割余额或盘口深度。

**English title:** Listed-trading volume, concentration, and monthly shares: CEA and CCER, 2025.

**English notes:** The common sample covers March 7–December 31, 2025 (203 identical trading dates). Both markets use listed-trading volume; CEA block trades and auctions are excluded. Panel (a) plots the empirical cumulative distribution of daily volume. The horizontal coordinate is ln(1 + volume in tons), with ticks in actual tons. Zero-volume observations are retained (CEA: 3; CCER table: 0). Panel (b) ranks days by volume from largest to smallest; the dotted diagonal represents equal volume on every trading day. Markers identify the ten largest-volume days. Panel (c) reports each month's share of the market's total volume within the sample; March starts on March 7, and the shaded region denotes the fourth quarter. CCER* is a secondary compilation with two corrections based on official daily bulletins. An unresolved difference of 9,020 tons and CNY 631,490.20 relative to official annual totals remains, with discrepancies concentrated around September 11–12. CCER distribution statistics are therefore approximate. Traded volume does not directly measure deliverable supply or order-book depth.

**来源 / Sources：** 上海环境能源交易所官方逐日公告，见 [2025 年每日概况目录](https://overview.cneeex.com/qgtpfqjy/mrgk/2025n/)；CCER 日量见[碳中和网 2025 年转载表](https://www.ccn.ac.cn/carbon-market/ccer/ccerdate/219.html)，更正与累计数核验见 `../DAILY_LIQUIDITY_AND_DELIVERABLE_SUPPLY_2025.md`。机器可读来源为 `../data/cea_daily_2025.csv` 和 `../data/ccer_daily_2025_secondary.csv`，图内统计均由代码重算。来源说明置于图注其他说明之后，依 AER [Style Guide](https://www.aeaweb.org/journals/aer/style-guide) 的图稿要求组织。

## 文件与复现

- `step2_liquidity_three_panel.pdf`：矢量图，8.4 × 2.8 英寸（21.336 × 7.112 cm），字体嵌入；本轮加宽并收紧排版。
- `step2_liquidity_three_panel.png`：400 dpi 预览图。
- `plot_step2_liquidity.py`：从本地 CSV 复现全部统计和图稿，不访问网络。
- `step2_liquidity_metrics.json`：绘图统计、样本口径、字体和软件版本。

依赖为 `matplotlib==3.10.8`、`numpy==2.4.0`。本次可复现命令（临时环境存在期间）：

```sh
/private/tmp/contract-design-plot-env/bin/python research/contract-design/figures/plot_step2_liquidity.py
```

该图使用 Times New Roman、7.5–9.5 pt 的图内文字、细灰全框和绿/橙配色（CEA：#20B795；CCER：#EE7B19），实线/虚线、圆/方标记及柱纹理确保不只依赖颜色识别。共享图例的线段和间距、坐标轴标题距离及面板留白均已收紧，月份标签水平排列。上述字体、字号、尺寸和配色是本图的设计选择；AER 官方明确要求矢量图、面板标识及图注来源顺序，未规定本图所用固定尺寸和字号。参考截图提供视觉样式，不提供本图的数据或分析方法。
