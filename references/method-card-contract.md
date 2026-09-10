# Method Card Contract

Method Card 连接“外部文献”与“当前题模型决策”，但不把外部结论升级为当前事实。

## Required fields

```yaml
card_id: MC-...
source:
  title:
  authors:
  year:
  doi_or_url:
evidence_level: FULLTEXT_VERIFIED | ABSTRACT_ONLY | METADATA_ONLY
problem_structure:
method:
assumptions: []
required_data: []
transferable_parts: []
non_transferable_parts: []
failure_modes: []
validation_pattern: []
evidence_locator: []
decision_role: CANDIDATE_PRIOR | PROBE_HINT | VALIDATION_PATTERN | BACKGROUND_ONLY | REJECT_FOR_CURRENT_TASK
current_task_status: CANDIDATE | ADAPTED | ADOPTED | REJECTED
reason:
```

## Semantics

- `evidence_level` 描述我们真正读到什么，不描述论文质量。
- `transferable_parts` 必须是结构/机制/验证方式，不复制历史数值结论。
- `ADOPTED` 只表示该方法已经实际影响当前方案；仍需要当前题自己的实现和验证。
- `REJECTED` 是有价值证据，应保留原因以避免后续重复踩坑。
- 一张卡只围绕一个可识别的方法主张；同一论文包含多条独立方法时可拆卡。

## Compatibility with historical experience

Historical Case Card 与 Method Card 可以共享 `problem_structure / assumptions / required_data / transferable_parts / failure_modes / validation` 等字段，便于 Coach 做统一结构检索；但两者都只能形成 prior，不能覆盖 Competition Repo 的当前事实。
