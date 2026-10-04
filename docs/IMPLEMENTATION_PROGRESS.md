# 项目进度与跨对话交接

本文件是缺少前文时的恢复入口；明确的新任务应先按用户指令和相关实际文件执行。记录与文件冲突时，以核实后的文件为准。

## Overall Objective
依据原始作业要求，完成广州期货交易所碳期货合约设计报告及真实的小组配套材料。

## Agreed Implementation Plan
1. 保存作业原件，整理要求并建立工作区规则。
2. 收集有出处的政策、交易数据和合约资料，记录拟议参数的依据。
3. 确定标的、合约条款、交割与结算、风险管理方案，形成报告并核对要求。
4. 整理三次真实讨论纪要与成员分工，导出并检查提交用 PDF。

## Completed
- [x] 保存作业原件，建立目录、作业要求清单和工作区规则。
- [x] 收集广期所五个现有期货品种的合约参照资料；四份一页正式合约转载 PDF 与钯交易指南、设计说明及合约表摘页列于 `research/gfex-futures/INDEX.md`。钯正式一页合约尚未取得。
- [x] 重新加载 `cross-chat-relay` skill，调整启动与交接规则，并把 README 中过时的“环境配置”阶段改为当前研究状态。
- [x] 2026-09-29：核对作业原件并检索官方碳市场制度、广期所结算规则、ICE 合约及期货设计研究，形成涵盖标的、数据、交割/价格、十项条款、风险、压力测试和提交的完整设计流程及来源地图。
- [x] 2026-09-30：阅读刘成伟《碳权投资的产品要素与交易机制》，对照现有流程及 2024—2026 年官方制度，形成面向合约设计的审查笔记 `research/contract-design/GLO_CARBON_RIGHTS_DESIGN_REVIEW.md`。笔记区分文章当时描述、当前核实制度和设计建议，列出标的、交割品年度/状态、CCER 抵销、价格、流动性、参与者和监管等待确认门槛；未据此预设合约参数。
- [x] 2026-09-30：依据作业原件和设计流程建立 `submission/carbon_futures_contract_template.tex`。模板包含四个核心模块、十项三列表格、APA 参考文献占位和可选的真实会议/分工附件结构；拟议参数及成员信息保留待填写。
- [x] 2026-09-30：新增根目录 `Makefile`，在项目根目录运行 `make` 即以 XeLaTeX 编译模板并输出 `submission/carbon_futures_contract_template.pdf`；中间文件保存在已忽略的 `submission/.build/`。README 已写明命令。
- [x] 2026-09-30：按用户提供的页首参考图调整 TeX 模板页眉：采用参考图青绿色 `#458377`、右对齐粗黑体标题和可缩放的矢量柱状折线图标；正文原大标题改为小组信息行，避免重复。
- [x] 2026-09-30：依用户进一步要求将页眉缩为右上角小尺寸，文案明确为“碳期货合约及规则设计说明”；正文恢复“广州期货交易所碳期货合约设计”独立主标题，并删除小组名称、成员姓名、提交日期显示区。
- [x] 2026-09-30：按用户要求将小页眉改为仅从第二页显示；第一页使用无页眉但保留页码的样式。
- [x] 2026-09-30：依据 AER 官方排版指引，将现有中文待填写模板另制为英文 AER 风格报告草稿 `submission/carbon_futures_contract_report.tex` 及 PDF。采用无封面首页、英文标题与 100 词以内摘要占位、无标题引言、罗马数字章节、booktabs 三栏合约表、11 点字体、1.5 倍行距与 1 英寸页边距。作业要求的 APA 参考文献优先于 AER 通常使用的 Chicago 作者—年份格式；原中文模板和用户的未提交改动保留。报告仍是待填写草稿，不含已核实合约参数或正式参考文献。
- [x] 2026-09-30：依用户新要求将英文报告改为更紧凑的双栏正文；合约规格表保持跨双栏通栏。为适应版面，英文稿现用 10 点字体、1.12 倍行距和 0.82 英寸页边距；这覆盖上一条记录中的字号、行距及页边距，仍为课程报告的 AER 风格草稿而非 AER 期刊投稿规格。
- [x] 2026-09-30：按用户明确指示，将 `intermediate/preparatory/contract_design_preparation.tex` 定为最终设计中文稿的主文件，篇幅不限；写作采用面向读者的 Writing 模式，过程与核验记录不进入成品正文。`submission/` 暂不修改，除非用户明确要求。已同步 `AGENTS.md`、两处 README 和主文件头部说明；主文件目前仍是待填写框架，尚未完成设计论证。
- [x] 2026-09-30：完成 `docs/CONTRACT_DESIGN_WORKFLOW.md` 的第 1 个研究步骤，形成 `research/contract-design/CEA_CCER_UNDERLYING_COMPARISON_2025.md` 与独立中文任务报告 `intermediate/task_reports/01_underlying_cea_ccer_comparison.tex`/`.pdf`。核对 CEA/CCER 权利、账户、年度/项目差异及 2025 年两家交易机构年度数据；以同自然年实现成交量和合规需求为依据，研究性暂选全国 CEA，不包括地方配额或 CCER。完整逐日价量、零成交日、可交割余额及期货交割接口尚未取得，故未确定具体交割年度或合约参数。
- [x] 2026-09-30：完成第 2 个研究步骤的公开资料核查，形成 `research/contract-design/DAILY_LIQUIDITY_AND_DELIVERABLE_SUPPLY_2025.md`、逐日 CSV、提取程序及独立中文任务报告 `intermediate/task_reports/02_daily_liquidity_and_deliverable_supply.tex`/`.pdf`。官方 CEA 2025 年 243 个交易日的逐日量额与年报完全对账，含 10 个零成交日；工作区 CSMAR 日表的 233 个有成交日九字段中的非空值逐行一致，空白经官方公告对照对应零值（2026-10-03 补明）。CCER 二次逐日表经两处官方更正后仍比官方全年累计数少 9,020 吨、631,490.20 元，差额尚未可靠分配到具体日。分年度/项目价量、合格资产可用余额和广期所交割账户/划转权限未取得；研究性暂选 CEA 仍成立，但不确定交割年度、交割方式或数值条款。
- [x] 2026-09-30：应用户后续要求，将第 2 步的日量、集中度、月度占比和交割证据缺口整合为一张精确 2:1 总图 `research/contract-design/figures/fig_02_integrated_liquidity_2to1.pdf`/`.png`。按截图改用青绿、蓝、灰色基准和橙色重点标注，并压缩标题区、面板间距及底注；保留两张拆分图作为放大检查版本。CCER 图表标明二次表差额，未将差额分配到具体日。

