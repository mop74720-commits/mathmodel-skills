from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
required={
    'PAPER_SYNTHESIS_NEEDED':'skills/writing/paper-synthesis/SKILL.md',
    'PAPER_TOO_BLOATED':'skills/writing/editorial-compression/SKILL.md',
    'PAPER_JUDGE_REVIEW_NEEDED':'skills/audit/judge-review/SKILL.md',
}
reg=(ROOT/'registry.yaml').read_text(encoding='utf-8')
for ev,rel in required.items():
    if ev not in reg: errors.append(f'missing registry event {ev}')
    if not (ROOT/rel).exists(): errors.append(f'missing {rel}')
contract=(ROOT/'references/paper-quality-contract.md')
if not contract.exists(): errors.append('missing paper-quality-contract.md')
else:
    t=contract.read_text(encoding='utf-8')
    for phrase in ['Repo completeness != Paper completeness','Main text / Appendix / Support','Judge scan path','Compliance overlay principle']:
        if phrase not in t: errors.append(f'paper quality contract missing {phrase}')
root=(ROOT/'SKILL.md').read_text(encoding='utf-8')
for phrase in ['Scientific Review、Judge Review、Compliance Review 分离','不把 Competition Repo 的完整性等同于论文正文的完整性']:
    if phrase not in root: errors.append(f'root invariant missing: {phrase}')
pr=(ROOT/'skills/audit/paper-review/SKILL.md').read_text(encoding='utf-8')
if 'scientific/semantic' not in pr: errors.append('paper-review not explicitly scientific/semantic')
fr=(ROOT/'skills/audit/final-review/SKILL.md').read_text(encoding='utf-8')
if 'compliance overlay degraded paper quality' not in fr: errors.append('final-review missing compliance degradation regression check')
if errors:
    print('PAPER_QUALITY_VALIDATION_FAIL')
    for e in errors: print('-',e)
    sys.exit(1)
print('PAPER_QUALITY_VALIDATION_PASS')
