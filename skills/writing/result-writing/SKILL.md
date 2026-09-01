---
name: result-writing
trigger: RESULT_SECTION_NEEDED
description: 把数值结果写成“结果 + 比较 + 原因 + 意义 + 限制”的证据段，并与图表、运行记录一一对应。
---

# result-writing

## Trigger

- 事件：`RESULT_SECTION_NEEDED`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

用于论文结果与分析部分，不重新发明计算结果。重点是让读者知道数字意味着什么，而不是重复表格中的所有数字。

## Inputs

- 结构化结果分析
- Final Run
- 相关表/图
- 模型合同
- 敏感性/鲁棒性结果（如有）

## Procedure

1. 每个段落先确定一个中心 claim；首句给出最重要结果，不先复述一遍求解过程。
2. 引用对应图/表并挑关键数字，不逐行抄表；单位、小数精度与表格保持一致。
3. 有 Baseline/候选时说明差异，并区分绝对差、相对差和统计/工程意义。
4. 解释结果为什么出现：关联约束激活、模型机制、数据特征或物理规律；没有证据时用“可能/表明”而非确定因果。
5. 将结果翻译成题目语境中的决策含义，例如成本节省、风险变化、资源分配或机制解释。
6. 在必要位置写限制：敏感参数、未覆盖场景、近似条件、数值误差，不要把所有限制都藏到最后一节。
7. 完成后用 run_id/Claim-Evidence Map 回查关键数字，避免正文二次手算造成漂移。

8. 对关键比较优先考虑“表/图 + 一段解释”的表达；不要把多个决定性数字全部埋在连续文字里。
9. Run ID、仓库路径、内部 QA 状态只用于证据回查，默认不写进科学正文；官方规则要求时按最小必要方式披露。

## Outputs

- 可直接进入正文的结果分析段落
- 图表引用位置
- 必要限制/适用条件

## Checks

- 段落中心 claim 明确
- 数字与表图一致
- 解释没有越过证据
- 不把相关性写成因果
- 没有重复整张表

## Failure

- 正文数字与 Final 不一致：转 `FINAL_RESULT_NEEDS_REVIEW`
- 需要新图支持：转 `FIGURE_NEEDED`
- claim 证据不足：转 `CLAIM_UNSUPPORTED`

## Handoff

完成后通常推荐 `PAPER_NEEDS_ATTACK`。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
