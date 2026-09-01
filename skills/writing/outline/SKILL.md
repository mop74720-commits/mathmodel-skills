---
name: outline
trigger: PAPER_OUTLINE_NEEDED
description: 从问题合同与证据链组织论文大纲，让每一节都有明确 claim 和证据落点，而不是套固定章节模板。
---

# outline

## Trigger

- 事件：`PAPER_OUTLINE_NEEDED`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

用于写长正文前组织结构。官方模板规定的章节必须服从官方要求，但在允许范围内按题目逻辑组织。

## Inputs

- 问题合同
- 模型合同
- Final 结果与图表
- Claim-Evidence Map（如有）
- 官方结构要求（如已知）

## Procedure

1. 按子问题和跨问题依赖列出论文必须回答的核心 claim；先确保覆盖题目，再考虑“漂亮结构”。
2. 为每个 claim 指定证据：公式/模型合同、结果表、图、run_id、文献；缺证据的 claim 不进入正文承诺。
3. 组织章节顺序：问题理解 → 假设/符号 → 模型与求解 → 结果/验证 → 评价/限制，具体拆分随题目而变，不强制每问固定四小节。
4. 跨问题共享的模型、数据处理和符号只定义一次，后文引用；避免每问重复大段背景。
5. 将验证、敏感性、鲁棒性放在能直接支撑对应结论的位置，而不是统一堆到最后造成证据断裂。
6. 标记摘要需要引用的关键结果，确保这些结果来自 Final Run 且正文有落点。
7. 检查篇章比例：真正决定答案的建模与结果应占主位，背景和工具介绍只保留必要内容。

## Outputs

- 论文大纲
- 逐节 claim-evidence 列表
- 缺证据/待补内容清单
- 摘要关键数字候选

## Checks

- 每个子问题都有明确落点
- 每个主要 claim 至少有一种直接证据
- 没有大段与结果无关的算法百科
- 共享内容不重复定义

## Failure

- 关键 claim 无证据：转 `CLAIM_UNSUPPORTED`
- 结果未冻结：转 `FINAL_RESULT_NEEDS_REVIEW`
- 大纲稳定后：可转 `RESULT_SECTION_NEEDED`/`ABSTRACT_NEEDED`

## Handoff

返回大纲和缺口，不自行决定论文何时冻结。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
