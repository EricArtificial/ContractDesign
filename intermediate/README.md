# 中间产物

本目录存放正式提交稿形成之前的 LaTeX 中间产物。正式稿仍位于 `submission/`，研究资料与来源原件仍位于 `research/` 和 `sources/`。

| 目录 | 内容 |
| --- | --- |
| `preparatory/` | 中文预备材料；沿用现有中文报告的版式与标的、条款、交割价格、风险管理框架，篇幅不限 |
| `task_reports/` | 仅在具体任务明确要求生成报告时保存中文任务报告；应独立记录推演、计算、假设、结果及来源 |
| `templates/` | 可复制的任务报告模板和两类文件共用的中文排版设置；这里的模板不进入自动编译清单 |

在项目根目录运行 `make intermediate`，或在本目录运行 `make`。编译系统会自动发现 `preparatory/` 和 `task_reports/` 下的所有 `.tex` 文件，在同目录生成同名 PDF；无需修改 Makefile。LaTeX 的辅助文件放在 `.build/`。运行 `make -C intermediate list` 可查看当前编译清单，`make -C intermediate clean` 清理此目录生成的 PDF 和辅助文件。

新增预备材料可复制 `preparatory/contract_design_preparation.tex`，新增任务报告可复制 `templates/task_report.tex` 到 `task_reports/` 并改名。文件名建议使用不含空格的英文或数字。编译命令从项目根目录运行 XeLaTeX，因此文件中的 `\input` 和本地图片路径请按项目根目录填写。模板中的待核实内容应在使用时补齐，不能当作已核实结论。
