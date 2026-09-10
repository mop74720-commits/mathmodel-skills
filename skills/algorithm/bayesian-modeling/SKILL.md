---
name: bayesian-modeling
trigger: ALGO_BAYESIAN_MODELING
description: 处理先验—似然—后验、层级模型、贝叶斯回归与后验预测，强调先验来源、可识别性、采样诊断和预测校准。
---

# bayesian-modeling

## Trigger

- 事件：`ALGO_BAYESIAN_MODELING`。
- 当问题需要显式表达参数不确定性、融合先验信息、处理层级/部分池化结构，或需要完整后验而非单点估计时调用。
- 用户直接点名 Bayesian / hierarchical Bayes / posterior inference 时也可调用，但仍先检查是否真的需要贝叶斯结构。

## Scope

覆盖共轭或数值贝叶斯推断、贝叶斯回归、层级模型、状态/参数后验与 posterior predictive。它不把“用了 MCMC”当创新，也不把主观先验包装成客观事实。若任务只是普通显著性检验或大样本点预测，优先考虑更简单的统计推断/监督学习 Baseline。

## Inputs

- 目标参数、潜变量与观测变量定义
- likelihood / 数据生成假设
- prior 来源、尺度与可解释范围
- 层级/分组结构与样本量
- 需要的决策量：后验均值、区间、概率、预测分布或风险
- 可用计算预算与推断后端

## Procedure

1. 先写生成模型：明确 `p(y|theta)`、参数约束和必要潜变量；区分数据事实、先验知识和纯建模假设。
2. 建立非贝叶斯或弱先验 Baseline，确认贝叶斯方案解决的是真实缺口，例如小样本稳定性、层级收缩、完整不确定性或先验融合。
3. 设计 prior：优先弱信息、领域可解释或历史数据可追溯的先验；对关键尺度参数检查 prior predictive 是否产生明显不合理样本。
4. 若有层级结构，明确组内/组间参数和 partial pooling；不要把每组独立拟合或完全合并冒充层级模型。
5. 选择推断机制：低维共轭/可解析时优先解析；一般连续模型使用 HMC/NUTS 等成熟采样；离散潜变量或复杂结构根据可行性选择枚举、边缘化、变分或其他方法。
6. 运行诊断：多链、R-hat、ESS、divergence、trace/energy 等适用指标；采样器“完成”不等于后验可信。
7. 做 posterior predictive check，检查模型能否复现决定结论的统计结构；对关键先验做敏感性分析。
8. 把后验转为题目真正需要的量，例如 `P(theta>threshold|data)`、预测区间、风险概率或决策效用，不只报一张后验密度图。

## Decision Rules

- 若数据量充分、目标只是稳定点预测且不确定性不是决策关键，先用频率学派/监督学习 Baseline。
- 若存在自然分组且每组样本偏少，层级 Bayes 可作为候选，但必须证明 partial pooling 比完全池化/独立拟合更合理。
- prior 对结论高度敏感时，结论应降级为条件性结果；不得选择“让结果好看”的先验。
- Bayesian optimization 属于昂贵黑箱优化的序贯策略，不等于 Bayesian modeling；需要时与 `ALGO_NONLINEAR_OPT` 组合。
- 普通回归换成 Bayesian regression 本身不构成创新，只有当后验结构解决了可验证问题才保留。

## Validation Design

1. Prior predictive：检查先验是否允许物理/业务上荒谬的数量级。
2. Sampling diagnostics：多链 R-hat、ESS、divergence 与必要的 reparameterization 检查。
3. Posterior predictive：比较关键统计量、残差、尾部/分组结构，而不是只看均值拟合。
4. Prior sensitivity：至少比较合理的弱信息/领域先验候选，报告结论是否翻转。
5. Simulation-based calibration 或合成数据回收参数，在模型重要且预算允许时验证推断链。
6. 与简单 Baseline 在同一预测/决策指标上比较，避免只比较训练内 log posterior。

## Outputs

- 生成模型与变量关系
- prior/likelihood 及来源说明
- 推断方法和计算设置
- 后验摘要、credible interval / posterior probability
- posterior predictive 与采样诊断
- prior sensitivity、适用边界和必要 fallback

## Checks

- 先验来源和尺度可追溯
- posterior 区间没有错误称为 frequentist confidence interval
- MCMC 有收敛/有效样本诊断
- 层级参数的可识别性与组样本量已检查
- 后验预测与题目主结论直接关联
- 结论未由单个武断 prior 驱动

## Failure

- 后验强依赖先验且数据无法更新：转 `ASSUMPTION_WEAK`。
- 采样 divergence / R-hat 异常 / ESS 过低：转 `NUMERICAL_SUSPECT` 或重参数化。
- 模型结构无法由数据辨识：返回 `MODEL_UNCERTAIN` 并简化参数化。
- 目标其实是纯预测且贝叶斯方案无额外价值：转 `ALGO_SUPERVISED_LEARNING` / `ALGO_TIME_SERIES`。

## Handoff

模型定义稳定后转 `MODEL_CONTRACT_MISSING`；需要实现时转 `IMPLEMENT_MODEL`；若后验结论依赖先验或场景，转 `NEED_SENSITIVITY` / `RESULT_UNSTABLE`。

统一回执：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。算法 Skill 可以建议下一事件，但不能替 Coach 做阶段或资源决策。
