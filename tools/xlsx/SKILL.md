---
name: tool-xlsx
description: 对 Excel 工作簿做只读结构/公式审计和受限行读取，避免在建模前猜字段。
---

# Tool: XLSX

## Scope
只读检查 `.xlsx`：工作表、行列、表头、公式、错误单元格、合并区域、隐藏状态和冻结窗格。当前版本不假装在 Python 中计算 Excel 公式。

## Commands
```bash
python tools/xlsx/scripts/audit_workbook.py data.xlsx --json
python tools/xlsx/scripts/read_rows.py data.xlsx --sheet Sheet1 --max-row 30 --max-col 15
```

## Checks
- 原始附件不覆盖。
- 公式单元格与缓存值是不同概念；需要权威重算时交给实际 Excel/兼容计算引擎，不用旧缓存冒充新结果。
- 清洗动作属于 `data-audit`，本工具只给事实。

## Handoff
结构和字段事实交给 `DATA_UNKNOWN` / `data-audit`。
