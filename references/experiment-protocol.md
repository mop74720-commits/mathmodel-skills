# Decision-Bearing Experiment Protocol

This is a contest-scale protocol, not a laboratory preregistration system. Use it before runs whose outcome can change model choice, headline results, or final claims.

## Minimal experiment contract

Before running, record:

1. `question`: what decision this experiment will resolve;
2. `hypothesis_or_expectation`: optional directional expectation, never retrofitted as fact;
3. `baseline`: the comparison needed to interpret improvement;
4. `variant`: exactly what changes and what stays frozen;
5. `data_split_or_scenario`: dataset/version/split/scenario identity;
6. `metrics`: primary metric plus any safety/feasibility metric;
7. `replication`: seeds/folds/repeats if stochastic;
8. `stopping_rule`: iteration/time/convergence/feasibility criterion known before reading the final result;
9. `failure_definition`: what outcome invalidates the candidate;
10. `outputs`: files/fields/figures that will bind to the `run_id`.

## Fair comparison rules

- Same task definition, data version and evaluation subset unless the experiment is explicitly about changing them.
- Tune competing models under comparable information/resource budgets when claiming superiority.
- Never compare a tuned final model against an intentionally weak or untuned baseline and call the difference an algorithmic gain.
- Separate model-selection data from final holdout evidence where the available sample permits.
- If repeated tries influenced the chosen configuration, record that selection path; do not present the last successful run as if it were prespecified.

## Adaptive exploration

Contest work is adaptive. Exploration is allowed, but preserve the distinction:

- `EXPLORATORY`: used to learn/debug/select;
- `CONFIRMATORY`: rerun after the decision contract is frozen to support a final claim.

A final paper may report exploratory insights, but strong performance claims should preferably bind to a confirmatory run or an explicitly honest validation procedure.

## Stop condition

Stop experimentation when the experiment question is resolved with enough evidence for the competition decision. More runs are not automatically better; Coach decides whether additional evidence is worth the time.
