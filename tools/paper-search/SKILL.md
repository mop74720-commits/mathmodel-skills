---
name: tool-paper-search
description: 为模型、公式或主张搜索可追溯文献证据。
---

# Tool: paper-search

## Scope
为模型、公式或主张搜索可追溯文献证据。

## Inputs
明确的 claim/模型族/关键词

## Outputs
题名、作者、年份、DOI/出版页、适用条件

## Rules
- Tool 负责载体与机械处理，不替代 modeling / coding / writing 的科学判断。
- 所有项目产物写入 `PROJECT_ROOT`。
- 已有官方模板、题面或权威数据时优先使用，不自行改写事实。

## Checks
不把搜索摘要当原文；关键方法回到 DOI/出版机构页面核验。

## Handoff
把产物路径、警告和未验证项返回调用它的专项 Skill。
