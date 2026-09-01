---
name: hypothesis
trigger: ASSUMPTION_WEAK
description: 把建模假设变成可审计的前提：来源、必要性、可验证性、影响和失效风险。
---

# hypothesis

## Trigger

- 事件：`ASSUMPTION_WEAK`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

用于题面不足以闭合模型、已有假设缺乏依据、或假设可能显著影响结论的情形。假设不是为了“凑论文格式”，也不是先选模型后倒推理由。

## Inputs

- 问题合同
- 数据审计
- 候选模型（如已有）
- 领域常识/文献证据（如有）

## Procedure

1. 列出真正需要补充的未知前提，并区分：结构假设、分布假设、边界/初始条件、独立性假设、稳定性/平稳性假设、工程简化。
2. 对每条假设填写五项：为什么需要、依据来自哪里、它改变了哪个方程/变量/约束、能否验证、失效时结论会怎样。
3. 优先验证可由当前数据直接检验的假设；不能验证的假设必须写成限制，而不是写成事实。
4. 建立“假设 → 模型组件”映射，识别哪些假设是高影响前提；高影响且不确定的假设应进入敏感性或鲁棒性计划。
5. 删除没有作用的装饰性假设，以及与题面事实重复的“伪假设”。
6. 若两个候选模型依赖不同关键假设，不在此处直接选模型，交给 `model-selection` 或 `model-comparison`。

## Outputs

- 假设登记表（建议并入 `problem/ASSUMPTIONS.md`）
- 假设-模型影响映射
- 需验证/需敏感性分析的高风险假设清单

## Checks

- 每条假设都能指出对模型的具体影响
- 可验证假设已经给出验证方法
- 不可验证假设没有被包装成“已证实”
- 不存在仅为迎合某算法而添加的假设

## Failure

- 关键假设被数据反驳：返回 `MODEL_UNCERTAIN` 或修订模型
- 关键假设不可验证且结论高度依赖：推荐 `NEED_SENSITIVITY`/`RESULT_UNSTABLE`
- 假设明确后模型定义仍缺：转 `MODEL_CONTRACT_MISSING`

## Handoff

返回假设状态和高风险项；是否接受高风险假设继续，由 Coach 决定。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
