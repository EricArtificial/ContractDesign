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
- [x] 2026-09-30：完成第 2 个研究步骤的公开资料核查，形成 `research/contract-design/DAILY_LIQUIDITY_AND_DELIVERABLE_SUPPLY_2025.md`、逐日 CSV、提取程序及独立中文任务报告 `intermediate/task_reports/02_daily_liquidity_and_deliverable_supply.tex`/`.pdf`。官方 CEA 2025 年 243 个交易日的逐日量额与年报完全对账，含 10 个零成交日；工作区 CSMAR 日表的 233 个有成交日九项字段逐行一致。CCER 二次逐日表经两处官方更正后仍比官方全年累计数少 9,020 吨、631,490.20 元，差额尚未可靠分配到具体日。分年度/项目价量、合格资产可用余额和广期所交割账户/划转权限未取得；研究性暂选 CEA 仍成立，但不确定交割年度、交割方式或数值条款。
- [x] 2026-09-30：应用户后续要求，将第 2 步的日量、集中度、月度占比和交割证据缺口整合为一张精确 2:1 总图 `research/contract-design/figures/fig_02_integrated_liquidity_2to1.pdf`/`.png`。按截图改用青绿、蓝、灰色基准和橙色重点标注，并压缩标题区、面板间距及底注；保留两张拆分图作为放大检查版本。CCER 图表标明二次表差额，未将差额分配到具体日。

## Current Task
- [ ] 核实拟议 CEA 交割年度的逐日挂牌价量、可用余额和登记账户划转权限，再进入 `docs/CONTRACT_DESIGN_WORKFLOW.md` 第 3 步交割与价格规则设计。第 2 步数据图已完成，此项尚未开始。

## Remaining
- [ ] 核对钯期货正式一页合约的可获取性及五个现有品种的合约版本；记录查得结果与仍未能核实的部分。
- [ ] 补足指定年度 CEA 的逐日价格和成交量、可交割余额及账户权限证据；CCER 二次日表差额待定位，再为合约数值参数建依据记录。
- [ ] 设计碳期货合约并撰写、核查报告。
- [ ] 在指定中文设计稿中写入经核实的方案、来源与必要计算；用户明确要求制作课程提交版时，再核对提交版正文长度、报告页数和附件。
- [ ] 根据真实小组活动整理附件，导出并核查提交 PDF。

## Architectural Decisions
- 原始作业 `sources/Group Assignment0914.docx` 优先于此前对话概述；作业要求整理见 `docs/ASSIGNMENT_REQUIREMENTS.md`。
- 当前指令和相关实际文件优先；`docs/IMPLEMENTATION_PROGRESS.md` 仅在需要恢复或同步进度时读取，避免把旧记录当作实时事实。
- 研究依据放在 `research/`；最终设计中文稿的主文件是 `intermediate/preparatory/contract_design_preparation.tex`，不受字数和页数限制。写作时用面向读者的成品正文，不混入审计过程或修改说明；`submission/` 暂不修改，除非用户明确要求。会议与贡献记录只能依据真实小组活动填写。
- 作业只写“10 月 13 日课前”，未注明年份或具体钟点；提交前核对课程信息。
- 合约设计先验证标的、交割/最终价格的可执行性，再确定数值条款；外部交易所与美国监管资料仅作方法参照，不作为中国规则。

## Files Changed
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
- `Makefile` — 默认编译英文报告 PDF；`make template` 可编译保留的中文模板，`make clean` 清理中间文件。
- `.gitignore` — 忽略 `submission/.build/` 中间编译文件。
- `README.md` — 补充 `make` 编译说明。
- `submission/carbon_futures_contract_template.pdf` — 中文模板预览，仍含待填写内容，不能作为最终提交稿。
- `submission/carbon_futures_contract_report.pdf` — 英文 AER 风格草稿预览，仍含待核实内容，不能作为最终提交稿。

## Tests
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
- 2026-09-30：第 2 步 CEA 逐日总量/额及挂牌、大宗、竞价各量额逐项对上官方年报；CSMAR 全国 CEA 233 个有成交日九个数值字段与官方逐日表一致，官方零成交日恰为另 10 日。CCER 日表差额以官方累计数定位至 9 月 10—15 日之间，尚不能归入具体日期。
- 2026-09-30：第 2 步任务报告运行 `make intermediate` 通过，生成 A4 四页 PDF；`pdftotext` 可抽取结论、计算和来源，LaTeX 日志无 Overfull/Underfull、Warning 或 Error。

## Known Issues / Blockers
- 钯正式一页合约尚未取得。此前记录广期所官网 HTTPS 证书不匹配、HTTP 返回访问校验脚本；这一访问状况本次未重新测试。
- 四份正式合约是公开转载件，尚未与广期所官网原始字节做哈希同一性核对；合约表的基础涨跌停板和保证金不代表当前执行标准。
- 尚无已核实的小组成员、分工、讨论日期或碳期货拟议参数；不要预填。截止日期年份及“5 页 / 2,000 words”的解释仍需课程确认。
- 已研究性暂选全国 CEA，2025 年官方综合日数据及零成交日已核清；分年度/批次价格和可交割余额仍未取得，实际交割对接能力与所有拟议数值参数仍待核实。CCER 全年官方量额与二次逐日表之间仍差 9,020 吨、631,490.20 元，不能把二次表当作完整官方日数据。
- 英文 AER 风格 PDF 是排版草稿；摘要、正文论证、表中条款及 APA 参考文献均需以核实材料替换。真实会议纪要和分工说明须另行完成。

## Resume Here
**Next unfinished task:** 补齐拟议 CEA 年度品级的日价量、可用余额与期货交割账户/划转权限证据，再开展第 3 步交割及价格规则设计。

**Recommended next step:** 从第二步骤研究底稿的缺口清单开始，向交易机构与登记机构核验指定年度日价量、可用余额及接收账户资格；CCER 逐日转载表的 9 月差额另行定位。钯正式合约版本核对作为独立剩余事项保留。

**Relevant files:**
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
