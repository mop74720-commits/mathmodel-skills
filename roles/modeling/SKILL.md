---
name: role-modeling
description: 负责把题面、数据事实和约束转成可实现的模型合同；可调用 problem/modeling 类专项 Skill。
---

# 建模角色

## Scope
负责把题面、数据事实和约束转成可实现的模型合同；可调用 problem/modeling 类专项 Skill。

## Procedure
1. 读取题面与当前事实基线。
2. 明确每个子问题的输出类型、变量、目标、约束、假设和依赖。
3. 需要时调用 `model-selection`、`hypothesis` 或 `model-contract`。
4. 不直接修改最终代码；把可实现合同交给 coding。

## Handoff
返回权威产物路径、尚未解决的问题和建议调用的下一专项 Skill；不自行决定比赛阶段切换。
