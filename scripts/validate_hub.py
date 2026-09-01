from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
required = ["## Trigger", "## Scope", "## Inputs", "## Procedure", "## Outputs", "## Checks", "## Failure", "## Handoff"]
files = sorted((ROOT / "skills").glob("*/*/SKILL.md"))
errors=[]
events=[]
paths=[]
for f in files:
    text=f.read_text(encoding="utf-8")
    for h in required:
        if h not in text:
            errors.append(f"{f.relative_to(ROOT)} missing {h}")
    m=re.search(r"^trigger:\s*(\S+)", text, re.M)
    if not m:
        errors.append(f"{f.relative_to(ROOT)} missing trigger")
    else:
        events.append(m.group(1))
    if "只完成本 Skill 的局部任务，不推进比赛阶段" in text and "读取输入并确认事实/合同版本" in text:
        errors.append(f"{f.relative_to(ROOT)} still contains v0.1.0 generic procedure")

reg=(ROOT/'registry.yaml').read_text(encoding='utf-8')
reg_rows=re.findall(r'- event:\s*([A-Z0-9_]+)\n\s+name:\s*([a-z0-9-]+)\n\s+path:\s*([^\n]+)',reg)
reg_events=[x[0] for x in reg_rows]
reg_paths=[x[2].strip() for x in reg_rows]

if len(events)!=len(set(events)):
    errors.append("duplicate trigger events in Skill files")
if len(reg_events)!=len(set(reg_events)):
    errors.append("duplicate events in registry")
if len(reg_paths)!=len(set(reg_paths)):
    errors.append("duplicate paths in registry")
if set(events)!=set(reg_events):
    errors.append(f"Skill/registry event mismatch: only_files={sorted(set(events)-set(reg_events))}, only_registry={sorted(set(reg_events)-set(events))}")
actual_paths={str(f.parent.relative_to(ROOT)).replace('\\','/') for f in files}
if actual_paths!=set(reg_paths):
    errors.append(f"Skill/registry path mismatch: only_files={sorted(actual_paths-set(reg_paths))}, only_registry={sorted(set(reg_paths)-actual_paths)}")
if 'COMPETITION_STRATEGY_NEEDED' in reg_events:
    errors.append('global competition strategy must remain Coach-owned, not a first-class SkillHub event')

# v0.1.13 retains v0.1.12 local route-decision regression
route_ref=ROOT/'references/route-decision-primitives.md'
if not route_ref.exists(): errors.append('missing route-decision-primitives.md')
for rel,phrases in {
    'skills/modeling/model-selection/SKILL.md':['strongest_objection','deciding_evidence','flip_condition','fallback'],
    'skills/modeling/model-challenge/SKILL.md':['strongest_objection','simplest_viable_replacement','flip_condition'],
    'skills/modeling/model-comparison/SKILL.md':['deciding_evidence','flip_condition'],
}.items():
    txt=(ROOT/rel).read_text(encoding='utf-8')
    for phrase in phrases:
        if phrase not in txt: errors.append(f'{rel} missing route-decision field {phrase}')
if any('contest-route-selection' in p for p in reg_paths): errors.append('contest-route-selection must not become a first-class SkillHub path')

version=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
root_skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
if f'version: {version}' not in root_skill:
    errors.append(f'root SKILL version does not match VERSION={version}')
if f'version: {version}' not in reg:
    errors.append(f'registry version does not match VERSION={version}')

if errors:
    print("FAIL")
    for e in errors: print("-",e)
    sys.exit(1)
print(f"PASS: {len(files)} deep skills, {len(set(events))} unique events, registry synchronized")
