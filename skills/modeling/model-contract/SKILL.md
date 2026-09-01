---
name: model-contract
trigger: MODEL_CONTRACT_MISSING
description: 冻结可执行模型定义，使公式、单位、参数、输入输出与验证可追溯。
---

# Model Contract

## Trigger
`MODEL_CONTRACT_MISSING` 或用户明确要求本局部能力。

## Scope
冻结可执行模型定义，使公式、单位、参数、输入输出与验证可追溯。

## Inputs
选定模型与题面

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
METHOD_CONTRACT.md 建议内容

## Checks
目标/状态或决策变量/参数/约束/初边值/算法/停止条件/验证全部明确。

## Failure
若合同不自洽转 `model-review`。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
