# MATLAB implementation profile

MATLAB is a first-class implementation backend when it matches the team environment or model. Apply the same scientific contract as Python: real execution, explicit dependencies, deterministic paths, reproducibility, solver-status checks and publication-quality output.

## Environment

Check only the capabilities actually used. Typical dependencies:

- base MATLAB: tables/matrices, graph basics, plotting, ODE solvers;
- Optimization Toolbox: `linprog`, `intlinprog`, `fmincon`, etc.;
- Statistics and Machine Learning Toolbox: regression/classification/clustering/statistics;
- Econometrics Toolbox: specialized econometric/time-series routines;
- Symbolic Math Toolbox: symbolic derivation when genuinely needed.

Missing an unrelated toolbox is not a project failure.

Use `roles/coding/scripts/check_matlab_env.m` to produce a machine-readable environment report.

## Project-safe code structure

Prefer a callable main function or batch-safe script. Use `fullfile` and a project root derived from the file location; do not depend on the interactive current directory.

```matlab
function main(seed)
arguments
    seed (1,1) double = 42
end
rng(seed, "twister");
root = fileparts(mfilename("fullpath"));
data = readtable(fullfile(root, "data", "input.csv"));
result = solveModel(data);
writetable(result.summary, fullfile(root, "results", "summary.csv"));
end
```

Use `readtable/writetable` for heterogeneous tabular data and `readmatrix/writematrix` for homogeneous numeric matrices. Validate dimensions explicitly before implicit expansion or matrix multiplication.

## Numerical requirements

- optimization: inspect `exitflag`, output structure, objective value and original constraint residuals;
- nonlinear/nonconvex: use multi-start or multiple seeds where appropriate and record budget;
- ODE: choose solver according to stiffness evidence, compare tolerances/step behavior and check invariants/residuals;
- PDE/discretization: perform mesh/time-step convergence rather than trusting default solver settings;
- ill-scaled models: scale or nondimensionalize before solver tuning;
- stochastic algorithms: `rng(seed,"twister")`, plus seed robustness when the conclusion depends on randomness.

A successful MATLAB return does not by itself establish mathematical correctness.

## Reproducibility

Record:

- `version` / release;
- only actually used toolbox names and versions;
- seed;
- input/output hashes;
- parameters and solver options;
- one replay command, typically `matlab -batch "main(42)"`.

`tools/reproducibility/run_manifest.py create` supports `--runtime matlab`, `--runtime-version`, and repeated `--dependency name=version` fields.

## Figure parity

MATLAB output is not a “lower quality” branch. Use the same Figure Contract and final-size/gray/color-blind checks as Python. Avoid universal style dogma (`grid off`, fixed DPI, mandatory zero baseline): those are chart- and rule-dependent. Export vector graphics when appropriate plus a raster preview for QA, and let verified competition/template rules override defaults.
