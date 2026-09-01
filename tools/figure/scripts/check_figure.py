#!/usr/bin/env python3
import argparse, glob, json, re
from pathlib import Path

def expand(items):
    out=[]
    for raw in items:
        p=Path(raw)
        if any(ch in raw for ch in '*?[]'):
            out.extend(Path(x) for x in glob.glob(raw, recursive=True))
        elif p.is_dir():
            out.extend(q for q in p.rglob('*') if q.is_file())
        else: out.append(p)
    seen=[]
    for p in out:
        rp=p.resolve()
        if rp not in seen: seen.append(rp)
    return seen

def raster(p, min_width, min_height, min_dpi):
    from PIL import Image
    issues=[]; warnings=[]
    with Image.open(p) as im:
        w,h=im.size; dpi=im.info.get('dpi') or (None,None)
        dx=dpi[0] if isinstance(dpi,(tuple,list)) and dpi else None
        dy=dpi[1] if isinstance(dpi,(tuple,list)) and len(dpi)>1 else dx
        if w < min_width or h < min_height: warnings.append('small_pixel_dimensions')
        if dx and dy and (dx < min_dpi or dy < min_dpi): warnings.append('low_embedded_dpi')
        if im.mode in ('P','L','1'): warnings.append('limited_color_mode')
        return {'kind':'raster','width_px':w,'height_px':h,'dpi':[dx,dy],'mode':im.mode,'issues':issues,'warnings':warnings}

def svg(p):
    text=p.read_text(encoding='utf-8',errors='replace')
    warnings=[]
    has_viewbox=bool(re.search(r'\bviewBox\s*=',text,re.I))
    if not has_viewbox: warnings.append('svg_missing_viewbox')
    width=re.search(r'\bwidth=["\']([^"\']+)',text,re.I); height=re.search(r'\bheight=["\']([^"\']+)',text,re.I)
    if not width or not height: warnings.append('svg_physical_size_not_explicit')
    text_nodes=len(re.findall(r'<text\b',text,re.I))
    return {'kind':'svg','viewBox':has_viewbox,'width':width.group(1) if width else None,'height':height.group(1) if height else None,'text_nodes':text_nodes,'issues':[],'warnings':warnings}

def pdf(p):
    import fitz
    d=fitz.open(p); warnings=[]; issues=[]
    pages=[]
    for pg in d:
        pages.append({'width_pt':round(pg.rect.width,2),'height_pt':round(pg.rect.height,2),'images':len(pg.get_images(full=True)),'text_chars':len(pg.get_text('text'))})
    if len(d)!=1: warnings.append('figure_pdf_not_single_page')
    if len(d)==0: issues.append('pdf_zero_pages')
    d.close(); return {'kind':'pdf','pages':pages,'issues':issues,'warnings':warnings}

def inspect(p,args):
    if not p.exists(): return {'path':str(p),'kind':'missing','issues':['file_missing'],'warnings':[],'status':'FAIL'}
    ext=p.suffix.lower()
    try:
        if ext in {'.png','.jpg','.jpeg','.tif','.tiff','.webp'}: r=raster(p,args.min_width,args.min_height,args.min_dpi)
        elif ext=='.svg': r=svg(p)
        elif ext=='.pdf': r=pdf(p)
        else: return {'path':str(p),'kind':'unsupported','issues':[],'warnings':['unsupported_extension'],'status':'WARN'}
    except Exception as e:
        return {'path':str(p),'kind':ext.lstrip('.'),'issues':[f'inspection_error:{type(e).__name__}'],'warnings':[],'status':'FAIL'}
    r['path']=str(p); r['bytes']=p.stat().st_size
    r['status']='FAIL' if r['issues'] else ('WARN' if r['warnings'] else 'PASS')
    return r

def main():
    ap=argparse.ArgumentParser(description='Mechanical audit for raster/SVG/PDF figures; accepts files, directories and globs.')
    ap.add_argument('paths',nargs='+'); ap.add_argument('--min-width',type=int,default=900); ap.add_argument('--min-height',type=int,default=600); ap.add_argument('--min-dpi',type=float,default=200)
    ap.add_argument('--strict',action='store_true'); ap.add_argument('--json',action='store_true')
    a=ap.parse_args(); files=expand(a.paths); results=[inspect(p,a) for p in files]
    summary={'files':len(results),'pass':sum(r['status']=='PASS' for r in results),'warn':sum(r['status']=='WARN' for r in results),'fail':sum(r['status']=='FAIL' for r in results)}
    obj={'summary':summary,'results':results,'note':'Mechanical QA does not establish scientific correctness or chart semantics.'}
    if a.json: print(json.dumps(obj,ensure_ascii=False,indent=2))
    else:
        for r in results: print(f"{r['status']:4} {r['path']} warnings={','.join(r.get('warnings',[]))} issues={','.join(r.get('issues',[]))}")
        print(summary)
    if summary['fail'] or (a.strict and summary['warn']): raise SystemExit(1)
if __name__=='__main__': main()
