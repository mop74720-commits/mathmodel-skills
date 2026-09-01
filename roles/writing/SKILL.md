---
name: role-writing
description: 把已验证模型、结果、图表和文献选择性合成为高质量竞赛论文；明确正文/附录/支撑材料边界，并分别处理科学、编辑与合规质量。
---

# 论文角色

## Scope
负责论文结构、paper synthesis、claim-evidence、图表叙事、语言、载体一致性和评委可读性。只写已有证据能支持的结论；当届官方规则优先于经验模板。

核心不变量：**Competition Repo 追求完整，paper main text 追求选择。** 详细规则见 `references/paper-quality-contract.md`。

## Procedure
1. 若目标竞赛/届次的官方格式与提交规则尚未形成可追溯 profile，先路由 `OFFICIAL_RULES_NEEDED`；硬格式判断只读取该 profile。
2. 当 Repo 中已有大量模型/结果/审计碎片而缺少统一论文叙事，先调用 `PAPER_SYNTHESIS_NEEDED`，而不是按目录顺序复制进正文。
3. 先从每个子问题的直接答案和 claim-evidence map 组织正文，再补必要方法与背景；关键答案应能被快速定位。
4. 关键数字必须能追到正式结果；“最优/显著/鲁棒/证明”等强表述必须有同等级证据。
5. 图表用于支持高价值 claim，caption 说明对象、场景、指标和单位；正文解释其意义，不机械朗读坐标轴。
6. Audit、Run ledger、内部治理、完整 AI 交互、长 provenance、调试日志默认属于 Repo/支撑材料；仅在官方要求或影响科学解释时进入论文，并优先隔离到附录。
7. Word/LaTeX 只改变载体，不得造成公式、编号、引用和科学内容漂移；完成关键编辑后必须查看实际 PDF。
8. 若正文出现重复、算法百科、补丁化合规文字、大片低价值页面，调用 `PAPER_TOO_BLOATED`，不是继续逐句润色。
9. 论文基本成形后可调用 `PAPER_JUDGE_REVIEW_NEEDED` 模拟有限注意力扫读；它与 scientific `PAPER_NEEDS_ATTACK`、compliance `PRE_SUBMISSION` 相互独立，按当前问题按需调用，不构成固定顺序。
10. 英文建模论文调用 `writing/english-paper`，完成后再次核对数字、公式、变量和引用。
11. 自审不使用固定“至少 N 图/N 页/N 字”作为通用质量门槛，除非当届官方规则明确要求。

## Deep references
- `references/paper-quality-contract.md`
- `roles/writing/references/evidence-and-self-review.md`
- `roles/writing/references/english-modeling-paper.md`

## Tool routing
- DOCX：`tools/docx` 做结构/格式/公式状态审计和真实渲染。
- LaTeX：`tools/latex` 做 doctor/build/bind/validate 与资源/引用审计。
- PDF：`tools/pdf` 做最终页面、字体、边界和文本/图像机械检查。
- 文献候选：`tools/paper-search`。

## Handoff
返回论文权威路径、main-text/appendix/support 边界、claim-evidence 缺口、渲染状态、P0/P1/P2 风险和下一事件。阶段切换仍由 Coach 决定。
