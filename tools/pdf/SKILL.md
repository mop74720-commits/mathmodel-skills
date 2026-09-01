---
name: tool-pdf
description: 最终 PDF 的页面、字体、文本/图像、边界和真实渲染机械 QA；只读，不复制限制性上游表单/编辑代码。
---

# Tool: PDF

```bash
python tools/pdf/scripts/inspect_pdf.py paper.pdf --json
python tools/pdf/scripts/extract_text.py paper.pdf --output paper.txt
python tools/pdf/scripts/check_bounds.py paper.pdf --edge-mm 2
python tools/pdf/scripts/render_pages.py paper.pdf --output-dir _pdf_render --dpi 150
```

## Checks
- SHA-256、页数、页面尺寸/旋转、文本块、嵌入图像和矢量 drawing；
- 字体名称与混合页面尺寸提示；
- 页面边界/近裁切区域的机械检查；
- 真正 rasterize 页面后做视觉检查。

## Boundary
上游 XiaoMa 的 PDF 工具能力更广，但部分目录带限制性许可。v0.1.6 采用独立只读审计实现，不复制其源码，也不把表单写入/编辑能力塞进数学建模 Hub。最终视觉与科学语义仍需人工/Reviewer 审查。


## Competition rule profile

PDF 的页数、字体、边距、命名、摘要页等“硬约束”不得来自工具默认值。若存在 `mathmodel-competition-rules/v1`，只执行其中已核验的 `OFFICIAL_HARD` 机械检查；`LOCAL_TARGET` 只能作为建议，不能触发官方违规结论。
