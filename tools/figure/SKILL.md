---
name: tool-figure
description: 数据剖析、标准科研图渲染、出版图导出、文件/源码/视觉机械 QA；机械工具不替代 figure-design 的科学判断。
---

# Tool: Figure

## Scope

负责“数据是否足以成图、标准图能否可靠渲染、图文件是否适合交付”。`figure-design` 决定 claim、统计口径和图型；`figure-render` 负责执行。本 Tool 不以固定图数为目标，也不把机械 PASS 当科学质量真值。

## Commands

```bash
python tools/figure/scripts/profile_data.py results.csv --group scenario --json

# 标准 Figure Contract -> 实际成图
python tools/figure/scripts/render_figure.py results.csv \
  --chart line --x time --y objective --group method \
  --output figures/q2_objective --formats svg png \
  --grayscale-preview --json

python tools/figure/scripts/check_figure.py "figures/*" --min-dpi 200 --json
python tools/figure/scripts/check_figure.py figures/ --strict --json
python tools/figure/scripts/validate_source.py src/plot_q2.py --json
python tools/figure/scripts/visual_qa.py figures/q2_result.png --preview figures/_qa/q2_gray.png --json
```

Python 项目脚本也可直接复用导出 helper：

```python
from tools.figure.scripts.export_figure import export_figure
export_figure(fig, "figures/q2_result", formats=("svg","png"), dpi=300, grayscale_preview=True)
```

## Standard renderer

`render_figure.py` 面向**已冻结 Figure Contract**，当前支持：

- `line`
- `scatter`
- `bar`
- `hist`
- `box`
- `heatmap`
- `errorbar`

它只执行显式指定的数据字段、过滤与聚合，不自行发明显著性、误差、拟合或坐标变换。多面板、空间/网络、Pareto、相图、3D 曲面等复杂图应写入 `PROJECT_ROOT` 的专用绘图脚本，再复用本 Tool 的导出与 QA。

## Quality contract

- 数据剖析报告缺失、异常值、偏度、相关性和分组统计；图型候选只作机械建议。
- 标准 renderer 的字段、聚合、log 轴、误差列等必须来自 Figure Contract。
- `check_figure.py` 支持文件、目录和 glob；检查 raster 像素/DPI、SVG viewBox/尺寸、PDF 单页性。
- `validate_source.py` 检查绘图源码中的可疑静态模式；`visual_qa.py` 检查灰度/对比度并生成预览。
- DPI、像素和尺寸阈值是可配置交付参数，不是科学质量真值；期刊/竞赛规则优先。
- 所有机械 PASS 都不能证明图表统计设计、结论或视觉表达正确，必须在最终物理尺寸下人工/语义复审。

## Deep references

语义选图与审稿按需读取：

- `references/figure-guides/selection-and-evidence.md`
- `references/figure-guides/encoding-and-layout.md`
- `references/figure-guides/pitfalls-and-review.md`

## Selection note

上游 XiaoMa 在 Figure 工具深度上胜过早期 Hub。当前 Hub 保留其“数据剖析→Figure Contract→执行成图→机械 QA→最终尺寸复审”的能力边界，但使用独立实现，不复制上游源码，也不继承固定图数要求。
