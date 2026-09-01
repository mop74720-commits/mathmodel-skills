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
python tools/figure/scripts/validate_source.py src/plot_q2.py --json
python tools/figure/scripts/visual_qa.py figures/q2_result.png --preview figures/_qa/q2_result_gray.png --json
```

Python 绘图代码可导入：
```python
from tools.figure.scripts.export_figure import export_figure
export_figure(fig, "figures/q2_result", formats=("svg","png"), dpi=300, grayscale_preview=True)
```

## Checks
- 统计标注必须来自数据计算。
- raster 检查尺寸/DPI；SVG 检查 viewBox；PDF 图建议单页。
- `check_figure.py` 只做文件级机械检查；`validate_source.py` 静态提示绘图源码中的可疑模式；`visual_qa.py` 生成灰度/对比度机械报告。
- `bbox_inches="tight"` 可能改变最终物理尺寸，因此只作为警告，不自动判错。
- 所有机械 QA 都不能替代实际尺寸下的视觉语义审查。

## Handoff
有格式/尺寸警告返回 `FIGURE_WEAK`；数据本身不足则返回 `CLAIM_UNSUPPORTED`。
