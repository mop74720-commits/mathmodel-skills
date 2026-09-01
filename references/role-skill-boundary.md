# Role / Skill / Coach Boundary — v0.1.12

- Coach decides global priority, question switching, freeze/rollback, risk acceptance and submission readiness.
- SkillHub solves local technical events and returns evidence/risk/handoff.
- `OFFICIAL_RULES_NEEDED` remains a valid local Skill because it extracts and classifies external rules.
- General competition strategy (for example “CUMCM vs MCM/ICM now what should we prioritize?”) is **not** a first-class SkillHub event; it belongs to Coach using current Competition Repo state plus official rules.
- Tool success is mechanical evidence only and cannot promote a global state.


判断示例：

- “现在是否该做 Q3？” → Coach。
- “Q3 用 MILP 还是启发式？” → `model-selection`。
- “MILP infeasible 为什么？” → `solver-debug`。
- “这张敏感性图怎么画？” → `figure-design` + Figure Tool。
- “论文这个结论是否有证据？” → `claim-evidence`。
