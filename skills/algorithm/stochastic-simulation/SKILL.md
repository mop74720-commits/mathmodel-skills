---
name: stochastic-simulation
trigger: ALGO_STOCHASTIC_SIM
description: 处理 Monte Carlo、随机过程、Markov 链、随机仿真与概率估计。
---

# stochastic-simulation

## Trigger

- 事件：`ALGO_STOCHASTIC_SIM`。
- 通常由 `model-selection` 在识别问题结构后路由；用户直接点名该算法族时也可调用。
- 本 Skill 只决定该算法族内的技术路线，不决定比赛阶段、时间预算、是否冻结或提交。

## Scope

当系统含随机输入、随机转移或需要通过采样估计概率/期望/风险时使用。核心是抽样机制、seed、收敛和置信区间。

## Inputs

- 随机变量/分布或转移机制
- 目标统计量：概率/期望/分位数/风险
- 样本依赖结构
- 仿真预算与精度要求
- 是否有解析/确定性 Baseline

## Procedure

1. 明确随机性的来源和分布依据，区分题面给定、数据拟合和人为假设；不把“随机”当不确定信息的万能替代。
2. 建立确定性或低成本 Baseline，能解析计算的部分不应全部靠 Monte Carlo。
3. 固定主随机种子并允许独立重复 seed；记录 PRNG、样本量和抽样方案。
4. 对概率/期望估计报告 Monte Carlo 标准误或置信区间，检查样本量增加时估计是否收敛。
5. 稀有事件或高方差问题考虑重要抽样、分层抽样、控制变量等方差缩减，并用无偏性/权重公式检查。
6. Markov 模型检查转移矩阵行和、状态定义、周期性/不可约性；需要稳态时验证收敛条件。
7. 若模拟路径有时间依赖，保持相关结构，不把独立抽样错误套到相关过程。

## Decision Rules

- 若随机变量只是“参数不知道”，先区分 epistemic uncertainty 与 aleatory randomness；前者可能更适合场景/区间分析。
- 估计极小概率时，朴素 Monte Carlo 可能需要不可接受样本量，应基于目标相对误差评估是否需要稀有事件方法。
- Markov 状态划分过粗会失去记忆性，过细又导致估计不稳；状态设计必须与题目机制一致。
- 相关随机变量不能独立采样；相关结构/copula/联合分布需有依据。

## Validation Design

1. 随样本量递增画估计值和 CI 收敛，不只给最终 N。
2. 用多个独立 seed 复核标准误。
3. 若有解析均值/方差或简单情形，用仿真复现这些基准。
4. Markov 链检查经验长期频率与理论稳态（若存在）一致。
5. 方差缩减方法必须与朴素 Monte Carlo 在相同计算预算下比较效率。

## Outputs

- 随机机制与分布依据
- seed/样本量/抽样合同
- 估计值与不确定性区间
- 收敛或方差缩减证据
- Markov/随机过程结构检查

## Checks

- 所有随机运行可由 seed 复现
- 概率估计附抽样误差
- 样本量增长时关键统计量趋稳
- 转移矩阵与状态空间合法
- 未把单次模拟轨迹当期望行为

## Failure

- 结果对 seed 高度敏感：转 `RESULT_UNSTABLE`
- 分布假设证据弱：转 `ASSUMPTION_WEAK`
- 仿真成本过高：转 `NEED_LOW_RISK_IMPROVEMENT` 寻找方差缩减/代理模型

## Handoff

实现后通常接 `NEED_SENSITIVITY` 或 `RESULT_UNSTABLE`。

统一回执：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。算法 Skill 可以建议下一事件，但不能替 Coach 做阶段或资源决策。
