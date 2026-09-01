---
name: implementation
trigger: IMPLEMENT_MODEL
description: 把模型合同实现为可运行、可复现的纵向切片，再扩展到正式计算；先正确后优化。
---

# implementation

## Trigger

- 事件：`IMPLEMENT_MODEL`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

实现代码、最小运行命令和基础结果。它不负责改变数学模型来迁就代码，也不在没有合同的情况下“边写边猜”。

## Inputs

- 冻结或足够完整的模型合同
- 原始/处理后数据
- 现有项目语言与环境
- 期望输出位置

## Procedure

1. 先实现最短纵向链：读取最小输入 → 核心计算/求解 → 输出一个可核验结果；不要先做批量扫描、漂亮图或复杂工程封装。
2. 把数据 I/O、模型核心、求解配置、评估和绘图分离；核心计算尽量使用显式参数而不是依赖全局变量。
3. 将单位转换、归一化、随机种子、容差、停止条件和默认参数写入配置或日志，禁止散落在代码中。
4. 加入关键断言：维度、边界、非空、可行性、有限数值、单位/范围等；失败应尽早暴露。
5. 运行最小实例并保存命令、环境、输入版本和关键输出。随机算法固定种子用于复现，但最终稳健性不能只依赖单一种子。
6. 纵向切片通过后再扩展到全量数据、正式参数和并行/加速；性能优化不得改变数学结果而无对照。
7. 把运行结果写入 Run Ledger/实验记录，并关联 Git commit（若项目使用 Git）。

## Outputs

- 可运行源代码
- 唯一或明确的最小运行命令
- 最小结果与日志
- 必要配置/依赖说明
- Run Ledger 更新

## Checks

- 从 PROJECT_ROOT 或项目约定根目录可独立运行
- 结果来自真实执行而非手填
- 代码参数与模型合同一致
- 没有静默吞掉 solver warning/NaN
- 随机性可复现

## Failure

- 程序报错/solver 失败：转 `SOLVER_FAILED`
- 结果能跑但数值可疑：转 `NUMERICAL_SUSPECT`
- 最小链已跑通需独立核验：转 `MVP_NEEDS_CHECK`

## Handoff

默认推荐 `MVP_NEEDS_CHECK`；是否立即扩大计算由 Coach 决定。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
