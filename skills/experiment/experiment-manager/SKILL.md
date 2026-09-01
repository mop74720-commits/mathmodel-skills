---
name: experiment-manager
trigger: EXPERIMENTS_UNTRACKED
description: 轻量管理实验，使成功与失败运行都可追溯，而不是引入完整 MLOps。
---

# Experiment Manager

## Trigger
`EXPERIMENTS_UNTRACKED` 或用户明确要求本局部能力。

## Scope
轻量管理实验，使成功与失败运行都可追溯，而不是引入完整 MLOps。

## Inputs
实验目的、commit、参数、结果

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
RUN_LEDGER 更新、final run 候选

## Checks
记录 run_id、commit、model、seed、key_result、status、superseded；失败运行保留原因。

## Failure
最终唯一结果交 result-review。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
