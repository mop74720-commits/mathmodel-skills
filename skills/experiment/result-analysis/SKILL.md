---
name: result-analysis
trigger: RESULT_NEEDS_INTERPRETATION
description: 把运行结果组织成可解释证据：结果是什么、相对 Baseline 如何、为什么、异常在哪里、对题目意味着什么。
---

# result-analysis

## Trigger

- 事件：`RESULT_NEEDS_INTERPRETATION`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

不负责凭空制造“优势”。结果分析应同时呈现主结果、不确定性、对比、机制解释和工程/经济意义。

## Inputs

- Final/Baseline 结果
- 模型合同
- 对比/敏感性/鲁棒性结果（如有）
- 题目评价目标

## Procedure

1. 先核对结果是否回答了问题合同中的“最终必须给出的结论”，缺项先补结果而不是开始写故事。
2. 建立主结果表：关键数字、单位、场景、run_id、约束状态；确保与 Final Run 一致。
3. 与 Baseline/必要候选比较，报告绝对差和相对差；若差异不确定，附分布/区间而不是只报百分比。
4. 解释原因：回到模型结构、约束激活、数据特征或物理机制。不能把“模型更复杂”当原因。
5. 检查异常、边界点和反直觉结果；必要时触发数值或模型复核，避免把异常包装成创新发现。
6. 把数学结果翻译成题目语境：成本、风险、效率、策略、物理行为等，同时避免超出题面/数据范围的外推。
7. 写出限制与适用条件，尤其是敏感参数、未覆盖场景和近似假设。

## Outputs

- 结构化结果分析报告
- 主结果表及 run_id
- Baseline/候选对比
- 机制解释、异常与限制

## Checks

- 所有关键数字都来自可追溯运行
- 结果和题目单位一致
- 相对改进计算口径正确
- 没有把相关性写成因果性
- 异常已核对

## Failure

- 关键数字不一致：转 `FINAL_RESULT_NEEDS_REVIEW`
- 异常疑似数值问题：转 `NUMERICAL_SUSPECT`
- 结论对场景不稳：转 `RESULT_UNSTABLE`

## Handoff

推荐 `RESULT_SECTION_NEEDED`、`FIGURE_NEEDED` 或 `FINAL_RESULT_NEEDS_REVIEW`。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
