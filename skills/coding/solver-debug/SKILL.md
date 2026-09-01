---
name: solver-debug
trigger: SOLVER_FAILED
description: 定位 infeasible、diverge、timeout、NaN、收敛失败等求解器问题。
---

# Solver Debug

## Trigger
`SOLVER_FAILED` 或用户明确要求本局部能力。

## Scope
定位 infeasible、diverge、timeout、NaN、收敛失败等求解器问题。

## Inputs
错误日志、模型合同、最小实例

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
故障分类、最小复现、修复建议

## Checks
区分实现 bug、数值条件差、模型不可行、求解器配置问题；不得通过删约束“修好”。

## Failure
若模型本身冲突，handoff modeling。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
