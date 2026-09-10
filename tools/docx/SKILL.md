---
name: tool-docx
description: DOCX 结构、样式、关系、OMML、内部流程残留和真实渲染 QA；强调机械审计，不复制受限上游编辑代码。
---

# Tool: DOCX

## Commands

```bash
python tools/docx/scripts/docx_audit.py paper.docx --json
python tools/docx/scripts/paper_content_audit.py paper.docx --strict --json
python tools/docx/scripts/inspect_template_format.py official-template.docx --json
python tools/docx/scripts/render_docx.py paper.docx --output-dir _docx_render --emit-pdf
python tools/docx/scripts/self_check.py paper.docx --render --output-dir _docx_render
```

## Checks

- 段落、表格、标题、drawing/media、样式使用；
- OMML 公式、残留字面 LaTeX；
- tracked changes、comments、fields、hyperlinks；
- internal relationship 是否断裂；
- 页面尺寸/页边距与模板样式摘要；
- LibreOffice headless 真实渲染后逐页 PNG 视觉 QA；
- `paper_content_audit.py` 对正文可见文本做高特异性扫描：`Subagent`、M1/P1/P2/W1/W2、Run Ledger、QA receipt、Checkpoint V1/V2、内部审计/质检回执/证据大纲/复现清单/内容冻结，以及 TODO/FIXME/TBD/DEBUG、明显 Markdown 残留等。

`paper_content_audit.py` **不禁止**“验证、复现、审计”等正常学术词。确属正文的命中项必须人工核对后再用 `--allow` 正则显式放行；不能为了过门禁把整类规则关闭。

## Boundary

XiaoMa 在 DOCX 工具深度上胜过早期 Hub，但其相关工具目录包含限制性许可。当前 Hub **没有复制、改写或分发其源码/模板**，而是独立实现只读 QA、格式检查和高特异性内容残留扫描。复杂批注编辑、tracked-change 接受、LaTeX→OMML 全功能转换不在本 Hub 内伪造；需要时由专门文档能力处理。

机械 PASS 不等于论文内容 PASS，也不代表不存在语义上更隐蔽的内部治理表述；最终仍需实际读文。

## Competition rule profile

DOCX 的页数、字体、边距、命名、摘要页等“硬约束”不得来自工具默认值。若存在 `mathmodel-competition-rules/v1`，只执行其中已核验的 `OFFICIAL_HARD` 机械检查；`LOCAL_TARGET` 只能作为建议，不能触发官方违规结论。
