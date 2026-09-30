# 中间产物

本目录存放最终设计中文稿、其他预备材料与任务报告。`submission/` 保留课程提交版相关文件，除用户明确要求外暂不修改；研究资料与来源原件位于 `research/` 和 `sources/`。

| 目录 | 内容 |
| --- | --- |
| `preparatory/` | `contract_design_preparation.tex` 是最终设计中文稿的主文件，字数和页数不限；同目录也可存放其他中文预备材料 |
| `task_reports/` | 仅在具体任务明确要求生成报告时保存中文任务报告；应独立记录推演、计算、假设、结果及来源 |
| `templates/` | 可复制的任务报告模板和两类文件共用的中文排版设置；这里的模板不进入自动编译清单 |

在项目根目录运行 `make intermediate`，或在本目录运行 `make`。编译系统会自动发现 `preparatory/` 和 `task_reports/` 下的所有 `.tex` 文件，在同目录生成同名 PDF；无需修改 Makefile。LaTeX 的辅助文件放在 `.build/`。运行 `make -C intermediate list` 可查看当前编译清单，`make -C intermediate clean` 清理此目录生成的 PDF 和辅助文件。

撰写 `preparatory/contract_design_preparation.tex` 时，直接面向最终读者写中文设计正文。可见稿件不写审计过程、写作理由、免责声明、修改报告或审计类措辞；研究推演和核验记录留在 `research/`，若具体任务明确要求报告则另放 `task_reports/`。合约依据、必要的计算结果、引用以及真正影响结论的不确定性仍应写入正文。该文件目前保留待填写的框架内容，不能视为已经完成的设计。

新增任务报告可复制 `templates/task_report.tex` 到 `task_reports/` 并改名。文件名建议使用不含空格的英文或数字。编译命令从项目根目录运行 XeLaTeX，因此文件中的 `\input` 和本地图片路径请按项目根目录填写。
