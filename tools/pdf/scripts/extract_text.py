#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import fitz

def parse_pages(spec, n):
    if not spec: return list(range(n))
    out=set()
    for part in spec.split(','):
        part=part.strip()
        if '-' in part:
            a,b=map(int,part.split('-',1)); out.update(range(max(1,a)-1,min(n,b)))
        else: out.add(int(part)-1)
    return sorted(i for i in out if 0<=i<n)

def main():
    ap=argparse.ArgumentParser(description='Extract embedded PDF text with page markers; no OCR.')
    ap.add_argument('pdf'); ap.add_argument('--pages'); ap.add_argument('--output'); ap.add_argument('--json',action='store_true')
    a=ap.parse_args(); doc=fitz.open(a.pdf); idx=parse_pages(a.pages,len(doc))
    rows=[{'page':i+1,'text':doc[i].get_text('text')} for i in idx]
    if a.json: content=json.dumps(rows,ensure_ascii=False,indent=2)
    else: content='\n\n'.join(f"--- PAGE {r['page']} ---\n{r['text'].rstrip()}" for r in rows)+'\n'
    if a.output: Path(a.output).write_text(content,encoding='utf-8')
    else: print(content,end='' if content.endswith('\n') else '\n')
if __name__=='__main__': main()
