# Coach -> Skill Hub Interface

Coach 调用 Hub 时建议只传当前任务所需信息：

```yaml
event: MODEL_UNCERTAIN
priority: high
project_root: /path/to/competition-repo
question: q2
objective: 选择可在当前数据与算力下完成的主模型
constraints:
  - 保留现有 baseline
  - 不改变题面事实
inputs:
  - problem/FACTS.md
  - models/q2/draft.md
  - data/processed/q2.csv
expected_output:
  - 推荐模型族
  - baseline/candidate 对比
  - 风险与验证方案
coach_policy:
  may_accept_warn: true
  may_change_stage: false
```

Hub 回执：

```yaml
skill: model-selection
status: DONE
inputs_used: []
outputs_written: []
key_findings: []
risks: []
qa_status: NOT_INDEPENDENTLY_VERIFIED
handoff:
  recommended_event: MODEL_CONTRACT_MISSING
  reason: 已选定模型但尚未冻结合同
```

## 规则

- `priority` 由 Coach 给出，Hub 不重算比赛优先级。
- `coach_policy` 可显式允许带 WARN 继续；Hub 仍必须如实返回风险。
- Hub 可以推荐下一事件，但不能直接切换比赛阶段。
- 若收到的其实是“剩余时间/取舍/是否放弃某题”问题，Hub 应返回 `HANDOFF_TO_COACH`。
