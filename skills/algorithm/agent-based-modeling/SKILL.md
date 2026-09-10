---
name: agent-based-modeling
trigger: ALGO_AGENT_BASED_MODELING
description: 处理异质个体、行为规则、局部交互与涌现结果的 Agent-Based Modeling，强调微观规则依据、初始化、校准、多种子与宏观验证。
---

# agent-based-modeling

## Trigger

- 事件：`ALGO_AGENT_BASED_MODELING`。
- 当独立个体具有不同属性、状态、行为与交互网络，且宏观结果由微观交互涌现时调用。
- 用户点名 ABM / agent-based simulation / individual-based model 时也可调用，但必须先证明“个体异质性”是决定性结构，而不是为了动画效果。

## Scope

覆盖个体代理、环境、行为规则、交互网络、调度机制、随机事件与宏观统计的建模。若系统核心是规则固定的空间格点，优先 `ALGO_CELLULAR_AUTOMATA`；若核心是库存—流量—反馈的宏观长期变化，优先 `ALGO_SYSTEM_DYNAMICS`；若个体互动本质是策略均衡，则与 `ALGO_GAME_THEORY` 联用。

## Inputs

- Agent 类型、属性、状态变量和数量
- 环境/空间/网络结构
- 行为规则、决策机制和交互范围
- 初始化分布和随机机制
- 可观测宏观统计或校准目标
- 仿真 horizon、时间步/事件调度方式与计算预算

## Procedure

1. 先写 Agent Contract：每类 agent 能看到什么、能做什么、何时行动、状态如何变化；区分题面事实、数据估计和行为假设。
2. 建立最小同质或聚合 Baseline，只有当异质性、局部交互或适应行为显著改变结论时才保留 ABM。
3. 明确环境与交互拓扑：格点、连续空间、固定网络或动态网络；不得让代码默认邻接关系偷偷成为模型假设。
4. 规定调度机制：同步、随机顺序、事件驱动或优先级更新，并测试更新顺序是否影响主结论。
5. 初始化 agent 数量、属性分布与网络；若来自数据，记录映射和抽样；若是假设，纳入敏感性。
6. 先跑小规模/极端情形，检查守恒、边界、不可行行为和规则冲突，再扩展到正式规模。
7. 校准时只使用少数可辨识的宏观统计量，不为匹配一条曲线不断添加自由参数；校准集与验证场景尽量分离。
8. 随机模型使用多 seed 独立重复，报告均值、区间和分布，而不是挑一条“最好看”的轨迹。
9. 最终把微观规则与宏观涌现建立解释链：哪些规则/异质性导致了哪些可观察结果，并通过消融或替代规则验证。

## Decision Rules

- 个体没有独立状态/行为、只有格点局部更新：优先 CA。
- 只有总体库存/流量而个体差异不影响结论：优先系统动力学或 ODE。
- 多主体目标函数和最优反应是核心：优先博弈论；ABM 只在有限理性、学习或复杂互动需要仿真时作为补充。
- 参数数量明显超过可观测统计所能约束的程度时，先简化规则，不用更多校准轮次掩盖不可辨识性。
- ABM 结果若不能在宏观指标上验证，只能作为机制情景，不应宣称精确预测。

## Validation Design

1. 规则级单元测试：给定固定状态时，agent 行为必须与合同一致。
2. 退化测试：关闭交互/异质性/随机性后，结果应接近对应聚合 Baseline 或可解释极限。
3. 多 seed 重复并报告 Monte Carlo 不确定性；必要时检查仿真长度与 agent 数量收敛。
4. 调度敏感性：同步/异步或随机顺序变化是否翻转结论。
5. 参数/规则消融：移除关键机制后宏观特征是否按理论预期消失或减弱。
6. 用未参与校准的时间段、空间区域或情景验证宏观统计；没有外部验证时明确标注证据等级。

## Outputs

- Agent / Environment / Interaction Contract
- 初始化、调度与随机机制
- Baseline 与采用 ABM 的结构理由
- 宏观指标、重复运行区间和涌现解释
- 校准/验证结果与规则消融
- 失效边界、计算风险和 fallback

## Checks

- 每条关键行为规则有事实、数据或显式假设来源
- 更新顺序和邻接机制明确
- 随机结果有 seed 与重复运行
- 校准参数没有明显不可辨识却被当成精确事实
- 结果不是只靠动画或单次轨迹证明
- 微观规则到宏观结论有可审计的机制链

## Failure

- 宏观结果对 seed/初始化/调度高度敏感：转 `RESULT_UNSTABLE`。
- 行为参数缺乏依据且主结论依赖它们：转 `ASSUMPTION_WEAK`。
- 个体异质性没有带来可验证增益：退回 `ALGO_SYSTEM_DYNAMICS` / `ALGO_ODE_DYNAMICS` / 简化模型。
- 计算成本过高而结论只需聚合统计：转 `NEED_LOW_RISK_IMPROVEMENT` 评估代理/降维或聚合模型。

## Handoff

合同稳定后转 `MODEL_CONTRACT_MISSING`；实现复杂时转 `IMPLEMENT_MODEL`；结果需要多情景/多种子审查时转 `RESULT_UNSTABLE`。

统一回执：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。算法 Skill 可以建议下一事件，但不能替 Coach 做阶段或资源决策。
