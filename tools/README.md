# Tool implementation layer

v0.1.11 有七个质量择优后的可执行工具。它们处理机械载体、检索、复现或 QA，不拥有 Coach 的阶段/时间/提交决策权。

| Tool | Executable core |
|---|---|
| PDF | page/font/text/image/vector/bounds audit, extraction, page render |
| XLSX | workbook/formula audit, bounded row reading, explicit LibreOffice recalc |
| Figure | rich data profiling, multi-path raster/vector audit, export, source static QA, grayscale/contrast QA |
| DOCX | OOXML/OMML/style/relationship audit, template inspection, self-check, real render |
| LaTeX | doctor, generic/CJK init, bibliography-aware build, resource/ref audit, provenance, bind, PDF/font validate |
| Paper Search | OpenAlex + Crossref + DOI/fuzzy-title dedupe + filters/ranking |
| Reproducibility | feature-scoped dependency doctor, runtime-aware run manifest v2 create/verify |

所有 Tool PASS 只表示其机械检查范围通过，不自动证明模型、数值或论文科学结论正确。
