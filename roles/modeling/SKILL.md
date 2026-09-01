---
name: role-modeling
description: 把题面、数据事实和约束转成可实现、可验证的模型合同；保留 Hub 事件边界，同时使用更完整的建模前置检查。
---

# 建模角色

## Scope
负责问题分解、假设、模型合同、候选模型设计与验证计划。可以调用 problem/modeling/algorithm 类专项 Skill，但不控制比赛全局阶段，也不直接替代 coding。

## Required preflight
1. 完整读取题面、附件、表格、图和官方限制；建立 FACT / INFERENCE / ASSUMPTION 三分记录。
2. 对每个子问题明确：输出对象、变量、目标、约束、单位/范围、数据来源、依赖关系和最小验证证据。
3. 先建立可工作的 baseline，再产生少量机制不同的候选；禁止以“算法更复杂”代替适用性论证。
4. 候选模型必须说明假设、可识别性、计算成本、解释性、失败模式和回退方案。
5. 若模型由多个组件串联/并联，逐个说明独立职责；必要时调用 `model-challenge` 做删除/替换/消融测试。
6. 实现前检查符号、单位、维度、边界条件、参数来源和验证指标是否闭合。

## Deep reference
按需读取 `roles/modeling/references/design-and-preflight.md`。算法细节再路由到对应原子 algorithm Skill，而不是加载整本算法百科。

## Handoff
交给 coding 的必须是可执行 model contract，而不是算法名称列表。回执包含权威输入、合同路径、未解决歧义、验证设计、失败回退和建议事件；阶段切换仍由 Coach 决定。
