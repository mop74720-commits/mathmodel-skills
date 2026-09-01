# Algorithm Overlap Selection

当前 Hub 与 XiaoMa 算法资源存在大量同主题重叠。v0.1.6 不以“文档更长”自动判优，而把两类优势拆开：

- **当前原子 algorithm Skill 胜出：** 触发事件、输入合同、适用/禁用条件、验证设计、失败模式、handoff。
- **XiaoMa 算法资源胜出：** 传统算法覆盖广、公式/实现提示/可视化示例更多。

因此主路由继续指向当前 18 个原子 Skill；需要深挖时读取独立 playbook/reference，而不是把七个大百科文件变成总入口。

| Hub family | 与上游重叠的典型算法 | 选择方式 |
|---|---|---|
| linear-integer-optimization | LP / IP / DP | Hub 合同为主；实现时补 solver/松弛/整数性检查 |
| nonlinear-optimization | GA / PSO / SA / DE / GWO 等 | Hub 结构 + `heuristic-optimization.md`；必须多 seed / baseline |
| grey-forecasting | GM 系列 | Hub 为主；保留级比、残差、后验/相对误差等检验思想，不用“小样本必选 GM”捷径 |
| time-series | ARIMA / exponential smoothing / regression / ML forecast | Hub 为主；按平稳性、滚动验证和泄漏检查选模型 |
| multi-criteria-evaluation | AHP / fuzzy-AHP / entropy / TOPSIS / GRA | Hub 为主；方法深度按需参考，主观权重必须做一致性/敏感性检查 |
| network-routing | shortest path / MST / flow / Euler/Hamilton / matching | Hub 为主；按图结构和约束选择算法，不把某单一图算法当万能 routing |
| statistical-inference | preprocessing / hypothesis tests / PCA/FA/CCA | Hub 为主；检验前检查假设与多重比较，降维后解释载荷而不是只报图 |
| unsupervised-learning | K-means / hierarchy / DBSCAN / GMM | Hub 为主；稳定性、尺度、cluster validity 必须验证 |
| supervised-learning | logistic/tree/KNN/NB/SVM/RF/boosting | Hub 为主 + classification playbook；严格防数据泄漏并使用合适评分 |
| stochastic-simulation | Monte Carlo | Hub 为主；报告随机误差、方差缩减和收敛，而非单次样本结果 |
| queueing | M/M/1, M/M/c 等 | Hub 为主；先核验到达/服务/稳态条件 |
| game-theory | matrix/zero-sum/non-zero-sum | Hub 为主；均衡概念和支付假设必须与题意绑定 |
| cellular-automata | traffic/space evolution | Hub 为主；规则、边界、初值和多次重复必须可复现 |
| ode-dynamics / pde-dynamics | differential equation modeling | Hub 为主；数值收敛、边界/初值、守恒/稳定性检查优先 |

上游公式和示例只作为能力覆盖对照，本包不复制其大段算法正文或代码。
