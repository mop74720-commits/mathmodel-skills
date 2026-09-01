---
name: tool-figure
description: 数据剖析、出版图导出、文件/源码/视觉机械 QA；v0.1.7 结合深度选图/编码/review guide，机械工具仍不替代 figure-design 的科学判断。
---

# Tool: Figure

## Scope
负责“图是否被可靠生成、文件是否适合交付、数据诊断是否暴露风险”，不以固定图数为目标，也不替代 `figure-design` 对 claim、统计口径和图型的语义判断。

## Commands
```bash
python tools/figure/scripts/profile_data.py results.csv --group scenario --json
python tools/figure/scripts/check_figure.py "figures/*" --min-dpi 200 --json
python tools/figure/scripts/check_figure.py figures/ --strict --json
python tools/figure/scripts/validate_source.py src/plot_q2.py --json
python tools/figure/scripts/visual_qa.py figures/q2_result.png --preview figures/_qa/q2_gray.png --json
```

Python 导出：
```python
from tools.figure.scripts.export_figure import export_figure
export_figure(fig, "figures/q2_result", formats=("svg","png"), dpi=300, grayscale_preview=True)
```

## Quality contract
- 数据剖析报告缺失、异常值、偏度、相关性和分组统计；图型候选只作机械建议。
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
上游 XiaoMa 在 Figure 工具深度上胜过早期 Hub，因此 v0.1.6 按其能力边界独立补强；没有复制上游源码。
