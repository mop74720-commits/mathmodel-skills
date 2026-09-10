# Han Algorithm-Depth Gap Audit — 2026-09-10

Source: `han69611/math-modeling-skills`, audited against current `mop74720-commits/mathmodel-skills` main.

This audit is about **depth**, not whether a method name appears somewhere. A capability is considered strong only when the Hub can answer: when to use it, when not to use it, what baseline to compare, how to validate it, and what evidence would make the route fail or flip.

## Decisions

### Promote to first-class algorithm families

1. `bayesian-modeling` → `ALGO_BAYESIAN_MODELING`
   - Rationale: prior/likelihood/posterior, hierarchical partial pooling and posterior predictive reasoning are not adequately represented by frequentist inference or generic supervised learning.
2. `signal-processing` → `ALGO_SIGNAL_PROCESSING`
   - Rationale: FFT/PSD/STFT/wavelet/filtering require sampling, aliasing, spectral leakage and edge-effect contracts that do not fit ordinary forecasting.
3. `agent-based-modeling` → `ALGO_AGENT_BASED_MODELING`
   - Rationale: heterogeneous autonomous agents and interaction topology are structurally different from cellular automata and aggregate system dynamics.

### Keep as depth playbooks, not Router events

- `robust-optimization.md`: robust counterpart, uncertainty sets, chance/scenario alternatives and price of robustness.
- `multi-objective-optimization.md`: weighted/epsilon/lexicographic routes, Pareto quality and NSGA-II evidence rules.
- `constraint-programming.md`: CP-SAT/global constraints for logical scheduling structures; remains under discrete optimization.
- `dynamic-programming.md`: state/recurrence/sufficient-state contract; not a separate top-level family.
- `evolutionary-game.md`: replicator dynamics / ESS as depth under game theory, optionally coupled to ODE/ABM.
- `mcdm-extensions.md`: VIKOR and GRA under multi-criteria evaluation.
- `advanced-forecasting.md`: Prophet, boosting forecasting and stacking under time-series/supervised learning.

## Explicit non-decisions

- Do **not** add XGBoost, LightGBM, Prophet, VIKOR, NSGA-II, GA, PSO or similar method-name Router events.
- Do **not** import Han's fixed contest workflow, subjective score systems or keyword-to-algorithm shortcuts.
- Do **not** treat upstream code snippets as trusted executable implementations; current Hub keeps independent contracts and validation rules.

## Coverage effect

Before this patch, Han's major ideas were already covered, but long-tail algorithm depth was uneven. The patch closes the largest structural gaps while preserving `minimal-primary-first` routing:

`problem structure -> one primary algorithm family -> optional depth playbook -> implementation -> independent validation`

Historical/upstream success remains a prior for candidate generation, never evidence that a method fits the current problem.
