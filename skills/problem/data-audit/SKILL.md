---
name: data-audit
trigger: DATA_UNKNOWN
description: 建立可复核的数据事实基线：结构、单位、质量、范围、可用变量和潜在泄漏。
---

# data-audit

## Trigger

- 事件：`DATA_UNKNOWN`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

只回答“数据实际上是什么、能不能直接用、有哪些风险”。不在此 Skill 里决定最终模型，也不凭文件名或常识猜字段含义。

## Inputs

- 原始附件或数据目录
- 题面字段说明/数据字典（如有）
- 问题合同

## Procedure

1. 盘点所有数据文件、工作表、表结构和编码；记录行列数、字段名、类型、单位、主键/时间键/空间键。
2. 建立数据合同：明确“一行代表什么”、主键/实体键/时间键/空间键、目标字段、允许 join key、单位与派生字段 lineage；行语义未知时不能仅凭 dtype 宣布数据可用。
3. 检查缺失、重复、异常值、常量列、非法值、单位混用、日期解析、类别拼写和显著录入错误；对重要缺失不仅报比例，还检查是否与分组/时间/目标相关，区分结构性缺失与未知机制。
4. 对数值字段检查量级、分布、极值和物理范围；对时间序列检查排序、频率、缺口与未来信息；对空间数据检查坐标系与距离口径。
5. 显式做 leakage audit：目标泄漏、时间泄漏、实体/分组泄漏、预处理泄漏、join 泄漏、人工构造泄漏；每个可疑字段记录 `ALLOW / EXCLUDE / REVIEW` 和理由。
6. 若存在训练/验证/测试或滚动评估，先根据最终泛化 claim 冻结 split contract：IID/stratified、chronological、group-aware、spatial holdout 等；所有 imputation/scaling/feature selection 必须只在允许的数据侧拟合。
7. 记录数据覆盖范围是否足以回答各子问题：样本数量、类别覆盖、时间跨度、边界场景、缺失的关键变量。
8. 若需要清洗，先定义可追溯规则，再生成 processed 数据；原始数据只读，不覆盖；不要因为通用 outlier 阈值就删除科学上可能真实的极值。
9. 输出“事实而非解释”：例如“第 7 列缺失 12.4%”，不要直接写“因此必须用 XGBoost”。

## Outputs

- 数据审计报告（建议 `data/DATA_AUDIT.md`）
- 字段/单位/类型表
- 缺失与异常清单
- 允许/禁止使用变量清单
- 必要时的清洗规则和 processed 数据路径

## Checks

- 任何派生变量都能追溯到原字段和公式
- 已完成目标/时间/实体/预处理/join 等泄漏检查；预测任务未把测试信息泄漏到训练
- 时间/空间索引与题面口径一致
- 原始数据未被覆盖

## Failure

- 字段语义存在两种解释：转 `PROBLEM_AMBIGUOUS`
- 数据不足但可通过合理假设继续：转 `ASSUMPTION_WEAK`
- 数据事实已清楚而模型不确定：转 `MODEL_UNCERTAIN`

## Handoff

把数据事实和风险返回 Coach；不要在本 Skill 中自行决定删掉整个问题或更换比赛策略。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。

## Tool Routing
- PDF/扫描题面附件：先用 `tools/pdf/scripts/inspect_pdf.py`；嵌入文本可用 `extract_text.py`，视觉内容仍回看页面。
- XLSX：先用 `tools/xlsx/scripts/audit_workbook.py`，再按需用 `read_rows.py`；不要先把整本工作簿盲目导入模型代码。

## Deep Reference

涉及预测、统计、优化校准或多表合并时按需读取 `references/data-quality-and-leakage.md`；它定义数据合同、缺失机制、leakage taxonomy 与 split integrity。
