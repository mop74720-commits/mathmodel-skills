from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
reg=(ROOT/'registry.yaml').read_text(encoding='utf-8')
registry=dict(re.findall(r'- event:\s*([A-Z0-9_]+)\n\s+name:\s*([a-z0-9-]+)',reg))
sc=(ROOT/'tests/scenarios.md').read_text(encoding='utf-8')
rows=re.findall(r'\d+\. .*?-> `([A-Z0-9_]+)` -> `([a-z0-9-]+)`',sc)
errors=[]
for ev,name in rows:
    if registry.get(ev)!=name:
        errors.append(f'{ev}: scenario={name}, registry={registry.get(ev)}')
for ev,name in registry.items():
    if ev.startswith('ALGO_') and (ev,name) not in rows:
        errors.append(f'missing algorithm scenario {ev}->{name}')
if len(rows)<39:
    errors.append(f'expected >=39 routed scenarios, got {len(rows)}')
if errors:
    print('FAIL')
    for e in errors: print('-',e)
    sys.exit(1)
print(f'SCENARIO_ROUTING_PASS: {len(rows)} routed scenarios')
