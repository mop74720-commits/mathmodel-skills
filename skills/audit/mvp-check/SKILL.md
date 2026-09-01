---
name: mvp-check
trigger: MVP_NEEDS_CHECK
description: 独立复现最小纵向切片，确认输入→核心算法→结果链真实可运行，并满足基本模型合同。
---

# mvp-check

## Trigger

- 事件：`MVP_NEEDS_CHECK`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

只检查 MVP，不要求最终性能、完整参数扫描或所有论文图。它回答“这个方案真的跑通了吗”。

## Inputs

- 最小运行命令
- 代码和配置
- 最小输入/等价小实例
- 模型合同
- 预期关键输出

## Procedure

1. 在尽量干净、独立的执行上下文中运行用户/实现者给出的唯一最小命令，记录退出码和环境。
2. 确认命令从明确输入开始，不依赖未记录的 notebook 状态、手工中间文件或本机绝对路径。
3. 检查核心输出是否生成、数值有限、单位/范围合理，并能关联到模型合同中的主要变量。
4. 验证至少一个关键约束/残差/不变量；solver 返回 success 但违反硬约束仍视为 FAIL。
5. 改变一个简单可预测输入或使用已知小案例，检查输出响应方向是否合理，防止“代码跑了但没有真正用输入”。
6. 记录可复现命令和问题；不在 reviewer 中直接修代码。

## Outputs

- MVP 复现回执：命令、退出码、输入快照、关键输出
- P0/P1/P2 发现
- 是否可继续扩大计算的局部建议

## Checks

- 实际运行而非只读代码
- 输出确实由本次运行产生
- 基本模型约束已核对
- 没有要求完整 Final 才给 MVP PASS

## Failure

- 运行失败：FAIL → `SOLVER_FAILED`/implementation
- 能跑但数值可疑：`NUMERICAL_SUSPECT`
- 通过后可建议扩大实验并 `EXPERIMENTS_UNTRACKED`

## Handoff

返回局部 QA 状态；是否开始大规模计算仍由 Coach 决定。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
