---
name: model-contract
trigger: MODEL_CONTRACT_MISSING
description: 冻结可实现的模型定义，使论文公式、代码参数、求解器和验证口径共享同一事实源。
---

# model-contract

## Trigger

- 事件：`MODEL_CONTRACT_MISSING`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

把“我们大概用某模型”变成可直接编码的合同。本 Skill 不负责把代码写出来，但必须让实现者不需要猜公式符号、单位、边界或目标方向。

## Inputs

- 选定模型族
- 问题合同
- 假设登记
- 数据字段表
- 已有公式/草稿

## Procedure

1. 定义状态/决策变量、索引集合、输入参数、常量和单位；同一符号不得承担两个含义。
2. 写出目标函数/输出方程/损失函数，并明确 maximize/minimize、评价口径和任何归一化。
3. 逐条写出硬约束、软约束、初始条件、边界条件和可行域；说明每条约束来源。
4. 若为统计/预测模型，固定数据划分、特征处理、训练目标和评估指标；若为机理模型，固定方程、参数、初边值与数值离散要求。
5. 明确算法接口：输入 schema、输出 schema、随机种子策略、停止条件、容差/精度参数和异常状态。
6. 定义最低验证合同：至少包含一个可计算的正确性检查（约束残差、守恒、退化极限、基准解、交叉方法等）。
7. 标注尚未冻结项；未冻结项不得在代码和论文中被当作确定事实。

## Outputs

- `METHOD_CONTRACT.md` 或项目内等价合同
- 符号/单位表
- 输入输出 schema
- 验证与失败判据

## Checks

- 公式与单位闭合
- 所有代码所需参数均有来源或默认策略
- 优化目标方向和约束不含歧义
- 验证判据可实际计算
- 论文和代码都能引用同一合同

## Failure

- 合同内部矛盾：回 `MODEL_UNCERTAIN` 或 `ASSUMPTION_WEAK`
- 缺数据字段：回 `DATA_UNKNOWN`
- 合同已冻结：转 `IMPLEMENT_MODEL`

## Handoff

推荐 `MODEL_NEEDS_REVIEW`（需要独立攻击时）或 `IMPLEMENT_MODEL`。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
