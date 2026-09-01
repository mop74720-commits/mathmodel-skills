---
name: figure-design
trigger: FIGURE_NEEDED
description: 围绕一个明确 claim 选择最小充分图型与统计口径。
---

# Figure Design

## Trigger
`FIGURE_NEEDED` 或用户明确要求本局部能力。

## Scope
围绕一个明确 claim 选择最小充分图型与统计口径。

## Inputs
claim、数据、目标尺寸

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
图表合同：claim/数据/图型/编码/统计/尺寸/caption 要点

## Checks
先回答图的含义、价值、证据作用；避免装饰性图。

## Failure
成图后转 visualization-review。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
