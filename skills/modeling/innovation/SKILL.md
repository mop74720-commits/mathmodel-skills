---
name: innovation
trigger: NEED_LOW_RISK_IMPROVEMENT
description: 生成与题目结构相关、可验证、可回滚的改进候选，不用主观 0-100 分冒充科学评价。
---

# Innovation

## Trigger
`NEED_LOW_RISK_IMPROVEMENT` 或用户明确要求本局部能力。

## Scope
生成与题目结构相关、可验证、可回滚的改进候选，不用主观 0-100 分冒充科学评价。

## Inputs
Baseline、当前模型、失败点/瓶颈

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
创新候选：收益/成本/风险/验证实验

## Checks
优先数据处理、约束、算法效率、验证设计或结构化改进；复杂度本身不算创新。

## Failure
候选交 Coach 取舍，选中后转 implementation/experiment。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
