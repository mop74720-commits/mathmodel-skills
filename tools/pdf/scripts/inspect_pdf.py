#!/usr/bin/env python3
import argparse, json, hashlib
from pathlib import Path
import fitz

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''): h.update(chunk)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser(description='Inspect PDF structure without OCR.')
    ap.add_argument('pdf')
    ap.add_argument('--json', action='store_true')
    args=ap.parse_args()
    path=Path(args.pdf)
    doc=fitz.open(path)
    pages=[]
    for i,p in enumerate(doc):
        text=p.get_text('text') or ''
        pages.append({
            'page':i+1,'width_pt':round(p.rect.width,2),'height_pt':round(p.rect.height,2),
            'rotation':p.rotation,'text_chars':len(text),'image_count':len(p.get_images(full=True)),
            'link_count':len(p.get_links()),'annotation_count':sum(1 for _ in (p.annots() or [])),
        })
    out={'path':str(path),'sha256':sha256(path),'pages':len(doc),'metadata':doc.metadata,'page_info':pages}
    if args.json: print(json.dumps(out,ensure_ascii=False,indent=2))
    else:
        print(f"PDF {path.name}: {len(doc)} pages sha256={out['sha256']}")
        for p in pages: print(f"p{p['page']}: {p['width_pt']}x{p['height_pt']} pt text={p['text_chars']} images={p['image_count']}")
if __name__=='__main__': main()
