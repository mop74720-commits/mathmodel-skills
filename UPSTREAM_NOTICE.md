# Upstream design notice

本项目参考以下公开仓库：

1. https://github.com/XiaoMaColtAI/math-modeling-skill
2. https://github.com/han69611/math-modeling-skills

本版本覆盖审计固定到：

- XiaoMa commit `e5d9313420d519f18ed1429d52d95fe0a72ae944`
- Han commit `b5b98aebcb25ff89a99ea1cbb52b31ccab5040ca`

许可证观察：XiaoMa 当前 GitHub 元数据为 `license: null`，根目录树未见 `LICENSE`；Han 的 GitHub 元数据同样为 `license: null`，但其 README 明确写有 `License: MIT`。本项目仍采用独立重写的方式，不把上游整仓源码/模板原样再分发。v0.1.4 新增的工具脚本也是依据公开能力边界重新实现，而非复制上游脚本正文。

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

- `references/upstream-coverage-matrix.md`
- `references/upstream-coverage-matrix.csv`

## v0.1.5 current-upstream refresh

2026-08-31 再次复核当前公开上游后，本版本只吸收能力边界与方法思想，并继续独立重写。新增的 solver robustness、algorithm playbooks、reproducibility、Figure QA、LaTeX provenance 与 English-paper 均不是对上游脚本/正文的逐文件复制。固定阶段链、固定图数/篇幅、平台专用封装和主观总评分继续排除。

## v0.1.6 overlap-selection note

本版本改用“同能力择优”而不是“只补缺失项”的策略。详细裁决见 `references/overlap-quality-selection.md`。

特别说明：XiaoMa 的 `tools/docx/LICENSE.txt` / `tools/pdf/LICENSE.txt` 在审计基线中包含限制提取、复制、衍生和再分发的条款。因此 v0.1.6 不复制这些目录的源码/模板，只根据可观察能力边界做独立实现；这也是为什么“XiaoMa 在能力上胜出”不等于“把其代码直接打进本包”。
