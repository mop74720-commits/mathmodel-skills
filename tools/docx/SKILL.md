---
name: tool-docx
description: 把已冻结正文、公式、表图组织为 DOCX，并检查结构和渲染。
---

# Tool: docx

## Scope
把已冻结正文、公式、表图组织为 DOCX，并检查结构和渲染。

## Inputs
正文源、官方/项目模板、图表

## Outputs
DOCX 与校验报告

## Rules
- Tool 负责载体与机械处理，不替代 modeling / coding / writing 的科学判断。
- 所有项目产物写入 `PROJECT_ROOT`。
- 已有官方模板、题面或权威数据时优先使用，不自行改写事实。

## Checks
优先官方模板；公式可编辑；表图编号与引用一致；渲染后目检。

## Handoff
把产物路径、警告和未验证项返回调用它的专项 Skill。
