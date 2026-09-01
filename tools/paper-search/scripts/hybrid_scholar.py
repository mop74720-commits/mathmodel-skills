#!/usr/bin/env python3
import argparse, json, re
from openalex_scholar import search as openalex
from crossref_scholar import search as crossref

def norm_title(s): return re.sub(r'[^a-z0-9]+',' ',(s or '').lower()).strip()
def merge(rows):
    seen={}; out=[]
    for r in rows:
        key=('doi',r['doi'].lower()) if r.get('doi') else ('title',norm_title(r.get('title')))
        if key in seen:
            prev=seen[key]; prev.setdefault('sources',[]).append(r.get('source'))
            for k in ['url','doi','year','authors']:
                if not prev.get(k) and r.get(k): prev[k]=r[k]
        else:
            x=dict(r); x['sources']=[x.pop('source',None)]; seen[key]=x; out.append(x)
    return out

def self_test():
    rows=[{'source':'a','title':'A Robust Model','doi':'10.1/x','year':2020,'url':None,'authors':[]},{'source':'b','title':'A robust model','doi':'10.1/X','year':2020,'url':'u','authors':['A']}]
    out=merge(rows); assert len(out)==1 and set(out[0]['sources'])=={'a','b'}; print('SELF_TEST_PASS')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--query'); ap.add_argument('--limit',type=int,default=10); ap.add_argument('--email'); ap.add_argument('--self-test',action='store_true'); a=ap.parse_args()
    if a.self_test: return self_test()
    if not a.query: ap.error('--query required unless --self-test')
    errors=[]; rows=[]
    for name,fn in [('openalex',lambda:openalex(a.query,a.limit,a.email)),('crossref',lambda:crossref(a.query,a.limit))]:
        try: rows.extend(fn())
        except Exception as e: errors.append(f'{name}: {e}')
    print(json.dumps({'query':a.query,'results':merge(rows),'errors':errors},ensure_ascii=False,indent=2))
    if not rows: raise SystemExit(2)
if __name__=='__main__': main()
