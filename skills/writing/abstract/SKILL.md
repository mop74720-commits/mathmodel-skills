---
name: abstract
trigger: ABSTRACT_NEEDED
description: 用已冻结结果写摘要：问题→方法→关键结果→验证/价值。
---

# Abstract

## Trigger
`ABSTRACT_NEEDED` 或用户明确要求本局部能力。

## Scope
用已冻结结果写摘要：问题→方法→关键结果→验证/价值。

## Inputs
最终结果、模型名、题目

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
摘要草稿事实清单/写作指引

## Checks
关键数字必须从 final result 复制；背景从简；不写未验证创新。

## Failure
结果未冻结则不生成定稿。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
