---
name: model-comparison
trigger: MODELS_NEED_COMPARISON
description: 用统一数据、指标、约束和计算预算比较候选模型。
---

# Model Comparison

## Trigger
`MODELS_NEED_COMPARISON` 或用户明确要求本局部能力。

## Scope
用统一数据、指标、约束和计算预算比较候选模型。

## Inputs
候选模型、统一评估协议

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
比较矩阵、差异解释、推荐

## Checks
避免因指标方向/样本划分不同制造伪优势；报告复杂度代价。

## Failure
无统一合同则先 `model-contract`。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
