---
name: experiment-manager
trigger: EXPERIMENTS_UNTRACKED
description: 轻量记录每次实验的代码版本、参数、输入、结果和淘汰原因，让成功与失败运行都可追溯。
---

# experiment-manager

## Trigger

- 事件：`EXPERIMENTS_UNTRACKED`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

不是建立完整 MLOps 平台。目标是比赛环境下避免“哪个结果是哪次跑出来的”“旧图是否对应旧代码”等常见失控。

## Inputs

- 项目 Git 状态（如使用 Git）
- 运行命令/配置
- 已有 Run Ledger 或实验目录
- 关键输出

## Procedure

1. 为每次有决策价值的运行分配稳定 `run_id`；探索性极小测试可以合并记录，不要求每次 print 都登记。
2. 记录最少字段：run_id、问题、时间、代码 commit/版本、输入版本、模型/配置、seed、状态、关键结果、备注。
3. 若参数很多，保存配置文件或参数哈希，不把几十列硬塞进 Ledger；Ledger 指向详细配置。
4. 对失败运行记录失败类型和淘汰原因；失败实验是后续排错和论文方法选择的证据。
5. 当某次运行被新结果替代，标记 `SUPERSEDED` 而不是删除；只允许一个明确的 Final 候选进入最终证据链。
6. 将结果文件/图表与 run_id 关联，避免手工复制后失去来源。
7. 只对关键工件做哈希或版本锚定，不要求给项目内每个临时文件计算 SHA。
8. 需要可机器验证的 manifest 时调用 `tools/reproducibility`：记录命令、seed、指定输入/产物 SHA-256、Git/运行时/依赖版本；禁止导出完整环境变量或秘密。

## Outputs

- 更新后的 Run Ledger
- 关键运行配置/manifest
- Final 候选与 superseded 关系

## Checks

- 任何论文关键数字都能追到 run_id
- 失败运行没有被误当 Final
- 同一 run_id 不对应多套互相冲突结果
- Git commit/代码版本记录存在（适用时）

## Failure

- 历史结果已无法追溯：返回风险并建议重新跑关键 Final
- 多个结果都被称为“最终”：转 `FINAL_RESULT_NEEDS_REVIEW`
- 需要比较实验：转 `MODELS_NEED_COMPARISON` 或 `RESULT_NEEDS_INTERPRETATION`

## Handoff

返回可追溯状态和当前 Final 候选；是否保留更多历史运行由 Coach/团队决定。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
