#!/usr/bin/env python3
import argparse, json, requests

def search(query,limit=10,timeout=20):
    r=requests.get('https://api.crossref.org/works',params={'query.bibliographic':query,'rows':min(max(limit,1),100)},headers={'User-Agent':'mathmodel-skills/0.1.6 (metadata research helper)'},timeout=timeout); r.raise_for_status(); out=[]
    for w in r.json()['message'].get('items',[]):
        title=(w.get('title') or [None])[0]; authors=[' '.join(x for x in [a.get('given'),a.get('family')] if x) for a in w.get('author',[])]
        year=None; parts=(w.get('published-print') or w.get('published-online') or w.get('issued') or {}).get('date-parts') or []
        if parts and parts[0]: year=parts[0][0]
        venue=(w.get('container-title') or [None])[0]
        out.append({'source':'crossref','title':title,'year':year,'doi':w.get('DOI'),'url':w.get('URL'),'authors':authors,'venue':venue,'cited_by_count':w.get('is-referenced-by-count') or 0,'type':w.get('type')})
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--query',required=True); ap.add_argument('--limit',type=int,default=10); a=ap.parse_args(); print(json.dumps(search(a.query,a.limit),ensure_ascii=False,indent=2))
if __name__=='__main__': main()
