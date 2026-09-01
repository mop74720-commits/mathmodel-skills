---
name: tool-docx
description: DOCX 结构、样式、关系、OMML、修订/批注和真实渲染 QA；强调只读机械审计，不复制受限上游编辑代码。
---

# Tool: DOCX

## Commands
```bash
python tools/docx/scripts/docx_audit.py paper.docx --json
python tools/docx/scripts/inspect_template_format.py official-template.docx --json
python tools/docx/scripts/render_docx.py paper.docx --output-dir _docx_render --emit-pdf
python tools/docx/scripts/self_check.py paper.docx --render --output-dir _docx_render
```

## Checks
- 段落、表格、标题、drawing/media、样式使用；
- OMML 公式、残留字面 LaTeX；
- tracked changes、comments、fields、hyperlinks；
- internal relationship 是否断裂；
- 页面尺寸/页边距与模板样式摘要；
- LibreOffice headless 真实渲染后逐页 PNG 视觉 QA。

## Boundary
XiaoMa 在 DOCX 工具深度上胜过早期 Hub，但其相关工具目录包含限制性许可。v0.1.6 **没有复制、改写或分发其源码/模板**，而是独立实现只读 QA 与格式检查。复杂批注编辑、tracked-change 接受、LaTeX→OMML 全功能转换不在本 Hub 内伪造；需要时由专门文档能力处理。

机械 PASS 不等于论文内容 PASS。
