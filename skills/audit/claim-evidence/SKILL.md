---
name: claim-evidence
trigger: CLAIM_UNSUPPORTED
description: 建立/审查论文关键主张到公式、运行、表图、数据和文献的直接证据路径。
---

# claim-evidence

## Trigger

- 事件：`CLAIM_UNSUPPORTED`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

目标是避免“论文说了但没有证据”“摘要数字找不到来源”“引用只证明背景不证明方法”等问题。

## Inputs

- 论文大纲或正文
- 模型合同
- Final Run/结果表
- 图表
- 已核验文献

## Procedure

1. 抽取需要证据的 claim：每个子问题核心结论、摘要数字、最优/优于/显著/稳定等强表述、关键假设和方法依据。
2. 为每个 claim 指定证据类型与精确位置：题面、公式/合同、run_id/结果字段、图表文件/编号、文献 DOI/页段。
3. 区分“直接证据”和“背景支持”：文献说某方法常用，不等于证明本题结果正确；另一段正文也不是结果证据。
4. 对所有关键数字回到 Final Run 核对，不允许用手工二次计算或旧表作为唯一来源。
5. 检查强度匹配：证据只能支持相关性时，claim 不得写因果；只做局部实验时，不得写“普遍优越”。
6. 标记缺证据 claim，明确需要 modeling/coding/experiment/writing 哪一层补齐；不要通过弱化证据标准来“补表”。
7. 更新 Claim-Evidence Map，并标记哪些 claim 已冻结。

## Outputs

- `CLAIM_EVIDENCE_MAP` 更新
- 缺证据/证据过弱的 claim 列表
- 需要返工的精确来源层

## Checks

- 每个摘要关键数字有 Final Run 来源
- 核心结论有至少一种直接证据
- 文献引用与实际 claim 匹配
- 没有循环引用正文作为证据

## Failure

- 缺计算证据：转 coding/experiment
- 缺模型依据：转 modeling/paper-search
- 只是措辞过强：转 writing/paper-review

## Handoff

返回证据覆盖状态；是否允许带 WARN 写作由 Coach 决定。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
