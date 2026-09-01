# Tool Implementation Matrix — v0.1.9

| Tool | Quality-selected implementation | Validation target | Known boundary |
|---|---|---|---|
| PDF | SHA/page/size/text/image/vector/font audit; page-aware text extraction; edge/bounds scan; page render to PNG | smoke + real render | read-only; no default OCR; no upstream form-edit code; visual/scientific meaning still requires review |
| XLSX | workbook/sheet/formula/error/merge audit; bounded row read; large-file read-only streaming; explicit LibreOffice recalculation to a new file | smoke; recalc when LibreOffice available | LibreOffice ≠ authoritative Excel for every proprietary function; no silent overwrite |
| Figure | richer CSV/TSV/XLSX profiling; outlier/skew/correlation/group diagnostics; multi-path raster/SVG/PDF audit; source QA; grayscale/contrast QA; export helper | smoke + actual output review | thresholds configurable; mechanics do not establish chart semantics or statistics |
| DOCX | paragraphs/tables/headings/media/styles/OMML/revisions/comments/fields/hyperlinks/relationship audit; template-style inspection; real render; deterministic self-check | smoke + real render | no copied restricted editing code; no full comment/redline/LaTeX→OMML editing suite |
| LaTeX | feature doctor; generic/CJK init; real build + bibliography; resource/ref checks; build provenance; SHA bind; PDF/font/page audit; optional explicit rule thresholds | real XeLaTeX smoke | contest class/template rules remain external/official; source-only checks cannot prove rendered quality |
| Paper Search | OpenAlex + Crossref; DOI + high-threshold fuzzy title dedup; year/citation filters; transparent relevance ranking | network-independent self-test | metadata discovery only; paper claims require source verification |
| Reproducibility | feature-scoped dependency doctor; run manifest v2 create/verify; Python/MATLAB/other runtime identity; explicit dependency versions; input/artifact hashes; Git provenance | smoke | records explicitly requested files/dependencies; MATLAB toolbox availability is reported separately; not a container/environment lockfile |

`PASS`/smoke 仅说明机械实现按测试用例运行，不代表模型、统计结论或论文科学质量通过。

## v0.1.9 Rehearsal patch

- XLSX: added `stream_rows.py` for large read-only attachments; choose it before full workbook loading when cell/style semantics are unnecessary.
- Reproducibility: `verify` now explicitly means artifact integrity; `replay` executes the recorded command and classifies EXACT_MATCH / SEMANTIC_MATCH / MISMATCH.
- Relative input/artifact paths are resolved against manifest `--cwd`.
