---
name: paper-review
trigger: PAPER_NEEDS_ATTACK
description: 以严格评委视角审查数学、逻辑、证据、图表、夸大、可读性和 AI 痕迹。
---

# Paper Review

## Trigger
`PAPER_NEEDS_ATTACK` 或用户明确要求本局部能力。

## Scope
以严格评委视角审查数学、逻辑、证据、图表、夸大、可读性和 AI 痕迹。

## Inputs
论文、claim-evidence、官方规则

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
按严重度排序的问题清单

## Checks
不输出伪官方总分；用 P0/P1/P2 + 风险说明；不直接改正文。

## Failure
修订后可复验。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
