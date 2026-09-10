# Robust Optimization Playbook

鲁棒优化用于“参数不确定性会直接改变可行性或最优决策”的问题。它不同于赛后做敏感性分析：鲁棒性必须进入优化模型本身。

## 1. 先确定不确定性类型

- 区间/集合已知但无可靠概率：优先 deterministic robust optimization。
- 有可信概率分布且允许违约概率：可考虑 chance-constrained / stochastic programming。
- 分布本身不确定：只有在样本和任务确实支持时才考虑 distributionally robust optimization；不要为高级感默认 DRO。

## 2. 最小路线

1. 建 nominal model，保存最优值、可行裕度和关键 active constraints。
2. 列出真正不确定的参数，不把所有常数都变成区间。
3. 为每类参数定义 uncertainty set，并记录边界来源；区间宽度不能凭空取固定百分比。
4. 推导 robust counterpart 或通过 scenario/cutting-plane 等方法求解。
5. 与 nominal 解比较 objective loss、worst-case feasibility、关键决策变化，报告 price of robustness。
6. 用独立压力场景验证，不只在构造 uncertainty set 的边界上自证。

## 3. 常见结构

- Box uncertainty：保守、易解释，适合独立区间但可能过度悲观。
- Budgeted uncertainty：允许只有部分系数同时达到极端值；预算参数必须有业务解释并做曲线。
- Ellipsoidal uncertainty：适合相关连续扰动，但尺度/协方差来源要可追溯。
- Chance constraints：必须明确概率分布、允许违约概率与近似误差。
- Two-stage / recourse：区分事前决策和观察不确定性后的补救决策，禁止使用未来信息。

## 4. 验证

- nominal 与 robust 使用同一目标、单位和基础约束。
- 扫描 uncertainty budget，画成本—风险/可行率 Pareto 曲线。
- 在 out-of-set 或留出情景中检查实际违约率。
- 若鲁棒解与 nominal 解完全相同，解释是否因为约束有足够 slack，而不是宣称方法必然有效。
- 若鲁棒代价巨大，检查 uncertainty set 是否过宽或结构设定错误。

## 5. 失效与回退

- 不确定性只影响结果解释而不影响决策：用 sensitivity/robustness review，不必鲁棒优化。
- 概率结构强且有充分数据：随机规划可能优于纯 worst-case。
- 模型已经是高维黑箱：先做 scenario optimization / simulation stress-test，再决定是否需要复杂 robust counterpart。

论文中至少报告：不确定参数、集合来源、nominal benchmark、鲁棒解、price of robustness、独立压力测试和结论翻转边界。
