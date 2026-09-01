---
name: problem-analysis
trigger: PROBLEM_UNCLEAR
description: 把题面拆为完整问题合同，避免漏问、错问和背景/任务混淆。
---

# Problem Analysis

## Trigger
`PROBLEM_UNCLEAR` 或用户明确要求本局部能力。

## Scope
把题面拆为完整问题合同，避免漏问、错问和背景/任务混淆。

## Inputs
题面、附件说明

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
问题清单、每问六要素、依赖图

## Checks
核对全部显式问题编号；区分事实/任务/约束/输出。

## Failure
若题面本身模糊，转 `ambiguity-resolution`。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
