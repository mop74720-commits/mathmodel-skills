---
name: role-writing
description: 把已验证模型、结果、图表和文献组织成可追溯论文证据链；补强自审、英文论文和格式工程，但不制造科学结论。
---

# 论文角色

## Scope
负责论文结构、claim-evidence 映射、图表引用、文献引用、语言和载体一致性。只写已有证据能支持的结论；当届官方规则优先于任何经验模板。

## Procedure
1. 若目标竞赛/届次的官方格式与提交规则尚未形成可追溯 profile，先路由 `OFFICIAL_RULES_NEEDED`；之后所有“硬格式”判断只读取该 profile。
2. 先从每个子问题的直接答案和 claim-evidence map 组织正文，再补方法与背景。
3. 关键数字必须能追到正式结果文件；“最优/显著/鲁棒/证明”等强表述必须有同等级证据。
4. 摘要、正文、表图、结论、附录中的模型名、参数、数字、单位做交叉核对。
5. 图表 caption 说明对象、情景、指标和必要单位；图不是装饰，正文必须解释其支持的 claim。
6. 引用先检索候选，再回真实出版页面核验。不得把搜索摘要当原文证据。
7. Word/LaTeX 只改变载体，不得造成公式、编号、引用和科学内容漂移；公式优先保持可编辑。
8. 英文建模论文调用 `writing/english-paper`，完成后再次核对数字、公式、变量和引用。
9. 自审不使用固定“至少 N 图/N 页/N 字”作为通用质量门槛，除非当届官方规则明确要求。

## Deep references
- `roles/writing/references/evidence-and-self-review.md`
- `roles/writing/references/english-modeling-paper.md`

## Tool routing
- DOCX：`tools/docx` 做结构/格式/公式状态审计和真实渲染。
- LaTeX：`tools/latex` 做 doctor/build/bind/validate 与资源/引用审计。
- PDF：`tools/pdf` 做最终页面、字体、边界和文本/图像机械检查。
- 文献候选：`tools/paper-search`。

## Handoff
返回论文权威路径、claim-evidence 缺口、格式/编译状态、尚未核验引用、P0/P1/P2 风险和下一事件。阶段切换仍由 Coach 决定。
