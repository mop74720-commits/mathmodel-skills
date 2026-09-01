# Skill Pruning Policy v0.1.12

目标：减少 Router 负担。

删除候选：
- 独立评分系统
- 重复工作流入口
- 项目管理类能力

原则：核心 Skill 执行，Reference 提供知识。


## External capability markets

ScholarSkill/其他能力市场只作为 discovery pool，不作为 dependency graph。优先强化已有 Skill/reference；只有当能力拥有独立 trigger、input/output contract、failure route，且不能作为深层 reference 表达时，才新增 Router event。
