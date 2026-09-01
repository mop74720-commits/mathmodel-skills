---
name: judge-review
trigger: PAPER_JUDGE_REVIEW_NEEDED
description: 模拟数学建模竞赛评委的有限注意力扫读，审查答案可定位性、结果故事线、图表证据密度和正文阅读摩擦，不使用虚构评分表。
---

# judge-review

## Trigger

- 事件：`PAPER_JUDGE_REVIEW_NEEDED`。
- 当论文已经基本成形，需要判断“评委能否在有限时间内理解本文为什么成立、为什么值得认可”时调用。
- 可在合规审查之前或之后调用；不是固定阶段。

## Scope

只读评阅。它不替代 `paper-review` 的数学/证据攻击，也不替代 `final-review` 的官方合规检查。必须遵守 `references/paper-quality-contract.md`。

## Inputs

- 实际最终候选 PDF/渲染正文
- 问题合同
- 关键 Final 结果
- Claim-Evidence Map
- 官方模板/结构规则（若有）

## Procedure

1. 先不深入公式，按有限注意力路径扫读：摘要 → 每问标题/首尾 → 关键表图 → 结论；记录每个问题第一次能明确找到“直接答案”的位置。
2. 建立 `5-minute map`：每问一句“解决什么、用什么核心模型、得到什么结果、为什么可信”。若无法从论文快速提取，记录 scan friction。
3. 检查信息层级：最重要结论是否被背景、算法百科、实现细节、审计/合规文字淹没。
4. 检查结果故事线：关键比较是否有表图锚点，图表是否被正文解释，是否存在“重要数字只藏在段落”或“图很多但没有 claim”的情况。
5. 检查模型可理解性：核心机制是否在必要公式附近被解释；是否出现连续多页公式却看不出它们如何回答题目。
6. 检查页面节奏：实际渲染中是否存在大块无意义空白、标题孤页、超小图表、表格过密、正文被附录/代码视觉污染。
7. 检查结论记忆点：评委读完后能否准确复述主要策略/数值/规律；若多个相近数字没有层级，建议突出主值、其余迁移表格。
8. 输出 P0/P1/P2 仅表示“论文呈现风险”优先级；不得把可读性问题冒充数学错误，也不得给虚构 0–100 总分。

## Outputs

- `5-minute map`
- scan-friction 清单（页/节定位）
- 最强/最弱的结果表达位置
- 建议保留、压缩、前移、后移、表图化的最小修改
- Judge-view P0/P1/P2 风险

## Checks

- 实际看过渲染页，而不是只看源码
- 每个子问题都能定位直接答案，或明确指出为什么不能
- 不根据个人审美要求统一模板
- 不用固定页数/图数/公式数作为评分标准
- 不把合规附录长度错误计入正文叙事质量；正文和附录分别评价

## Failure

- 数学/证据错误：转 `PAPER_NEEDS_ATTACK` / 对应 scientific QA
- 主要问题是冗长补丁化：转 `PAPER_TOO_BLOATED`
- 关键结果缺表图：转 `FIGURE_NEEDED`
- 官方格式/提交要求不明：转 `OFFICIAL_RULES_NEEDED`

## Handoff

返回评委视角的最小高价值修改建议；是否继续润色由 Coach 根据时间和收益决定。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
