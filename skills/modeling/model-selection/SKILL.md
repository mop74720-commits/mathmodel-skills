---
name: model-selection
trigger: MODEL_UNCERTAIN
description: 基于任务类型、数据规模、可解释性、约束与验证成本选择 Baseline + 首选 + 必要备选。
---

# Model Selection

## Trigger
`MODEL_UNCERTAIN` 或用户明确要求本局部能力。

## Scope
基于任务类型、数据规模、可解释性、约束与验证成本选择 Baseline + 首选 + 必要备选。

## Inputs
问题合同、数据审计、假设

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
模型候选表和推荐顺序

## Checks
必须有 Baseline；最多推荐少数真正独立模型族；写明失败模式。

## Failure
需定量比较时转 `model-comparison`。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
