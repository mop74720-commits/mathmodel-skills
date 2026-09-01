# Tool implementation layer

v0.1.4 开始，六个工具从纯契约升级为可执行核心实现：

| Tool | Executable core |
|---|---|
| PDF | structure audit, page-aware embedded-text extraction |
| XLSX | workbook audit, bounded row reading |
| Figure | CSV/TSV profiling, raster/vector audit, matplotlib export helper |
| DOCX | OOXML/OMML audit, real DOCX render to page PNG |
| LaTeX | doctor, CJK smoke init, build, bind, validate |
| Paper Search | OpenAlex + Crossref + DOI/title dedupe |

这些是 Skill Hub 的机械能力，不拥有 Coach 的阶段/时间/提交权。
