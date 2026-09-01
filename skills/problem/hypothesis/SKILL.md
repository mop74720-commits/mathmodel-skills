---
name: hypothesis
trigger: ASSUMPTION_WEAK
description: 把假设视为模型前提，记录理由、可验证性、影响和失效风险。
---

# Hypothesis

## Trigger
`ASSUMPTION_WEAK` 或用户明确要求本局部能力。

## Scope
把假设视为模型前提，记录理由、可验证性、影响和失效风险。

## Inputs
问题合同、数据事实、候选模型

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
假设表：内容/依据/影响/验证/失效后果

## Checks
每条假设必须在模型中有用途；区分事实、近似和人为选择。

## Failure
直接改变模型族时转 `model-selection`。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
