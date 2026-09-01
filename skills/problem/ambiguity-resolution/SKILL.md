---
name: ambiguity-resolution
trigger: PROBLEM_AMBIGUOUS
description: 对有多种解释的题意建立竞争解释并用递进性、量纲、后续问题边际效果筛选。
---

# Ambiguity Resolution

## Trigger
`PROBLEM_AMBIGUOUS` 或用户明确要求本局部能力。

## Scope
对有多种解释的题意建立竞争解释并用递进性、量纲、后续问题边际效果筛选。

## Inputs
模糊句、上下文、后续问题

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
解释候选、证据、选定解释、回滚条件

## Checks
至少保留一个反例/冲突检查；不得把便利性当唯一理由。

## Failure
仍无法裁决则明确未知项并交 Coach。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
