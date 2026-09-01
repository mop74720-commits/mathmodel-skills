#!/usr/bin/env python3
import argparse, hashlib, json, os, re, shutil, subprocess, sys, time
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

def safe_main(raw):
    p=Path(raw).expanduser().resolve()
    if not p.exists(): raise FileNotFoundError(p)
    if p.is_symlink(): raise ValueError('main_tex_symlink_not_allowed')
    return p

def doctor(a):
    names=list(dict.fromkeys([a.engine,'latexmk','bibtex','biber','pandoc','pdffonts']))
    tools={}
    for name in names:
        path=shutil.which(name); tools[name]={'path':path,'version':version_of(path)}
    required=[a.engine]
    if a.need_biber: required.append('biber')
    if a.need_pandoc: required.append('pandoc')
    missing=[x for x in required if not tools.get(x,{}).get('path')]
    obj={'ok':not missing,'required':required,'missing':missing,'tools':tools}
    print(json.dumps(obj,ensure_ascii=False,indent=2)); return 0 if not missing else 2

def init_cjk(a):
    src=Path(__file__).resolve().parents[1]/'assets'/'cjk_minimal.tex'; dst=Path(a.output)
    dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dst); print(dst); return 0

def init_project(a):
    out=Path(a.output_dir).resolve(); out.mkdir(parents=True,exist_ok=True)
    main=out/'main.tex'; bib=out/'references.bib'; figs=out/'figures'; figs.mkdir(exist_ok=True)
    if main.exists() and not a.overwrite: raise FileExistsError(main)
    title='Mathematical Modeling Paper' if a.contest=='generic' else ('CUMCM Modeling Paper' if a.contest=='cumcm' else 'MCM/ICM Modeling Paper')
    template=r'''\documentclass[11pt]{article}
\usepackage[margin=2.5cm]{geometry}
\usepackage{amsmath,amssymb,booktabs,graphicx,hyperref}
\usepackage[UTF8]{ctex}
\title{%s}
\author{}
\date{}
\begin{document}
\maketitle
\begin{abstract}
State the problem, model, main quantitative results, validation, and limitations.
\end{abstract}
\section{Problem Analysis}
\section{Assumptions and Notation}
\section{Model}
\section{Results and Validation}
\section{Sensitivity and Limitations}
\bibliographystyle{plain}
\bibliography{references}
\end{document}
''' % title
    main.write_text(template,encoding='utf-8'); bib.write_text('% Add verified references here.\n',encoding='utf-8')
    print(json.dumps({'main':str(main),'bib':str(bib),'contest':a.contest},ensure_ascii=False)); return 0

def parse_log(text):
    low=text.lower(); warnings=[]; fatal=[]
    if 'latex error:' in low or '!  ==> fatal error occurred' in low or 'emergency stop' in low: fatal.append('latex_error')
    if re.search(r'(undefined references|undefined citation|citation .* undefined)',low): fatal.append('undefined_references_or_citations')
    if 'overfull \\hbox' in low: warnings.append('overfull_hbox')
    if 'underfull \\hbox' in low: warnings.append('underfull_hbox')
    if 'rerun to get cross-references right' in low or 'label(s) may have changed' in low: warnings.append('rerun_requested')
    return sorted(set(fatal)), sorted(set(warnings))

def source_refs(main):
    text=main.read_text(encoding='utf-8',errors='replace')
    graphics=[]
    for g in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',text): graphics.append(g)
    bibs=[]
    for x in re.findall(r'\\bibliography\{([^}]+)\}',text): bibs.extend(v.strip() for v in x.split(','))
    citations=re.findall(r'\\cite\w*\{([^}]+)\}',text)
    labels=re.findall(r'\\label\{([^}]+)\}',text); refs=re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',text)
    return {'graphics':graphics,'bibliographies':bibs,'citation_calls':citations,'labels':labels,'refs':refs}

def resolve_graphic(main, token):
    p=main.parent/token
    if p.suffix and p.exists(): return p
    for ext in ('.pdf','.png','.jpg','.jpeg','.svg','.eps'):
        q=Path(str(p)+ext)
        if q.exists(): return q
    return None

