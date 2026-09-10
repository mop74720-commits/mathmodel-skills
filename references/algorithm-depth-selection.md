# Algorithm Overlap Selection

当前 Hub 与多个数学建模上游资源存在大量同主题重叠。本文件不以“文档更长”自动判优，而把两类能力拆开：

- **原子 algorithm Skill：** 负责触发事件、输入合同、适用/禁用条件、验证设计、失败模式、handoff。
- **algorithm playbook/reference：** 负责同一算法族内部的具体方法选择、实现注意点与更细的验证知识。

2026-09-10 对 `han69611/math-modeling-skills` 做 algorithm-depth audit 后，主路由由 18 个扩展为 **21 个结构性算法族**：新增 Bayesian modeling、signal processing、agent-based modeling。XGBoost、Prophet、VIKOR、NSGA-II、GA/PSO 等仍不成为一级 Router Event。

| Hub family | 典型具体方法 | 深度选择方式 |
|---|---|---|
| linear-integer-optimization | LP / IP / MILP / 0-1 | Hub 合同为主；逻辑排程加载 `constraint-programming.md`，阶段状态结构加载 `dynamic-programming.md` |
| nonlinear-optimization | local NLP / GA / PSO / SA / DE / GWO | Hub + `heuristic-optimization.md`；不确定参数进入决策时加载 `robust-optimization.md`；真实多目标加载 `multi-objective-optimization.md` |
| network-routing | shortest path / MST / flow / matching / TSP / VRP | Hub + `network-search-routing.md`；组合规模大时可与 MILP/CP/heuristic 联用 |
| time-series | naive / ETS / ARIMA / Prophet / ML forecast | Hub 为主；复杂趋势、boosting、ensemble/stacking 加载 `advanced-forecasting.md` |
| grey-forecasting | GM(1,1) / rolling GM / Verhulst | Hub 为主；保留级比、滚动验证与外推边界，不用“小样本必选 GM”捷径 |
| supervised-learning | linear/logistic/tree/KNN/NB/SVM/RF/boosting | Hub + `classification-baselines.md`；时序 boosting/stacking 按 `advanced-forecasting.md` 的时间切分规则 |
| unsupervised-learning | K-means / hierarchy / DBSCAN / GMM / PCA | Hub 为主；稳定性、尺度、cluster validity 和原变量解释必须验证 |
| multi-criteria-evaluation | AHP / entropy / TOPSIS / FCE / VIKOR / GRA | Hub + `fuzzy-comprehensive-evaluation.md`；VIKOR/GRA 加载 `mcdm-extensions.md` |
| efficiency-analysis | DEA CCR/BCC / slack / cross/super efficiency | Hub 为主；先检查 DMU 同质性、维度与极端点 |
| ode-dynamics / pde-dynamics | differential equation modeling | Hub 为主；数值收敛、初边值、守恒与参数可辨识性优先 |
| stochastic-simulation | Monte Carlo / Markov | Hub 为主；报告 CI、收敛、方差缩减，不用单次样本结果 |
| queueing | M/M/1, M/M/c, M/G/1, DES | Hub 为主；先核验到达/服务/稳态条件 |
| system-dynamics | stock-flow / feedback / delay | Hub 为主；政策情景与量纲/时步验证 |
| cellular-automata | traffic / spread / spatial evolution | Hub 为主；格点、邻域、边界、更新顺序和多 seed 可复现 |
| game-theory | Nash / Stackelberg / cooperative / Shapley | Hub 为主；群体策略比例随时间演化时加载 `evolutionary-game.md` |
| statistical-inference | estimation / tests / regression inference | Hub 为主；若核心是 prior→posterior/层级收缩，转 `bayesian-modeling` |
| geometry-reconstruction | geometry / collision / reconstruction | Hub 为主；坐标、有限尺寸和边界容差必须显式 |
| bayesian-modeling | conjugate / Bayesian regression / hierarchical Bayes / HMC | 一级 Skill；重点 prior predictive、sampling diagnostics、posterior predictive 与 prior sensitivity |
| signal-processing | FFT / Welch PSD / STFT / wavelet / filtering | 一级 Skill；重点 sampling、aliasing、spectral leakage、edge effect 与下游 leakage |
| agent-based-modeling | heterogeneous agents / network interaction / individual-based simulation | 一级 Skill；重点规则来源、初始化、调度、多 seed、校准与宏观验证 |

## 不单独升为一级 Skill 的深度主题

- **Robust optimization**：属于优化族内部“不确定性进入决策”的 formulation 深度，而不是实验层 `robustness` 的同义词；加载 `robust-optimization.md`。
- **Multi-objective optimization**：属于优化 formulation 深度；加载 `multi-objective-optimization.md`。
- **Constraint Programming / CP-SAT**：属于离散约束求解深度；加载 `constraint-programming.md`。
- **Dynamic Programming**：属于具有充分状态和 Bellman recurrence 的求解结构；加载 `dynamic-programming.md`。
- **Evolutionary game**：属于 game-theory 的动力学扩展；加载 `evolutionary-game.md`。
- **VIKOR / GRA**：属于 MCDM 内部方法；加载 `mcdm-extensions.md`。
- **Prophet / boosting forecast / stacking**：属于 forecasting 内部模型；加载 `advanced-forecasting.md`。

## 选择协议

1. 先用 `model-selection` / `algorithm-index.md` 识别一个 primary family。
2. 原子 Skill 先建立 baseline、适用条件和验证合同。
3. 只有当当前问题出现明确深度结构时加载一个相关 playbook，不预加载全部算法百科。
4. 具体方法必须给出 `deciding evidence / failure condition / fallback`；不能仅凭名称、流行度或上游获奖案例选用。
5. 上游历史经验只用于产生候选 prior，不替代当前数据、约束和验证证据。

上游公式、代码与例子只作为能力覆盖对照，本包保持独立重写，不复制大段算法正文或实现。
