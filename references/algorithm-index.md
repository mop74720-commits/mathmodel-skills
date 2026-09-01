# Algorithm Index

本索引只用于从问题结构定位模型族，不是“看到关键词就套模型”的菜单。

| 问题结构 | Baseline | 常见候选 | 首要检查 |
|---|---|---|---|
| 线性资源分配 | LP | MILP / robust LP | 变量类型、约束方向、可行性 |
| 路由/调度 | shortest path / assignment | VRP/TSP/MILP/heuristic | 图方向、容量、子回路、时间窗 |
| 连续非线性优化 | local NLP | multi-start / global heuristic | 尺度、初值、约束违反 |
| 时序预测 | naive / seasonal naive | ARIMA/ETS/ML | 时间切分、泄漏、区间 |
| 小样本趋势 | simple regression / naive | grey model / Bayesian | 样本量、假设敏感性 |
| 多指标评价 | equal weight / direct metric | entropy/TOPSIS/AHP/PCA | 指标方向、归一化、权重解释 |
| 分类 | majority / logistic | tree/SVM/boosting | 类别不平衡、泄漏、校准 |
| 聚类 | simple k-means baseline | hierarchical/DBSCAN/GMM | 尺度、簇稳定性、可解释性 |
| 机理动力学 | conservation / simple ODE | ODE/PDE/state-space | 单位、初边值、守恒、刚性 |
| 随机系统 | deterministic baseline | Monte Carlo / Markov | seed、置信区间、收敛 |
| 几何重建 | direct geometry | optimization / distance transform | 坐标、边界、实体尺寸 |

复杂模型只有在 Baseline 无法解释关键结构或性能缺口时才升级。
