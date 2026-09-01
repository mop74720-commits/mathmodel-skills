# Upstream design notice

本项目参考以下公开仓库的设计思想：

1. https://github.com/XiaoMaColtAI/math-modeling-skill
2. https://github.com/han69611/math-modeling-skills

截至本版本生成时，两者 GitHub 仓库元数据显示 `license: null`，仓库根目录也未提供可供本项目直接再分发其源码/文本的许可证声明。因此：

- 本项目不包含两仓库原始脚本、模板或大段原文复制；
- 仅吸收公开可观察到的架构思想、能力划分和工作流模式；
- Role、Skill、Tool、QA 的文字与接口均在本项目中重新编写；
- 若上游未来补充明确许可证，可再评估是否引入兼容的原始资产。

主要设计映射：

- XiaoMa：三角色分工、Skill Root / Project Root 隔离、渐进加载、独立质检、工具技能化。
- Han：假设设计、模型选择、实验记录、结果对比、创新候选、严格 reviewer 与 final verify 的局部能力。

本项目额外做出的关键改变：

- 移除固定阶段强制链；
- 移除“无 Subagent 即全局阻断”；
- 移除固定图数量、篇幅数量等非官方硬指标；
- 移除用户逐阶段审批依赖；
- 将 QA 改成状态与风险回执，由 Coach 决定是否继续、返工或降级。
