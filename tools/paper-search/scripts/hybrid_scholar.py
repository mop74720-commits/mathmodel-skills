#!/usr/bin/env python3
import argparse, json, math, re
from difflib import SequenceMatcher
from openalex_scholar import search as openalex
from crossref_scholar import search as crossref

def norm_title(s): return re.sub(r'[^a-z0-9]+',' ',(s or '').lower()).strip()
def doi_norm(s): return (s or '').lower().replace('https://doi.org/','').replace('doi:','').strip()
def token_set(s): return {x for x in norm_title(s).split() if len(x)>1}
def title_similarity(a,b): return SequenceMatcher(None,norm_title(a),norm_title(b)).ratio()

def equivalent(a,b,threshold=.96):
    da,db=doi_norm(a.get('doi')),doi_norm(b.get('doi'))
    if da and db: return da==db
    na,nb=norm_title(a.get('title')),norm_title(b.get('title'))
    return bool(na and nb and (na==nb or title_similarity(na,nb)>=threshold))

def merge(rows,threshold=.96):
    out=[]
    for r in rows:
        hit=next((x for x in out if equivalent(x,r,threshold)),None)
        if hit:
            src=r.get('source'); hit.setdefault('sources',[])
            if src and src not in hit['sources']: hit['sources'].append(src)
            for k in ('url','doi','year','authors','venue','type'):
                if not hit.get(k) and r.get(k): hit[k]=r[k]
            hit['cited_by_count']=max(int(hit.get('cited_by_count') or 0),int(r.get('cited_by_count') or 0))
        else:
            x=dict(r); src=x.pop('source',None); x['sources']=[src] if src else []; out.append(x)
    return out

def relevance(query,row):
    q=token_set(query); t=token_set(row.get('title')); venue=token_set(row.get('venue'))
    overlap=len(q&t)/max(1,len(q)); venue_overlap=len(q&venue)/max(1,len(q)); citation=math.log1p(max(0,int(row.get('cited_by_count') or 0)))
    return round(0.78*overlap+0.07*venue_overlap+0.15*min(citation/10,1),6)

def filter_rank(query,rows,year_from=None,year_to=None,min_citations=0,sort='relevance'):
    out=[]
    for r in rows:
        year=r.get('year'); cites=int(r.get('cited_by_count') or 0)
        if year_from is not None and (year is None or year<year_from): continue
        if year_to is not None and (year is None or year>year_to): continue
        if cites<min_citations: continue
        x=dict(r); x['relevance_score']=relevance(query,x); out.append(x)
    if sort=='citations': out.sort(key=lambda x:(x.get('cited_by_count') or 0,x['relevance_score']),reverse=True)
    elif sort=='year': out.sort(key=lambda x:(x.get('year') or -1,x['relevance_score']),reverse=True)
    else: out.sort(key=lambda x:(x['relevance_score'],x.get('cited_by_count') or 0),reverse=True)
    return out

def self_test():
    rows=[{'source':'a','title':'A Robust Model for Routing','doi':'10.1/x','year':2020,'url':None,'authors':[],'cited_by_count':5},{'source':'b','title':'A robust model for routing','doi':'10.1/X','year':2020,'url':'u','authors':['A'],'cited_by_count':7},{'source':'c','title':'Robust Models for Routing','doi':None,'year':2021,'url':'v','authors':[],'cited_by_count':1}]
    out=merge(rows); assert len(out)==2 and set(out[0]['sources'])=={'a','b'}; ranked=filter_rank('robust routing',out); assert ranked[0]['relevance_score']>=ranked[-1]['relevance_score']; print('SELF_TEST_PASS')

def main():
    ap=argparse.ArgumentParser(description='Public-source academic metadata search with DOI/fuzzy-title dedup and transparent ranking.')
    ap.add_argument('--query'); ap.add_argument('--limit',type=int,default=10); ap.add_argument('--fetch-per-source',type=int); ap.add_argument('--email'); ap.add_argument('--year-from',type=int); ap.add_argument('--year-to',type=int); ap.add_argument('--min-citations',type=int,default=0); ap.add_argument('--sort',choices=['relevance','citations','year'],default='relevance'); ap.add_argument('--title-similarity',type=float,default=.96); ap.add_argument('--self-test',action='store_true'); a=ap.parse_args()
    if a.self_test: return self_test()
    if not a.query: ap.error('--query required unless --self-test')
    n=a.fetch_per_source or max(a.limit*2,20); errors=[]; rows=[]
    for name,fn in [('openalex',lambda:openalex(a.query,n,a.email)),('crossref',lambda:crossref(a.query,n))]:
        try: rows.extend(fn())
        except Exception as e: errors.append(f'{name}: {type(e).__name__}: {e}')
    merged=merge(rows,a.title_similarity); ranked=filter_rank(a.query,merged,a.year_from,a.year_to,a.min_citations,a.sort)[:a.limit]
    print(json.dumps({'query':a.query,'sources_attempted':['openalex','crossref'],'raw_records':len(rows),'deduplicated_records':len(merged),'results':ranked,'errors':errors,'warning':'Metadata/relevance scores are discovery aids; verify key claims in the actual publication.'},ensure_ascii=False,indent=2))
    if not rows: raise SystemExit(2)
if __name__=='__main__': main()
