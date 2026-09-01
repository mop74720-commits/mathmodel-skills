---
name: flowchart
trigger: FLOWCHART_NEEDED
description: 生成真正表达决策、数据流或反馈回路的流程图，不把文字列表包装成图。
---

# Flowchart

## Trigger
`FLOWCHART_NEEDED` 或用户明确要求本局部能力。

## Scope
生成真正表达决策、数据流或反馈回路的流程图，不把文字列表包装成图。

## Inputs
流程节点、分支、回退关系

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
流程图结构合同/可绘制源

## Checks
节点短、分支有条件、反馈有原因；无分支的简单步骤不强制画图。

## Failure
交给 figure 工具渲染。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
