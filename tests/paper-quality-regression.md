# Paper Quality Regression Cases

这些案例用于防止“科学/合规更严格，但论文正文反而退化”的回归。它们不是固定流程。

| Case | 症状 | Expected primary event | 不应误路由为 |
|---|---|---|---|
| Repo dump | Run、审计、provenance、AI 详情按目录顺序进入正文 | `PAPER_SYNTHESIS_NEEDED` | `WRITING_STYLE_WEAK` 单纯逐句润色 |
| Compliance patch bloat | 规则补丁、完整代码或披露内容使成熟正文被打散 | `PAPER_TOO_BLOATED` | 继续向正文追加说明 |
| Judge scan failure | 数学正确，但五分钟内找不到每问直接答案和关键结果 | `PAPER_JUDGE_REVIEW_NEEDED` | `PAPER_NEEDS_ATTACK` 冒充数学错误 |
| Scientific contradiction | 摘要/表图/公式与 Final Run 或模型合同冲突 | `PAPER_NEEDS_ATTACK` | `PAPER_JUDGE_REVIEW_NEEDED` |
| Official rule unknown | 论文是否需要特定附录/声明尚未核验 | `OFFICIAL_RULES_NEEDED` | 根据内部模板猜规则 |

## Required invariants

1. Scientific / Judge / Compliance 三类审查分别报告，不合成主观总分。
2. Appendix 很长时仍单独评价 main text；附录长度不能掩盖正文退化。
3. 合规 overlay 破坏排版或叙事时，应回稳定正文重新设计，而不是继续堆补丁。
4. 任何压缩都不能删除决定可行域、结论、强 claim 或验证成立的必要证据。
5. 所有事件仍由当前局部问题触发，不形成 `synthesis -> compression -> judge -> final` 强制链。
