# Competition Rule Profile

A competition rule profile separates **official constraints** from internal quality targets and user preferences. It exists to prevent reusable modeling Skills from hard-coding rules that change by contest or year.

## Authority classes

- `OFFICIAL_HARD`: explicitly stated in the target contest's current official rules/template/instructions. Violation can make a submission invalid.
- `OFFICIAL_GUIDANCE`: official recommendation or convention, but not a hard rejection condition.
- `USER_REQUIREMENT`: explicit user/team requirement for this project.
- `LOCAL_TARGET`: internal quality target or heuristic. Never present it as an official requirement.
- `UNKNOWN`: not verified yet. Unknown rules must not be silently converted into defaults.

## Source hierarchy

Prefer, in order:

1. official contest website or current official rule PDF;
2. official template distributed for the same contest/year;
3. official organizer notice/FAQ;
4. only then secondary summaries, and mark them non-authoritative.

Record source URL/title, contest/year, retrieval date, and, when a local rule/template file is available, SHA-256. A rule profile is time-scoped: a 2025 rule is not automatically valid for 2026.

## Rule dimensions

Capture only dimensions that matter to the current deliverable:

- submission file types and naming;
- page/word limits and what pages count;
- anonymity/team identifiers;
- abstract/summary sheet requirements;
- allowed appendices/supporting materials/code;
- citation/reference expectations;
- AI/tool disclosure rules if any;
- template/font/margin/column requirements when explicitly mandated;
- language requirements;
- deadline/timezone and upload portal constraints;
- contest-specific declarations/forms.

## Hard-rule extraction protocol

For every candidate rule:

1. quote or paraphrase the smallest necessary official clause in the project note;
2. classify it as `OFFICIAL_HARD` or `OFFICIAL_GUIDANCE` only if the wording supports that strength;
3. store source locator (page/section/URL anchor when available);
4. express the rule in a mechanically checkable form where possible;
5. if two official documents conflict, mark `CONFLICT` and escalate rather than guessing.

## Example profile fragment

```yaml
contest: example
season: 2026
verified_at_utc: 2026-08-31T00:00:00Z
rules:
  - id: body_page_limit
    authority: OFFICIAL_HARD
    value: 30
    unit: pages
    scope: body
    source:
      title: Official formatting rules
      locator: section 3
  - id: target_figure_count
    authority: LOCAL_TARGET
    value: null
    note: figure count is claim-driven; no universal minimum
```

## Consumption by other Skills

- `final-review` may fail a submission on `OFFICIAL_HARD` violations.
- `tools/docx`, `tools/latex`, and `tools/pdf` may mechanically check profile values that have verified machine-readable fields.
- `writing/outline` and `figure-design` may use `OFFICIAL_GUIDANCE`, but should not treat it as a hard gate.
- `LOCAL_TARGET` is advisory and can be overridden by evidence or the Coach.

The rule profile does not decide competition strategy; Coach still owns time allocation, freeze and submit decisions.