def build(a):
    main=safe_main(a.main); cwd=main.parent; engine=shutil.which(a.engine)
    if not engine: print(f'missing engine: {a.engine}',file=sys.stderr); return 2
    started=time.time(); logs=[]; last=None
    cmd=[engine,'-interaction=nonstopmode','-halt-on-error',main.name]
    for _ in range(max(1,a.runs)):
        last=run(cmd,cwd=cwd,timeout=a.timeout); logs.append(last.stdout)
        if last.returncode: break
        aux=cwd/(main.stem+'.aux')
        if aux.exists() and a.bibliography!='none':
            auxtext=aux.read_text(errors='replace')
            if '\\bibdata' in auxtext:
                tool='biber' if a.bibliography=='biber' else 'bibtex'
                exe=shutil.which(tool)
                if exe:
                    br=run([exe,main.stem],cwd=cwd,timeout=a.timeout); logs.append(f'[{tool}]\n'+br.stdout)
                    if br.returncode: break
    log_path=cwd/(main.stem+'.build.log'); log_path.write_text('\n\n'.join(logs),encoding='utf-8')
    pdf=cwd/(main.stem+'.pdf'); fatal,warnings=parse_log('\n'.join(logs)); ok=bool(last and last.returncode==0 and pdf.exists() and not fatal)
    manifest={'schema':'mathmodel-latex-build/v2','created_at_utc':datetime.now(timezone.utc).isoformat(),'main':str(main),'main_sha256':sha256(main),'engine':a.engine,'engine_path':engine,'engine_version':version_of(engine),'runs_requested':max(1,a.runs),'bibliography':a.bibliography,'returncode':last.returncode if last else None,'elapsed_sec':round(time.time()-started,3),'pdf':str(pdf),'pdf_sha256':sha256(pdf) if pdf.exists() else None,'fatal':fatal,'warnings':warnings,'log':str(log_path)}
    mp=cwd/(main.stem+'.build.json'); mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    if ok and a.publish:
        pub=Path(a.publish).resolve(); pub.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(pdf,pub)
    print(json.dumps({'ok':ok,'pdf':str(pdf) if pdf.exists() else None,'manifest':str(mp),'fatal':fatal,'warnings':warnings},ensure_ascii=False,indent=2))
    return 0 if ok else (last.returncode if last and last.returncode else 1)

def bind(a):
    root=Path(a.root).resolve(); output=Path(a.output).resolve(); files=[]
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.resolve()!=output and '.git' not in p.parts and not p.is_symlink():
            files.append({'path':str(p.relative_to(root)).replace('\\','/'),'sha256':sha256(p),'bytes':p.stat().st_size})
    out={'schema':'mathmodel-latex-bind/v2','created_at_utc':datetime.now(timezone.utc).isoformat(),'root':str(root),'files':files}
    output.parent.mkdir(parents=True,exist_ok=True); output.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8'); print(output); return 0

