---
name: tool-latex
description: 管理 LaTeX 项目、真实编译、引用与 PDF 技术检查。
---

# Tool: latex

## Scope
管理 LaTeX 项目、真实编译、引用与 PDF 技术检查。

## Inputs
LaTeX 源、模板、资源

## Outputs
源码项目、PDF、编译日志

## Rules
- Tool 负责载体与机械处理，不替代 modeling / coding / writing 的科学判断。
- 所有项目产物写入 `PROJECT_ROOT`。
- 已有官方模板、题面或权威数据时优先使用，不自行改写事实。

## Checks
真实编译而不是只检查源码；官方模板优先；未解析引用/编译错误必须暴露。

## Handoff
把产物路径、警告和未验证项返回调用它的专项 Skill。
