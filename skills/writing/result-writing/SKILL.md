---
name: result-writing
trigger: RESULT_SECTION_NEEDED
description: 把数值结果写成“结果+比较+原因+意义+限制”的正文证据段。
---

# Result Writing

## Trigger
`RESULT_SECTION_NEEDED` 或用户明确要求本局部能力。

## Scope
把数值结果写成“结果+比较+原因+意义+限制”的正文证据段。

## Inputs
结果分析、图表、claim

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
结果章节内容要点

## Checks
不重复表中全部数字；正文突出决定性结果和解释。

## Failure
主张缺证据转 claim-evidence。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
