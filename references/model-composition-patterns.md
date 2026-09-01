# Model Composition Patterns — diagnostic, not prescriptive

This reference captures recurring *structures* in mathematical-modeling problems. It is a hypothesis generator, not a decision tree that automatically chooses a model.

## Operating rule

For every pattern, separate four layers:

1. **Signature** — what structural clues are actually present in the problem/data.
2. **Candidate composition** — a reasonable chain of model families to test.
3. **Required evidence** — what must be checked before trusting the composition.
4. **Invalidation / fallback** — observations that make the pattern inappropriate.

Never convert a weak clue such as “small sample”, “many indicators”, or “large search space” into a mandatory algorithm choice.

## P1 Exact optimization → sensitivity / shadow analysis

**Signature:** explicit objective, algebraic constraints, discrete/resource-allocation decisions, tractable exact formulation.

**Candidate:** LP/MILP/MINLP baseline → perturb RHS/objective coefficients → report solution stability and active constraints.

**Required evidence:** feasibility, integrality, solver status, constraint residuals, optimality gap when available.

**Invalidate when:** the core uncertainty dominates the deterministic optimum, or the formulation is only a surrogate with large structural error.

## P2 Hard combinatorial optimization → exact small case + heuristic large case

**Signature:** TSP/VRP/scheduling/routing or another combinatorial problem whose exact formulation scales poorly.

**Candidate:** exact solver on reduced instances + one or more heuristics on target instances.

**Required evidence:** equal computational budget, multi-seed distribution, feasibility rate, small-instance optimality/near-optimality comparison, convergence history.

**Do not claim:** “global optimum” from a stochastic heuristic without proof/certificate.

## P3 Multi-objective optimization → Pareto set → decision rule

**Signature:** genuinely conflicting objectives that cannot be collapsed without a preference assumption.

**Candidate:** ε-constraint / weighted family / multi-objective solver → Pareto frontier → transparent compromise rule.

**Required evidence:** objective scaling, dominance check, frontier coverage, sensitivity to preference weights. If TOPSIS or another ranking method is used on the Pareto set, its weights become a new assumption and must be audited.

## P4 Forecast → temporal validation → decision

**Signature:** future values are inputs to a downstream decision.

**Candidate:** naive/seasonal baseline + appropriate forecasting family → rolling/expanding validation → propagate forecast uncertainty into the decision model.

**Required evidence:** chronological split, leakage audit, forecast error by horizon, uncertainty treatment.

**Invalidate when:** downstream decisions are insensitive to the forecast or a robust policy dominates forecast-then-optimize.

## P5 Decompose → model components → recombine

**Signature:** trend/seasonality/regimes/subpopulations have distinct mechanisms.

**Candidate:** decomposition or segmentation → component-specific models → recombination.

**Required evidence:** decomposition is identifiable, component models outperform a unified baseline, recombination conserves the relevant quantity.

**Risk:** decomposition can manufacture structure. Always compare against a direct baseline.

## P6 Weighting → multi-criteria evaluation → ranking robustness

**Signature:** alternatives are evaluated over several indicators and weights are substantively meaningful.

**Candidate:** objective/subjective/combined weights → TOPSIS/GRA/FCE/etc. → perturb weights and normalization.

**Required evidence:** indicator direction, normalization, weight provenance, rank stability, tie/near-tie behavior.

**Invalidate when:** the task is actually prediction or causal inference rather than preference aggregation.

## P7 Efficiency frontier → projection / improvement target

**Signature:** comparable DMUs with multiple inputs and outputs.

**Candidate:** DEA family → efficiency decomposition → slack/projection → scale-return interpretation.

**Required evidence:** DMU homogeneity, input/output orientation rationale, enough DMUs relative to dimensionality, sensitivity to outliers.

## P8 Simulation ↔ optimization under uncertainty

**Signature:** random scenarios or uncertain parameters materially alter feasibility/value.

**Candidate A:** scenario generation → optimize each/scenario set → summarize risk.

**Candidate B:** optimization proposes policy → simulation stress-tests policy.

**Required evidence:** sampling convergence, scenario representativeness, policy feasibility, risk measure definition, seed robustness.

## P9 Mechanistic dynamics → parameter estimation → intervention

**Signature:** conservation/transition/differential equations describe evolution and parameters must be inferred.

**Candidate:** ODE/PDE/state-space model → parameter estimation → identifiability check → scenario/intervention analysis.

**Required evidence:** units, initial/boundary conditions, numerical convergence, parameter confidence/profile, residual structure.

## P10 Classification / clustering → downstream model

**Signature:** heterogeneous regimes plausibly obey different relationships.

**Candidate:** supervised/unsupervised partition → group-specific model.

**Required evidence:** partition stability, out-of-sample improvement over a global model, enough data per subgroup, no leakage from target into grouping.

## P11 Network structure → path/flow → robustness

**Signature:** entities and interactions are naturally a graph and the question asks connectivity, routing, flow, matching or resilience.

**Candidate:** graph construction → path/flow/matching/routing model → perturb edges/capacities/demand.

**Required evidence:** graph construction is justified, connectivity assumptions are explicit, route/flow is feasible in the original domain.

## Selection protocol

When one of these patterns appears:

- use it to propose at most a few candidate *compositions*;
- route each component to the corresponding atomic algorithm Skill;
- keep a simple baseline;
- write the evidence required to distinguish candidates before running them;
- if evidence is insufficient, leave the pattern as `candidate`, not `selected`.

This reference deliberately avoids universal rules such as “small sample ⇒ GM(1,1)”, “large problem ⇒ genetic algorithm”, or “multi-index ⇒ AHP+TOPSIS”.
