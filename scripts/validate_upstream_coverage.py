from pathlib import Path
import csv, sys
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'references'/'upstream-coverage-matrix.csv'
errors=[]
with p.open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f))
allowed={'FULL','TRANSFORMED','PARTIAL','EXCLUDED'}
if len(rows)!=72:
    errors.append(f'expected 72 upstream rows, got {len(rows)}')
for i,r in enumerate(rows,2):
    if r['status'] not in allowed:
        errors.append(f'row {i}: invalid status {r["status"]}')
    for k in ['source','item','mapping','decision','notes']:
        if not r[k].strip(): errors.append(f'row {i}: empty {k}')
xs=[r for r in rows if r['source'].startswith('XiaoMaColtAI/')]
hs=[r for r in rows if r['source'].startswith('han69611/')]
if len(xs)!=35: errors.append(f'expected 35 XiaoMa rows, got {len(xs)}')
if len(hs)!=37: errors.append(f'expected 37 Han rows, got {len(hs)}')
# Key newly closed gaps must be FULL.
required_full={
    'assets/02-预测类算法说明.md','assets/03-评价类算法说明.md','assets/06-综合类算法说明.md',
    'challenge-yourself','domain-knowledge'
}
for item in required_full:
    matches=[r for r in rows if r['item']==item]
    if not matches or matches[0]['status']!='FULL':
        errors.append(f'{item}: expected FULL')
if errors:
    print('FAIL')
    for e in errors: print('-',e)
    sys.exit(1)
print(f'UPSTREAM_COVERAGE_PASS: {len(rows)} rows (XiaoMa={len(xs)}, Han={len(hs)})')
