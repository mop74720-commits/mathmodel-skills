---
name: robustness
trigger: RESULT_UNSTABLE
description: 识别结论对种子、采样、边界条件、参数区间或数据扰动的稳定性。
---

# Robustness

## Trigger
`RESULT_UNSTABLE` 或用户明确要求本局部能力。

## Scope
识别结论对种子、采样、边界条件、参数区间或数据扰动的稳定性。

## Inputs
模型、结果、扰动方案

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
稳健性报告、稳定/不稳定结论

## Checks
区分统计随机性与数值误差；不能只挑有利 seed。

## Failure
若根因数值转 numerical-check；模型结构转 model-selection。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
