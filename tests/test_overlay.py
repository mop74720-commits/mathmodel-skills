from pathlib import Path
import json
root = Path(__file__).resolve().parents[1]
assert (root / "SKILL.md").exists()
assert (root / "registry.yaml").exists()
lock = json.loads((root / "upstream-lock.json").read_text(encoding="utf-8"))
assert len(lock["xiaoma"]["commit"]) == 40
assert len(lock["han"]["commit"]) == 40
for f in ["authority.md","qa-policy.md","quantity-policy.md","routing-policy.md"]:
    assert (root / "overlay" / f).exists()
print("OVERLAY_TEST_PASS")
