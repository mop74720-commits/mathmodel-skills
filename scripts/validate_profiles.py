from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
required=[
 'references/model-composition-patterns.md',
 'references/competition-rule-profile.md',
 'templates/competition-rules.yaml',
 'roles/coding/references/matlab-implementation.md',
 'roles/coding/scripts/check_matlab_env.m',
 'references/figure-guides/selection-and-evidence.md',
 'references/figure-guides/encoding-and-layout.md',
 'references/figure-guides/pitfalls-and-review.md',
 'skills/problem/competition-rules/SKILL.md',
]
errors=[]
for rel in required:
    if not (ROOT/rel).exists(): errors.append('missing '+rel)
reg=(ROOT/'registry.yaml').read_text(encoding='utf-8')
if 'OFFICIAL_RULES_NEEDED' not in reg or 'skills/problem/competition-rules' not in reg:
    errors.append('competition-rules event not registered')
cr=(ROOT/'references/competition-rule-profile.md').read_text(encoding='utf-8')
for token in ['OFFICIAL_HARD','OFFICIAL_GUIDANCE','USER_REQUIREMENT','LOCAL_TARGET','UNKNOWN']:
    if token not in cr: errors.append('competition rule authority missing '+token)
pat=(ROOT/'references/model-composition-patterns.md').read_text(encoding='utf-8')
if 'small sample ⇒ GM(1,1)' not in pat: errors.append('anti-hard-mapping guard missing')
mat=(ROOT/'roles/coding/scripts/check_matlab_env.m').read_text(encoding='utf-8')
for token in ['Optimization Toolbox','Statistics and Machine Learning Toolbox','mathmodel-matlab-env/v1']:
    if token not in mat: errors.append('matlab profile missing '+token)
if errors:
    print('PROFILE_VALIDATION_FAIL'); [print('-',x) for x in errors]; sys.exit(1)
print('PROFILE_VALIDATION_PASS: competition-rules + model-patterns + MATLAB + figure-guides')
