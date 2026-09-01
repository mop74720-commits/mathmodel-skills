# Router Scenarios

这些不是完整比赛流程，只用于验证 Router 是否选到最小 Skill。

1. “题面里‘损失’到底含不含返工成本？” -> `PROBLEM_AMBIGUOUS` -> ambiguity-resolution。
2. “Q2 用整数规划还是遗传算法？” -> `MODEL_UNCERTAIN` -> model-selection。
3. “Gurobi 显示 infeasible。” -> `SOLVER_FAILED` -> solver-debug。
4. “换 seed 后结果差很多。” -> `RESULT_UNSTABLE` -> robustness。
5. “论文写最优，但没有对应运行记录。” -> `CLAIM_UNSUPPORTED` -> claim-evidence。
6. “最终 PDF 图中文字太小。” -> `FIGURE_WEAK` -> visualization-review。
7. “提交前最后检查。” -> `PRE_SUBMISSION` -> final-review。

反例：
- “现在还剩 8 小时，要不要放弃 Q4？”不是 Hub 事件，必须返回 Coach。
