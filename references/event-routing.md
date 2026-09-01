# Event Routing Guide

Coach 或用户不必知道所有 Skill 名称，只需给出局部事件。

- 题意/数据：`PROBLEM_UNCLEAR`, `DATA_UNKNOWN`, `PROBLEM_AMBIGUOUS`, `ASSUMPTION_WEAK`
- 模型：`MODEL_UNCERTAIN`, `MODELS_NEED_COMPARISON`, `MODEL_CONTRACT_MISSING`, `NEED_LOW_RISK_IMPROVEMENT`
- 实现：`IMPLEMENT_MODEL`, `SOLVER_FAILED`, `NUMERICAL_SUSPECT`
- 实验：`EXPERIMENTS_UNTRACKED`, `NEED_SENSITIVITY`, `RESULT_UNSTABLE`, `RESULT_NEEDS_INTERPRETATION`
- 图表：`FIGURE_NEEDED`, `FIGURE_WEAK`, `FLOWCHART_NEEDED`
- 写作：`PAPER_OUTLINE_NEEDED`, `ABSTRACT_NEEDED`, `RESULT_SECTION_NEEDED`
- 审计：`MODEL_NEEDS_REVIEW`, `MVP_NEEDS_CHECK`, `FINAL_RESULT_NEEDS_REVIEW`, `CLAIM_UNSUPPORTED`, `PAPER_NEEDS_ATTACK`, `PRE_SUBMISSION`

一个事件原则上只有一个 primary Skill。若用户一次提出多个独立问题，可并列路由，但不要因此自动执行整条链。

## v0.1.3 coverage-driven events

| Signal | Event | Skill |
|---|---|---|
| 专业领域机制会改变约束/指标 | `DOMAIN_CONTEXT_NEEDED` | `domain/domain-context` |
| 现有模型需做必要性/简化/消融挑战 | `MODEL_NEEDS_CHALLENGE` | `modeling/model-challenge` |
| 技术内容正确但表达模板化/无解释 | `WRITING_STYLE_WEAK` | `writing/technical-style` |
| 小样本趋势型灰色预测候选 | `ALGO_GREY_FORECAST` | `algorithm/grey-forecasting` |
| 多投入多产出效率/DEA | `ALGO_EFFICIENCY_ANALYSIS` | `algorithm/efficiency-analysis` |
| 到达-服务-等待 | `ALGO_QUEUEING` | `algorithm/queueing` |
| 库存-流量-反馈-时滞 | `ALGO_SYSTEM_DYNAMICS` | `algorithm/system-dynamics` |
| 空间格点+局部更新 | `ALGO_CELLULAR_AUTOMATA` | `algorithm/cellular-automata` |
| 多主体策略互动 | `ALGO_GAME_THEORY` | `algorithm/game-theory` |
