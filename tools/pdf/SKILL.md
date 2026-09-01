---
name: tool-pdf
description: 读取/检查题面和参考 PDF，优先保持页码与布局证据。
---

# Tool: pdf

## Scope
读取/检查题面和参考 PDF，优先保持页码与布局证据。

## Inputs
PDF 文件

## Outputs
文本摘录、页码定位、必要页面截图/结构信息

## Rules
- Tool 负责载体与机械处理，不替代 modeling / coding / writing 的科学判断。
- 所有项目产物写入 `PROJECT_ROOT`。
- 已有官方模板、题面或权威数据时优先使用，不自行改写事实。

## Checks
不把 OCR 当首选；表格/公式解析不可靠时回到页面图像。

## Handoff
把产物路径、警告和未验证项返回调用它的专项 Skill。
