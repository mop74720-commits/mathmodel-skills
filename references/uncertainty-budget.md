# Uncertainty Budget & Propagation

Use from `experiment/robustness`, `experiment/sensitivity`, statistical inference, or numerical review when a conclusion depends on uncertain inputs or stochastic computation.

## Uncertainty inventory

For each important source record:

| Field | Meaning |
|---|---|
| source | measurement, sampling, parameter, model structure, scenario, algorithmic, numerical |
| quantity | affected variable/parameter/component |
| evidence |题面、数据重复、文献、估计标准误、solver tolerance 等 |
| representation | interval, distribution, scenario set, alternative model, seed set |
| range/rule | justified perturbation or sampling rule |
| propagation | analytic, bootstrap, Monte Carlo, scenario sweep, alternative specification |
| output effect | performance spread, interval, feasibility, rank/decision flip |
| action | accept, narrow claim, collect evidence, redesign, robustify |

## Important distinctions

- **Data/sampling uncertainty** is not the same as **parameter uncertainty**.
- **Model-form uncertainty** requires alternative plausible specifications; tiny parameter perturbations cannot establish it.
- **Algorithmic randomness** requires repeated seeds/runs.
- **Numerical uncertainty** requires tolerance/grid/step/solver checks and should not be disguised as real-world uncertainty.
- A deterministic scenario range is not automatically a probability distribution.

## Propagation choices

Use the cheapest defensible method:

- local smooth response → derivative/local sensitivity can diagnose influence;
- sample uncertainty → bootstrap/CV where dependence assumptions permit;
- several uncertain inputs → Monte Carlo/scenario design with justified joint sampling;
- structural uncertainty → alternative model/specification comparison;
- optimization decisions → report objective degradation, feasibility rate and decision/assignment changes;
- probabilistic predictions → check interval coverage/calibration when ground truth is available.

## Reporting

Do not reduce everything to one “robustness score.” Report which sources dominate, how much the headline quantity changes, whether the final decision changes, and the known failure region.
