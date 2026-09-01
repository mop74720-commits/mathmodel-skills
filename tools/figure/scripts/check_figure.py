#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path
from PIL import Image
import fitz

def inspect(p):
    ext=p.suffix.lower(); out={'path':str(p),'format':ext.lstrip('.'),'warnings':[]}
    if ext in {'.png','.jpg','.jpeg','.tif','.tiff'}:
        im=Image.open(p); out['pixels']=[im.width,im.height]; out['mode']=im.mode; out['dpi']=list(im.info.get('dpi',())) or None
        if min(im.width,im.height)<600: out['warnings'].append('small_raster_dimension')
    elif ext=='.svg':
        text=p.read_text(encoding='utf-8',errors='replace'); out['has_viewbox']='viewBox' in text; out['text_elements']=len(re.findall(r'<text\b',text));
        if not out['has_viewbox']: out['warnings'].append('svg_missing_viewBox')
    elif ext=='.pdf':
        d=fitz.open(p); out['pages']=len(d); out['page_sizes']=[[round(x.rect.width,1),round(x.rect.height,1)] for x in d]
        if len(d)!=1: out['warnings'].append('figure_pdf_not_single_page')
    else: out['warnings'].append('unsupported_format')
    return out

def main():
    ap=argparse.ArgumentParser(description='Mechanical figure audit: format, dimensions and basic vector/raster metadata.')
    ap.add_argument('path'); ap.add_argument('--json',action='store_true'); a=ap.parse_args(); p=Path(a.path)
    files=[p] if p.is_file() else sorted(x for x in p.rglob('*') if x.suffix.lower() in {'.png','.jpg','.jpeg','.tif','.tiff','.svg','.pdf'})
    out=[inspect(x) for x in files]
    print(json.dumps(out,ensure_ascii=False,indent=2) if a.json else '\n'.join(f"{x['path']}: {x['format']} warnings={','.join(x['warnings']) or 'none'}" for x in out))
    raise SystemExit(1 if any(x['warnings'] for x in out) else 0)
if __name__=='__main__': main()
