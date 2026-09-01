---
name: visualization-review
trigger: FIGURE_WEAK
description: 在论文实际尺寸与灰度/色盲条件下审查可读性和证据表达。
---

# Visualization Review

## Trigger
`FIGURE_WEAK` 或用户明确要求本局部能力。

## Scope
在论文实际尺寸与灰度/色盲条件下审查可读性和证据表达。

## Inputs
图文件、对应 claim

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
问题清单和修图建议

## Checks
检查裁切、字体、单位、图例、尺度、误导轴、统计标注、面板主次。

## Failure
严重数据语义问题返回 figure-design/result-analysis。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
