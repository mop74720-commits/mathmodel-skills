---
name: tool-docx
description: 审计 DOCX 的结构、OMML 公式、修订/批注和媒体，并可真实渲染为页面 PNG 做视觉 QA。
---

# Tool: DOCX

## Scope
处理论文载体与机械质量，不修改科学结论。优先使用当届官方 Word 模板。

## Commands
```bash
python tools/docx/scripts/docx_audit.py paper.docx --json
python tools/docx/scripts/render_docx.py paper.docx --output-dir _docx_render --emit-pdf
```

## Checks
`docx_audit.py` 检查段落、表格、标题、媒体、OMML、修订、批注和残留 LaTeX 标记。`render_docx.py` 使用 LibreOffice headless 转 PDF 后逐页 rasterize；渲染图必须实际检查。

## Boundary
当前版本不重实现 XiaoMa 的整套评论编辑、tracked-change 接受、复杂 LaTeX→OMML 转换；这些在 coverage matrix 中继续明确标注。

## Handoff
结构警告返回 writing / `PAPER_NEEDS_ATTACK`；公式仍为字面 LaTeX 时必须修复后再交付。
