---
name: tool-latex
description: LaTeX 工程 doctor/init/build/bind/validate；检查引用、图资源、字体、页数和构建 provenance，赛事阈值均显式传入而非硬编码。
---

# Tool: LaTeX

## Commands
```bash
python tools/latex/scripts/latex_paper.py doctor --engine xelatex
python tools/latex/scripts/latex_paper.py init paper --contest generic
python tools/latex/scripts/latex_paper.py init-cjk scratch/main.tex
python tools/latex/scripts/latex_paper.py build paper/main.tex --engine xelatex --runs 2
python tools/latex/scripts/latex_paper.py bind paper --output paper/project-manifest.json
python tools/latex/scripts/latex_paper.py validate paper/main.tex --pdf paper/main.pdf
```

可选的页数/公式/图/表阈值只在用户或当届规则明确时传入：`--max-pages`、`--min-pages`、`--min-equations`、`--min-figures`、`--min-tables`。它们没有通用默认值。

## Checks
- engine / bibliography / Pandoc 等依赖按任务检查；
- 真正编译并记录 engine、版本、耗时、source/PDF SHA-256 与日志；
- 检查 `includegraphics`、bibliography 文件、局部 label/ref；
- PDF 页面/字体做机械审计；Overfull/Underfull 默认是 warning，不冒充编译失败；
- `bind` 对工程文件建立可验证哈希清单。

## Selection note
XiaoMa 的 LaTeX 工程能力明显胜过早期 Hub；v0.1.6 因此采用同等级能力目标重新独立实现，并保留 Hub 的“官方规则外置、无固定页数/图数”边界。
