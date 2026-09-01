---
name: outline
trigger: PAPER_OUTLINE_NEEDED
description: 从问题结构和证据链组织论文，不按固定模板机械凑章节。
---

# Outline

## Trigger
`PAPER_OUTLINE_NEEDED` 或用户明确要求本局部能力。

## Scope
从问题结构和证据链组织论文，不按固定模板机械凑章节。

## Inputs
题面、模型合同、结果、claim-evidence

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
章节大纲与每节证据落点

## Checks
每个子问题都有结论、公式/算法、结果和验证落点。

## Failure
缺证据转 claim-evidence。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
