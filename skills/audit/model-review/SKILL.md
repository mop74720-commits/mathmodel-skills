---
name: model-review
trigger: MODEL_NEEDS_REVIEW
description: 独立攻击模型合同的正确性、覆盖性、单位、假设、约束和可实现性。
---

# Model Review

## Trigger
`MODEL_NEEDS_REVIEW` 或用户明确要求本局部能力。

## Scope
独立攻击模型合同的正确性、覆盖性、单位、假设、约束和可实现性。

## Inputs
题面、数据事实、模型合同

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
QA 回执

## Checks
reviewer 默认只读；P0 正确性 > P1 复现/一致性 > P2 改进。

## Failure
问题返 modeling。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
