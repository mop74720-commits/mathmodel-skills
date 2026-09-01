---
name: tool-figure
description: 数据剖析、图文件导出与机械成图审计；科学结论和图型选择仍由 figure-design 决定。
---

# Tool: Figure

## Scope
工具层处理数据剖析、文件输出和机械 QA，不以固定图数为目标，也不替代 `figure-design` 的 claim/统计口径判断。

## Commands
```bash
python tools/figure/scripts/profile_data.py results.csv --group scenario --json
python tools/figure/scripts/check_figure.py figures/ --json
```

Python 绘图代码可导入：
```python
from tools.figure.scripts.export_figure import export_figure
export_figure(fig, "figures/q2_result", formats=("svg","png"), dpi=300, grayscale_preview=True)
```

## Checks
- 统计标注必须来自数据计算。
- raster 检查尺寸/DPI；SVG 检查 viewBox；PDF 图建议单页。
- `check_figure.py` 只做机械检查，视觉语义仍需实际读图。

## Handoff
有格式/尺寸警告返回 `FIGURE_WEAK`；数据本身不足则返回 `CLAIM_UNSUPPORTED`。