- [x] 2026-10-03：用户明确确定全国碳排放配额（CEA）为合约标的，不包括地方试点配额或 CCER；已同步中文设计主文件、作业要求清单的当前状态及第一步研究底稿的决策更新。具体交割年度、合格状态、交割方式与数值参数仍待确定。

- [x] 2026-10-03：复核已完成步骤，新增问题处理记录、标准库复算脚本和 JSON 结果；CEA 243 行对账通过，明确 CSMAR 非空值与官方一致、554 个空白字段对应官方零值（不能由空白直接推定零）；补两种 CEA 价格变动间隔口径、CCER 未分配差额敏感性和 2026 年 CEA25 价格权重。修正研究底稿及步骤 2 报告，旧步骤报告补后续状态；未修改原始 CSV 或提交版。接口、余额、授权、完整年度品级量额及广期所原件版本核验仍未关闭。
- [x] 2026-10-04：完成中文主稿第一节“标的资产与交易品种”，插入现有三联矢量图，补机构来源与计算依据；提出 1,000 吨/手设计值并同步表中交易单位和报价单位，依据见 `research/contract-design/SECTION1_WRITING_DECISIONS_20261004.md`。`make intermediate` 编译成功，其余核心章节仍为模板。

- [x] 2026-10-04：完成用户指定的 CEA/CCER 市场深度与流动性比较，记录于 `research/contract-design/LIQUIDITY_COMPARISON_20261004.md`，新增标准库复算程序及 `data/liquidity_comparison_20261004.json`。共同窗口为 2025-03-07—12-31、203 日、挂牌协议；补零收益日、微量成交日和机械 Amihud 诊断值，明确综合收盘价/跨项目均价不支持同质流动性排名。在线核到 CEA 2024 年实际交易主体 1,471 家与 CCER 截至 2025 年 8 月底累计 90 家，期别不同，不直接比较数量；管理单位和开户数不视为活跃数。盘口价差/深度、逐笔冲击、平均可流通存量及共同期活跃主体仍缺。未修改中文主稿或提交版；本任务未另生成 LaTeX 报告。
- [x] 2026-10-04：依用户要求统一项目 LaTeX 引用：中文设计主稿、两份研究任务报告与英文提交草稿均设置 APA 书目格式和数字型 `\cite`（正文显示为 `[n]`），条目集中在 `research/contract-design/references.bib`。中文机构作者使用拼音排序键；书目采用悬挂缩进和双倍条目间距。根目录及 `intermediate/` 的 Makefile 均将 `.bib` 列为编译依赖。主稿与研究报告已成功编译，PDF 文本显示数字引注及 APA 书目。英文草稿目前没有实际文内引注，书目为空。

