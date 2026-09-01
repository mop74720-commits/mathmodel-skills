---
name: tool-figure
description: 把已定义的图表合同渲染成可用于论文的图，并做机械视觉检查。
---

# Tool: figure

## Scope
把已定义的图表合同渲染成可用于论文的图，并做机械视觉检查。

## Inputs
图表合同、数据

## Outputs
SVG/PNG/PDF 等图文件

## Rules
- Tool 负责载体与机械处理，不替代 modeling / coding / writing 的科学判断。
- 所有项目产物写入 `PROJECT_ROOT`。
- 已有官方模板、题面或权威数据时优先使用，不自行改写事实。

## Checks
不自行选择科学结论；统计标注必须由数据计算；实际尺寸可读。

## Handoff
把产物路径、警告和未验证项返回调用它的专项 Skill。
