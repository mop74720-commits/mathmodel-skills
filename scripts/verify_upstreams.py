from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
lock = json.loads((root / "upstream-lock.json").read_text(encoding="utf-8"))
required = {
    "xiaoma": [
        "SKILL.md",
        "references/roles/建模手/SKILL.md",
        "references/roles/编程手/SKILL.md",
        "references/roles/论文手/SKILL.md",
        "references/Subagent调度.md",
        "tools/docx/SKILL.md",
        "tools/figure/SKILL.md",
        "tools/latex/SKILL.md",
        "tools/paper_search/SKILL.md",
        "tools/pdf/SKILL.md",
        "tools/xlsx/SKILL.md",
    ],
    "han": [
        "skills/03-hypothesis/SKILL.md",
        "skills/03-model-selection/SKILL.md",
        "skills/06-experiment-manager/SKILL.md",
        "skills/07-result-analysis/SKILL.md",
        "skills/10-innovation-engine/SKILL.md",
        "skills/11-reviewer-mode/SKILL.md",
        "skills/12-verify/SKILL.md",
    ],
}

errors = []
for name, meta in lock.items():
    path = root / meta["path"]
    if not (path / ".git").exists():
        errors.append(f"{name}: not cloned")
        continue
    actual = subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()
    if actual != meta["commit"]:
        errors.append(f"{name}: commit {actual} != {meta['commit']}")
    for rel in required[name]:
        if not (path / rel).exists():
            errors.append(f"{name}: missing {rel}")

if errors:
    print("UPSTREAM_VERIFY_FAIL")
    print("\n".join(errors))
    sys.exit(1)
print("UPSTREAM_VERIFY_PASS")
for name, meta in lock.items():
    print(f"{name}: {meta['commit']}")
