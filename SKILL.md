---
name: mathmodel-skills
version: 0.1.13
description: 数学建模专项 Skill Hub。接收 Coach 或用户给出的局部事件，渐进式路由到 Role、专项 Skill、工具和 QA；不管理比赛时间线与全局优先级。
---

# MathModel Skills Router

## 1. 权限边界

本 Skill Hub 是执行层，不是 Coach。

Coach 权威：
- 当前项目状态、剩余时间和全局优先级；
- 是否冻结模型、切换问题、提前写作；
- 是否接受 WARN、是否返工、是否降级目标；
- 最终提交范围。

Skill Hub 权威：
- 当前局部问题的技术分析与执行；
- 选择最小必要 Skill / Tool；
- 产生可验证的局部产物；
- 返回 QA 状态、证据、风险与 handoff。

不得因为 Hub 内部建议覆盖 Coach 的显式决策。

## 2. 根目录合同

- `SKILL_ROOT`：本仓库，只读。
- `PROJECT_ROOT`：真实比赛仓库，所有权威产物写入这里。
- 禁止把比赛数据、结果、论文正文写回 `SKILL_ROOT`。

## 3. Router 规则

1. 优先根据事件匹配 `registry.yaml`。
2. 一次优先调用一个 primary Skill；只有 primary 输出明确缺口时才加载 secondary Skill。
3. 先读目标 Skill 的 `SKILL.md`；只有其 `Procedure` 要求时才加载 Role、Tool 或 references。
4. 不运行完整流水线来解决单点问题。
5. Tool 只处理载体/格式/检索/绘图，不替代建模判断；七个 Tool 均有可执行核心，具体命令见各 `tools/*/SKILL.md`。
6. QA reviewer 默认只读，不直接修改权威产物。

## 4. 常见事件

| Event | Primary Skill |
|---|---|
| `PROBLEM_UNCLEAR` | `problem/problem-analysis` |
| `DATA_UNKNOWN` | `problem/data-audit` |
| `LITERATURE_EVIDENCE_NEEDED` | `problem/literature-evidence` |
| `OFFICIAL_RULES_NEEDED` | `problem/competition-rules` |
| `PROBLEM_AMBIGUOUS` | `problem/ambiguity-resolution` |
| `ASSUMPTION_WEAK` | `problem/hypothesis` |
| `DOMAIN_CONTEXT_NEEDED` | `domain/domain-context` |
| `MODEL_UNCERTAIN` | `modeling/model-selection` |
| `MODELS_NEED_COMPARISON` | `modeling/model-comparison` |
| `MODEL_CONTRACT_MISSING` | `modeling/model-contract` |
| `NEED_LOW_RISK_IMPROVEMENT` | `modeling/innovation` |
| `MODEL_NEEDS_CHALLENGE` | `modeling/model-challenge` |
| `IMPLEMENT_MODEL` | `coding/implementation` |
| `SOLVER_FAILED` | `coding/solver-debug` |
| `NUMERICAL_SUSPECT` | `coding/numerical-check` |
| `EXPERIMENT_DESIGN_NEEDED` | `experiment/experimental-design` |
| `EXPERIMENTS_UNTRACKED` | `experiment/experiment-manager` |
| `NEED_SENSITIVITY` | `experiment/sensitivity` |
| `RESULT_UNSTABLE` | `experiment/robustness` |
| `RESULT_NEEDS_INTERPRETATION` | `experiment/result-analysis` |
| `FIGURE_NEEDED` | `visualization/figure-design` |
| `FIGURE_RENDER_NEEDED` | `visualization/figure-render` |
| `FIGURE_WEAK` | `visualization/visualization-review` |
| `FLOWCHART_NEEDED` | `visualization/flowchart` |
| `PAPER_OUTLINE_NEEDED` | `writing/outline` |
| `ABSTRACT_NEEDED` | `writing/abstract` |
| `RESULT_SECTION_NEEDED` | `writing/result-writing` |
| `PAPER_SYNTHESIS_NEEDED` | `writing/paper-synthesis` |
| `PAPER_TOO_BLOATED` | `writing/editorial-compression` |
| `WRITING_STYLE_WEAK` | `writing/technical-style` |
| `ENGLISH_PAPER_NEEDED` | `writing/english-paper` |
| `MODEL_NEEDS_REVIEW` | `audit/model-review` |
| `MVP_NEEDS_CHECK` | `audit/mvp-check` |
| `FINAL_RESULT_NEEDS_REVIEW` | `audit/result-review` |
| `CLAIM_UNSUPPORTED` | `audit/claim-evidence` |
| `PAPER_NEEDS_ATTACK` | `audit/paper-review` |
| `PAPER_JUDGE_REVIEW_NEEDED` | `audit/judge-review` |
| `PRE_SUBMISSION` | `audit/final-review` |

