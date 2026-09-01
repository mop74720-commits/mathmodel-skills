# Role / Skill / Tool / QA Boundary

- Role：长期责任域，例如 Modeling/Coding/Writing；负责整合局部 Skill 的输出。
- Skill：针对一个明确问题的可调用能力，例如 solver-debug、sensitivity。
- Tool：处理文件、检索、绘图、编译等载体任务。
- QA：独立检查，不修改权威产物。
- Coach：在本仓库之外，拥有比赛时间和优先级决策权。

判断方法：
- “现在是否该做 Q3？” -> Coach。
- “Q3 用 MILP 还是启发式？” -> model-selection。
- “MILP infeasible 为什么？” -> solver-debug。
- “这张敏感性图怎么画？” -> figure-design + figure tool。
- “论文这个结论是否有证据？” -> claim-evidence。
