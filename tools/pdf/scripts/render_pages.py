#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(description='Render PDF pages to PNG for actual visual QA.')
    ap.add_argument('pdf'); ap.add_argument('--output-dir',required=True); ap.add_argument('--dpi',type=int,default=150); ap.add_argument('--start-page',type=int,default=1); ap.add_argument('--end-page',type=int); a=ap.parse_args()
    import fitz
    p=Path(a.pdf); out=Path(a.output_dir); out.mkdir(parents=True,exist_ok=True); d=fitz.open(p)
    end=min(a.end_page or len(d),len(d)); paths=[]; zoom=a.dpi/72.0; mat=fitz.Matrix(zoom,zoom)
    for n in range(max(1,a.start_page),end+1):
        pix=d[n-1].get_pixmap(matrix=mat,alpha=False); dest=out/f'page-{n}.png'; pix.save(dest); paths.append(str(dest))
    d.close(); print(json.dumps({'pages':paths,'dpi':a.dpi,'output_dir':str(out)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
