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
22. “中文稿结果已冻结，需要转成 MCM/ICM 英文论文。” -> `ENGLISH_PAPER_NEEDED` -> `english-paper`

## Audit

23. “模型合同写完了，想让另一个视角专门找数学漏洞。” -> `MODEL_NEEDS_REVIEW` -> `model-review`
24. “最小代码链刚跑通，确认不是假跑通。” -> `MVP_NEEDS_CHECK` -> `mvp-check`
25. “有一个 Final Run 候选，需要确认论文就引用这一版。” -> `FINAL_RESULT_NEEDS_REVIEW` -> `result-review`
26. “论文写‘最优’，但找不到直接运行证据。” -> `CLAIM_UNSUPPORTED` -> `claim-evidence`
27. “整篇论文内容基本齐了，按评阅视角攻击一轮。” -> `PAPER_NEEDS_ATTACK` -> `paper-review`
28. “准备提交，做最后的规则、PDF、数字和附件检查。” -> `PRE_SUBMISSION` -> `final-review`

## Algorithm Knowledge Layer

29. “Q2 是 0-1 选址和产能约束。” -> `ALGO_LINEAR_INTEGER` -> `linear-integer-optimization`
30. “目标函数非凸，变量连续而且初值敏感。” -> `ALGO_NONLINEAR_OPT` -> `nonlinear-optimization`
31. “带容量和时间窗的配送车辆路径。” -> `ALGO_NETWORK_ROUTING` -> `network-routing`
32. “用过去 36 个月预测未来 6 个月。” -> `ALGO_TIME_SERIES` -> `time-series`
33. “有标签数据做二分类。” -> `ALGO_SUPERVISED_LEARNING` -> `supervised-learning`
34. “没有标签，要找稳定群组。” -> `ALGO_UNSUPERVISED_LEARNING` -> `unsupervised-learning`
35. “十个指标综合评价并排序。” -> `ALGO_MULTI_CRITERIA` -> `multi-criteria-evaluation`
36. “状态随时间由微分方程演化。” -> `ALGO_ODE_DYNAMICS` -> `ode-dynamics`
37. “温度场同时随空间和时间变化。” -> `ALGO_PDE_DYNAMICS` -> `pde-dynamics`
38. “用 Monte Carlo 求失效概率。” -> `ALGO_STOCHASTIC_SIM` -> `stochastic-simulation`
39. “比较两组差异并报告置信区间。” -> `ALGO_STATISTICAL_INFERENCE` -> `statistical-inference`
40. “有限尺寸物体的碰撞和空间轨迹。” -> `ALGO_GEOMETRY` -> `geometry-reconstruction`

## 必须返回 Coach 的反例

- “现在还剩 8 小时，要不要放弃 Q4？” -> `HANDOFF_TO_COACH`
- “Q1 和 Q3 哪个优先？” -> `HANDOFF_TO_COACH`
- “现在能不能冻结模型？” -> `HANDOFF_TO_COACH`
- “要不要为了创新冒险换一整套模型？” -> Skill 可以分析局部风险，但最终取舍 -> `HANDOFF_TO_COACH`

41. 赛题是公共卫生决策，当前模型没有考虑删失/重复测量/领域评价口径 -> `DOMAIN_CONTEXT_NEEDED` -> `domain-context`
42. 模型已经很复杂，需要检查某个模块到底有没有必要 -> `MODEL_NEEDS_CHALLENGE` -> `model-challenge`
43. 论文数字正确，但语言模板化、结果只报数不解释 -> `WRITING_STYLE_WEAK` -> `technical-style`
44. 只有很短的趋势序列，想评估 GM(1,1) 是否值得作为候选 -> `ALGO_GREY_FORECAST` -> `grey-forecasting`
45. 多个单位有多投入多产出，需要相对效率而不是普通综合排名 -> `ALGO_EFFICIENCY_ANALYSIS` -> `efficiency-analysis`
46. 服务窗口到达-服务-等待问题，需要估计等待时间和容量 -> `ALGO_QUEUEING` -> `queueing`
47. 题目核心是库存-流量-反馈-时滞和政策情景 -> `ALGO_SYSTEM_DYNAMICS` -> `system-dynamics`
48. 扩散/拥挤由空间格点上的局部更新规则驱动 -> `ALGO_CELLULAR_AUTOMATA` -> `cellular-automata`
49. 多个自主主体的最优策略彼此依赖，需要均衡分析 -> `ALGO_GAME_THEORY` -> `game-theory`

50. “准备按 2026 当届规则排版，但还没核验官方页数、模板和提交要求。” -> `OFFICIAL_RULES_NEEDED` -> `competition-rules`

## v0.1.12 route-decision regression

- “高级模型看起来更强，但简单 baseline 可能已经够用；什么实验决定是否值得升级？” -> `MODEL_NEEDS_CHALLENGE` -> `model-challenge`
- “两个路线当前都合理，什么新证据会让推荐翻转？” -> `MODELS_NEED_COMPARISON` -> `model-comparison`
- “A/B/C 选哪题？” -> `HANDOFF_TO_COACH`（SkillHub 不新增 contest-route-selection）

## v0.1.13 paper-quality regression

51. “Competition Repo 很完整，但论文像把实验日志和审计记录全打印出来，想重新合成竞赛正文。” -> `PAPER_SYNTHESIS_NEEDED` -> `paper-synthesis`
52. “论文科学结果正确，但正文越来越长，算法百科、重复说明和合规补丁把主线冲散了。” -> `PAPER_TOO_BLOATED` -> `editorial-compression`
53. “论文已经成形，想模拟评委五分钟扫读，看每问答案和关键贡献能不能快速抓住。” -> `PAPER_JUDGE_REVIEW_NEEDED` -> `judge-review`

## 2026-09-10 algorithm-depth regression

54. “每个地区样本都很少，希望用层级先验做部分池化并给后验预测区间。” -> `ALGO_BAYESIAN_MODELING` -> `bayesian-modeling`
55. “传感器信号里有明显瞬态和频率漂移，需要做时频分析和去噪。” -> `ALGO_SIGNAL_PROCESSING` -> `signal-processing`
56. “不同个体有异质属性和局部交互，希望模拟行为规则如何形成宏观涌现。” -> `ALGO_AGENT_BASED_MODELING` -> `agent-based-modeling`

## 2026-09-10 XiaoMa 1.3 delta regression

57. “Figure Contract 已经确定，真实 CSV 也有了，现在把折线/误差图实际渲染成 SVG 和 PNG。” -> `FIGURE_RENDER_NEEDED` -> `figure-render`
