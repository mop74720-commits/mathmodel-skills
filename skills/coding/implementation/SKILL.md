---
name: implementation
trigger: IMPLEMENT_MODEL
description: 把 model contract 实现为最小可运行纵向切片，再扩展到正式计算。
---

# Implementation

## Trigger
`IMPLEMENT_MODEL` 或用户明确要求本局部能力。

## Scope
把 model contract 实现为最小可运行纵向切片，再扩展到正式计算。

## Inputs
模型合同、数据

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
代码、最小运行命令、初始结果

## Checks
不静默改变公式；固定随机性；记录环境与参数。

## Failure
运行失败转 solver-debug；数值异常转 numerical-check。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
