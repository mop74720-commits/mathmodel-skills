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
