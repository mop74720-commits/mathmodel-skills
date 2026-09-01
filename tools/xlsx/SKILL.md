---
name: tool-xlsx
description: 工作簿结构/公式审计、受限范围读取和显式 LibreOffice 重算；融合 Hub 审计优势与上游重算能力。
---

# Tool: XLSX

```bash
python tools/xlsx/scripts/audit_workbook.py data.xlsx --json
python tools/xlsx/scripts/read_rows.py data.xlsx --sheet Sheet1 --min-row 1 --max-row 50
python tools/xlsx/scripts/recalc.py model.xlsx --output _recalc/model.xlsx
```

## Selection
早期 Hub 的 workbook/formula 审计比上游单纯读取更适合防错；上游的“真实重算”能力有价值。因此 v0.1.6 采用融合方案：保留审计和 bounded read，并独立增加显式重算。重算始终写新文件，不静默覆盖源文件。

## Boundary
LibreOffice 与 Excel 的函数兼容性并非完全等价；关键公式若依赖 Excel 专有功能，必须在目标环境复核。缓存值存在也不等于公式逻辑正确。
