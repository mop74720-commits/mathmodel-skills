---
name: solver-debug
trigger: SOLVER_FAILED
description: 系统定位 infeasible、diverge、timeout、NaN、奇异、收敛失败等问题，区分模型、实现、数值和配置故障。
---

# solver-debug

## Trigger

- 事件：`SOLVER_FAILED`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

目标不是“让求解器返回 success”，而是确定失败原因并给出最小修复。禁止通过删除约束、扩大容差或修改目标来掩盖模型错误。

## Inputs

- 完整错误日志/solver status
- 模型合同
- 最小可复现实例
- 当前参数/容差/初值
- 最近代码改动（如有）

## Procedure

1. 先按症状分类：不可行/无界、迭代不收敛、NaN/Inf、奇异矩阵/条件差、超时/规模爆炸、积分失败、随机算法停滞。
2. 建立最小复现：缩小数据/时间区间/变量规模，但保持失败机制；确认失败是否稳定复现。
3. 做模型层检查：约束是否互相矛盾、边界是否为空、目标方向是否写反、初边值是否一致、整数/逻辑约束是否错误。
4. 做实现层检查：索引错位、符号正负、单位转换、广播/shape、梯度/Jacobian、NaN 来源、整数舍入、数据类型。
5. 做数值层检查：尺度差异、病态矩阵、步长/网格、容差、初值、变量变换、参数数量级；任何缩放都要保持数学等价。
6. 做求解器层检查：算法是否适合非光滑/非凸/混合整数/刚性系统，状态码和警告是否被正确读取。
7. 每次只改一类因素并重新运行最小复现，记录“修改 → 结果”，避免多项同时改导致无法定位。
8. 若确认是模型不可行，不再通过调 solver 规避，携证据返回 modeling。

## Outputs

- 故障分类与最小复现
- 已排除原因列表
- 根因证据或当前最可能根因
- 最小修复方案与复测结果

## Checks

- 修复后仍满足原模型合同
- 没有静默删约束/改目标
- solver success 之外还检查可行性残差和结果范围
- 根因与修复之间有可复现实验

## Failure

- 模型合同本身矛盾：转 `MODEL_UNCERTAIN`/`MODEL_CONTRACT_MISSING`
- 修复后结果仍对容差/步长敏感：转 `NUMERICAL_SUSPECT`
- 只是规模慢但正确：向 Coach 返回性能风险而非自行换问题

## Handoff

根因解决后推荐 `MVP_NEEDS_CHECK` 或 `NUMERICAL_SUSPECT`。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
