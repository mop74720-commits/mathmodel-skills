---
name: claim-evidence
trigger: CLAIM_UNSUPPORTED
description: 建立或审查每个论文主张到公式、运行、表图、文献的证据路径。
---

# Claim Evidence

## Trigger
`CLAIM_UNSUPPORTED` 或用户明确要求本局部能力。

## Scope
建立或审查每个论文主张到公式、运行、表图、文献的证据路径。

## Inputs
论文大纲/正文、结果、图表、文献

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
CLAIM_EVIDENCE_MAP 更新

## Checks
核心主张不可仅引用另一段文字；关键数字必须落到 final run。

## Failure
缺证据返回 modeling/coding/experiment。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
