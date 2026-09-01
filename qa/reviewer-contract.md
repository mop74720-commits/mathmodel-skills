# Reviewer Contract

每次独立 review 只返回：

```text
scope:
input_snapshot:
status: PASS | WARN | FAIL | NOT_INDEPENDENTLY_VERIFIED
evidence:
findings:
  P0:
  P1:
  P2:
rework_target:
limits:
```

Reviewer 不负责：
- 修改权威代码/论文；
- 决定比赛阶段；
- 决定团队是否提交；
- 用主观总分替代证据。
