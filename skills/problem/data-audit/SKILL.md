---
name: data-audit
trigger: DATA_UNKNOWN
description: 建立数据事实基线，不凭经验猜结构。
---

# Data Audit

## Trigger
`DATA_UNKNOWN` 或用户明确要求本局部能力。

## Scope
建立数据事实基线，不凭经验猜结构。

## Inputs
原始数据或附件

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
数据档案：字段、形状、类型、单位、缺失、异常、重复、范围

## Checks
实际读取样本与元数据；保留原始数据只读。

## Failure
数据语义不清转 `problem-analysis` 或 `ambiguity-resolution`。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