def validate(a):
    main=safe_main(a.main); pdf=Path(a.pdf).resolve() if a.pdf else main.with_suffix('.pdf')
    fatal=[]; warnings=[]; refs=source_refs(main); text=main.read_text(encoding='utf-8',errors='replace')
    # resource references
    missing_graphics=[g for g in refs['graphics'] if resolve_graphic(main,g) is None]
    if missing_graphics: fatal.append('missing_graphics:'+','.join(missing_graphics[:10]))
    missing_bib=[]
    for b in refs['bibliographies']:
        q=main.parent/(b if b.endswith('.bib') else b+'.bib')
        if not q.exists(): missing_bib.append(str(q.name))
    if missing_bib: fatal.append('missing_bibliography:'+','.join(missing_bib[:10]))
    labelset=set(refs['labels']); unresolved=sorted({r for r in refs['refs'] if r not in labelset})
    if unresolved: warnings.append('source_ref_without_local_label:'+','.join(unresolved[:20]))
    log=next((p for p in [main.with_suffix('.log'),main.parent/(main.stem+'.build.log')] if p.exists()),None)
    if log:
        f2,w2=parse_log(log.read_text(encoding='utf-8',errors='replace')); fatal.extend(f2); warnings.extend(w2)
    elif refs['citation_calls'] or refs['refs']: warnings.append('references_present_but_build_log_missing')
    pdf_meta=None
    if not pdf.exists(): fatal.append('pdf_missing')
    else:
        try:
            import fitz
            d=fitz.open(pdf); sizes=[]; image_count=0; min_dpi=None
            for pg in d:
                sizes.append((round(pg.rect.width,1),round(pg.rect.height,1)))
                for img in pg.get_images(full=True):
                    try:
                        pix=fitz.Pixmap(d,img[0]); image_count+=1
                        # PDF image DPI cannot be inferred reliably without placement transform; do not fake it.
                        pix=None
                    except Exception: pass
            pdf_meta={'pages':len(d),'page_sizes':sorted(set(sizes)),'embedded_images':image_count}; d.close()
            if pdf_meta['pages']==0: fatal.append('pdf_zero_pages')
            if a.min_pages is not None and pdf_meta['pages']<a.min_pages: warnings.append(f'page_count_below_requested_min:{a.min_pages}')
            if a.max_pages is not None and pdf_meta['pages']>a.max_pages: fatal.append(f'page_count_above_requested_max:{a.max_pages}')
        except Exception as e: warnings.append(f'pdf_metadata_unavailable:{type(e).__name__}')
        pdffonts=shutil.which('pdffonts')
        if pdffonts:
            r=run([pdffonts,str(pdf)],timeout=30)
            if r.returncode==0:
                lines=[x for x in r.stdout.splitlines()[2:] if x.strip()]
                not_emb=[]
                for line in lines:
                    parts=line.split()
                    if len(parts)>=5 and parts[3].lower()=='no': not_emb.append(parts[0])
                if not_emb: warnings.append('fonts_not_embedded:'+','.join(not_emb[:10]))
    equations=len(re.findall(r'\\begin\{(?:equation\*?|align\*?|gather\*?)\}|\\\[',text))
    figures=len(refs['graphics']); tables=len(re.findall(r'\\begin\{table\*?\}',text))
    if a.min_equations is not None and equations<a.min_equations: warnings.append(f'equations_below_requested_min:{a.min_equations}')
    if a.min_figures is not None and figures<a.min_figures: warnings.append(f'figures_below_requested_min:{a.min_figures}')
    if a.min_tables is not None and tables<a.min_tables: warnings.append(f'tables_below_requested_min:{a.min_tables}')
    info={'schema':'mathmodel-latex-validate/v2','main':str(main),'pdf':str(pdf),'main_sha256':sha256(main),'pdf_sha256':sha256(pdf) if pdf.exists() else None,'source_counts':{'equations':equations,'graphics':figures,'tables':tables,'labels':len(refs['labels']),'refs':len(refs['refs']),'citation_calls':len(refs['citation_calls'])},'pdf_meta':pdf_meta,'fatal':sorted(set(fatal)),'warnings':sorted(set(warnings))}
    info['status']='FAIL' if info['fatal'] else ('WARN' if info['warnings'] else 'PASS')
    print(json.dumps(info,ensure_ascii=False,indent=2)); return 1 if info['fatal'] else 0

def main():
    ap=argparse.ArgumentParser(description='Independent LaTeX project doctor/init/build/bind/validate with provenance and resource checks.')
    sub=ap.add_subparsers(dest='cmd',required=True)
    p=sub.add_parser('doctor'); p.add_argument('--engine',default='xelatex'); p.add_argument('--need-biber',action='store_true'); p.add_argument('--need-pandoc',action='store_true'); p.set_defaults(func=doctor)
    p=sub.add_parser('init-cjk'); p.add_argument('output'); p.set_defaults(func=init_cjk)
    p=sub.add_parser('init'); p.add_argument('output_dir'); p.add_argument('--contest',choices=['generic','cumcm','mcm-icm'],default='generic'); p.add_argument('--overwrite',action='store_true'); p.set_defaults(func=init_project)
    p=sub.add_parser('build'); p.add_argument('main'); p.add_argument('--engine',default='xelatex'); p.add_argument('--runs',type=int,default=2); p.add_argument('--bibliography',choices=['auto','bibtex','biber','none'],default='auto'); p.add_argument('--timeout',type=int,default=180); p.add_argument('--publish'); p.set_defaults(func=build)
    p=sub.add_parser('bind'); p.add_argument('root'); p.add_argument('--output',required=True); p.set_defaults(func=bind)
    p=sub.add_parser('validate'); p.add_argument('main'); p.add_argument('--pdf'); p.add_argument('--min-pages',type=int); p.add_argument('--max-pages',type=int); p.add_argument('--min-equations',type=int); p.add_argument('--min-figures',type=int); p.add_argument('--min-tables',type=int); p.set_defaults(func=validate)
    a=ap.parse_args()
    if getattr(a,'bibliography',None)=='auto': a.bibliography='bibtex'
    try: rc=a.func(a)
    except Exception as e:
        print(json.dumps({'status':'FAIL','error':f'{type(e).__name__}: {e}'},ensure_ascii=False),file=sys.stderr); rc=2
    raise SystemExit(rc)
if __name__=='__main__': main()
