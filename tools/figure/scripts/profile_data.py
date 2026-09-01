#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import pandas as pd

def main():
    ap=argparse.ArgumentParser(description='Profile CSV/TSV data before figure selection.')
    ap.add_argument('data'); ap.add_argument('--group',action='append',default=[]); ap.add_argument('--json',action='store_true')
    a=ap.parse_args(); p=Path(a.data)
    sep='\t' if p.suffix.lower() in {'.tsv','.tab'} else ','
    df=pd.read_csv(p,sep=sep)
    cols=[]
    for c in df.columns:
        s=df[c]; item={'name':str(c),'dtype':str(s.dtype),'n':int(s.notna().sum()),'missing':int(s.isna().sum()),'unique':int(s.nunique(dropna=True))}
        if pd.api.types.is_numeric_dtype(s):
            d=s.describe(percentiles=[.25,.5,.75]); item.update({k:(None if pd.isna(v) else float(v)) for k,v in {'min':d.get('min'),'q25':d.get('25%'),'median':d.get('50%'),'mean':d.get('mean'),'q75':d.get('75%'),'max':d.get('max'),'std':d.get('std')}.items()})
        cols.append(item)
    groups={}
    for g in a.group:
        if g in df.columns: groups[g]={str(k):int(v) for k,v in df[g].value_counts(dropna=False).head(50).items()}
    num=df.select_dtypes(include='number')
    corr=num.corr().round(4).to_dict() if 1 < num.shape[1] <= 30 else None
    out={'path':str(p),'rows':len(df),'cols':len(df.columns),'columns':cols,'groups':groups,'numeric_correlation':corr}
    print(json.dumps(out,ensure_ascii=False,indent=2,default=str) if a.json else f"{p.name}: {len(df)} rows x {len(df.columns)} cols\n"+"\n".join(f"- {x['name']}: {x['dtype']} missing={x['missing']} unique={x['unique']}" for x in cols))
if __name__=='__main__': main()
