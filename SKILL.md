---
name: mathmodel-skills
version: 0.2.0
description: 数学建模专项 Skill Hub。以 XiaoMa 原仓库作为角色/工具/QA 基座，以 Han 原仓库提供细粒度专项 Skill；Coach 只传入事件，本 Hub 路由到原始上游内容并应用最小 overlay。
---

# MathModel Skills Hub

## 1. 权力边界

本 Hub 不决定比赛时间、题目取舍、模型冻结时点或最终提交。这些由 `mathmodel-pro` Coach 决定。

本 Hub 只做：

1. 接收 Coach 或用户给出的局部事件；
2. 选择一个或少数几个上游 Skill/Role/Tool；
3. 按原始上游内容执行具体任务；
4. 应用 `overlay/` 中的冲突覆盖规则；
5. 返回结构化结果、证据和下一事件建议。

## 2. 上游优先级

### XiaoMa — 主底座

原始入口：

- `upstream/xiaoma/SKILL.md`
- `upstream/xiaoma/references/roles/建模手/SKILL.md`
- `upstream/xiaoma/references/roles/编程手/SKILL.md`
- `upstream/xiaoma/references/roles/论文手/SKILL.md`
- `upstream/xiaoma/tools/*/SKILL.md`
- `upstream/xiaoma/references/Subagent调度.md`

用于：角色合同、工具使用、渐进加载、项目根目录隔离、QA 结构。

### Han — 专项 Skill 库

原始入口：`upstream/han/skills/*/SKILL.md`

用于：假设、模型选择、实验管理、结果分析、创新、审稿、验证、可视化等局部能力。

## 3. Overlay 优先于冲突规则

上游原文保持不变；当原规则与 Coach 分层设计冲突时，不修改 upstream，而是读取：

- `overlay/authority.md`
- `overlay/qa-policy.md`
- `overlay/quantity-policy.md`
- `overlay/routing-policy.md`

例如：

- 上游的“必须等待用户批准”不自动变成 Hub 全局阻塞；
- 上游的固定图数/篇幅目标不自动变成比赛硬要求；
- 无 Subagent 不等于整场比赛 BLOCKED；
- 上游阶段编号不构成必须顺序执行的 01→12 流程。

## 4. 路由流程

1. 读取 `registry.yaml`。
2. 匹配事件。
3. 读取对应 `upstream_path` 的原始 `SKILL.md`。
4. 如涉及角色/工具，再渐进加载 XiaoMa 原始 Role/Tool。
5. 同时读取相关 overlay。
6. 执行并写入 `PROJECT_ROOT`，不改 `upstream/`。
7. 返回 `status / evidence / outputs / risks / suggested_next_event`。

## 5. 状态

允许：`PASS`, `WARN`, `FAIL`, `NOT_INDEPENDENTLY_VERIFIED`, `BLOCKED_BY_DEPENDENCY`。

不得把“缺独立 reviewer”自动升级为整个竞赛 `BLOCKED`。
