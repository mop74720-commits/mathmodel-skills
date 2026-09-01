---
name: result-review
trigger: FINAL_RESULT_NEEDS_REVIEW
description: 对候选 Final Run 做独立复现与关键结论核对。
---

# Result Review

## Trigger
`FINAL_RESULT_NEEDS_REVIEW` 或用户明确要求本局部能力。

## Scope
对候选 Final Run 做独立复现与关键结论核对。

## Inputs
run id、commit、命令、输入、结果

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
Final Run QA 回执

## Checks
核对 seed/参数/commit/结果；论文引用前应唯一化 final run。

## Failure
FAIL 时保持旧 final 不变并返工。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
