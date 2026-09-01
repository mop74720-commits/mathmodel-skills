# Tool Implementation Matrix — v0.1.5

| Tool | Implemented | Smoke status | Known boundary |
|---|---|---|---|
| PDF | SHA/page/size/text/image audit; page-aware embedded text extraction | PASS | no default OCR; complex formula/table meaning still requires visual inspection |
| XLSX | workbook/sheet/formula/error/merge audit; bounded row reading | PASS | no authoritative Excel formula engine/recalc; no full template writer yet |
| Figure | CSV/TSV profiling; PNG/JPEG/TIFF/SVG/PDF mechanical audit; matplotlib export helper; plotting-source static QA; grayscale/contrast raster QA | PASS | semantic figure quality still requires actual visual review; static warnings are not scientific failures |
| DOCX | paragraphs/tables/headings/media/OMML/revisions/comments/LaTeX-marker audit; real render to PNG | PASS | no full LaTeX→OMML conversion/comment editing/tracked-change editing suite |
| LaTeX | doctor; CJK smoke init; real build; build provenance JSON; SHA-256 bind; fatal/warning log/PDF validate | PASS | contest-specific class/template rules remain external/official |
| Paper Search | OpenAlex + Crossref clients; DOI/title merge/dedupe | SELF-TEST PASS | live network query not exercised in the offline build container |
| Reproducibility | feature-scoped dependency doctor; run manifest create/verify; input/artifact hashes; Git/runtime/package provenance | PASS | records only explicitly requested files/packages; not a full environment/container lockfile |

`PASS` only covers the mechanical behavior exercised by `tests/tool_smoke.py`; it is not a scientific/modeling PASS.
