---
name: result-analysis
trigger: RESULT_NEEDS_INTERPRETATION
description: 把结果从“报数字”提升为 Baseline 对比、原因解释、异常和决策含义。
---

# Result Analysis

## Trigger
`RESULT_NEEDS_INTERPRETATION` 或用户明确要求本局部能力。

## Scope
把结果从“报数字”提升为 Baseline 对比、原因解释、异常和决策含义。

## Inputs
最终/候选结果、Baseline、题目目标

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
RESULTS_ANALYSIS.md 建议内容

## Checks
只有存在重复样本与合适设计时才做显著性检验；不要机械套 t-test。

## Failure
需要论文表述转 result-writing。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
