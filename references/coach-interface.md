# Coach → Skill Hub Interface

建议请求：

```yaml
event: MODEL_UNCERTAIN
project_root: D:/CUMCM-2026-B
question: q2
objective: 选择可实现、可验证的模型族
constraints:
  - 保留现有 baseline
  - 不改 q1
artifacts:
  - problem/FACTS.md
  - models/q2.md
```

Hub 回执：

```yaml
status: PASS
skills_used:
  - upstream/han/skills/03-model-selection/SKILL.md
roles_used:
  - upstream/xiaoma/references/roles/建模手/SKILL.md
outputs: []
evidence: []
risks: []
suggested_next_event: MODEL_REVIEW_NEEDED
```
