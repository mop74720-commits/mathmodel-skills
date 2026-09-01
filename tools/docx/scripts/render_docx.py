#!/usr/bin/env python3
import argparse, os, shutil, subprocess, tempfile
from pathlib import Path
import fitz

def main():
    ap=argparse.ArgumentParser(description='Render DOCX via LibreOffice to PDF and page PNGs for visual QA.')
    ap.add_argument('docx'); ap.add_argument('--output-dir',required=True); ap.add_argument('--dpi',type=int,default=160); ap.add_argument('--emit-pdf',action='store_true')
    a=ap.parse_args(); src=Path(a.docx).resolve(); out=Path(a.output_dir).resolve(); out.mkdir(parents=True,exist_ok=True)
    exe=shutil.which('soffice') or shutil.which('libreoffice')
    if not exe: raise SystemExit('LibreOffice/soffice not found')
    with tempfile.TemporaryDirectory(prefix='docx_render_') as td:
        env=os.environ.copy(); env['HOME']=td
        cmd=[exe,'--headless','--convert-to','pdf','--outdir',td,str(src)]
        r=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,env=env,timeout=120)
        pdf=Path(td)/(src.stem+'.pdf')
        if r.returncode or not pdf.exists(): raise SystemExit(f"render failed: {r.stdout}")
        doc=fitz.open(pdf); scale=a.dpi/72
        for i,p in enumerate(doc): p.get_pixmap(matrix=fitz.Matrix(scale,scale),alpha=False).save(out/f'page-{i+1}.png')
        if a.emit_pdf: shutil.copy2(pdf,out/(src.stem+'.pdf'))
        print(f"rendered_pages={len(doc)} output={out}")
if __name__=='__main__': main()
