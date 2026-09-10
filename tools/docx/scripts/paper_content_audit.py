#!/usr/bin/env python3
"""High-specificity scan for internal workflow residue and placeholders in paper text.

The scanner is intentionally conservative. It does not ban generic academic words such as
"validation", "audit", or "reproducibility". Findings may be explicitly allow-listed after
human verification; mechanical PASS never proves scientific correctness.
"""
from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

PATTERNS = {
    "governance": [
        ("stage_gate_code", r"(?<![A-Za-z0-9])(?:M1|P1|P2|W1|W2)(?![A-Za-z0-9])"),
        ("subagent", r"\bSubagent\b"),
        ("run_ledger", r"\bRun\s+Ledger\b"),
        ("qa_receipt", r"\bQA\s+receipt\b"),
        ("provenance_bundle", r"\bprovenance\s+bundle\b"),
        ("checkpoint", r"\bCheckpoint\s+V[12]\b"),
        ("internal_audit_cn", r"内部审计"),
        ("qa_receipt_cn", r"质检回执"),
        ("evidence_outline_cn", r"证据大纲"),
        ("repro_manifest_cn", r"复现清单"),
        ("content_freeze_cn", r"内容冻结"),
        ("gate_cn", r"阶段门禁|论文门禁|建模门禁|编程门禁"),
    ],
    "placeholder": [
        ("todo", r"(?<![A-Za-z])TODO(?![A-Za-z])"),
        ("fixme", r"(?<![A-Za-z])FIXME(?![A-Za-z])"),
        ("debug", r"(?<![A-Za-z])DEBUG(?![A-Za-z])"),
        ("tbd", r"(?<![A-Za-z])TBD(?![A-Za-z])"),
        ("pending_cn", r"\[(?:待补充|待完善|待核验|待替换)[^\]]*\]"),
    ],
    "markdown": [
        ("markdown_bold", r"\*\*[^*\n]{1,120}\*\*"),
        ("markdown_code", r"`[^`\n]{1,120}`"),
        ("markdown_heading", r"(?m)^\s{0,3}#{1,6}\s+\S+"),
    ],
}


def extract_docx(path: Path) -> str:
    chunks: list[str] = []
    with zipfile.ZipFile(path) as zf:
        names = [
            n for n in zf.namelist()
            if re.fullmatch(r"word/(?:document|header\d+|footer\d+|footnotes|endnotes)\.xml", n)
        ]
        for name in sorted(names):
            try:
                root = ET.fromstring(zf.read(name))
            except ET.ParseError:
                continue
            for paragraph in root.findall(".//w:p", NS):
                text = "".join(node.text or "" for node in paragraph.findall(".//w:t", NS))
                if text.strip():
                    chunks.append(text)
    return "\n".join(chunks)


def load_text(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        return extract_docx(path)
    return path.read_text(encoding="utf-8", errors="replace")


def scan(text: str, allow: list[str], categories: set[str]) -> list[dict]:
    allow_re = [re.compile(p, re.I | re.M) for p in allow]
    findings = []
    for category, specs in PATTERNS.items():
        if category not in categories:
            continue
        for rule, pattern in specs:
            rx = re.compile(pattern, re.I | re.M)
            for m in rx.finditer(text):
                snippet = text[max(0, m.start() - 60): min(len(text), m.end() + 60)].replace("\n", " ")
                if any(a.search(m.group(0)) or a.search(snippet) for a in allow_re):
                    continue
                findings.append({
                    "category": category,
                    "rule": rule,
                    "match": m.group(0),
                    "offset": m.start(),
                    "context": snippet,
                })
    return findings


def main() -> int:
    p = argparse.ArgumentParser(description="Scan DOCX/TXT/MD paper text for internal workflow residue.")
    p.add_argument("path")
    p.add_argument("--category", action="append", choices=("governance", "placeholder", "markdown", "all"))
    p.add_argument("--allow", action="append", default=[], help="Regex allow-list after explicit human verification.")
    p.add_argument("--strict", action="store_true", help="Return exit code 1 when any finding remains.")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    path = Path(args.path)
    if not path.exists():
        report = {"status": "error", "error": f"file not found: {path}"}
        print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else report["error"])
        return 2

    selected = set(args.category or ["all"])
    if "all" in selected:
        selected = set(PATTERNS)
    try:
        text = load_text(path)
        findings = scan(text, args.allow, selected)
    except Exception as exc:
        report = {"status": "error", "error": f"{type(exc).__name__}: {exc}"}
        print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else report["error"])
        return 2

    counts = {c: sum(1 for f in findings if f["category"] == c) for c in PATTERNS}
    report = {
        "status": "pass" if not findings else "findings",
        "path": str(path),
        "characters_scanned": len(text),
        "categories": sorted(selected),
        "counts": counts,
        "findings": findings,
        "note": "High-specificity mechanical scan only; review each finding in context.",
    }
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("PAPER_CONTENT_AUDIT_PASS" if not findings else "PAPER_CONTENT_AUDIT_FINDINGS")
        for f in findings:
            print(f"- {f['category']}/{f['rule']}: {f['match']!r} :: {f['context']}")
    return 1 if args.strict and findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
