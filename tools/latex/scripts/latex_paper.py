#!/usr/bin/env python3
import argparse, hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path

def sha256(p):
    h=hashlib.sha256();
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(1024*1024),b''): h.update(c)
    return h.hexdigest()

def run(cmd,cwd=None,timeout=180):
    return subprocess.run(cmd,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=timeout)

def doctor(a):
    tools={x:shutil.which(x) for x in [a.engine,'bibtex','biber','pandoc','pdffonts']}; ok=bool(tools[a.engine]);
    print(json.dumps({'ok':ok,'tools':tools},indent=2)); return 0 if ok else 2

def init_cjk(a):
    src=Path(__file__).resolve().parents[1]/'assets'/'cjk_minimal.tex'; dst=Path(a.output); dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dst); print(dst); return 0

def build(a):
    main=Path(a.main).resolve(); cwd=main.parent; engine=shutil.which(a.engine)
    if not engine: print(f"missing engine: {a.engine}",file=sys.stderr); return 2
    logs=[]
    for _ in range(max(1,a.runs)):
        r=run([engine,'-interaction=nonstopmode','-halt-on-error',main.name],cwd=cwd); logs.append(r.stdout)
        if r.returncode: break
    (cwd/(main.stem+'.build.log')).write_text('\n\n'.join(logs),encoding='utf-8')
    pdf=cwd/(main.stem+'.pdf')
    if r.returncode or not pdf.exists(): print(logs[-1][-4000:],file=sys.stderr); return r.returncode or 1
    if a.publish: shutil.copy2(pdf,a.publish)
    print(f"pdf={pdf} sha256={sha256(pdf)}"); return 0

def bind(a):
    root=Path(a.root).resolve(); files=[]
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.name!=Path(a.output).name and '.git' not in p.parts:
            files.append({'path':str(p.relative_to(root)).replace('\\','/'),'sha256':sha256(p),'bytes':p.stat().st_size})
    out={'root':str(root),'files':files}; Path(a.output).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8'); print(a.output); return 0

def validate(a):
    main=Path(a.main).resolve(); pdf=Path(a.pdf).resolve() if a.pdf else main.with_suffix('.pdf'); log=main.with_suffix('.log'); warnings=[]
    if not pdf.exists(): warnings.append('pdf_missing')
    text=main.read_text(encoding='utf-8',errors='replace')
    if re.search(r'\\(ref|cite)\{[^}]+\}',text) and log.exists():
        lt=log.read_text(encoding='utf-8',errors='replace').lower()
        if 'undefined references' in lt or 'undefined citations' in lt: warnings.append('undefined_references_or_citations')
    if log.exists() and 'LaTeX Error:' in log.read_text(encoding='utf-8',errors='replace'): warnings.append('latex_error_in_log')
    info={'main':str(main),'pdf':str(pdf),'main_sha256':sha256(main),'pdf_sha256':sha256(pdf) if pdf.exists() else None,'warnings':warnings}
    print(json.dumps(info,ensure_ascii=False,indent=2)); return 1 if warnings else 0

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
    p=sub.add_parser('doctor'); p.add_argument('--engine',default='xelatex'); p.set_defaults(func=doctor)
    p=sub.add_parser('init-cjk'); p.add_argument('output'); p.set_defaults(func=init_cjk)
    p=sub.add_parser('build'); p.add_argument('main'); p.add_argument('--engine',default='xelatex'); p.add_argument('--runs',type=int,default=2); p.add_argument('--publish'); p.set_defaults(func=build)
    p=sub.add_parser('bind'); p.add_argument('root'); p.add_argument('--output',required=True); p.set_defaults(func=bind)
    p=sub.add_parser('validate'); p.add_argument('main'); p.add_argument('--pdf'); p.set_defaults(func=validate)
    a=ap.parse_args(); raise SystemExit(a.func(a))
if __name__=='__main__': main()
