# Data Quality & Leakage Protocol

Use this reference from `problem/data-audit` when data will feed prediction, evaluation, optimization, statistical inference, or simulation calibration.

## 1. Data contract

Record for each modeling table/file:

- row unit (what one row physically represents);
- primary/entity key, group key, time key and spatial key;
- target/output fields;
- features/inputs and their units;
- observation window and prediction/decision horizon;
- derivation lineage for engineered fields;
- allowed join keys and cardinality assumptions.

A table with unknown row semantics is not ready for modeling even if every column has a numeric dtype.

## 2. Missingness

For important fields report both rate and pattern. Distinguish at least:

- structurally not applicable;
- missing because of collection/process rules;
- apparently random/unknown mechanism;
- missingness correlated with target/group/time.

Do not automatically impute before examining whether the missingness itself carries process information. Any imputation must be fitted only on the training/calibration partition when a split exists.

## 3. Leakage taxonomy

Check explicitly for:

- **target leakage**: target or post-outcome proxy used as input;
- **temporal leakage**: future information available in training features or preprocessing;
- **group/identity leakage**: repeated entity appears across train/test when generalization is supposed to be to new entities;
- **preprocessing leakage**: scaling, imputation, feature selection, dimensionality reduction or encoding fitted using held-out data;
- **join leakage**: downstream labels/results reintroduced through merges;
- **manual leakage**: features hand-created using knowledge of held-out outcomes.

For each suspected variable record `ALLOW / EXCLUDE / REVIEW` and the reason.

## 4. Split integrity

Choose split logic from the intended generalization claim, not convenience:

- IID rows → random/stratified split may be appropriate;
- time forecast → chronological/rolling split;
- repeated entities → group-aware split;
- spatial transfer → spatial/region holdout when that is the claim;
- small samples → repeated CV/bootstrap only when dependence assumptions permit.

The paper must describe the split that matches the actual code.

## 5. Units, ranges and impossible states

Record unit transformations explicitly. Flag:

- mixed units in one field;
- impossible physical states;
- silent percentage/fraction conversion;
- duplicated records with conflicting values;
- categories differing only by spelling/whitespace;
- outliers caused by parsing or unit errors.

Do not delete a scientifically plausible extreme value just because a generic z-score marks it as an outlier.

## 6. Data readiness decision

A dataset is ready when critical fields have known semantics/units, leakage risks are dispositioned, split logic is defined where relevant, and every destructive cleaning transformation is reproducible. Otherwise return the unresolved risk to the owning Skill/Coach.
