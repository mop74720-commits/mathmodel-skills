---
name: nonlinear-optimization
trigger: ALGO_NONLINEAR_OPT
description: 处理连续非线性优化、约束非线性、非凸目标、多起点与全局启发式。
---

# nonlinear-optimization

## Trigger

- 事件：`ALGO_NONLINEAR_OPT`。
- 通常由 `model-selection` 在识别问题结构后路由；用户直接点名该算法族时也可调用。
- 本 Skill 只决定该算法族内的技术路线，不决定比赛阶段、时间预算、是否冻结或提交。

## Scope

用于目标或约束包含连续非线性关系的优化问题。重点是辨别凸/非凸、尺度、初值和约束处理，而不是默认上粒子群/遗传算法。

## Inputs

- 目标与约束的数学表达式
- 变量边界、单位和物理可行域
- 可导性/光滑性信息
- 初值来源和规模
- 是否存在多峰、离散变量或仿真黑箱

## Procedure

1. 先做结构分类：线性/二次/一般光滑 NLP、非光滑、黑箱、凸/疑似非凸。能转凸问题时优先保留凸性。
2. 对变量和残差做尺度检查。量级跨越过大时先无量纲化或变量缩放，避免把数值病态误判为算法失败。
3. 建立局部求解 Baseline：有梯度时优先使用成熟梯度法；无梯度且维度不高时考虑模式搜索/信赖域等。先确认局部方法能稳定得到可行解。
4. 若存在明显多峰或初值敏感性，设计 multi-start/随机重启并记录种子；全局启发式只在局部方法证据显示不足时升级。
5. 约束优先原生处理。惩罚函数需说明惩罚形式和权重选择，检查是否出现“目标更优但约束更差”的假最优。
6. 对候选解计算一阶条件/梯度范数（适用时）、约束违反量、边界活跃情况，并用多个初值或不同 solver 交叉检查。
7. 若最终靠启发式，报告重复运行分布、最好/中位/最差结果和可行率，不把单次最优值当确定事实。

## Decision Rules

- 可解析梯度且维度中高时，优先成熟梯度方法；不要因为“全局算法”名字更高级就默认 PSO/GA。
- 目标连续但非光滑时，先识别 kink 来源；若来自 max/min/absolute value，可考虑引入辅助变量转为更稳定 formulation。
- 黑箱仿真每次评估昂贵时，应评估 surrogate/Bayesian optimization 是否值得，但必须保留真实模型复核。
- 多峰证据应来自多初值、剖面或可视化，不从“算法有随机性”反推问题一定非凸。

## Validation Design

1. 对可导模型用有限差分检查自动/解析梯度。
2. 从边界点、随机点、经验点进行多起点，比较是否收敛到同一 basin。
3. 对最优解做小邻域扰动，确认不是数值噪声形成的尖峰。
4. 在结论重要且环境允许时，用不同机制 solver 或更高精度局部 polish 交叉检查关键 objective/decision 是否一致。
5. 若全局启发式声称改善，必须和相同计算预算下的 multi-start baseline 对比，而不是只比单次局部结果。

## Outputs

- 问题结构与凸性判断
- Baseline 与升级算法路线
- 缩放/初值/边界策略
- 多起点或重复运行设计
- 候选最优解的可行性与稳定性证据

## Checks

- 变量尺度与容差匹配
- 没有用惩罚项掩盖真实约束
- 初值来源可追溯
- 非凸问题不无依据宣称全局最优
- 启发式结果含 seed 和重复运行证据

## Failure

- 局部 solver 发散/NaN：转 `SOLVER_FAILED`
- 结果对容差或尺度高度敏感：转 `NUMERICAL_SUSPECT`
- 模型含关键整数决策：与 `ALGO_LINEAR_INTEGER` 或混合策略联合评估

## Handoff

路线冻结后转 `MODEL_CONTRACT_MISSING` 或 `IMPLEMENT_MODEL`。

统一回执：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。算法 Skill 可以建议下一事件，但不能替 Coach 做阶段或资源决策。
