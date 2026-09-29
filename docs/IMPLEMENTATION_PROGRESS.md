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

## Current Task
- [ ] 核对钯期货正式一页合约的可获取性及五个现有品种的合约版本；记录查得结果与仍未能核实的部分。

## Remaining
- [ ] 收集 CEA、CCER 的官方资料和碳市场价格、成交数据，形成可追溯的参数依据记录。
- [ ] 设计碳期货合约并撰写、核查报告。
- [ ] 根据真实小组活动整理附件，导出并核查提交 PDF。

## Architectural Decisions
- 原始作业 `sources/Group Assignment0914.docx` 优先于此前对话概述；作业要求整理见 `docs/ASSIGNMENT_REQUIREMENTS.md`。
- 当前指令和相关实际文件优先；`docs/IMPLEMENTATION_PROGRESS.md` 仅在需要恢复或同步进度时读取，避免把旧记录当作实时事实。
- 研究依据放在 `research/`，提交稿放在 `submission/`；会议与贡献记录只能依据真实小组活动填写。
- 作业只写“10 月 13 日课前”，未注明年份或具体钟点；提交前核对课程信息。

## Files Changed
- `AGENTS.md` — 按 skill 调整为任务优先、按需读取交接文件，并明确实质进展时同步记录。
- `README.md` — 更新新对话入口和实际研究阶段。
- `docs/IMPLEMENTATION_PROGRESS.md` — 改为 skill 要求的恢复结构，保留已核实进展、单一当前任务和可执行下一步。

## Tests
- `file 'sources/Group Assignment0914.docx' research/gfex-futures/*.pdf` — PASS；原件识别为 DOCX，研究资料识别为 PDF，四份正式合约转载及钯合约表摘页均为一页。
- `shasum -a 256 research/gfex-futures/*.pdf` — PASS；七份 PDF 的哈希与 `research/gfex-futures/INDEX.md` 一致。
- `git diff --check` — PASS；三个修改文件均无空白错误。

## Known Issues / Blockers
- 钯正式一页合约尚未取得。此前记录广期所官网 HTTPS 证书不匹配、HTTP 返回访问校验脚本；这一访问状况本次未重新测试。
- 四份正式合约是公开转载件，尚未与广期所官网原始字节做哈希同一性核对；合约表的基础涨跌停板和保证金不代表当前执行标准。
- 尚无已核实的小组成员、分工、讨论日期或碳期货拟议参数；不要预填。截止日期年份及“5 页 / 2,000 words”的解释仍需课程确认。

## Resume Here
**Next unfinished task:** 核对钯期货正式一页合约的可获取性及五个现有品种的合约版本。

**Recommended next step:** 阅读现有索引，优先查广期所的合约页及修订公告；仅把可核实的结果写回索引。若官网仍无法访问，记下访问障碍并继续 CEA/CCER 资料收集。

**Relevant files:**
- `research/gfex-futures/INDEX.md`
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
