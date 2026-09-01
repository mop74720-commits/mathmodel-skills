---
name: numerical-check
trigger: NUMERICAL_SUSPECT
description: 检查离散误差、容差、随机误差、尺度病态和守恒/边界残差。
---

# Numerical Check

## Trigger
`NUMERICAL_SUSPECT` 或用户明确要求本局部能力。

## Scope
检查离散误差、容差、随机误差、尺度病态和守恒/边界残差。

## Inputs
代码、结果、数值参数

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
收敛/残差/重复运行检查报告

## Checks
优先做步长/容差/种子/尺度对照；报告误差量级而非形容词。

## Failure
不稳定转 robustness。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
