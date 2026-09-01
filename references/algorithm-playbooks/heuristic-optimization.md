# Heuristic Optimization Playbook

覆盖 GA、PSO、GWO、DE、免疫/群智能等随机启发式的共同使用规范，不把某一种算法包装成默认“高级解法”。

1. 先建立可行的确定性或局部 solver baseline；只有非凸、多峰、离散复杂或黑箱证据支持时再升级。
2. 决策变量编码必须保持边界/整数/排列等结构，优先 repair/结构化算子，避免只靠巨大 penalty。
3. 明确 population、迭代数、停止条件、随机 seed 和计算预算；不同算法按函数评估次数或可比墙钟预算比较。
4. 记录每次运行的最优值、可行率、收敛轨迹和重复运行分布；单次 best 不作为稳健证据。
5. 在可精确求解的小实例上对照最优值；大实例至少与局部/multi-start baseline 和已知下界/上界比较（若存在）。
6. 最优个体必须通过独立可行性检查器和 objective 重算。
7. 算法改进必须做消融：新增机制是否在相同预算下贡献稳定增益。
8. 启发式没有可验证的全局最优证书时，只能表述为“best found / near-optimal candidate / empirically improved”。
