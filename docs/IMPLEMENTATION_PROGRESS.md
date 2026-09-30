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

## Current Task
- [ ] 收集 CEA 与 CCER 同口径的逐日价格、成交量及合格资产范围资料，按 `docs/CONTRACT_DESIGN_WORKFLOW.md` 第 1–2 步形成标的比较底稿。

## Remaining
- [ ] 核对钯期货正式一页合约的可获取性及五个现有品种的合约版本；记录查得结果与仍未能核实的部分。
- [ ] 在来源地图的待补证据清单基础上，完成 CEA/CCER 标的比较与参数依据记录。
- [ ] 设计碳期货合约并撰写、核查报告。
- [ ] 根据真实小组活动整理附件，导出并核查提交 PDF。

## Architectural Decisions
- 原始作业 `sources/Group Assignment0914.docx` 优先于此前对话概述；作业要求整理见 `docs/ASSIGNMENT_REQUIREMENTS.md`。
- 当前指令和相关实际文件优先；`docs/IMPLEMENTATION_PROGRESS.md` 仅在需要恢复或同步进度时读取，避免把旧记录当作实时事实。
- 研究依据放在 `research/`，提交稿放在 `submission/`；会议与贡献记录只能依据真实小组活动填写。
- 作业只写“10 月 13 日课前”，未注明年份或具体钟点；提交前核对课程信息。
- 合约设计先验证标的、交割/最终价格的可执行性，再确定数值条款；外部交易所与美国监管资料仅作方法参照，不作为中国规则。

## Files Changed
- `AGENTS.md` — 按 skill 调整为任务优先、按需读取交接文件，并明确实质进展时同步记录。
- `README.md` — 更新新对话入口和实际研究阶段。
- `docs/IMPLEMENTATION_PROGRESS.md` — 改为 skill 要求的恢复结构，保留已核实进展、单一当前任务和可执行下一步。
- `docs/CONTRACT_DESIGN_WORKFLOW.md` — 新增逐步设计、十项条款定值方法、风险与压力测试、三次会议和提交验收流程。
- `research/contract-design/SOURCE_MAP.md` — 新增一手资料用途、局限及下一步证据缺口。
- `research/contract-design/GLO_CARBON_RIGHTS_DESIGN_REVIEW.md` — 新增针对 2021 年法律评论的期货设计审查与现行制度交叉核对。

## Tests
- `file 'sources/Group Assignment0914.docx' research/gfex-futures/*.pdf` — PASS；原件识别为 DOCX，研究资料识别为 PDF，四份正式合约转载及钯合约表摘页均为一页。
- `shasum -a 256 research/gfex-futures/*.pdf` — PASS；七份 PDF 的哈希与 `research/gfex-futures/INDEX.md` 一致。
- `git diff --check` — PASS；三个修改文件均无空白错误。
- 2026-09-29：作业原件中的长度、三次讨论、每人写作与提交要求已再次从 DOCX 提取核对；所用外部来源有可访问的官方或原始研究页面。`git diff --check` 通过；新增流程含十项必填字段；两个新增文件的本地相对链接均存在。
- 2026-09-30：文章原文、2024 年国务院条例、2023 年 CCER 办法、2024 年配额结转方案、2026 年工作通知及 2026 年最新配额方案已在线打开核对；审查笔记已落盘，`git diff --check` 通过。

## Known Issues / Blockers
- 钯正式一页合约尚未取得。此前记录广期所官网 HTTPS 证书不匹配、HTTP 返回访问校验脚本；这一访问状况本次未重新测试。
- 四份正式合约是公开转载件，尚未与广期所官网原始字节做哈希同一性核对；合约表的基础涨跌停板和保证金不代表当前执行标准。
- 尚无已核实的小组成员、分工、讨论日期或碳期货拟议参数；不要预填。截止日期年份及“5 页 / 2,000 words”的解释仍需课程确认。
- 目前只形成设计方法和来源地图；所选标的、所有拟议参数、实际交割对接能力及可用逐日数据仍待核实。

## Resume Here
**Next unfinished task:** 按 `docs/CONTRACT_DESIGN_WORKFLOW.md` 第 1–2 步收集 CEA/CCER 同口径逐日价格、成交量及合格资产范围资料，形成标的比较底稿。

**Recommended next step:** 阅读流程和来源地图，从生态环境部制度及交易机构公开数据建立 CEA/CCER 对照；只写已核实的数值与规则。钯正式合约版本核对作为独立剩余事项保留。

**Relevant files:**
- `research/gfex-futures/INDEX.md`
- `docs/CONTRACT_DESIGN_WORKFLOW.md`
- `research/contract-design/SOURCE_MAP.md`
- `research/contract-design/GLO_CARBON_RIGHTS_DESIGN_REVIEW.md`
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
