# Upstream design notice

本项目参考以下公开仓库：

1. https://github.com/XiaoMaColtAI/math-modeling-skill
2. https://github.com/han69611/math-modeling-skills

历史逐项覆盖矩阵的固定基线：

- XiaoMa commit `e5d9313420d519f18ed1429d52d95fe0a72ae944`（1.2.0）
- Han commit `b5b98aebcb25ff89a99ea1cbb52b31ccab5040ca`

最新增量复核基线：

- XiaoMa `1.3.0`，复核到 `3527fad922660397834a6167fc2b4c29ee64ba17`（2026-09-09；最新提交仅更新 Star 图，但工作树已包含 1.3.0 能力）
- Han 仍以 `b5b98aebcb25ff89a99ea1cbb52b31ccab5040ca` 为当前能力审计基线

许可证观察：XiaoMa 当前 GitHub 元数据为 `license: null`，根目录树未见 `LICENSE`；Han 的 GitHub 元数据同样为 `license: null`，但其 README 明确写有 `License: MIT`。本项目仍采用独立重写的方式，不把上游整仓源码/模板原样再分发。工具脚本也是依据公开能力边界重新实现，而非复制上游脚本正文。

主要设计映射：

- XiaoMa：三角色、Skill/Project Root 隔离、渐进加载、独立 QA、工具技能化、算法索引、复现与文档质量思想。
- Han：假设设计、模型选择、实验管理、结果分析、创新、领域知识、自我挑战、Reviewer、Verify、可视化审查等细粒度能力。

本项目的架构性改造：

- 固定阶段工作流由 Coach 管理，Skill Hub 改为事件路由；
- 无 Subagent 时返回 `NOT_INDEPENDENTLY_VERIFIED`，不把整场比赛全局 BLOCKED；
- 固定图数、页数、字数、固定扰动比例等非官方指标不作为硬规则；
- Innovation Score / paper-score 等主观总分不作为官方或科学真值；
- 平台专用 DSH 插件、仓库运营元数据和 Legacy 重复工作流不进入通用 Hub。

逐项覆盖情况见：

- `references/upstream-coverage-matrix.md`（历史固定基线）
- `references/upstream-coverage-matrix.csv`
- `references/xiaoma-1.3-delta-review.md`（当前 1.3.0 增量复核）

## v0.1.5 current-upstream refresh

2026-08-31 再次复核当前公开上游后，本版本只吸收能力边界与方法思想，并继续独立重写。新增的 solver robustness、algorithm playbooks、reproducibility、Figure QA、LaTeX provenance 与 English-paper 均不是对上游脚本/正文的逐文件复制。固定阶段链、固定图数/篇幅、平台专用封装和主观总评分继续排除。

## v0.1.6 overlap-selection note

本版本改用“同能力择优”而不是“只补缺失项”的策略。详细裁决见 `references/overlap-quality-selection.md`。

特别说明：XiaoMa 的 `tools/docx/LICENSE.txt` / `tools/pdf/LICENSE.txt` 在审计基线中包含限制提取、复制、衍生和再分发的条款。因此 v0.1.6 不复制这些目录的源码/模板，只根据可观察能力边界做独立实现；这也是为什么“XiaoMa 在能力上胜出”不等于“把其代码直接打进本包”。

## v0.1.12 ScholarSkill discovery note

2026-08-31 的定向筛选把 ScholarSkill 视为能力发现/比较入口，不作为代码、文本或大规模 registry 的复制来源。采用的思想被独立转化为数据泄漏审计、决策性实验合同、不确定性预算、citation planning 与 provenance bundle；筛选裁决见 `references/scholarskill-selection-2026-08-31.md`。

## v0.1.12 route-selection integration note

选择性参考 `y3519712124-ui/math-modeling-contest-route-selection`（MIT）。只吸收局部 model-choice/refutation/flip/fallback 原语；A/B/C 选题和全局 route selection 明确保留为 Coach 决策，不新增 `competition-strategy` 或 `contest-route-selection` Skill。固定 45/55 权重、固定分差和固定 Day-One gate 未采用。

## 2026-09-10 XiaoMa 1.3.0 delta note

本次不覆盖历史 1.2.0 matrix，而是新增可追溯的增量审计。选择性吸收三类高价值变化：

1. Figure 从“设计 + 导出/QA”补成“设计 → `FIGURE_RENDER_NEEDED` → 实际成图 → QA”的执行闭环；通用 renderer 只覆盖标准图，复杂图仍写项目专用脚本。
2. DOCX/final-review 增加高特异性的内部流程残留、占位和 Markdown 机械扫描，不把正常学术词当违规词。
3. XiaoMa 的 Checkpoint V1/V2、early delivery smoke test 与 deadline engineering 属于 Coach/比赛调度职责，不下沉为 SkillHub 全局阶段；对应策略放在 `mathmodel-pro`，避免重新引入固定三阶段/门禁。

继续排除固定图数、固定篇幅、DSH 平台插件、硬阶段门禁和仓库运营元数据。
