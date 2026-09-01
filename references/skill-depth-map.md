# Skill Depth Map

v0.1.1 保持 v0.1.0 的 27 个事件和目录不变，只把内部内容深化到执行级。

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
