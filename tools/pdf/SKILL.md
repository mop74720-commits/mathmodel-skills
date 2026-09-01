---
name: tool-pdf
description: 读取和审计题面/参考 PDF，保留页码、尺寸和结构证据；OCR 只作为最后手段。
---

# Tool: PDF

## Scope
机械读取 PDF，不替代题意判断。优先读取嵌入文本；公式、表格或扫描页解析不可靠时必须回到页面图像核对。

## Commands
```bash
python tools/pdf/scripts/inspect_pdf.py problem.pdf --json
python tools/pdf/scripts/extract_text.py problem.pdf --pages 1-3 --output problem.txt
```

`inspect_pdf.py` 输出 SHA-256、页数、页尺寸、文本量、图片/链接/批注数量。`extract_text.py` 保留页码标记，不做 OCR。

## Checks
- 原 PDF 只读。
- 文本为空不等于页面为空；可能是扫描件。
- 数学公式、图形和复杂表格以页面视觉证据为准。

## Handoff
返回页面定位、抽取文本路径、结构警告；语义歧义交给 `PROBLEM_AMBIGUOUS`。
