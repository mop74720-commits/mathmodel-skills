# XiaoMa 1.3.0 Delta Review — 2026-09-10

上游：`XiaoMaColtAI/math-modeling-skill`  
历史逐项矩阵基线：`e5d9313420d519f18ed1429d52d95fe0a72ae944`（1.2.0）  
本次复核：`3527fad922660397834a6167fc2b4c29ee64ba17`（仓库 VERSION=1.3.0）

本文件只记录历史 matrix 之后的增量能力，不把 Star 图、DSH UI 或仓库运营改动算作数学建模能力。

## Delta decisions

| 1.3.0 / post-baseline capability | Decision | Local mapping | Rationale |
|---|---|---|---|
| Figure 的数据剖析→合同→绘制→QA 完整执行链 | TRANSFORMED | `figure-design` + `figure-render` + `tools/figure` | 补标准科研图实际渲染层；不复制上游源码，不继承固定图数 |
| `setup_style` / recipe / journal preset 思路 | PARTIAL-BY-DESIGN | `figure-render` + project-specific plotting scripts | 通用 Hub 只保留可迁移执行合同；期刊/竞赛尺寸由当前规则传入，不建立永久固定 style 真值 |
| 交付与截止时间协议：early end-to-end smoke | TRANSFORMED/COACH-OWNED | `mathmodel-pro` delivery-safety playbook | 属于时间、风险和全局调度，不新增 SkillHub 全局阶段 |
| Checkpoint V1/V2、内容冻结、最终导出、回滚 | TRANSFORMED/COACH-OWNED | `mathmodel-pro` delivery-safety playbook | 保留“始终有可提交版本”和可逆性；不恢复固定三阶段 |
| 论文内部流程术语残留检测 | TRANSFORMED | `tools/docx/scripts/paper_content_audit.py` + `final-review` | 采用高特异性规则，避免把“验证/复现/审计”等正常学术词误杀 |
| CUMCM/MCM 题型固定打法、固定图数/篇幅质量目标 | EXCLUDED | — | 可以作为经验提示，但不能成为跨竞赛硬规则 |
| DSH UI / Agent preset / mm_* tools | EXCLUDED | — | 平台专用封装，不属于通用 Skill Hub |
| Star history / README 展示更新 | EXCLUDED | — | 仓库运营元数据 |

## Figure closure

历史 Hub 的 Figure 能力主要是：

`Figure Contract → data/profile/export/source QA/visual QA`

本次补为：

`FIGURE_NEEDED → figure-design → FIGURE_RENDER_NEEDED → figure-render → FIGURE_WEAK → visualization-review`

`render_figure.py` 只承担可标准化的 line/scatter/bar/hist/box/heatmap/errorbar。复杂图必须在 Competition Repo 内建立专用绘图脚本，避免把通用 renderer 变成隐藏的“大而全画图框架”。

## Paper-content scan boundary

机械扫描只抓高特异性内部治理词、占位和明显 Markdown，例如：

- `Subagent`
- M1/P1/P2/W1/W2
- Run Ledger / QA receipt / Checkpoint V1/V2
- 内部审计 / 质检回执 / 证据大纲 / 复现清单 / 内容冻结
- TODO / FIXME / TBD / DEBUG / `[待补充]`
- 明显 Markdown bold/code/heading

不单独禁止“验证、复现、审计、质量检查”等正常论文表达。允许项只能经人工核对后使用精确 `--allow` 放行。

## Remaining gap after this delta

XiaoMa 仍比 Hub 更重视“现成 recipe/style preset”的工具便利性；Hub 当前选择把复杂/特殊图留给项目专用脚本，以避免样式和统计口径被隐藏默认值支配。若未来实际比赛显示标准 renderer 覆盖不足，应按真实失败案例补 recipe，而不是一次性复制整个上游工具面。
