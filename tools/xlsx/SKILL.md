---
name: tool-xlsx
description: 检查或处理 Excel/CSV 数据，保持字段、类型、单位和公式语义。
---

# Tool: xlsx

## Scope
检查或处理 Excel/CSV 数据，保持字段、类型、单位和公式语义。

## Inputs
xlsx/xls/csv

## Outputs
数据档案、清洗后副本或指定结果表

## Rules
- Tool 负责载体与机械处理，不替代 modeling / coding / writing 的科学判断。
- 所有项目产物写入 `PROJECT_ROOT`。
- 已有官方模板、题面或权威数据时优先使用，不自行改写事实。

## Checks
原始附件只读；先审计工作表、行列、缺失、异常、重复和单位。

## Handoff
把产物路径、警告和未验证项返回调用它的专项 Skill。
