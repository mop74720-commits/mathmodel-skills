# Tool Implementation Matrix — v0.1.4

| Tool | Implemented | Smoke status | Known boundary |
|---|---|---|---|
| PDF | SHA/page/size/text/image audit; page-aware embedded text extraction | PASS | no default OCR; complex formula/table meaning still requires visual inspection |
| XLSX | workbook/sheet/formula/error/merge audit; bounded row reading | PASS | no authoritative Excel formula engine/recalc; no full template writer yet |
| Figure | CSV/TSV profiling; PNG/JPEG/TIFF/SVG/PDF mechanical audit; matplotlib export helper | PASS | semantic figure quality still requires actual visual review |
| DOCX | paragraphs/tables/headings/media/OMML/revisions/comments/LaTeX-marker audit; real render to PNG | PASS | no full LaTeX→OMML conversion/comment editing/tracked-change editing suite |
| LaTeX | doctor; CJK smoke init; real build; SHA-256 bind; basic log/PDF validate | PASS | contest-specific class/template rules remain external/official |
| Paper Search | OpenAlex + Crossref clients; DOI/title merge/dedupe | SELF-TEST PASS | live network query not exercised in the offline build container |

`PASS` only covers the mechanical behavior exercised by `tests/tool_smoke.py`; it is not a scientific/modeling PASS.
