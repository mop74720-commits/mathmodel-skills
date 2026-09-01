# Figure encoding and layout contract

## Visual channel priority

Use position and length for precise quantitative comparison before area, angle or color intensity. Color should rarely carry the only encoding for a critical distinction.

For groups, combine a limited number of channels (color + line style/marker) and verify grayscale/color-vision robustness. For continuous values, use perceptually ordered colormaps; for signed deviations, use a diverging scale centered on the meaningful neutral value.

## Axis rules are contextual

- A bar chart encodes magnitude by length, so a non-zero baseline can materially mislead and needs strong justification.
- A line/scatter plot can legitimately zoom a range when the purpose is variation, provided the axis is explicit and the presentation does not exaggerate the claim.
- Log scale is appropriate for multiplicative structure or several orders of magnitude, but zero/negative handling must be explicit.
- Never turn “y must start at zero” into a universal rule.

## Uncertainty

Every interval must name its meaning: SD, SE, quantile, bootstrap CI, model CI, prediction interval, etc. For stochastic optimization, a distribution over seeds/runs is often more informative than a single best trajectory.

## Layout

Allocate visual area by evidence importance, not mechanically equal subplot widths. A large main panel plus small diagnostics is often better than equal panels. Use aligned axes where comparison is intended; do not align incompatible quantities just for symmetry.

## Text and legend

Prefer direct labels when they reduce lookup burden. Legends should not obscure data. Captions carry definitions and experimental conditions; titles carry the reader-facing message only when the contest/paper style permits it.

## Export

Vector output is preferred for line art/text when the final workflow supports it; raster output should meet the verified template/contest requirement. DPI is an output parameter, not a scientific-quality score. Always review at the final physical size.
