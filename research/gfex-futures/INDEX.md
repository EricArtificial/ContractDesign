# 广州期货交易所期货合约资料索引

检索与下载日期：2026-09-28。范围：广期所官网所列的五个已上市**期货**品种（SI、LC、PS、PT、PD），不含期权。以下是研究资料，不代表拟设计的碳期货条款。

## 本地文件与来源

| 品种 | 本地文件 | 文件性质与核对来源 | SHA-256 |
| --- | --- | --- | --- |
| 工业硅 SI | [SI_Gfex_contract_reprint.pdf](SI_Gfex_contract_reprint.pdf) | 广期所《工业硅期货合约》2024 年修订版的一页 PDF，下载自[东方财富转载附件](https://np-newsimg.dfcfw.com/download/A2_cms_f_20240206161211882819?abc2958.pdf%3F=&direct=1)；与[广期所公开 PDF](https://www.gfex.com.cn/gfex/llbb/202402/73cd6f4cc26b4dd5b3d127b5462b59a7/files/%E5%B9%BF%E5%B7%9E%E6%9C%9F%E8%B4%A7%E4%BA%A4%E6%98%93%E6%89%80%E5%B7%A5%E4%B8%9A%E7%A1%85%E6%9C%9F%E8%B4%A7%E5%90%88%E7%BA%A6%EF%BC%882022%E5%B9%B412%E6%9C%8812%E6%97%A5%E7%89%88%EF%BC%89.pdf)可见条款交叉核对。 | `8665f1d7df3cbe7fcd6a685a6840495fa8a56b3a12eda0b1bb5e6a251860955e` |
| 碳酸锂 LC | [LC_Gfex_contract_reprint.pdf](LC_Gfex_contract_reprint.pdf) | 广期所《碳酸锂期货合约》一页 PDF，下载自[东方财富转载附件](https://np-newsimg.dfcfw.com/download/A2_cms_f_20241206154420247245?abc5761.pdf=&direct=1)；与[广期所合约页](https://www.gfex.com.cn/gfex/sytslqhhy/202307/9ad927b8ec4c458594e172fd1ada2a9b.shtml)交叉核对。 | `4dc046ab060d79571481fd0652a0d90fdfdda1230739bccd0d578cab3af622c3` |
| 多晶硅 PS | [PS_Gfex_contract_reprint.pdf](PS_Gfex_contract_reprint.pdf) | 广期所《多晶硅期货合约》一页 PDF，下载自[东方财富转载附件](https://np-newsimg.dfcfw.com/download/A2_cms_f_20241213203157998518?abc6474.pdf=&direct=1)；[广期所发布通知的转载页](https://qhweb.eastmoney.com/news/202412133268112122.html)核对其发布背景。 | `db7408e3327ff74a7f47a1c622b63b2d7420adaea24e7027adc347e9f3ce43ef` |
| 铂 PT | [PT_Gfex_contract_reprint.pdf](PT_Gfex_contract_reprint.pdf) | 广期所《铂期货合约》一页 PDF，下载自[东方财富转载附件](https://np-newsimg.dfcfw.com/download/A2_cms_f_20251107175956812245?abc9006.pdf=&direct=1)；与[广期所合约页](https://www.gfex.com.cn/gfex/sspzb/sspz.shtml)交叉核对。 | `b4a3c96be0adf7de78bc93fe546818450e41a3d4f39d5bf7f16bbd8252b8a245` |
| 钯 PD | [PD_contract_table_excerpt_from_Gfex_guide.pdf](PD_contract_table_excerpt_from_Gfex_guide.pdf) | **非正式合约原件**。从广期所编写的《钯期货交易指南》第 5 页提取完整合约条款表；[国海良时期货转载页](https://www.ghlsqh.com.cn/education/show-27281.html)。正式一页合约 PDF 尚未取得。 | `25c5de97029f784447d843f5d701cb85623bf2fce217d22f11b8377a1c2132d7` |

钯的完整辅助资料：[交易指南](PD_Gfex_trading_guide_reprint.pdf)（SHA-256 `028da46d3a1d63df487c9aeaab16fcfb888e9ca0acf31583edd7e25d44e21719`）、[合约和规则设计说明](PD_Gfex_design_notes_reprint.pdf)（SHA-256 `b8c78f3328a3bb0281e60e7655f11c01262ba5d411eaa793209cd7980e7e45e5`）。两份均由[国海良时期货](https://www.ghlsqh.com.cn/education/305.html)转载并注明资料来源为广州期货交易所。钯正式合约发布见[广期所通知的期货公司转载](https://www.ccbfutures.com/main/a/20251107/75736.shtml)。

## 已核对的基本条款

| 代码 | 标的 | 交易单位 | 最小变动价位 | 合约月份 | 合约表中的涨跌停板、最低保证金 | 交割 |
| --- | --- | --- | --- | --- | --- | --- |
| SI | 工业硅 | 5 吨/手 | 5 元/吨 | 全部月份 | ±4%；5% | 实物 |
| LC | 碳酸锂 | 1 吨/手 | 20 元/吨 | 全部月份 | ±4%；5% | 实物 |
| PS | 多晶硅 | 3 吨/手 | 5 元/吨 | 全部月份 | ±4%；5% | 实物 |
| PT | 铂 | 1000 克/手 | 0.05 元/克 | 2、4、6、8、10、12 月 | ±4%；5% | 实物 |
| PD | 钯 | 1000 克/手 | 0.05 元/克 | 2、4、6、8、10、12 月 | ±4%；5% | 实物 |

五种合约表均写明最后交易日为合约月份第 10 个交易日、最后交割日为此后第 3 个交易日。此处的 ±4% 与 5% 是**合约文本中的基础条款**，不是 2026-09-28 各合约实际执行标准；交易所可通过后续公告调整。设计碳期货时只能将这些数字作为广期所现有产品的制度参照，不能照搬。

## 文件校验与局限

- 四个正式合约 PDF 均为一页，`file` 识别为 PDF，`pdftotext` 提取的标题、交易单位和最小变动价位与相应来源相符。钯指南为 12 页扫描 PDF，已目视核对其第 5 页合约表；摘录文件为该页的单页 PDF。
- 直接访问广期所官网时，HTTPS 返回与 `www.gfex.com.cn` 不匹配的证书；HTTP 返回访问校验脚本。因此未把该响应伪装成官方 PDF，也不能声称已对转载件与官网原始字节做哈希同一性核对。
- 后续如官网可正常访问，优先补下钯的正式一页合约，并对五份文本复核版本、现行修订及实际保证金和涨跌停板公告。

## 2026-10-03 访问复查

官网铂品种页再次返回与 `www.gfex.com.cn` 不匹配的 TLS 证书，未关闭证书验证；记录见 `../contract-design/raw/20261003/manifest.json`。已通过[钯正式合约发布通知转载](https://www.jrqh.com.cn/detail/7449)定位官方附件链接，但附件访问失败，尚未新增正式一页原件。五个品种当前版本与原件字节核验仍未完成，不能把本索引的历史基础条款写成当前执行标准。
