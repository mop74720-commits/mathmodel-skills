---
name: sensitivity
trigger: NEED_SENSITIVITY
description: 量化关键参数/假设扰动对目标和结论的影响。
---

# Sensitivity

## Trigger
`NEED_SENSITIVITY` 或用户明确要求本局部能力。

## Scope
量化关键参数/假设扰动对目标和结论的影响。

## Inputs
冻结模型、基准参数、合理扰动域

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
敏感度表/曲线、质变点

## Checks
扰动范围要有依据；整数优化不用连续对偶量替代真实重算。

## Failure
出现结论翻转转 robustness。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
