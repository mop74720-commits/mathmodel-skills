#!/usr/bin/env python3
import argparse, json, requests

def search(query,limit=10,email=None,timeout=20):
    params={'search':query,'per-page':limit};
    if email: params['mailto']=email
    r=requests.get('https://api.openalex.org/works',params=params,timeout=timeout); r.raise_for_status(); out=[]
    for w in r.json().get('results',[]): out.append({'source':'openalex','title':w.get('display_name'),'year':w.get('publication_year'),'doi':(w.get('doi') or '').replace('https://doi.org/','') or None,'url':w.get('primary_location',{}).get('landing_page_url'),'authors':[a.get('author',{}).get('display_name') for a in w.get('authorships',[]) if a.get('author')]})
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--query',required=True); ap.add_argument('--limit',type=int,default=10); ap.add_argument('--email'); a=ap.parse_args(); print(json.dumps(search(a.query,a.limit,a.email),ensure_ascii=False,indent=2))
if __name__=='__main__': main()