- [x] 2026-10-04：完成换手率分母收集及中文第一节整合。综合表覆盖交易基础、真实参与主体、共同窗口量额/连续性/集中度及七项流动性指标；式（1）采用同期平均可交易存量，CEA/CCER 均未取得对应余额，未用累计发放量、应清缴量或年末累计登记量生成伪换手率。收集底稿为 `research/contract-design/TURNOVER_SUPPLY_RESEARCH_20261004.md`，新增发展报告及 Amihud（2002）书目。已读取 Writing Style 与 AER 正文/图表技能；未取得可确认的个人写作参考，按指定 AER 规范及项目 Writing 模式完成正文。`make intermediate` 成功，中文主稿为 6 页，最终日志无 Warning、Error、Overfull 或 Underfull；综合表完整置于第 2 页并完成版面检查，数字引注及新增 APA 条目已生成。仅修改中文主稿、共用书目及研究/交接记录，未修改提交版或原始价量数据。


- [x] 2026-10-04：完成用户指定的 Part I 三层结构调整。主稿以“标准化适配性—价格风险—潜在套保需求”三个问题组织 A/B/C 小节，仅保留支持 CEA 相对优势的差异；三张表分别对应三层，原三联图放于套保需求小节。删除跨期参与者数量和 Amihud 等非必要指标，保留交易单位段。新增 CEA 日价格变动标准差 1.04 元/吨（219 对相邻且两日均有挂牌成交的综合收盘价），复算脚本及 JSON 存于 research/contract-design/。官方价格基准及 CCER 项目均价已重查；正文保留品级匹配、纳管数与实际套保需求的区别及 CCER 日表差额。研究决策记录已同步。make intermediate 成功，主稿共 6 页、Part I 3 页，完成逐页目视检查；最终日志无 Warning、Error、Overfull 或 Underfull。内置编译因外部图文件限制未成功，源文件保留于编辑器。未修改提交版或原始数据。


- [x] 2026-10-04：依最新指令恢复中文主稿中的“CEA 与 CCER 的交易基础、活跃程度与流动性指标”完整表，保留实际文件中的三层正文。恢复交易基础/参与者、共同窗口成交及 Amihud 三组指标，表注明确跨期参与者、价格口径和 CCER 日表差额；完整表位于图之前并单页显示。make intermediate 成功，日志无 Warning、Error、Overfull 或 Underfull，表格已目视检查。研究写作记录已同步，未修改提交版。


