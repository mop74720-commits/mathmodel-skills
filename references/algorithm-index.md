# Algorithm Knowledge Index

本索引负责从“问题结构”路由到算法族 Skill。它不是按关键词套算法的菜单，也不决定比赛阶段。

| 结构信号 | Primary event | Baseline 思路 | 首要风险 |
|---|---|---|---|
| 线性目标/约束，含连续、整数、0-1变量 | `ALGO_LINEAR_INTEGER` | LP / 简单 MILP | 可行性、Big-M、整数回代 |
| 连续非线性、黑箱、多峰 | `ALGO_NONLINEAR_OPT` | 局部 NLP | 尺度、初值、非凸、约束处理 |
| 节点/边/路径/流/车辆/时间窗 | `ALGO_NETWORK_ROUTING` | shortest path / assignment | 负权、容量、子回路、未来信息 |
| 时间有序、预测未来 | `ALGO_TIME_SERIES` | naive / seasonal naive | 泄漏、切分、结构突变 |
| 有标签回归/分类 | `ALGO_SUPERVISED_LEARNING` | linear/logistic/majority | split 泄漏、不平衡、校准 |
| 无标签分群/降维 | `ALGO_UNSUPERVISED_LEARNING` | k-means / PCA | 距离尺度、稳定性、伪解释 |
| 多指标综合排序/评价 | `ALGO_MULTI_CRITERIA` | 等权归一化 | 指标方向、权重、排名稳定性 |
| 时间连续动力学、状态方程 | `ALGO_ODE_DYNAMICS` | 简化 ODE | 单位、刚性、守恒、可辨识性 |
| 空间+时间场、边界条件 | `ALGO_PDE_DYNAMICS` | 简化 PDE/解析特例 | 适定性、网格、稳定性、收敛 |
| 随机输入、概率/期望、Markov | `ALGO_STOCHASTIC_SIM` | 解析/确定性近似 | seed、方差、CI、收敛 |
| 参数估计、差异检验、效应判断 | `ALGO_STATISTICAL_INFERENCE` | 描述统计/简单检验 | 独立性、效应量、多重比较 |
| 几何边界、姿态、碰撞、重建 | `ALGO_GEOMETRY` | 解析几何 | 坐标、实体尺寸、边界容差 |

## 混合问题的组合规则

- 优先识别“决定结论的主结构”，只加载一个 primary algorithm Skill。
- Secondary 只用于明确耦合，例如 `network-routing + linear-integer-optimization`、`ODE + nonlinear-optimization`。
- 同一模型族的不同 solver/超参数不算新的 algorithm Skill。
- 如果算法选择会改变假设或问题定义，必须回到 `ASSUMPTION_WEAK` / `PROBLEM_AMBIGUOUS`，不能在算法层偷偷改题。

## 升级原则

复杂方法只有在 Baseline 暴露了明确缺口后升级。升级证据可以是：约束无法表达、系统性偏差、泛化缺口、计算复杂度、非线性/随机结构或验证结果，而不是“看起来更高级”。
