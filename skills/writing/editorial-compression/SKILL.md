---
name: editorial-compression
trigger: PAPER_TOO_BLOATED
description: 在不损失数学正确性和证据强度的前提下压缩冗长、补丁化、审计化正文，把低价值细节迁移到附录或支撑材料。
---

# editorial-compression

## Trigger

- 事件：`PAPER_TOO_BLOATED`。
- 当论文科学内容基本正确，但正文过长、重复、信息密度失衡、合规/审计补丁破坏叙事或页面大量低价值占用时调用。

## Scope

这是编辑压缩，不改变模型、结果或官方硬约束。必须遵守 `references/paper-quality-contract.md`；不得为了变短删除决定结论的假设、约束、验证和限制。

## Inputs

- 当前正文与实际渲染 PDF
- Claim-Evidence Map
- 模型合同和 Final 结果
- 官方规则 profile（若有）
- 附录/支撑材料结构

## Procedure

1. 实际查看正文渲染，标记四类负担：重复、百科式方法、内部治理/审计、低价值实现细节。
2. 对每个候选段落做 remove/move/merge test：删除是否损害理解或证据？若否删除；若只影响复现而不影响正文理解，迁移附录/支撑材料；若重复则合并。
3. 合并跨问题重复的符号、假设、共享模型和算法说明，保留问题特异部分。
4. 将结果段从“逐项报数”压成关键比较 + 表图引用 + 解释；完整数表可留表格/附录。
5. 把 Audit、Run ID、仓库路径、AI 交互详情等改为最小必要披露或迁移；官方强制要求的内容按 profile 保留，但避免成为科学叙事主线。
6. 检查公式：重复定义、只为展示复杂度而存在的公式、可用一句话引用前式的推导应压缩；关键机制公式不得删。
7. 检查渲染页的标题孤立、大片无意义空白、图表尺寸失衡和代码附录侵入正文等问题；必要时重新分页或重新设计 section break。
8. 压缩后逐项回查关键数字、公式编号、图表引用和 Claim-Evidence，防止编辑造成证据断裂。

## Outputs

- 压缩后的正文或逐段编辑方案
- `delete / merge / move-to-appendix / move-to-support / keep` 清单
- 因压缩可能引入的引用/编号修复项
- 渲染质量问题清单

## Checks

- 关键 claim、硬约束、模型机制和验证未被压缩掉
- 正文显著减少内部治理/审计语言
- 共享内容不重复
- 关键结果更容易被扫读而不是更难
- 附录长短不作为正文质量替代品
- 不以固定页数作为唯一成功标准

## Failure

- 冗长来自模型本身尚未理清：转 `PAPER_SYNTHESIS_NEEDED`
- 压缩暴露证据缺口：转 `CLAIM_UNSUPPORTED`
- 排版载体问题：调用 DOCX/LaTeX/PDF Tool 机械处理
- 压缩完成后仍无法快速理解：转 `PAPER_JUDGE_REVIEW_NEEDED`

## Handoff

返回压缩版和迁移清单；是否接受大幅删改由 Coach/用户决定。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