- [x] 2026-10-04：应本轮用户要求，在既有横向图左侧新增图 (a) 的上下两栏：CEA 综合收盘价/CCER 日均成交价，以及各自相邻观测日价格差绝对值；原面板顺延为 (b)—(d)。输出 `research/contract-design/figures/step2_liquidity_four_panel.pdf`/`.png`、统计 JSON 和中英文图注；203 个同日期价格观测对应 202 个价差，首日及非交易日期未补零。原三面板图保留，脚本新增 `--include-prices` 选项。价格口径差异、CCER 二次表差额及无挂牌成交日价格限制在图注说明。

- [x] 2026-10-04：按用户要求将中文设计稿正文的图片替换为 `step2_liquidity_four_panel.pdf`，同步图题、价格/价差说明及第四季度分布的面板引用 (d)，并更新 `intermediate/Makefile` 的图片依赖。`make intermediate` 通过，正文 PDF 已更新；编译日志无警告或版面溢出，PDF 文本包含新四面板及对应图注，`git diff --check` 通过。

## Current Task
- [x] 2026-10-04：依最新指令合并价格波动表。已删除单独的 2025 年履约采购价格风险表，在完整 CEA/CCER 比较表新增 D 组：共同窗口日价格变动标准差为 1.07、7.14 元/吨；二次时间趋势回归残差标准差/样本平均价格为 7.46%、9.30%（口径由用户明确确认）。正文及表引用同步；新增复算脚本 calculate_detrended_price_risk_20261004.py 与 data/detrended_price_risk_20261004.json，原全年 1.04 元/吨计算保留作为历史结果。完整表第 2 页单页显示，make intermediate 成功、最终日志无排版/引用警告，已目视检查。未改提交版和原始数据。

## Remaining
- [ ] 核对钯期货正式一页合约的可获取性及五个现有品种的合约版本；记录查得结果与仍未能核实的部分。
- [ ] 补足指定年度 CEA 的逐日价格和成交量、可交割余额及账户权限证据；CCER 二次日表差额待定位，再为合约数值参数建依据记录。
- [ ] 设计碳期货合约并撰写、核查报告。
- [ ] 在指定中文设计稿中写入经核实的方案、来源与必要计算；用户明确要求制作课程提交版时，再核对提交版正文长度、报告页数和附件。
- [ ] 根据真实小组活动整理附件，导出并核查提交 PDF。

## Architectural Decisions
- 2026-10-03 用户决策：明确采用全国碳排放配额（CEA）作为合约标的，不包括地方试点配额和 CCER；此前“研究性暂选”记录保留为历史。交割年度、合格状态、交割方式和数值参数另行确定。
- 原始作业 `sources/Group Assignment0914.docx` 优先于此前对话概述；作业要求整理见 `docs/ASSIGNMENT_REQUIREMENTS.md`。
- 当前指令和相关实际文件优先；`docs/IMPLEMENTATION_PROGRESS.md` 仅在需要恢复或同步进度时读取，避免把旧记录当作实时事实。
- 研究依据放在 `research/`；最终设计中文稿的主文件是 `intermediate/preparatory/contract_design_preparation.tex`，不受字数和页数限制。写作时用面向读者的成品正文，不混入审计过程或修改说明；`submission/` 暂不修改，除非用户明确要求。会议与贡献记录只能依据真实小组活动填写。
- 作业只写“10 月 13 日课前”，未注明年份或具体钟点；提交前核对课程信息。
- 合约设计先验证标的、交割/最终价格的可执行性，再确定数值条款；外部交易所与美国监管资料仅作方法参照，不作为中国规则。

