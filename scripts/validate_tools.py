from pathlib import Path
import subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
required={
 'pdf':['scripts/inspect_pdf.py','scripts/extract_text.py'],
 'xlsx':['scripts/audit_workbook.py','scripts/read_rows.py'],
 'figure':['scripts/profile_data.py','scripts/check_figure.py','scripts/export_figure.py','scripts/validate_source.py','scripts/visual_qa.py'],
 'docx':['scripts/docx_audit.py','scripts/render_docx.py'],
 'latex':['scripts/latex_paper.py','assets/cjk_minimal.tex'],
 'paper-search':['scripts/openalex_scholar.py','scripts/crossref_scholar.py','scripts/hybrid_scholar.py'],
 'reproducibility':['scripts/run_manifest.py'],
}
errors=[]
for tool, rels in required.items():
    if not (ROOT/'tools'/tool/'SKILL.md').exists(): errors.append(f'{tool}: missing SKILL.md')
    for rel in rels:
        p=ROOT/'tools'/tool/rel
        if not p.exists(): errors.append(f'{tool}: missing {rel}')
for p in (ROOT/'tools').glob('*/scripts/*.py'):
    r=subprocess.run([sys.executable,str(p),'--help'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    if r.returncode not in (0,): errors.append(f'{p.relative_to(ROOT)} --help exit={r.returncode}')
if errors:
    print('TOOL_VALIDATION_FAIL'); [print('-',x) for x in errors]; raise SystemExit(1)
print(f"TOOL_VALIDATION_PASS: {sum(len(v) for v in required.values())} implementation files across {len(required)} tools")
