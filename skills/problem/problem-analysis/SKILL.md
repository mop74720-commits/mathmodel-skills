---
name: problem-analysis
trigger: PROBLEM_UNCLEAR
description: 把题面拆成可执行的问题合同，确保每个子问题的输入、目标、约束、依赖和交付都被识别。
---

# problem-analysis

## Trigger

- 事件：`PROBLEM_UNCLEAR`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

用于“还没有真正搞清楚题目要回答什么”的阶段。它不选择最终模型，也不把背景描述当作任务。核心目标是形成事实基线和逐问合同，让后续模型选择能够引用稳定输入。

## Inputs

- 完整题面与全部附件
- 官方输出要求或用户明确要求
- 已有 FACTS/ASSUMPTIONS（如存在）

## Procedure

1. 逐页/逐段读取题面，先列显式编号的子问题；不要依据段落数量或背景描述自行增加“问题”。
2. 为每个子问题建立六元素合同：已知输入/条件、待求量或决策变量、目标或评价口径、硬约束、与前后问题依赖、预期结果形态（标量/表/曲线/策略/证明）。
3. 把题面原文能直接支持的内容标为 FACT，把合理推断标为 INFERENCE，把必须补充的建模前提标为 ASSUMPTION；三者禁止混写。
4. 画出子问题依赖关系：哪些量由 q1 传入 q2，哪些问题可独立求解，哪些结果只用于验证而不是输入。
5. 检查量纲、时间范围、空间范围、对象粒度和“最优/最好/合理”等评价词是否有明确定义；不明确则触发 `PROBLEM_AMBIGUOUS`。
6. 对每个子问题写一句“最终必须给出的结论”，用于后续检查是否答非所问。
7. 形成问题合同并标注仍未解决的未知项，不在本阶段用模型术语掩盖题意缺口。

## Outputs

- 问题合同（建议写入 `problem/PROBLEM_CONTRACT.md` 或现有等价文件）
- FACT / INFERENCE / ASSUMPTION 分层清单
- 子问题依赖图或依赖表
- 未决歧义清单

## Checks

- 所有显式子问题均有合同且没有漏问
- 每个目标都能对应一个输出
- 所有硬约束有题面来源或被明确标成假设
- 后续问题引用的前置量有明确来源

## Failure

- 存在两种以上合理解释且会改变模型或答案：转 `PROBLEM_AMBIGUOUS`
- 附件结构或字段未知：转 `DATA_UNKNOWN`
- 题意已经清楚但模型未定：转 `MODEL_UNCERTAIN`

## Handoff

通常推荐 `DATA_UNKNOWN`、`PROBLEM_AMBIGUOUS` 或 `MODEL_UNCERTAIN`，具体顺序由 Coach 根据当前项目状态决定。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