## Files Changed
- `research/contract-design/COMPLETED_STEPS_ISSUES_20261003.md`、`check_completed_steps.py`、`data/completed_steps_check_20261003.json`、`raw/20261003/` — 已完成步骤的问题、处理结果、复算和官方原文快照；包含等待用户决定的研究范围。
- `research/contract-design/figures/` — 第 2 步精确 2:1 整合总图、两张拆分图的 PDF/PNG 及可复现脚本；研究底稿增列口径和链接。
- `research/contract-design/DAILY_LIQUIDITY_AND_DELIVERABLE_SUPPLY_2025.md` — 第二研究步骤的来源、逐日统计、对账差额、可交割余额与账户权限缺口底稿。
- `research/contract-design/build_2025_daily_data.py`、`research/contract-design/data/cea_daily_2025.csv`、`research/contract-design/data/ccer_daily_2025_secondary.csv` — 提取程序和带逐行来源的机器可读数据。工作区新增的 CSMAR 原文件仅用于交叉核查，未修改。
- `intermediate/task_reports/02_daily_liquidity_and_deliverable_supply.tex` / `.pdf` — 第二研究步骤独立中文任务报告及编译版。
- `research/contract-design/CEA_CCER_UNDERLYING_COMPARISON_2025.md` — 第一研究步骤的法规、年度数据、计算、暂选理由与逐日数据缺口底稿。
- `intermediate/task_reports/01_underlying_cea_ccer_comparison.tex` / `.pdf` — 可独立阅读的中文任务报告及编译版。
- `AGENTS.md` — 按 skill 调整为任务优先、按需读取交接文件，并明确实质进展时同步记录。
- `README.md` — 更新新对话入口和实际研究阶段。
- `docs/IMPLEMENTATION_PROGRESS.md` — 改为 skill 要求的恢复结构，保留已核实进展、单一当前任务和可执行下一步。
- `docs/CONTRACT_DESIGN_WORKFLOW.md` — 新增逐步设计、十项条款定值方法、风险与压力测试、三次会议和提交验收流程。
- `research/contract-design/SOURCE_MAP.md` — 新增一手资料用途、局限及下一步证据缺口。
- `research/contract-design/GLO_CARBON_RIGHTS_DESIGN_REVIEW.md` — 新增针对 2021 年法律评论的期货设计审查与现行制度交叉核对。
- `submission/carbon_futures_contract_template.tex` — 保留可编译的中文模板；附件开关默认关闭，避免空白纪要进入报告。
- `submission/carbon_futures_contract_report.tex` — 新增英文 AER 风格报告草稿，十项条款与四个核心模块完整保留，未核实内容明确标注。
- `research/contract-design/references.bib` — 中文主稿、研究报告及英文草稿共用的 APA 书目条目库。
- `intermediate/preparatory/contract_design_preparation.tex`、`intermediate/task_reports/01_underlying_cea_ccer_comparison.tex`、`intermediate/task_reports/02_daily_liquidity_and_deliverable_supply.tex` — 使用共享 `.bib` 并以数字型 `\cite` 引用。
- `intermediate/templates/shared.tex`、`intermediate/templates/task_report.tex`、`intermediate/Makefile` — 将共享书目与引用设置接入后续报告模板和构建依赖。
- `submission/carbon_futures_contract_report.tex`、`Makefile` — 为英文草稿接入同一引文设置，并在 `.bib` 更新时触发重编译。
- `Makefile` — 默认编译英文报告 PDF；`make template` 可编译保留的中文模板，`make clean` 清理中间文件。
- `.gitignore` — 忽略 `submission/.build/` 中间编译文件。
- `README.md` — 补充 `make` 编译说明。
- `submission/carbon_futures_contract_template.pdf` — 中文模板预览，仍含待填写内容，不能作为最终提交稿。
- `submission/carbon_futures_contract_report.pdf` — 英文 AER 风格草稿预览，仍含待核实内容，不能作为最终提交稿。

