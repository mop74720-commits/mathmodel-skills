#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

def sha256(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser(description='Read-only PDF page/font/text/image/boundary audit.')
    ap.add_argument('pdf'); ap.add_argument('--json',action='store_true'); a=ap.parse_args(); p=Path(a.pdf)
    import fitz
    d=fitz.open(p); pages=[]; fonts=set(); issues=[]; warnings=[]
    for i,pg in enumerate(d):
        blocks=pg.get_text('blocks'); imgs=pg.get_images(full=True); pfonts=pg.get_fonts(full=True)
        for f in pfonts:
            if len(f)>3: fonts.add(str(f[3]))
        drawings=pg.get_drawings()
        pages.append({'page':i+1,'width_pt':round(pg.rect.width,2),'height_pt':round(pg.rect.height,2),'rotation':pg.rotation,'text_chars':len(pg.get_text('text')),'text_blocks':len(blocks),'images':len(imgs),'vector_drawings':len(drawings)})
    if len(d)==0: issues.append('zero_pages')
    sizes={(x['width_pt'],x['height_pt']) for x in pages}
    if len(sizes)>1: warnings.append('mixed_page_sizes')
    metadata=d.metadata or {}; encrypted=d.is_encrypted; d.close()
    obj={'status':'FAIL' if issues else ('WARN' if warnings else 'PASS'),'file':str(p),'bytes':p.stat().st_size,'sha256':sha256(p),'pages':pages,'page_count':len(pages),'fonts':sorted(fonts),'metadata':metadata,'encrypted':encrypted,'issues':issues,'warnings':warnings,'note':'Mechanical audit only. Inspect rendered pages for clipping/overlap and scientific meaning.'}
    print(json.dumps(obj,ensure_ascii=False,indent=2)); raise SystemExit(1 if issues else 0)
if __name__=='__main__': main()
