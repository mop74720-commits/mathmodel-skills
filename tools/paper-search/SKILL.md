---
name: tool-paper-search
description: 用两个独立公共学术元数据源检索并按 DOI/题名去重，给模型/公式/主张提供可追溯入口。
---

# Tool: Paper Search

## Commands
```bash
python tools/paper-search/scripts/openalex_scholar.py --query "vehicle routing robust optimization" --limit 10
python tools/paper-search/scripts/crossref_scholar.py --query "vehicle routing robust optimization" --limit 10
python tools/paper-search/scripts/hybrid_scholar.py --query "vehicle routing robust optimization" --limit 10
python tools/paper-search/scripts/hybrid_scholar.py --self-test
```

## Policy
本实现采用 OpenAlex + Crossref，而不是复制上游 AnySearch 代码。检索结果只是候选元数据；关键公式、假设和方法主张仍需打开 DOI/出版机构原页面核验。

## Handoff
返回 title/authors/year/DOI/source URL 和检索错误；不要把搜索摘要直接当论文原文。
