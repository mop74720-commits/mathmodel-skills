# mathmodel-skills

数学建模竞赛的第二层 Skill Hub。它不决定比赛时间线、模型冻结时点或团队优先级；这些属于 `mathmodel-pro` Coach。它负责在收到明确局部任务或事件后，路由到最小必要的 Role / Skill / Tool / QA，并把结构化结果交还给真实 Competition Repo。

## v0.1.3：48 个事件驱动 Skill + Upstream Coverage Matrix

本版本在 v0.1.2 的 39 个 Skill 上继续补齐两个上游的高价值缺口，现有 48 个事件驱动 Skill，其中 18 个为算法族。新增 `references/upstream-coverage-matrix.md/.csv`，逐项记录 XiaoMa 与 Han 的能力映射、完整/部分吸收和主动排除项。所有 Skill 继续采用 Trigger、Scope、Inputs、Procedure、Outputs、Checks、Failure、Handoff 合同。

设计原则：

- 不引入固定 01→12 阶段链；仍由事件路由。
- 不使用页数、图数、统一百分比扰动等伪硬指标。
- Skill 不拥有比赛阶段/时间/提交决策权，仍归 Coach。
- QA 返回证据化 PASS/WARN/FAIL/NOT_INDEPENDENTLY_VERIFIED，不用主观总分代替问题。
- 论文/结果关键数字优先绑定 Final Run 与 Claim-Evidence Map。

## v0.1.3 新增缺口补齐

- `DOMAIN_CONTEXT_NEEDED` → `domain-context`：9 类常见领域机制/陷阱/评价口径。
- `MODEL_NEEDS_CHALLENGE` → `model-challenge`：简化、替换、去掉、解释测试。
- `WRITING_STYLE_WEAK` → `technical-style`：技术表达去模板化，但不以“规避 AI 检测”为目标。
- 新增 6 个算法族：灰色预测、DEA/效率、排队、系统动力学、元胞自动机、博弈论。
- 新增 `references/upstream-coverage-matrix.md` 和 CSV，对两个上游共 72 个重要条目逐项映射。

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
- `han69611/math-modeling-skills`：吸收假设设计、模型选择、实验管理、结果分析、创新、领域知识、模型自挑战、Reviewer、Verify 等细粒度能力思想。

本项目继续采用独立重写而非整仓复制。XiaoMa 当前根目录未见明确 LICENSE；Han 的 README 声明 MIT，但仓库元数据未识别出 license。具体来源与处理见 `UPSTREAM_NOTICE.md`。

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
│   ├── algorithm/
│   ├── domain/
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
python scripts/validate_algorithm_routing.py
python scripts/validate_scenarios.py
python scripts/validate_upstream_coverage.py
```