## 4A. Algorithm Knowledge Events

当 `MODEL_UNCERTAIN` 已识别出结构后，Router 优先进入一个算法族 Skill，而不是继续让 model-selection 承担全部算法知识。具体算法名继续通过 `references/algorithm-depth-selection.md` 和 playbook 按需加载。

| Event | Algorithm Skill |
|---|---|
| `ALGO_LINEAR_INTEGER` | `algorithm/linear-integer-optimization` |
| `ALGO_NONLINEAR_OPT` | `algorithm/nonlinear-optimization` |
| `ALGO_NETWORK_ROUTING` | `algorithm/network-routing` |
| `ALGO_TIME_SERIES` | `algorithm/time-series` |
| `ALGO_GREY_FORECAST` | `algorithm/grey-forecasting` |
| `ALGO_SUPERVISED_LEARNING` | `algorithm/supervised-learning` |
| `ALGO_UNSUPERVISED_LEARNING` | `algorithm/unsupervised-learning` |
| `ALGO_MULTI_CRITERIA` | `algorithm/multi-criteria-evaluation` |
| `ALGO_EFFICIENCY_ANALYSIS` | `algorithm/efficiency-analysis` |
| `ALGO_ODE_DYNAMICS` | `algorithm/ode-dynamics` |
| `ALGO_PDE_DYNAMICS` | `algorithm/pde-dynamics` |
| `ALGO_STOCHASTIC_SIM` | `algorithm/stochastic-simulation` |
| `ALGO_QUEUEING` | `algorithm/queueing` |
| `ALGO_SYSTEM_DYNAMICS` | `algorithm/system-dynamics` |
| `ALGO_CELLULAR_AUTOMATA` | `algorithm/cellular-automata` |
| `ALGO_GAME_THEORY` | `algorithm/game-theory` |
| `ALGO_STATISTICAL_INFERENCE` | `algorithm/statistical-inference` |
| `ALGO_CAUSAL_INFERENCE` | `algorithm/causal-inference` |
| `ALGO_GEOMETRY` | `algorithm/geometry-reconstruction` |
| `ALGO_BAYESIAN_MODELING` | `algorithm/bayesian-modeling` |
| `ALGO_SIGNAL_PROCESSING` | `algorithm/signal-processing` |
| `ALGO_AGENT_BASED_MODELING` | `algorithm/agent-based-modeling` |

## 4B. Tool Dispatch

专项 Skill 在 Procedure 明确需要机械处理时才加载 Tool：

- PDF 题面/参考资料 → `tools/pdf`
- XLSX 工作簿 → `tools/xlsx`
- 数据剖析/标准科研图渲染/图文件 QA → `tools/figure`
- Word 结构/内容残留/渲染 → `tools/docx`
- LaTeX 编译/绑定/验证 → `tools/latex`
- 文献候选检索 → `tools/paper-search`
- 运行复现 manifest / 功能依赖检查 → `tools/reproducibility`

Tool 的成功只证明其机械检查范围，不自动把上层科学结论判为 PASS。比赛格式或提交硬约束应先由 `OFFICIAL_RULES_NEEDED` 生成 rule profile，再传给载体 Tool。

## 5. 标准 Skill 回执

每个 Skill 最终返回：

```text
skill:
status: DONE | PARTIAL | FAIL
inputs_used:
outputs_written:
key_findings:
risks:
qa_status: PASS | WARN | FAIL | NOT_INDEPENDENTLY_VERIFIED
handoff:
```

`FAIL` 表示该局部任务未满足其自身正确性条件；不等于整场比赛停止。

## 6. QA 状态

- `PASS`：检查范围内无阻断问题。
- `WARN`：存在可接受但需要 Coach 知晓的风险。
- `FAIL`：存在会使该局部结论失效的正确性或证据问题。
- `NOT_INDEPENDENTLY_VERIFIED`：只有作者/主 Agent 自检，没有独立 reviewer。

## 7. 禁止事项

- 不维护 12 阶段强制链。
- 不要求每一步用户审批后才继续。
- 不把复杂度当创新。
- 不把固定图数、页数、字数当通用质量门槛。
- 不以评分表伪装官方评审分数。
- 不允许 writer 编造未运行结果。
- 不允许 coding 通过偷偷改模型公式来绕开 model contract。
- 不把 Competition Repo 的完整性等同于论文正文的完整性；正文必须选择性表达。
- 不允许为了合规把内部 audit/provenance/AI 历史无必要塞进科学正文。
- Scientific Review、Judge Review、Compliance Review 分离；任何一个 PASS 都不自动代表另外两个 PASS。
- 论文质量判断优先看实际渲染页，不靠固定页数、图数或主观总分。
