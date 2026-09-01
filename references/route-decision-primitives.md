# Route Decision Primitives for Local Skills

本文件只服务局部模型/算法路线选择。选哪个赛题、是否换题、全局时间分配仍属于 Coach。

按需使用：

- `baseline_or_minimal_witness`
- `current_claim`
- `strongest_objection`
- `rejected_alternative`
- `deciding_evidence`
- `refutation_test`
- `flip_condition`
- `fallback_trigger`
- `fallback_action`
- `binding_constraints`

复杂模型的合法性来自“修复 baseline 的真实缺陷，并通过决定性证据”，而不是模型名称。若不存在真实候选竞争，不必强制制造多路线；若关键未知在上游，应先路由解决题意、数据、参数或可辨识性。

数值评分可辅助整理维度，但不得替代公平实验、硬约束、Pareto tradeoff 和 flip condition。

选择性吸收 `y3519712124-ui/math-modeling-contest-route-selection` 的 model-choice tournament、refutation、engineering feasibility、flip condition 与 fallback 思想。全局 topic selection 未并入 SkillHub，以避免重新引入 `competition-strategy` 越权。许可见 `THIRD_PARTY_NOTICES.md`。
