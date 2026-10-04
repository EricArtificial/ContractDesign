# 合约设计流程来源地图

检索日期：2026-09-29。此表记录流程所用的**一手法规、交易所资料及原始研究**。规则可能修订；正式报告引用时须再核对版本、适用范围和原文。课程要求见[作业原件](../../sources/Group%20Assignment0914.docx)，不由外部资料替代。

| 编号 | 来源 | 设计用途与已核实信息 | 使用边界 |
| --- | --- | --- | --- |
| S1 | [国务院《碳排放权交易管理暂行条例》](https://www.mee.gov.cn/zcwj/gwywj/202402/t20240205_1065850.shtml)，2024 | 规定全国配额市场的登记、交易、清缴框架；注册登记机构负责产品登记及交易结算，交易机构组织现货集中交易。 | 这是现货制度，不能直接证明拟议期货已可上市或可与登记系统对接。 |
| S2 | [生态环境部《碳排放权交易管理办法（试行）》](https://www.mee.gov.cn/gzk/gz/202112/t20211213_963865.shtml)及[登记、交易、结算三项规则公告](https://www.mee.gov.cn/xxgk2018/xxgk/xxgk01/202105/t20210519_833574.html) | 核对 CEA 权属、账户、变更、清缴及结算流程；登记系统记录是权属判断依据。 | 需检查后续修订与拟议交割操作权限。 |
| S3 | [生态环境部、市场监管总局《温室气体自愿减排交易管理办法（试行）》](https://www.mee.gov.cn/xxgk2018/xxgk/xxgk02/202310/t20231020_1043694.html)，2023 | 核对 CCER 计量单位、登记、持有、变更、注销、交易和系统数据交换。 | CCER 有独立规则；不能与 CEA 的登记和交割流程混同。 |
| S4 | [生态环境部《2025年全国碳市场平稳有序运行》](https://www.mee.gov.cn/ywgz/ydqhbh/wsqtkz/202601/t20260101_1139528.shtml)，2026-01-01 | 官方 2025 年市场规模初筛：CEA 2025 年成交量 2.35 亿吨；CCER 累计成交量 921.94 万吨。 | **一个是全年量，一个是累计量**，不能据此直接比较同期间流动性；也不足以计算逐日波动率。 |
| S5 | [生态环境部《全国碳市场发展报告（2025）》](https://www.mee.gov.cn/ywgz/ydqhbh/wsqtkz/202509/W020250927515316322073.pdf)，2025 | 核对市场沿革、履约周期与价格、成交量阶段性；报告称 2024 年第四季度成交量占全年 79%。 | 应核对价格系列的品种、交易方式和时间范围，避免以聚合数据代替可交割标的的数据。 |
| S6 | [广期所《结算规则》英文参考译本](https://www.gfex.com.cn/en/TradingRules/202601/00e76b0dcdcc466abb0e9d798431a7f5.shtml)，网页标注 2026-01-09、规则发布于 2025-05-09；另见[现有合约资料索引](../gfex-futures/INDEX.md) | 广期所逐日盯市、保证金和结算安排的制度参照；现有品种展示标准化合约表格式。 | **网站明确中文原文有约束力**；需核对当前中文文本及具体品种后续通知。现有品种参数不能照搬。 |
| S7 | [ICE Endex EUA Futures 产品规格](https://www.ice.com/products/197) | 可核实 1 手为 1,000 EUA、报价单位、最小价位、交割期和实物交割规则，供国际比较。 | 欧盟市场及登记基础设施不同；任何一项数字都不是中国合约的指定答案。 |
| S8 | [Corkish、Holland、Vila，Bank of England Working Paper 70](https://www.bankofengland.co.uk/working-paper/1997/the-determinants-of-successful-financial-innovation)，1997 | 原始研究发现 LIFFE 合约成功与标的市场规模、波动相关，支持先评估现货市场与套保需求。 | 历史英国样本，不能据此预测中国碳期货的成功概率。 |
| S9 | [Tashjian, *Optimal futures contract design*](https://www.sciencedirect.com/science/article/abs/pii/1062976995900128)，1995 | 原始研究概述合约条款需与现货市场特征相联系。 | 目前可核对摘要；若正式稿引用具体结论，应取得全文并核对。 |
| S10 | [CFTC Economic Requirements](https://www.cftc.gov/IndustryOversight/ContractsProducts/EconomicRequirements/interpretative.html)及[交割品级与价差说明](https://www.cftc.gov/IndustryOversight/ContractsProducts/EconomicRequirements/differential.html) | 实物交割检验可交割供给、到期收敛和防操纵；现金交割检验基础现货价格的可靠性、公开性、及时性和代表性。 | 美国监管方法参照，不是中国法规或本课程额外要求。 |
| S11 | [CME Futures and Options Margin Model](https://www.cmegroup.com/solutions/risk-management/performance-bonds-margins/futures-and-options-margin-model.html) | 保证金设计参考历史和前瞻波动、流动性、季节性及事件风险。 | CME 的目标覆盖率和模型参数不自动适用于广期所；作业可用透明、可复核的简化压力测试。 |
| S12 | [证监会法规库《中华人民共和国期货和衍生品法》](https://neris.csrc.gov.cn/falvfagui/rdqsHeader/mainbody?navbarId=1&secFutrsLawId=c9f4df6454d745eeb1d614c0d57bfe60) | 核对期货合约、保证金、当日无负债结算和交割的上位制度。 | 需与广期所现行规则及具体碳资产制度一并解释，不以法律一般条款替代操作细则。 |

## 后续需补的直接证据

- 所选标的的同口径逐日成交价与成交量、零成交日、交易方式及年度/批次信息；用于合约单位、价位、月份、涨跌停板和保证金定量校准。
- 可交割资产余额、可交易主体和账户权限、登记系统冻结/划转与期货结算对接的正式说明；用于验证实物交割是否可行。
- 如选现金交割：可公开获取的原始现货价格序列、指数编制权与授权、异常交易识别及备用价格规则；用于验证最终结算价的可复制性和防操纵性。
- 广期所现行中文交易、结算和风险规则及后续通知；用于判断拟议条款能否与交易所制度一致。

## 2026-10-03 补核

已确认标的为全国 CEA。2025 年全市场官方日量额已取得并对账，不再将其列为整体缺失；指定年度品级价量、可用余额、交割接口及价格授权仍缺。交易所 2026 年综合价格方案规定 CEA25 权重为 1，其余年度为 0；详见[已完成步骤问题处理记录](COMPLETED_STEPS_ISSUES_20261003.md)。S9 仅核对摘要，后续正文不使用未经全文核实的具体结论。S6 英文译本保留为方法参照，现行中文版本与修订仍待核对。
