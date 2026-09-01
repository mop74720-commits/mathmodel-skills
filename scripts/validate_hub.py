from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
required=['Trigger','Scope','Inputs','Procedure','Outputs','Checks','Failure','Handoff']
skills=list((ROOT/'skills').rglob('SKILL.md'))
seen_names=set(); seen_events=set()
for p in skills:
    t=p.read_text(encoding='utf-8')
    for key in ('name','trigger','description'):
        if not re.search(rf'^{key}:\s*.+$',t,re.M): errors.append(f'{p}: missing frontmatter {key}')
    m=re.search(r'^name:\s*(.+)$',t,re.M); e=re.search(r'^trigger:\s*(.+)$',t,re.M)
    if m:
        name=m.group(1).strip()
        if name in seen_names: errors.append(f'duplicate skill name: {name}')
        seen_names.add(name)
    if e:
        event=e.group(1).strip()
        if event in seen_events: errors.append(f'duplicate primary event: {event}')
        seen_events.add(event)
    for h in required:
        if f'## {h}' not in t: errors.append(f'{p}: missing section {h}')
reg=(ROOT/'registry.yaml').read_text(encoding='utf-8')
for p in skills:
    rel=str(p.parent.relative_to(ROOT)).replace('\\','/')
    if f'path: {rel}' not in reg: errors.append(f'registry missing {rel}')
for role in ('modeling','coding','writing'):
    if not (ROOT/'roles'/role/'SKILL.md').exists(): errors.append(f'missing role {role}')
for tool in ('pdf','xlsx','figure','docx','latex','paper-search'):
    if not (ROOT/'tools'/tool/'SKILL.md').exists(): errors.append(f'missing tool {tool}')
if errors:
    print('FAIL')
    for x in errors: print('-',x)
    sys.exit(1)
print(f'PASS: {len(skills)} skills, {len(seen_events)} unique events, 3 roles, 6 tools')
