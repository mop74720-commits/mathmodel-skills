---
name: tool-paper-search
description: OpenAlex + Crossref + Semantic Scholar + arXiv 四个公共学术来源的元数据检索，支持 DOI/高阈值题名去重、年份/引用过滤、透明相关性排序和单源失败降级；不依赖专有搜索服务。
---

# Tool: Paper Search

```bash
python tools/paper-search/scripts/hybrid_scholar.py --query "robust vehicle routing" --limit 15 --sort relevance
python tools/paper-search/scripts/hybrid_scholar.py --query "causal inference difference in differences" --year-from 2018 --min-citations 5
python tools/paper-search/scripts/hybrid_scholar.py --self-test
```

## Sources

默认尝试四个独立公开来源：

1. OpenAlex：广覆盖 scholarly metadata；
2. Crossref：DOI/出版元数据；
3. Semantic Scholar：论文元数据、引用量和可用的开放 PDF 链接；
4. arXiv：预印本与较新的方法论文。

任一来源超时、限流或临时失败时，错误会写入 `errors`，其余来源继续返回；只有四个来源都没有产生记录时命令才以失败状态退出。该机制是 discovery fallback，不意味着不同数据库结果具有相同权威性。

## Selection

当前实现保留公共、低依赖和可替换原则：

- DOI 精确去重 + 高阈值模糊题名去重；
- 合并来源标签，避免同一论文被重复计数；
- 可选年份、最低引用量和排序；
- 相关性分数算法透明，仅用于 discovery，不冒充论文质量评分；
- arXiv 的 citation count 记为 0，避免伪造跨库引用量；
- Semantic Scholar 的开放 PDF URL 仅作为访问入口，仍需核验实际文档身份与内容。

## Recommended handoff

检索结果进入 `LITERATURE_EVIDENCE_NEEDED` / `literature-evidence`，由 Method Card 记录证据层级、方法前提、可迁移部分、失败模式与 evidence locator。不要直接从搜索排名跳到模型采用。

## Evidence boundary

检索结果只是候选元数据。关键公式、定理、算法条件和性能主张必须打开真实论文/出版页面核验；不得从题名、摘要、citation count 或搜索相关性分数直接推出科学结论。若只能核到元数据，证据层级必须保持 `METADATA_ONLY`。
