\
from pathlib import Path
import py_compile, sys
ROOT=Path(__file__).resolve().parents[1]
required={
 'pdf':['scripts/inspect_pdf.py','scripts/extract_text.py','scripts/render_pages.py','scripts/check_bounds.py'],
 'xlsx':['scripts/audit_workbook.py','scripts/read_rows.py','scripts/stream_rows.py','scripts/recalc.py'],
 'figure':['scripts/profile_data.py','scripts/render_figure.py','scripts/check_figure.py','scripts/export_figure.py','scripts/validate_source.py','scripts/visual_qa.py'],
 'docx':['scripts/docx_audit.py','scripts/paper_content_audit.py','scripts/render_docx.py','scripts/inspect_template_format.py','scripts/self_check.py'],
 'latex':['scripts/latex_paper.py','assets/cjk_minimal.tex'],
 'paper-search':['scripts/openalex_scholar.py','scripts/crossref_scholar.py','scripts/hybrid_scholar.py'],
 'reproducibility':['scripts/run_manifest.py'],
}
errors=[]
py_files=[]
for tool, rels in required.items():
    if not (ROOT/'tools'/tool/'SKILL.md').exists(): errors.append(f'{tool}: missing SKILL.md')
    for rel in rels:
        p=ROOT/'tools'/tool/rel
        if not p.exists(): errors.append(f'{tool}: missing {rel}')
        elif p.suffix=='.py': py_files.append(p)
# Structural release check: compile without executing imports or launching external apps.
for p in sorted((ROOT/'tools').glob('*/scripts/*.py')):
    if p not in py_files: py_files.append(p)
for p in py_files:
    try: py_compile.compile(str(p), doraise=True)
    except Exception as exc: errors.append(f'{p.relative_to(ROOT)} compile failed: {exc}')
if errors:
    print('TOOL_VALIDATION_FAIL'); [print('-',x) for x in errors]; raise SystemExit(1)
print(f"TOOL_VALIDATION_PASS: {sum(len(v) for v in required.values())} implementation files across {len(required)} tools; structural compile only")
print('DEEP_TOOL_SMOKE: run tests/tool_smoke.py separately when LibreOffice/LaTeX/runtime dependencies are available')
