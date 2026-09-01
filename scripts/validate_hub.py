from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
required = ["## Trigger", "## Scope", "## Inputs", "## Procedure", "## Outputs", "## Checks", "## Failure", "## Handoff"]
files = sorted((ROOT / "skills").glob("*/*/SKILL.md"))
errors=[]
events=[]
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
    # Guard against the old generic placeholder procedure.
    if "只完成本 Skill 的局部任务，不推进比赛阶段" in text and "读取输入并确认事实/合同版本" in text:
        errors.append(f"{f.relative_to(ROOT)} still contains v0.1.0 generic procedure")
if len(files)!=39:
    errors.append(f"expected 39 skills (27 core + 12 algorithm), got {len(files)}")
if len(events)!=len(set(events)):
    errors.append("duplicate trigger events")
if errors:
    print("FAIL")
    for e in errors: print("-",e)
    sys.exit(1)
print(f"PASS: {len(files)} deep skills, {len(set(events))} unique events")
