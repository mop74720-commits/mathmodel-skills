# Skill Depth Map

v0.1.3 在 v0.1.2 的 39 个事件上补齐上游覆盖缺口，v0.1.12 目前共 50 个事件驱动 Skill。下表前 27 项是原核心事件；后续新增项按版本补充。

| Category | Skill | Event | 核心输出 |
|---|---|---|---|
| problem | problem-analysis | PROBLEM_UNCLEAR | 问题合同、FACT/INFERENCE/ASSUMPTION 分层、依赖 |
| problem | data-audit | DATA_UNKNOWN | 数据事实基线、字段/单位/质量/泄漏风险 |
| problem | ambiguity-resolution | PROBLEM_AMBIGUOUS | 竞争解释、证据裁决、回滚条件 |
| problem | hypothesis | ASSUMPTION_WEAK | 假设登记、影响映射、验证/敏感性计划 |
| modeling | model-selection | MODEL_UNCERTAIN | Baseline、主候选、条件备选、失败模式 |
| modeling | model-contract | MODEL_CONTRACT_MISSING | 变量/公式/约束/单位/I-O/验证合同 |
| modeling | model-comparison | MODELS_NEED_COMPARISON | 公平比较协议、差异与条件式推荐 |
| modeling | innovation | NEED_LOW_RISK_IMPROVEMENT | 可验证改进、最小实验、回滚条件 |
| coding | implementation | IMPLEMENT_MODEL | 最小纵向切片、运行命令、日志/ledger |
| coding | solver-debug | SOLVER_FAILED | 故障分类、最小复现、根因与复测 |
| coding | numerical-check | NUMERICAL_SUSPECT | 收敛、残差、不变量、精度建议 |
| experiment | experiment-manager | EXPERIMENTS_UNTRACKED | Run Ledger、配置/版本、Final/superseded |
| experiment | sensitivity | NEED_SENSITIVITY | 参数响应、敏感阈值、结论稳定性 |
| experiment | robustness | RESULT_UNSTABLE | 压力场景、决策稳定性、失效边界 |
| experiment | result-analysis | RESULT_NEEDS_INTERPRETATION | 主结果、Baseline 对比、机制与限制 |
| visualization | figure-design | FIGURE_NEEDED | claim 驱动的 Figure Contract |
| visualization | flowchart | FLOWCHART_NEEDED | 流程语义合同、节点/边/循环 |
| visualization | visualization-review | FIGURE_WEAK | 实际尺寸图审、误导风险、重画项 |
| writing | outline | PAPER_OUTLINE_NEEDED | 章节 claim-evidence 大纲 |
| writing | abstract | ABSTRACT_NEEDED | 基于 Final Run 的摘要 |
| writing | result-writing | RESULT_SECTION_NEEDED | 结果+比较+原因+意义+限制正文 |
| audit | model-review | MODEL_NEEDS_REVIEW | 独立模型攻击、P0/P1/P2 |
| audit | mvp-check | MVP_NEEDS_CHECK | 最小命令独立复现与基本约束检查 |
| audit | result-review | FINAL_RESULT_NEEDS_REVIEW | Final Run 冻结、关键数字核对 |
| audit | claim-evidence | CLAIM_UNSUPPORTED | Claim-Evidence Map、缺证据路由 |
| audit | paper-review | PAPER_NEEDS_ATTACK | 语义审稿问题矩阵 |
| audit | final-review | PRE_SUBMISSION | 官方规则+最终渲染+提交物审计 |

## 深化原则

- 每个 Skill 都能单独执行，不依赖固定前一阶段 PASS。
- 每个 Skill 都有明确失败分流，而不是“出错就整场 BLOCKED”。
- 数值、模型、论文审计以证据为中心，不使用虚构综合分。
- 需要时可以组合第二个 Skill，但组合应由第一个 Skill 的失败/风险证据触发。
- Coach 仍拥有 priority、stage、freeze、abandon、submit 决策权。

## v0.1.2 Algorithm Family Additions

- 12 个算法族：线性/整数优化、非线性优化、网络路由、时序、监督学习、无监督学习、多指标评价、ODE、PDE、随机仿真、统计推断、几何重建。

## v0.1.3 Coverage-Driven Additions

| Category | Skill | Event | 核心输出 |
|---|---|---|---|
| domain | domain-context | DOMAIN_CONTEXT_NEEDED | 领域机制—建模影响、特有陷阱、指标/约束 |
| modeling | model-challenge | MODEL_NEEDS_CHALLENGE | 简化/替换/去掉/解释测试、组件必要性 |
| writing | technical-style | WRITING_STYLE_WEAK | 技术表达修订、证据缺口，不改变数学事实 |
| algorithm | grey-forecasting | ALGO_GREY_FORECAST | 灰色预测适用性、Baseline、滚动外推验证 |
| algorithm | efficiency-analysis | ALGO_EFFICIENCY_ANALYSIS | DEA 规格、效率/slack、稳健性 |
| algorithm | queueing | ALGO_QUEUEING | 排队系统合同、稳态/仿真、等待与容量 |
| algorithm | system-dynamics | ALGO_SYSTEM_DYNAMICS | 因果回路、stock-flow、政策情景 |
| algorithm | cellular-automata | ALGO_CELLULAR_AUTOMATA | 元胞/邻域/更新/边界与涌现验证 |
| algorithm | game-theory | ALGO_GAME_THEORY | 玩家/策略/收益/均衡与集中式基准 |

## v0.1.5 Selective Addition

| Category | Skill | Event | 核心输出 |
|---|---|---|---|
| writing | english-paper | ENGLISH_PAPER_NEEDED | 英文化正文、术语/符号表、数字/公式/引用一致性审计 |

算法族数量保持 18；新增具体算法知识通过 `references/algorithm-playbooks/*` 渐进加载，不为每个算法都新增 Router Event。

## v0.1.7 Deep Selection Addition

| Category | Skill | Event | 核心输出 |
|---|---|---|---|
| problem | competition-rules | OFFICIAL_RULES_NEEDED | 当届官方 rule profile、来源/locator、硬约束、UNKNOWN/CONFLICT |

同时新增不占 Router Event 的深度参考：模型组合模式、MATLAB 实现规范、Figure 三份选图/编码/review guide。


## v0.1.13 recovered paper-quality capabilities

| layer | skill | event | depth |
|---|---|---|---|
| writing | paper-synthesis | PAPER_SYNTHESIS_NEEDED | Repo→正文选择、main/appendix/support 映射、每问证据闭环 |
| writing | editorial-compression | PAPER_TOO_BLOATED | delete/merge/move/keep 清单、压缩正文、渲染节奏修复 |
| audit | judge-review | PAPER_JUDGE_REVIEW_NEEDED | 5-minute map、scan friction、评委视角最小修改 |

三者按当前问题触发，不构成 synthesis→compression→judge→final 强制链。
