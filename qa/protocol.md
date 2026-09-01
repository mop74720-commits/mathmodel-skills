# QA Protocol

QA 是独立检查层，不是第二个 Coach。

## 状态

- `PASS`：本次范围内没有 P0/P1 问题。
- `WARN`：无 P0/P1，但存在需知晓的 P2 风险或范围限制。
- `FAIL`：存在 P0/P1，使当前局部结论不可安全使用。
- `NOT_INDEPENDENTLY_VERIFIED`：只做了作者/主 Agent 自检。

## 严重度

- `P0`：数学正确性、题面/官方硬约束、数据事实错误。
- `P1`：复现、关键一致性、证据链、约束/单位等会影响结论可信度的问题。
- `P2`：非阻断的表达、效率、可读性和增强项。

## 规则

1. reviewer 默认只读，不直接修权威产物。
2. reviewer 不接收“作者认为已经正确”的预期结论。
3. 输入实质变化后，旧 QA 只对旧快照有效。
4. 没有独立 reviewer 时不写 `PASS`，写 `NOT_INDEPENDENTLY_VERIFIED`。
5. `FAIL` 不等于整场比赛停止；Coach 决定是否返工、降级或接受风险。
