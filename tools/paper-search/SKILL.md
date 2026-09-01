---
name: tool-paper-search
description: OpenAlex + Crossref 双公共源检索，加入 DOI/模糊题名去重、年份/引用过滤与透明相关性排序；不依赖专有搜索服务。
---

# Tool: Paper Search

```bash
python tools/paper-search/scripts/hybrid_scholar.py --query "robust vehicle routing" --limit 15 --sort relevance
python tools/paper-search/scripts/hybrid_scholar.py --query "grey prediction GM(1,1)" --year-from 2015 --min-citations 5
python tools/paper-search/scripts/hybrid_scholar.py --self-test
```

## Selection
XiaoMa 在过滤、排序和去重深度上优于早期 Hub；Hub 的 OpenAlex + Crossref 方案则具有公共、无密钥、可替换的优势。v0.1.6 选择融合：
- 保留两个公共独立元数据源；
- DOI 精确去重 + 高阈值模糊题名去重；
- 可选年份、最低引用量和排序；
- 相关性分数算法透明，仅用于 discovery，不冒充论文质量评分。

## Evidence boundary
检索结果只是候选元数据。关键公式、定理、算法条件和性能主张必须打开真实论文/出版页面核验；不得从题名、摘要或 citation count 直接推出科学结论。
