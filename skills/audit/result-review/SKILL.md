---
name: result-review
trigger: FINAL_RESULT_NEEDS_REVIEW
description: 对候选 Final Run 做独立复现与关键结论核对，冻结论文唯一数值事实源。
---

# result-review

## Trigger

- 事件：`FINAL_RESULT_NEEDS_REVIEW`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

用于“已有最终候选结果，但需要确认它确实对应当前代码、数据和模型”的阶段。重点是防旧结果、错版本、手工改表和数值漂移。

## Inputs

- 候选 Final run_id
- 唯一复现命令
- 代码 commit/版本
- 输入版本
- 模型合同
- 论文拟引用关键数字

## Procedure

1. 确认 Final 候选唯一：若多个 run 都被标成 final，先列冲突，不自行选择赢家。
2. 从记录的输入与代码版本重新运行或在可验证条件下核对产物哈希/日志，确认关键输出属于该 run。
3. 逐项核对论文将引用的关键数字：目标值、误差、概率、时间、策略、排名、约束残差和单位。
4. 检查硬约束、边界、守恒/概率等结构条件，以及关键结果的数值合理性。
5. 检查 Final 结果与当前模型合同是否一致，尤其是参数、数据范围、目标方向、随机种子和求解器配置。
6. 标记所有旧图/旧表/旧 run 为 superseded 或非权威，避免后续写作误引用。
7. 给出 Final Run 冻结快照；任何实质代码/参数变化后该 QA 状态失效。

## Outputs

- Final Run 审查回执
- 冻结的关键数字清单
- superseded 结果清单
- 复现/约束证据

## Checks

- 关键数字全部可追溯
- 不存在多个互相冲突的“最终答案”
- 最终结果满足硬约束
- 当前论文数据与 Final 一致

## Failure

- 无法复现：FAIL → implementation/solver-debug
- 数值随精度漂移：`NUMERICAL_SUSPECT`
- 结果稳定但需解释：`RESULT_NEEDS_INTERPRETATION`

## Handoff

通过后建议 writing/claim-evidence；Coach 决定何时正式冻结。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