## Tests
- 2026-10-04：`make intermediate` 成功编译中文设计主稿及两份研究报告；PDF 文本核实正文为 `[n]`、参考文献由共享 `.bib` 生成。最终日志无未定义引用、Overfull 或 Underfull；`git diff --check` 通过。根目录 `make` 成功编译英文草稿；因草稿尚无文内引注，biblatex 提示参考文献表为空。
- 2026-10-03：复算脚本通过唯一日期、分方式/年度量额、CSMAR 非空字段及空白对应零值检查；CCER 差额的假设分配不写回实际数据。`make intermediate` 通过，步骤 1/2 报告分别为三页和四页，编译日志无 Warning、Error、Overfull 或 Underfull；`git diff --check` 通过。
- 2026-10-03：CEA 标的决策更新后，中文设计主文件通过桌面编辑器编译及 `make intermediate`，已更新两页 PDF；`git diff --check` 通过。
- `file 'sources/Group Assignment0914.docx' research/gfex-futures/*.pdf` — PASS；原件识别为 DOCX，研究资料识别为 PDF，四份正式合约转载及钯合约表摘页均为一页。
- `shasum -a 256 research/gfex-futures/*.pdf` — PASS；七份 PDF 的哈希与 `research/gfex-futures/INDEX.md` 一致。
- `git diff --check` — PASS；三个修改文件均无空白错误。
- 2026-09-29：作业原件中的长度、三次讨论、每人写作与提交要求已再次从 DOCX 提取核对；所用外部来源有可访问的官方或原始研究页面。`git diff --check` 通过；新增流程含十项必填字段；两个新增文件的本地相对链接均存在。
- 2026-09-30：文章原文、2024 年国务院条例、2023 年 CCER 办法、2024 年配额结转方案、2026 年工作通知及 2026 年最新配额方案已在线打开核对；审查笔记已落盘，`git diff --check` 通过。
- 2026-09-30：`latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=/private/tmp/carbon-tex-build submission/carbon_futures_contract_template.tex` 通过；模板 PDF 为 A4、2 页，日志无 Overfull/Underfull、Warning 或 Error；十项条款和四模块在 PDF 文本中可读。
- 2026-09-30：项目根目录 `make` 通过，生成 193,948 字节、A4 两页的 `submission/carbon_futures_contract_template.pdf`；再次运行 `make -n` 显示无需重编译，日志无未定义引用、警告或版面溢出，`git diff --check` 通过。
- 2026-09-30：页眉更新后运行 `make` 通过；PDF 仍为 A4 两页，已查看第一页顶部预览，页眉与正文无重叠；最终编译日志无未定义引用、警告或版面溢出，`git diff --check` 通过。
- 2026-09-30：小页眉版本运行 `make` 通过，PDF 为 A4 两页；已目视检查第一页顶部层级，PDF 文本含正确页眉及正文标题且不含小组/成员/日期占位；日志无警告、未定义引用或版面溢出，`git diff --check` 通过。
- 2026-09-30：再次运行 `make` 通过，PDF 仍为 A4 两页；逐页文本核查显示第一页只有正文主标题、第二页开始出现“小页眉”文字；日志无警告或版面溢出，`git diff --check` 通过。
- 2026-09-30：英文稿运行 `make` 通过，输出 A4 两页 PDF；`pdftotext -layout` 核实十项合约字段、四个核心模块与参考文献占位，目视检查表格完整落在第一页；最终 LaTeX 日志无警告或版面溢出。
- 2026-09-30：双栏版本运行 `make` 通过，输出 A4 两页 PDF；目视检查正文为双栏、合约表通栏且十项完整；LaTeX 日志无警告或版面溢出，`git diff --check` 通过。
- 2026-09-30：第 1 步任务报告运行 `make intermediate` 通过，生成 A4 三页 PDF；`pdftotext` 可抽取研究结论、关键数据和来源，LaTeX 日志无 Overfull/Underfull、Warning 或 Error，`git diff --check` 通过。
- 2026-09-30：第 2 步 CEA 逐日总量/额及挂牌、大宗、竞价各量额逐项对上官方年报；CSMAR 全国 CEA 233 个有成交日九字段的非空值与官方一致、空白对应官方零值（2026-10-03 补明），官方零成交日恰为另 10 日。CCER 日表差额以官方累计数定位至 9 月 10—15 日之间，尚不能归入具体日期。
- 2026-09-30：第 2 步任务报告运行 `make intermediate` 通过，生成 A4 四页 PDF；`pdftotext` 可抽取结论、计算和来源，LaTeX 日志无 Overfull/Underfull、Warning 或 Error。

