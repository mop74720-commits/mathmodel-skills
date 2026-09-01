---
name: tool-latex
description: LaTeX 环境诊断、CJK 基线初始化、真实编译、资源哈希绑定和基础 PDF/日志验证。
---

# Tool: LaTeX

## Commands
```bash
python tools/latex/scripts/latex_paper.py doctor --engine xelatex
python tools/latex/scripts/latex_paper.py init-cjk paper/main.tex
python tools/latex/scripts/latex_paper.py build paper/main.tex --engine xelatex --publish paper/final.pdf
python tools/latex/scripts/latex_paper.py bind paper --output paper/latex-project.json
python tools/latex/scripts/latex_paper.py validate paper/main.tex --pdf paper/final.pdf
```

## Checks
- `build` 真实运行 TeX engine，不以源码存在代替编译。
- `validate` 暴露 PDF 缺失、LaTeX Error、未解析引用/引文。
- `bind` 对项目资源做 SHA-256 清单，用于最终结果追溯。
- 官方模板优先，`init-cjk` 只是无官方模板时的环境 smoke baseline。

## Handoff
编译/引用问题返回 writing；内容或数值问题不在本工具修正。
