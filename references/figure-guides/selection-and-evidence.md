# Figure selection by evidence task

Choose a chart from the **claim + variable structure + sample support**, not from decoration preference.

## Evidence tasks

| Evidence task | Typical structure | Strong default | Common failure |
|---|---|---|---|
| distribution | one continuous variable | histogram/KDE; raw points when tiny n | smooth density with too little data |
| group comparison | categorical + continuous | raw points + interval/box/violin as justified | mean-only bars hiding spread |
| relationship | two continuous variables | scatter + fitted relation/CI when modelled | connecting unordered points |
| time/dose trend | ordered x + response | line/points + uncertainty | using lines for IDs/categories |
| composition | parts of a whole | sorted bars / stacked bars | 3D pies and angle-heavy encodings |
| correlation | several continuous variables | correlation matrix / selected pair plots | huge unreadable pairplot |
| matrix/pattern | 2D numeric matrix | heatmap with meaningful scale | rainbow/jet perceptual artifacts |
| prediction performance | classifier/regressor | residuals/calibration/ROC-PR as task demands | reporting only one aggregate metric |
| uncertainty | estimate + sampling/parameter uncertainty | interval/band/distribution | decorative error bars with undefined meaning |
| spatial/network | coordinates/graph | map/network only when topology is evidence | geographic-looking plot without coordinate meaning |

## Small-sample discipline

Do not derive universal n-thresholds mechanically. The principle is:

- when sample support is weak, expose raw observations;
- avoid distribution summaries whose quantiles/density are unstable;
- state n and the uncertainty definition;
- if repeated/paired observations exist, preserve pairing rather than pretending independence.

## Same data, different claim

The same dataset may need different charts. A treatment×time dataset can support:

- overall treatment difference → grouped distribution/interval;
- temporal evolution → treatment-specific time curves;
- individual response → paired/spaghetti plot for a controlled number of subjects;
- model fit → observed vs fitted/residual panels.

Therefore Figure Contract starts from the reader question, not from a fixed chart lookup.

## Split or combine panels?

Use one panel when one visual question can be answered without legend/encoding overload. Split when:

- scales are incompatible;
- more visual channels are needed than readers can reliably decode;
- a secondary diagnostic competes with the main result;
- dense lines/markers hide the key evidence.

Small multiples are preferable to forcing many unrelated series into one axis.
