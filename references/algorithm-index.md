# Algorithm Knowledge Index

本索引负责从“问题结构”路由到算法族 Skill。它不是按关键词套算法的菜单，也不决定比赛阶段。

| 结构信号 | Primary event | Baseline 思路 | 首要风险 |
|---|---|---|---|
| 线性目标/约束，含连续、整数、0-1变量 | `ALGO_LINEAR_INTEGER` | LP / 简单 MILP | 可行性、Big-M、整数回代 |
| 连续非线性、黑箱、多峰 | `ALGO_NONLINEAR_OPT` | 局部 NLP | 尺度、初值、非凸、约束处理 |
| 节点/边/路径/流/车辆/时间窗 | `ALGO_NETWORK_ROUTING` | shortest path / assignment | 负权、容量、子回路、未来信息 |
| 时间有序、预测未来 | `ALGO_TIME_SERIES` | naive / seasonal naive | 泄漏、切分、结构突变 |
| 小样本、信息不完全、平滑趋势 | `ALGO_GREY_FORECAST` | naive / linear trend | 适用性、训练内拟合冒充外推 |
| 有标签回归/分类 | `ALGO_SUPERVISED_LEARNING` | linear/logistic/majority | split 泄漏、不平衡、校准 |
| 无标签分群/降维 | `ALGO_UNSUPERVISED_LEARNING` | k-means / PCA | 距离尺度、稳定性、伪解释 |
| 多指标综合排序/评价 | `ALGO_MULTI_CRITERIA` | 等权归一化 | 指标方向、权重、排名稳定性 |
| 多投入多产出相对效率/前沿 | `ALGO_EFFICIENCY_ANALYSIS` | 描述性投入产出比 | DMU同质性、维度、极端点 |
| 时间连续动力学、状态方程 | `ALGO_ODE_DYNAMICS` | 简化 ODE | 单位、刚性、守恒、可辨识性 |
| 空间+时间场、边界条件 | `ALGO_PDE_DYNAMICS` | 简化 PDE/解析特例 | 适定性、网格、稳定性、收敛 |
| 随机输入、概率/期望、Markov | `ALGO_STOCHASTIC_SIM` | 解析/确定性近似 | seed、方差、CI、收敛 |
| 到达—服务—等待/拥堵 | `ALGO_QUEUEING` | 经典 M/M/c 或简单仿真 | 稳态、分布假设、warm-up |
| 库存—流量—反馈—时滞 | `ALGO_SYSTEM_DYNAMICS` | 简化 stock-flow | 因果、量纲、延迟、步长 |
| 空间格点+局部更新规则 | `ALGO_CELLULAR_AUTOMATA` | 最小规则 CA | 网格尺度、边界、seed |
| 多自主主体策略相互依赖 | `ALGO_GAME_THEORY` | 简单收益矩阵/集中式基准 | 收益依据、信息结构、多均衡 |
| 参数估计、差异检验、效应判断 | `ALGO_STATISTICAL_INFERENCE` | 描述统计/简单检验 | 独立性、效应量、多重比较 |
| 几何边界、姿态、碰撞、重建 | `ALGO_GEOMETRY` | 解析几何 | 坐标、实体尺寸、边界容差 |
| 先验信息、层级/部分池化、完整参数后验 | `ALGO_BAYESIAN_MODELING` | 频率学派/弱先验模型 | 先验敏感、不可辨识、采样诊断 |
| 采样信号、频率/时频、滤波/去噪 | `ALGO_SIGNAL_PROCESSING` | 原始时域统计 / FFT baseline | aliasing、谱泄漏、边界效应、泄漏 |
| 异质自主个体+环境/网络交互产生涌现 | `ALGO_AGENT_BASED_MODELING` | 聚合/同质模型 | 规则依据、校准、seed、调度敏感 |

## 混合问题的组合规则

- 优先识别“决定结论的主结构”，只加载一个 primary algorithm Skill。
- Secondary 只用于明确耦合，例如 `network-routing + linear-integer-optimization`、`ODE + nonlinear-optimization`、`game-theory + agent-based-modeling`。
- 同一模型族的不同 solver/超参数不算新的 algorithm Skill。
- 如果算法选择会改变假设或问题定义，必须回到 `ASSUMPTION_WEAK` / `PROBLEM_AMBIGUOUS`，不能在算法层偷偷改题。

## 深度方法按需加载

具体算法不继续膨胀 Router event。需要时按 `references/algorithm-depth-selection.md` 加载 `references/algorithm-playbooks/*`，例如 robust / multi-objective optimization、CP-SAT、DP、evolutionary game、VIKOR/GRA、Prophet/boosting/stacking。算法名本身不是一级路由依据。

## 升级原则

复杂方法只有在 Baseline 暴露了明确缺口后升级。升级证据可以是：约束无法表达、系统性偏差、泛化缺口、计算复杂度、非线性/随机结构或验证结果，而不是“看起来更高级”。
