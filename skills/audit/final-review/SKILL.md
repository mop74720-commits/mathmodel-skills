---
name: final-review
trigger: PRE_SUBMISSION
description: 提交前执行有限且高价值的最终审计：当届官方硬约束、最终 PDF/文档视觉、数字、引用、附件、内部流程残留、文件命名和 AI 使用声明。
---

# final-review

## Trigger

- 事件：`PRE_SUBMISSION`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

这是提交前最后防错，不再推动结构性创新。官方规则必须以当届来源为准，仓库内历史模板只能当工具基线。

## Inputs

- 最终论文/PDF/DOCX
- 官方当届规则/模板
- Final Run 与 Claim-Evidence Map
- 提交附件清单
- AI 使用记录（适用时）

## Procedure

0. 先读取 `rules/OFFICIAL_RULES.md` 与 `rules/RULE_PROFILE.json`。若 profile 缺失、`verified != true`、届次不匹配、`blocking_unknowns` 非空或存在影响提交的 `UNKNOWN/CONFLICT`，立即返回 `OFFICIAL_RULES_NEEDED`；不要用仓库默认页数/图数替代官方规则，也不得给出 submission-ready 结论。

1. 核对当届官方要求：提交格式、页数上限/模板、匿名信息、文件命名、附件、AI 相关声明等；规则不确定时先查官方来源。
2. 实际打开最终 PDF/文档逐页检查：空白页、裁切、乱码、字体、公式、图表、页码、目录/引用、横竖页、分辨率。
3. 对最终 DOCX 运行 `python tools/docx/scripts/paper_content_audit.py <paper.docx> --strict --json`，扫描高特异性的内部流程残留、占位符和明显 Markdown。确属正文的命中只能在人工核对后用 `--allow` 精确放行，禁止整类关闭。若最终只提交 PDF，则应对其可提取文本或权威正文源做等价检查；无文本层且没有可检查源时不能声称该项已验证。
4. 抽查并优先核对摘要和结论中的所有关键数字、单位、模型名称与 Final Run；检查旧结果是否残留。
5. 检查图表/公式/表格编号连续、正文引用存在、参考文献双向对应；无正文引用的关键图表或文献需处理。
6. 检查附录代码/数据说明是否与正文方法一致，禁止附录使用不同参数却声称可复现正文。
7. 核对 AI 使用记录和官方要求的声明/详情文件（若适用）。若官方要求记录模型/版本、使用环节、关键交互、人工修改/核验，则逐项检查真实证据；**不得为了过审补造 AI 记录、版本或“人工独立完成”声明**。缺失关键历史信息时应明确 BLOCKED。
8. 核对论文附录与支撑材料：若官方要求源程序进入论文附录和/或独立支撑材料，必须检查“文件列表、完整可运行源、支撑包内容、正文方法”四者一致。
9. 生成提交清单和关键文件哈希（只对最终提交物/关键源做锚定，不给所有临时文件哈希）。
10. 合规修复遵循最小必要修改：AI 详情、完整 provenance、源程序等若官方要求存在，应优先放入官方指定位置/隔离附录/支撑材料，不把治理语言扩写成正文主线。
11. 每次较大合规修改后重新查看正文渲染；若正文信息层级、分页、表图尺寸或阅读节奏明显恶化，必须报告“compliance overlay degraded paper quality”，并建议回到稳定正文重新设计 overlay，而不是继续堆补丁。
12. 如果发现结构性模型错误，明确 FAIL 并回对应层；否则只修提交所需的最小格式/一致性问题。

## Outputs

- 最终审计清单
- P0/P1/P2 问题
- 提交文件清单与关键哈希
- 规则来源记录
- paper-content audit 结果及任何显式 allow-list

## Checks

- 官方规则为当届有效来源
- 实际查看最终渲染而非只看源文件
- 摘要关键数字全部与 Final 一致
- 不存在 TODO/占位/内部提示残留
- 不存在无必要的 Subagent/门禁/Checkpoint/Run Ledger/provenance 等内部治理文本残留
- 提交物完整
- 规则要求的支撑材料/源程序/AI 详情真实且完整
- 不存在用占位或推测信息冒充正式 AI 披露
- 合规 overlay 没有无必要污染主正文；正文质量和附录合规分别检查

## Failure

- 官方规则缺失：BLOCKED/需先核验
- 论文内容扫描存在未解释的内部流程残留或占位：FAIL，回 writing/docx 修复
- P0 数学/结果错误：返回对应 Skill，不以“临近提交”为由掩盖
- 仅非阻断美化项：由 Coach 决定是否放弃修改

## Handoff

返回最终风险状态；只有 Coach/用户决定是否提交，本 Skill 不执行“提交许可”裁决。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
