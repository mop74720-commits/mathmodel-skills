#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
import pandas as pd

def load(p):
    if p.suffix.lower()=='.tsv': return pd.read_csv(p,sep='\t')
    if p.suffix.lower() in {'.xlsx','.xlsm'}: return pd.read_excel(p)
    return pd.read_csv(p)

def num_stats(s):
    x=pd.to_numeric(s,errors='coerce').dropna()
    if x.empty: return None
    q1,q3=x.quantile(.25),x.quantile(.75); iqr=q3-q1
    outliers=int(((x<q1-1.5*iqr)|(x>q3+1.5*iqr)).sum()) if pd.notna(iqr) else 0
    return {'n':int(x.size),'missing':int(s.isna().sum()),'min':float(x.min()),'max':float(x.max()),'mean':float(x.mean()),'median':float(x.median()),'std':float(x.std(ddof=1)) if x.size>1 else 0.0,'q1':float(q1),'q3':float(q3),'iqr_outliers':outliers,'skew':float(x.skew()) if x.size>2 else None,'unique':int(x.nunique())}

def suggest(df):
    nums=list(df.select_dtypes(include='number').columns); cats=[c for c in df.columns if c not in nums]
    s=[]
    if len(nums)>=2: s.append('scatter_or_line_for_numeric_relationship')
    if nums: s.append('distribution_or_boxplot_for_numeric_diagnostics')
    if nums and cats: s.append('grouped_box_or_point_plot_for_group_comparison')
    if len(nums)>=3: s.append('correlation_heatmap_only_if_pairwise_association_is_relevant')
    if cats: s.append('bar_or_count_plot_for_categorical_composition')
    return s

def main():
    ap=argparse.ArgumentParser(description='Data profiler for figure planning; computes diagnostics but does not choose scientific claims.')
    ap.add_argument('file'); ap.add_argument('--group'); ap.add_argument('--json',action='store_true'); a=ap.parse_args()
    p=Path(a.file); df=load(p)
    cols={}
    for c in df.columns:
        ns=num_stats(df[c]); cols[str(c)] = {'dtype':str(df[c].dtype),'missing':int(df[c].isna().sum()),'unique':int(df[c].nunique(dropna=True)),'numeric':ns}
    corr=None
    ndf=df.select_dtypes(include='number')
    if 2<=ndf.shape[1]<=30: corr={str(i):{str(j):float(v) for j,v in row.items() if pd.notna(v)} for i,row in ndf.corr().to_dict().items()}
    groups=None
    if a.group and a.group in df.columns:
        numeric_cols=[c for c in df.select_dtypes(include='number').columns if c != a.group]
        if numeric_cols:
            g=df.groupby(a.group,dropna=False)[numeric_cols].agg(['count','mean','median','std'])
            groups=json.loads(g.to_json(orient='index'))
        else:
            groups={str(k): {'rows': int(v)} for k,v in df.groupby(a.group,dropna=False).size().items()}
    obj={'file':str(p),'rows':int(len(df)),'columns':int(len(df.columns)),'column_profiles':cols,'correlation':corr,'group_summary':groups,'chart_candidates':suggest(df),'warning':'Chart candidates are mechanical suggestions. Final chart choice must follow the claim and statistical design.'}
    if a.json: print(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False))
    else: print(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False))
if __name__=='__main__': main()
