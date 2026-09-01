#!/usr/bin/env python3
import argparse, hashlib, json, re, shutil, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path

def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(1024*1024),b''): h.update(c)
    return h.hexdigest()

def run(cmd,cwd=None,timeout=180):
    return subprocess.run(cmd,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=timeout)

def version_of(path):
    if not path: return None
    for flag in ('--version','-version','-v'):
        try:
            r=run([path,flag],timeout=15)
            if r.stdout.strip(): return r.stdout.strip().splitlines()[0][:300]
        except Exception: pass
    return None

def doctor(a):
    names=[a.engine,'bibtex','biber','pandoc','pdffonts']
    tools={}
    for name in names:
        path=shutil.which(name); tools[name]={'path':path,'version':version_of(path)}
    ok=bool(tools[a.engine]['path'])
    print(json.dumps({'ok':ok,'tools':tools},ensure_ascii=False,indent=2)); return 0 if ok else 2

def init_cjk(a):
    src=Path(__file__).resolve().parents[1]/'assets'/'cjk_minimal.tex'; dst=Path(a.output)
    dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dst); print(dst); return 0

def parse_log(text):
    low=text.lower(); warnings=[]; fatal=[]
    if 'latex error:' in low or '!  ==> fatal error occurred' in low: fatal.append('latex_error')
    if 'undefined references' in low or 'undefined citation' in low or 'citation' in low and 'undefined' in low: fatal.append('undefined_references_or_citations')
    if 'overfull \\hbox' in low: warnings.append('overfull_hbox')
    if 'underfull \\hbox' in low: warnings.append('underfull_hbox')
    if 'rerun to get cross-references right' in low: warnings.append('rerun_requested')
    return sorted(set(fatal)), sorted(set(warnings))

def build(a):
    main=Path(a.main).resolve(); cwd=main.parent; engine=shutil.which(a.engine)
    if not engine: print(f"missing engine: {a.engine}",file=sys.stderr); return 2
    started=time.time(); logs=[]; last=None
    for _ in range(max(1,a.runs)):
        last=run([engine,'-interaction=nonstopmode','-halt-on-error',main.name],cwd=cwd); logs.append(last.stdout)
        if last.returncode: break
    log_path=cwd/(main.stem+'.build.log'); log_path.write_text('\n\n'.join(logs),encoding='utf-8')
    pdf=cwd/(main.stem+'.pdf'); fatal,warnings=parse_log('\n'.join(logs))
    ok=bool(last is not None and last.returncode==0 and pdf.exists())
    manifest={
        'schema':'mathmodel-latex-build/v1','created_at_utc':datetime.now(timezone.utc).isoformat(),
        'main':str(main),'main_sha256':sha256(main),'engine':a.engine,'engine_path':engine,'engine_version':version_of(engine),
        'runs_requested':max(1,a.runs),'returncode':last.returncode if last else None,'elapsed_sec':round(time.time()-started,3),
        'pdf':str(pdf),'pdf_sha256':sha256(pdf) if pdf.exists() else None,'fatal':fatal,'warnings':warnings,'log':str(log_path)
    }
    manifest_path=cwd/(main.stem+'.build.json'); manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    if not ok:
        if logs: print(logs[-1][-4000:],file=sys.stderr)
        print(f'manifest={manifest_path}',file=sys.stderr); return last.returncode if last and last.returncode else 1
    if a.publish:
        pub=Path(a.publish); pub.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(pdf,pub)
    print(f"pdf={pdf} sha256={sha256(pdf)} manifest={manifest_path}"); return 0

def bind(a):
    root=Path(a.root).resolve(); output=Path(a.output).resolve(); files=[]
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.resolve()!=output and '.git' not in p.parts:
            files.append({'path':str(p.relative_to(root)).replace('\\','/'),'sha256':sha256(p),'bytes':p.stat().st_size})
    out={'schema':'mathmodel-latex-bind/v1','created_at_utc':datetime.now(timezone.utc).isoformat(),'root':str(root),'files':files}
    output.parent.mkdir(parents=True,exist_ok=True); output.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8'); print(output); return 0

def validate(a):
    main=Path(a.main).resolve(); pdf=Path(a.pdf).resolve() if a.pdf else main.with_suffix('.pdf')
    candidates=[main.with_suffix('.log'),main.parent/(main.stem+'.build.log')]
    log=next((p for p in candidates if p.exists()),None); fatal=[]; warnings=[]
    if not pdf.exists(): fatal.append('pdf_missing')
    text=main.read_text(encoding='utf-8',errors='replace')
    logtext=log.read_text(encoding='utf-8',errors='replace') if log else ''
    f2,w2=parse_log(logtext); fatal.extend(f2); warnings.extend(w2)
    if re.search(r'\\(ref|cite\w*)\{[^}]+\}',text) and not log: warnings.append('references_present_but_log_missing')
    pdf_meta=None
    if pdf.exists():
        try:
            import fitz
            d=fitz.open(pdf); pdf_meta={'pages':len(d),'page_sizes':sorted({(round(p.rect.width,1),round(p.rect.height,1)) for p in d})}; d.close()
            if pdf_meta['pages']==0: fatal.append('pdf_zero_pages')
        except Exception as e: warnings.append(f'pdf_metadata_unavailable:{type(e).__name__}')
    info={'main':str(main),'pdf':str(pdf),'main_sha256':sha256(main),'pdf_sha256':sha256(pdf) if pdf.exists() else None,'pdf_meta':pdf_meta,'fatal':sorted(set(fatal)),'warnings':sorted(set(warnings))}
    info['status']='FAIL' if info['fatal'] else ('WARN' if info['warnings'] else 'PASS')
    print(json.dumps(info,ensure_ascii=False,indent=2)); return 1 if info['fatal'] else 0

def main():
    ap=argparse.ArgumentParser(description='LaTeX doctor/build/bind/validate with provenance manifests.')
    sub=ap.add_subparsers(dest='cmd',required=True)
    p=sub.add_parser('doctor'); p.add_argument('--engine',default='xelatex'); p.set_defaults(func=doctor)
    p=sub.add_parser('init-cjk'); p.add_argument('output'); p.set_defaults(func=init_cjk)
    p=sub.add_parser('build'); p.add_argument('main'); p.add_argument('--engine',default='xelatex'); p.add_argument('--runs',type=int,default=2); p.add_argument('--publish'); p.set_defaults(func=build)
    p=sub.add_parser('bind'); p.add_argument('root'); p.add_argument('--output',required=True); p.set_defaults(func=bind)
    p=sub.add_parser('validate'); p.add_argument('main'); p.add_argument('--pdf'); p.set_defaults(func=validate)
    a=ap.parse_args(); raise SystemExit(a.func(a))
if __name__=='__main__': main()
