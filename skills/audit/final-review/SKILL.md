---
name: final-review
trigger: PRE_SUBMISSION
description: 提交前做有限且高价值的最终审计：官方硬约束、PDF视觉、数字一致、引用、附件、AI声明。
---

# Final Review

## Trigger
`PRE_SUBMISSION` 或用户明确要求本局部能力。

## Scope
提交前做有限且高价值的最终审计：官方硬约束、PDF视觉、数字一致、引用、附件、AI声明。

## Inputs
最终论文、final run、规则、附件

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
提交前 QA 回执

## Checks
最后阶段不主动发明新模型；P0 错误必须暴露，格式细节不得掩盖科学错误。

## Failure
最终裁决交 Coach/团队。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
