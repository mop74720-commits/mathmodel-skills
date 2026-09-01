# Figure pitfalls and review attacks

Use this as a reviewer attack list, not as a universal style checklist.

## Statistical deception risks

- mean-only bars conceal spread, outliers or multimodality;
- smoothing/KDE implies structure unsupported by sample size;
- error bars are undefined or switch definitions between figures;
- paired/repeated data are plotted as independent groups;
- post-selection of “best run” hides stochastic instability;
- regression line shown without checking functional form/residuals;
- heatmap color limits chosen after seeing the desired pattern.

## Visual deception risks

- truncated bar baseline exaggerates differences;
- dual y-axes create an arbitrary apparent correlation;
- 3D perspective changes perceived magnitude;
- rainbow colormap introduces false boundaries;
- dense markers/labels imply precision but destroy readability;
- only color distinguishes critical series;
- cropped legend/labels appear only after export or Word/PDF embedding.

## Evidence-density risks

- several near-duplicate figures repeat the same claim;
- one overloaded figure attempts to answer multiple unrelated questions;
- decorative process diagrams are included without changing understanding;
- raw/process/result figure quotas drive output rather than the paper's evidence needs.

## Final-size review

Review the *embedded* or final PDF/DOCX rendering, not only the source PNG/SVG. Check:

- font/marker/line readability at actual page size;
- gray and color-vision distinction;
- axis units, scales and tick precision;
- legend/caption correspondence;
- no clipping/overlap;
- main claim visible in a reviewer scan of a few seconds;
- figure is referenced and interpreted in text.
