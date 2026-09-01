# mathmodel-skills

数学建模竞赛的第二层 Skill Hub。它不决定比赛时间线、模型冻结时点或团队优先级；这些属于 `mathmodel-pro` Coach。它负责在收到明确局部任务或事件后，路由到最小必要的 Role / Skill / Tool / QA，并把结构化结果交还给真实 Competition Repo。

## 定位

```text
mathmodel-pro (Coach)
        |
        |  event + priority + project context
        v
mathmodel-skills (Skill Hub)
        |
        |  role / skill / tool / review
        v
Competition Repo
```

设计来源：

- `XiaoMaColtAI/math-modeling-skill`：吸收角色分工、渐进式加载、SKILL_ROOT/PROJECT_ROOT 分离、独立 reviewer/QA、工具分类等设计思想。
- `han69611/math-modeling-skills`：吸收假设设计、模型选择、实验管理、结果分析、创新、Reviewer、Verify 等细粒度能力思想。

两个上游仓库当前均未声明许可证，因此本项目不复制其原文、脚本或模板；所有内容均为按上述思想重新设计和独立编写。见 `UPSTREAM_NOTICE.md`。

## 最重要的边界

1. Coach 决定“现在做什么”；Skill Hub 决定“这个局部问题怎么做”。
2. Skill Hub 不读取比赛小时数来擅自阻断工作。
3. QA 返回 `PASS / WARN / FAIL / NOT_INDEPENDENTLY_VERIFIED`，不越权宣布整个比赛 `BLOCKED`。
4. 不要求固定图数、固定页数、固定模型数；只要求证据覆盖与题目/官方规则一致。
5. 一个事件优先调用一个 Skill；必要时再组合第二个，避免 12 阶段式全链路强制执行。

## 目录

```text
mathmodel-skills/
├── SKILL.md
├── registry.yaml
├── roles/
│   ├── modeling/
│   ├── coding/
│   └── writing/
├── skills/
│   ├── problem/
│   ├── modeling/
│   ├── coding/
│   ├── experiment/
│   ├── visualization/
│   ├── writing/
│   └── audit/
├── tools/
│   ├── pdf/
│   ├── xlsx/
│   ├── figure/
│   ├── docx/
│   ├── latex/
│   └── paper-search/
├── qa/
├── references/
├── scripts/
└── tests/
```

## 使用方式

Coach 推荐事件：

```text
MODEL_UNCERTAIN
```

Router 查 `registry.yaml`：

```text
MODEL_UNCERTAIN -> skills/modeling/model-selection
```

该 Skill 只完成模型选择，返回：候选、Baseline、适用条件、风险、验证方案和下一步 handoff。它不会自行推进“编程阶段”。

## 校验

```bash
python scripts/validate_hub.py
```
