#!/usr/bin/env python3
import argparse, json, shutil, subprocess, tempfile
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(description='Recalculate XLSX/XLSM with LibreOffice in an isolated directory and write a new file.')
    ap.add_argument('input'); ap.add_argument('--output',required=True); ap.add_argument('--timeout',type=int,default=120); a=ap.parse_args()
    src=Path(a.input).resolve(); dst=Path(a.output).resolve(); exe=shutil.which('libreoffice') or shutil.which('soffice')
    if not exe:
        print(json.dumps({'status':'FAIL','error':'LibreOffice/soffice not found'},ensure_ascii=False)); raise SystemExit(2)
    with tempfile.TemporaryDirectory(prefix='xlsx_recalc_') as td:
        td=Path(td); r=subprocess.run([exe,'--headless','--convert-to',src.suffix.lstrip('.'),'--outdir',str(td),str(src)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=a.timeout)
        candidate=td/src.name
        if r.returncode or not candidate.exists():
            print(json.dumps({'status':'FAIL','returncode':r.returncode,'log':r.stdout[-3000:]},ensure_ascii=False,indent=2)); raise SystemExit(1)
        dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(candidate,dst)
    print(json.dumps({'status':'PASS','input':str(src),'output':str(dst),'engine':exe,'note':'Recalculation writes a new file and never overwrites the source implicitly.'},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
