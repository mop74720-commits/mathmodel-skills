# ScholarSkill Targeted Selection — 2026-08-31

## Purpose

ScholarSkill is treated as an external capability-discovery pool, not as a new router or authority layer. The site currently exposes a very large public research-skill catalog, so this review uses targeted screening rather than attempting to ingest the full registry.

Selection rule: a candidate is useful only if it adds a decision/check that reduces modeling error, experiment bias, unsupported claims, or reproducibility loss. Domain-specific automation and duplicate orchestration are excluded.

## Directly observed candidates

| Candidate | Useful idea | v0.1.9 decision | Destination |
|---|---|---|---|
| `literature-review` | distinguish narrative/scoping/systematic rigor; explicit screening and evidence synthesis | TRANSFORMED | writing/audit references; competition use defaults to lightweight evidence search unless rigor is required |
| `paper-citation-planner` | plan citation purpose before drafting from outline + source pack | ADOPTED-AS-METHOD | `citation-evidence-planning.md`, `claim-evidence` |
| `bio-orchestrator` | input-aware routing, multi-step handoff, reproducibility bundle | TRANSFORMED | keep current Coach/Hub authority; adopt provenance-bundle concept only |
| `grouped-statistics` | grouped summaries, missingness-aware multi-table analysis | TRANSFORMED | `data-audit` / XLSX reference, not a new Skill |
| `paper-search` | multi-source search and fallback | PARTIAL/DEFER | current OpenAlex+Crossref is simpler and keyless; only source diversity/fallback idea retained |
| `paper-interpreter` | structured critical reading, terminology map, method/result separation | DEFER | useful for research mode, not core contest router |
| `autoresearch` | experiment/protocol orientation in study-design collection | THEME-ONLY | strengthens experiment contract; no direct dependency |
| `protocolsio-integration` | protocol persistence/versioning | EXCLUDE-AS-TOOL | external service integration is unnecessary for contest Hub |
| `research-pipeline` / broad orchestrators | end-to-end research automation | EXCLUDE | duplicates Coach and would reintroduce a second global workflow |

## High-value capability themes retained

1. **Data quality before modeling** — schema, units, missingness mechanism, leakage class, split integrity, grouping/identity leakage, derivation lineage.
2. **Experiment protocol before decision-bearing runs** — question/hypothesis, baseline, metric, split, seeds, stopping rule, expected failure, run identity.
3. **Uncertainty budget** — source/type/evidence/range/propagation/decision effect, with explicit distinction among data, parameter, model, scenario, algorithmic, and numerical uncertainty.
4. **Citation planning before drafting** — claim purpose → evidence type → verified source → exact use; separate background/method justification from local numerical evidence.
5. **Provenance bundle** — manifest + command + hashes + runtime/dependencies + selected run-ledger/rule-profile pointers, without dumping secrets.

## Explicit non-goals

- Do not install thousands of ScholarSkill entries into `registry.yaml`.
- Do not add biomedical or software-package-specific pipelines without a concrete competition need.
- Do not replace Coach with a general research orchestrator.
- Do not import a skill solely because it is popular or highly starred.
- Do not copy third-party skill text/code into this repository without clear licensing and a real need; v0.1.9 independently defines the resulting contracts.

## Outcome

No new Router event is required. The selected ideas strengthen existing `data-audit`, `experiment-manager`, `robustness`, `claim-evidence`, and `reproducibility` components. This follows the v0.1.8 pruning policy: richer references, stable router surface.


## v0.1.12 integration disposition

This record originated on a same-day v0.1.9 enhancement branch. v0.1.12 applies the selected research-quality ideas on top of the audited v0.1.10 structure: the five reference protocols and provenance-bundle concept are retained, while the branch's first-class `competition-strategy` is not imported. The production Router therefore remains at 50 local events.