## Known Issues / Blockers
- 钯正式一页合约尚未取得。2026-10-03 再次访问官网铂品种页，HTTPS 证书仍与主机名不匹配；本轮未关闭验证。钯正式附件虽已定位但获取失败。
- 四份正式合约是公开转载件，尚未与广期所官网原始字节做哈希同一性核对；合约表的基础涨跌停板和保证金不代表当前执行标准。
- 尚无已核实的小组成员、分工和讨论日期；不要预填。第一节已提出交易单位和报价单位，其余数值参数仍待设计。截止日期年份及“5 页 / 2,000 words”的解释仍需课程确认。
- 已由用户明确确定全国 CEA 为标的，2025 年官方综合日数据及零成交日已核清；分年度/批次价格和可交割余额仍未取得，实际交割对接能力与所有拟议数值参数仍待核实。CCER 全年官方量额与二次逐日表之间仍差 9,020 吨、631,490.20 元，不能把二次表当作完整官方日数据。
- 英文 AER 风格 PDF 是排版草稿；摘要、正文论证、表中条款及 APA 参考文献均需以核实材料替换。真实会议纪要和分工说明须另行完成。

## Resume Here
**Next unfinished task:** 第一节图文写作已完成；下一建议事项是比较交割与结算方案，并为其余合约条款建立依据，待用户后续指令。未锁定交割方式或年度品级。

**Recommended next step:** 以已完成第一节为基础研究指定年度价量、交割路径和结算价格，随后设计其余条款。1,000 吨/手为本轮提出的设计值，不能从日量推断真实期货成交或可交割深度；接口、授权和余额仍作为相应方案的实施条件。不得在未获明确指令时联系机构。旧问题记录的 A/B 等待状态是历史状态。

**Relevant files:**
- `research/contract-design/COMPLETED_STEPS_ISSUES_20261003.md`
- `research/contract-design/check_completed_steps.py`
- `research/contract-design/data/completed_steps_check_20261003.json`
- `research/contract-design/DAILY_LIQUIDITY_AND_DELIVERABLE_SUPPLY_2025.md`
- `research/contract-design/data/cea_daily_2025.csv`
- `research/contract-design/data/ccer_daily_2025_secondary.csv`
- `intermediate/task_reports/02_daily_liquidity_and_deliverable_supply.tex`
- `research/gfex-futures/INDEX.md`
- `research/contract-design/CEA_CCER_UNDERLYING_COMPARISON_2025.md`
- `intermediate/task_reports/01_underlying_cea_ccer_comparison.tex`
- `docs/CONTRACT_DESIGN_WORKFLOW.md`
- `research/contract-design/SOURCE_MAP.md`
- `research/contract-design/GLO_CARBON_RIGHTS_DESIGN_REVIEW.md`
- `intermediate/preparatory/contract_design_preparation.tex`
- `docs/ASSIGNMENT_REQUIREMENTS.md`
- `sources/Group Assignment0914.docx`

**Commands:**
```sh
rg --files -g '!**/.git/**'
git status --short
cat research/gfex-futures/INDEX.md
```

**Assumptions / context:**
- 广期所现有合约仅作制度参照，不能直接作为拟议碳期货参数。
- 作业原件与研究 PDF 都应保留；未核实内容标为“待核实”。
