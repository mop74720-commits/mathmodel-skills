# Tool implementation layer

v0.1.5 有七个可执行工具。它们处理机械载体、检索、复现或 QA，不拥有 Coach 的阶段/时间/提交决策权。

| Tool | Executable core |
|---|---|
| PDF | structure audit, page-aware embedded-text extraction |
| XLSX | workbook audit, bounded row reading |
| Figure | data profiling, raster/vector audit, matplotlib export, source static QA, grayscale raster QA |
| DOCX | OOXML/OMML audit, real DOCX render to page PNG |
| LaTeX | doctor, CJK smoke init, real build, build provenance, bind, validate |
| Paper Search | OpenAlex + Crossref + DOI/title dedupe |
| Reproducibility | feature-scoped dependency doctor, run manifest create/verify |

所有 Tool PASS 只表示其机械检查范围通过，不自动证明模型、数值或论文科学结论正确。
