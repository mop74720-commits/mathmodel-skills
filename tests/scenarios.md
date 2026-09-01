# Router Scenarios

这些不是固定比赛流程，只用于验证 Router 能否按当前小情景选择最小 Skill。每个场景优先命中一个事件；只有第一个 Skill 返回证据表明确要求时，才组合第二个。

## Problem

1. “我还没理清题目四问到底分别要什么。” -> `PROBLEM_UNCLEAR` -> `problem-analysis`
2. “附件 Excel 有哪些列、缺失和单位？” -> `DATA_UNKNOWN` -> `data-audit`
3. “题目里的‘损失’到底含不含返工成本？” -> `PROBLEM_AMBIGUOUS` -> `ambiguity-resolution`
4. “这个独立性假设是不是太强？” -> `ASSUMPTION_WEAK` -> `hypothesis`

## Modeling

5. “Q2 用整数规划、启发式还是别的方法？” -> `MODEL_UNCERTAIN` -> `model-selection`
6. “模型选好了，但公式和输入输出还没有冻结。” -> `MODEL_CONTRACT_MISSING` -> `model-contract`
7. “两个候选模型都能跑，怎么公平选？” -> `MODELS_NEED_COMPARISON` -> `model-comparison`
8. “Baseline 已经稳定，想做一个风险较低的提升。” -> `NEED_LOW_RISK_IMPROVEMENT` -> `innovation`

## Coding

9. “合同已经定了，现在把它跑起来。” -> `IMPLEMENT_MODEL` -> `implementation`
10. “Gurobi 显示 infeasible / ODE 发散 / 出 NaN。” -> `SOLVER_FAILED` -> `solver-debug`
11. “程序能跑，但 dt、容差一变结果就漂。” -> `NUMERICAL_SUSPECT` -> `numerical-check`

## Experiment

12. “我们跑了十几个版本，已经分不清哪个结果是哪次。” -> `EXPERIMENTS_UNTRACKED` -> `experiment-manager`
13. “论文要说明参数变化会不会影响结论。” -> `NEED_SENSITIVITY` -> `sensitivity`
14. “换 seed / 样本 / 场景以后结论经常翻转。” -> `RESULT_UNSTABLE` -> `robustness`
15. “结果出来了，但只是很多数字，不知道怎么解释。” -> `RESULT_NEEDS_INTERPRETATION` -> `result-analysis`

## Visualization

16. “这个结论该画什么图最合适？” -> `FIGURE_NEEDED` -> `figure-design`
17. “需要把算法分支和反馈过程画出来。” -> `FLOWCHART_NEEDED` -> `flowchart`
18. “图做出来了，但论文尺寸下看不清/容易误导。” -> `FIGURE_WEAK` -> `visualization-review`

## Writing

19. “论文准备开写，先把证据组织成结构。” -> `PAPER_OUTLINE_NEEDED` -> `outline`
20. “最终数字冻结了，现在写摘要。” -> `ABSTRACT_NEEDED` -> `abstract`
21. “Q2 的结果表已经有了，写成分析正文。” -> `RESULT_SECTION_NEEDED` -> `result-writing`

## Audit

22. “模型合同写完了，想让另一个视角专门找数学漏洞。” -> `MODEL_NEEDS_REVIEW` -> `model-review`
23. “最小代码链刚跑通，确认不是假跑通。” -> `MVP_NEEDS_CHECK` -> `mvp-check`
24. “有一个 Final Run 候选，需要确认论文就引用这一版。” -> `FINAL_RESULT_NEEDS_REVIEW` -> `result-review`
25. “论文写‘最优’，但找不到直接运行证据。” -> `CLAIM_UNSUPPORTED` -> `claim-evidence`
26. “整篇论文内容基本齐了，按评阅视角攻击一轮。” -> `PAPER_NEEDS_ATTACK` -> `paper-review`
27. “准备提交，做最后的规则、PDF、数字和附件检查。” -> `PRE_SUBMISSION` -> `final-review`

## 必须返回 Coach 的反例

- “现在还剩 8 小时，要不要放弃 Q4？” -> `HANDOFF_TO_COACH`
- “Q1 和 Q3 哪个优先？” -> `HANDOFF_TO_COACH`
- “现在能不能冻结模型？” -> `HANDOFF_TO_COACH`
- “要不要为了创新冒险换一整套模型？” -> Skill 可以分析局部风险，但最终取舍 -> `HANDOFF_TO_COACH`
