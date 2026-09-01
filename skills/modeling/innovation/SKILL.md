---
name: innovation
trigger: NEED_LOW_RISK_IMPROVEMENT
description: 从题目结构、约束、数据处理、算法效率和验证设计中生成可验证、可回滚的改进，而不是追求表面复杂度。
---

# innovation

## Trigger

- 事件：`NEED_LOW_RISK_IMPROVEMENT`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

用于已经有 Baseline/MVP，但希望增加有证据的改进。默认偏好低风险、能独立验证的增量，不应在临近提交时诱导大规模重构。

## Inputs

- 当前模型合同
- Baseline/当前结果
- 失败案例或误差来源
- 剩余算力/实现约束（由 Coach 提供）

## Procedure

1. 先定位当前方案真正的瓶颈：模型偏差、数据表示、约束遗漏、求解效率、稳定性、解释性或验证不足。没有问题定义就不生成“创新点”。
2. 按五类产生少量候选：结构化新约束/目标、数据或特征改造、算法/搜索空间改进、机理与数据融合、验证/不确定性增强。
3. 每个候选写清“预期改善什么指标、为什么可能有效、最小实现成本、最大失败风险、如何一键回滚”。
4. 优先选择能在现有 Baseline 上做 A/B 验证的改进，避免一次同时改多个组件导致无法归因。
5. 不使用主观 0-100 Innovation Score 作为科学证据；可以做定性优先级（低/中/高风险或成本）但必须附理由。
6. 若候选改变模型核心假设或问题定义，则不是“低风险改进”，返回 Coach 重新评估。

## Outputs

- 改进候选清单
- 每个候选的机制解释、验证方案和回滚条件
- 推荐的最小实验顺序

## Checks

- 每个候选都与一个已知问题或机会绑定
- 创新不是单纯换更复杂算法
- 可以通过实验判断是否有效
- 失败不会污染原 Baseline

## Failure

- 需要模型重构：返回 `MODEL_UNCERTAIN` 并标为高风险
- 候选需要比较：转 `MODELS_NEED_COMPARISON`
- 实施后效果不稳：转 `RESULT_UNSTABLE`

## Handoff

推荐事件通常是 `IMPLEMENT_MODEL`、`MODELS_NEED_COMPARISON` 或 `EXPERIMENTS_UNTRACKED`。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
