# 碳期货合约设计作业

本工作区用于完成广州期货交易所碳期货合约设计作业。新对话先按 [`AGENTS.md`](AGENTS.md) 执行当前任务；涉及作业要求时查阅 [`docs/ASSIGNMENT_REQUIREMENTS.md`](docs/ASSIGNMENT_REQUIREMENTS.md)，需要恢复未说明的进度时查阅 [`docs/IMPLEMENTATION_PROGRESS.md`](docs/IMPLEMENTATION_PROGRESS.md)。

| 位置 | 用途 |
| --- | --- |
| `sources/` | 老师给的作业原件；不要修改原件 |
| `docs/` | 作业要求与跨对话进度恢复文件 |
| `research/` | 政策、文献、市场数据及参数依据的工作记录 |
| `meetings/` | 真实的小组讨论纪要和成员分工 |
| `intermediate/` | 最终设计中文稿、其他预备材料与任务报告；目录和编译说明见 [`intermediate/README.md`](intermediate/README.md) |
| `submission/` | 课程提交版相关文件；暂不修改 |

当前已有广期所现有期货合约的研究资料，见 [`research/gfex-futures/INDEX.md`](research/gfex-futures/INDEX.md)。`submission/` 中有英文 AER 风格报告草稿和保留的中文模板；拟议参数、已核实报告正文、会议记录和成员贡献尚未完成。需要继续未指明的工作时，以进度文件为入口，并核对实际文件。

现有提交版构建命令保留：`make` 可编译英文 [`submission/carbon_futures_contract_report.tex`](submission/carbon_futures_contract_report.tex)，`make template` 可编译保留的中文模板，`make clean` 只清理提交版的辅助文件。在用户明确要求处理 `submission/` 前，不运行这些目标。

最终设计中文稿的主文件是 [`intermediate/preparatory/contract_design_preparation.tex`](intermediate/preparatory/contract_design_preparation.tex)，字数和页数不限。撰写时采用面向读者的写作模式，成品正文不呈现审计过程、写作理由或修改记录；资料核验与过程记录放在研究文件或明确要求生成的任务报告中。运行 `make intermediate` 可编译 `intermediate/preparatory/` 和 `intermediate/task_reports/` 中的全部 `.tex` 文件；新增文件会自动进入编译清单。除用户明确要求外，暂不修改 `submission/`。
