# QA Overlay

保留 XiaoMa 的独立质检思想，但改变全局阻塞语义。

- 有独立 reviewer 且通过：`PASS`
- 只有作者自检：`NOT_INDEPENDENTLY_VERIFIED`
- 有明确正确性/规则错误：`FAIL`
- 缺运行环境/数据/依赖：`BLOCKED_BY_DEPENDENCY`

`FAIL` 表示当前局部任务需要修复；是否暂停整场比赛由 Coach 决定。
