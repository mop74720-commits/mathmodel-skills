---
name: tool-xlsx
description: XLSX 工作簿结构/公式审计、受限读取、百万行级只读流式读取和显式 LibreOffice 重算；编辑与大数据读取分开处理。
---

# Tool: XLSX — v0.1.11

普通工作簿：

```bash
python tools/xlsx/scripts/audit_workbook.py data.xlsx --json
python tools/xlsx/scripts/read_rows.py data.xlsx --sheet Sheet1 --min-row 1 --max-row 50
```

百万行级只读附件优先：

```bash
python tools/xlsx/scripts/stream_rows.py invoices.xlsx --sheet Sheet1 --max-rows 20
python tools/xlsx/scripts/stream_rows.py invoices.xlsx --sheet Sheet1 --json-summary --sample-rows 10
python tools/xlsx/scripts/stream_rows.py invoices.xlsx --sheet Sheet1 --output _extract/invoices.csv
```

需要真实公式重算时显式写新文件：

```bash
python tools/xlsx/scripts/recalc.py model.xlsx --output _recalc/model.xlsx
```

## Selection

- `audit_workbook.py`：需要样式/公式/合并区域等 workbook 结构时使用；
- `read_rows.py`：小范围事实核对；
- `stream_rows.py`：超大附件的只读扫描/采样/导出，不加载完整 cell/style 对象；
- `recalc.py`：只有确实需要公式重算时才调用。

不要因为附件是 XLSX 就先完整加载整个 workbook。先根据文件规模和任务选择最低成本模式。

## Boundary

LibreOffice 与 Excel 函数兼容性并非完全等价；关键公式若依赖 Excel 专有功能，必须在目标环境复核。流式读取只负责数据值，不承诺保留样式、图表、宏或所有日期格式语义。
