---
name: competition-rules
trigger: OFFICIAL_RULES_NEEDED
description: 把目标竞赛当届官方规则/模板提取成可追溯 rule profile，区分官方硬约束、官方建议、用户要求和内部质量目标。
---

# competition-rules

## Trigger

- 事件：`OFFICIAL_RULES_NEEDED`。
- 生成论文/最终提交物前，如果比赛届次或官方格式规则尚未核验，应调用本 Skill。
- 本 Skill 不决定比赛阶段、时间预算、冻结或提交时机；这些仍由 Coach 管理。

## Scope

只建立“规则事实基线”。不把往届经验、仓库默认值或写作偏好冒充当届官方要求。

## Inputs

- 目标竞赛与届次/年份
- 官方规则、官方模板、官方通知或其 URL/本地文件
- 用户额外要求（如有）
- 当前交付物类型（DOCX/LaTeX/PDF/附件/代码等）

## Procedure

1. 确认竞赛名称与届次。不能用未标年份的旧规则自动覆盖当前届次。
2. 按 `references/competition-rule-profile.md` 的权威层级读取来源；优先官方站点/官方规则 PDF/官方模板。
3. 逐条提取与当前交付有关的约束：文件类型/命名、页数或字数、匿名信息、摘要页、附录/附件、引用、语言、AI/工具声明、模板格式、截止时间等。
4. 每条规则标记 `OFFICIAL_HARD / OFFICIAL_GUIDANCE / USER_REQUIREMENT / LOCAL_TARGET / UNKNOWN`，并记录 source locator。强度不明确时不得升级为硬约束。
5. 若本地规则/模板文件可访问，记录 SHA-256；若只核验 URL，记录检索时间和稳定定位信息。
6. 将能机械检查的规则写成机器可读字段；无法机械验证的保留自然语言说明和人工检查项。
7. 对冲突或缺失规则显式返回 `CONFLICT/UNKNOWN`；不要自行猜测。
8. 生成 `mathmodel-competition-rules/v1` profile，并把后续 DOCX/LaTeX/PDF/final-review 的规则输入统一指向该文件。

## Outputs

- `competition-rules.yaml` 或等价的 `mathmodel-competition-rules/v1` 文件
- 官方来源列表与版本/届次
- `OFFICIAL_HARD` 约束清单
- `UNKNOWN/CONFLICT` 待核项
- 可供载体工具执行的机械检查参数

## Checks

- 所有硬约束都有官方来源和 locator
- 没有把固定图数、固定正文长度、固定模型数等内部目标冒充官方规则
- 往届规则不会无提示地用于新届次
- 用户偏好与官方规则分开记录
- 冲突项没有被静默覆盖

## Failure

- 找不到当届官方来源：保持 `UNKNOWN` 并返回风险，不伪造规则。
- 官方规则之间冲突：返回 `CONFLICT`，要求 Coach/用户决定是否继续核验。
- 规则已明确但交付物违反硬约束：转 `PRE_SUBMISSION`/载体工具修复，不在本 Skill 内改论文内容。

## Handoff

将 rule profile 交给 writing、`tools/docx`、`tools/latex`、`tools/pdf` 和 `final-review`。Coach 只需要据此处理比赛级决策，不需要重新解析规则全文。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。
