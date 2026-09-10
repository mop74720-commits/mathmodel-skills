# ScholarSkill Capability Gap Audit — 2026-09-10

## Purpose

这是对 2026-08-31 定向筛选的第二轮补充。ScholarSkill 继续只作为**外部能力发现池**，不作为新的 Router、事实权威或大规模依赖。目标不是导入大量第三方 Skill，而是发现会显著减少数学建模错误、实验浪费、因果误判、证据错配或执行缺口的通用能力。

公开入口：`https://scholarskill.com/zh`。本轮仅依据公开可观察的任务分类与候选能力做 capability-level review，所有本地 Skill/Tool 均独立重写。

## Existing coverage confirmed before adding anything

截至本轮开始，仓库已经具备以下此前被认为是缺口的能力，因此不重复造轮子：

- `figure-design -> figure-render -> visualization-review`：科研图从设计到实际渲染再到 QA 已闭环；
- `literature-evidence`：把论文候选转为 Method Card，区分全文/摘要/元数据证据层级，并明确 transferable / non-transferable / failure modes；
- `bayesian-modeling`：先验—似然—后验、层级模型、采样诊断与 posterior predictive；
- `signal-processing`：FFT/PSD、时频/小波、滤波与采样风险；
- `agent-based-modeling`：异质 agent、环境/网络交互、校准、多 seed 与涌现验证。

因此本轮不新增 `paper-interpreter`、`figure-generator`、`Bayesian`、`signal` 或 `ABM` 的重复入口。

## Second-round decisions

| Observed capability/theme | Gap judgment | Decision | Local destination |
|---|---|---|---|
| structured paper interpretation / critical reading | 已由 Method Card 覆盖主要比赛需求 | TRANSFORMED / ALREADY COVERED | `problem/literature-evidence` |
| multi-source paper search + fallback | 当前只有 OpenAlex + Crossref，来源多样性不足 | DEEPEN | `tools/paper-search`: + Semantic Scholar + arXiv |
| epidemiology-style bias/confounding + causal DAG | 领域封装不应导入，但因果识别是通用建模缺口 | EXTRACT GENERIC CORE | new `ALGO_CAUSAL_INFERENCE` |
| study design / protocol orientation | experiment-manager 管追踪，不负责 DOE 设计 | ADD LOCAL SKILL | new `EXPERIMENT_DESIGN_NEEDED` |
| research-idea generation/ranking | 与现有 `innovation` / `model-challenge` 重叠 | NO NEW SKILL | retain existing modeling layer |
| broad research pipeline/orchestrator | 会与 Coach 形成第二套全局工作流 | EXCLUDE | Coach remains sole global authority |
| biomedical/software-package specific automation | 迁移性低，容易污染竞赛 Hub | EXCLUDE BY DEFAULT | only extract generic method if a real contest need appears |
| spatial/GIS-specific modeling | 有潜在价值，但本轮未完成足够深度审计 | DEFER | future capability audit |

## Why causal inference is a first-class algorithm family

普通统计推断主要问“差异/关联有多大、区间是什么”；因果推断先问“目标反事实效应是否可识别”。这会改变建模合同、变量角色和验证方式：

```text
causal question
  -> treatment / outcome / estimand
  -> DAG / assignment mechanism
  -> identification assumptions
  -> design-specific estimator
  -> balance / overlap / pre-trend / cutoff / first-stage diagnostics
  -> placebo / falsification / sensitivity
  -> causal wording or downgrade to association
```

因此 `causal-inference` 值得独立一级事件；但 DiD、RDD、IV、IPW、AIPW、synthetic control 等仍是族内方法，不继续膨胀 Router。

## Why experimental design is separate from experiment-manager

`experiment-manager` 解决 run identity、追踪和结果版本；`experimental-design` 解决信息结构：

- factors / levels / ranges；
- randomization / replication / blocking；
- factorial / screening / response-surface / sequential design；
- power/precision 与 simulation-based power；
- exploratory vs confirmatory freeze；
- stochastic simulation 的 seed / pairing。

这两者串联而不是合并：先设计“跑什么”，再管理“哪一次真的跑了”。

## Paper-search expansion boundary

新增 Semantic Scholar 与 arXiv 只提高 discovery coverage 和 fallback resilience。任何来源的搜索记录都不自动成为论文证据：

```text
paper-search metadata
  -> literature-evidence
  -> FULLTEXT_VERIFIED / ABSTRACT_ONLY / METADATA_ONLY
  -> Method Card
  -> model-selection candidate prior
  -> current-task probe / validation
```

搜索结果、引用量或热门度不能直接决定模型采用。

## Non-goals

- 不安装或镜像 ScholarSkill 的大规模 registry；
- 不复制第三方 Skill 正文或代码；
- 不把生物医学等领域流水线塞进通用数学建模 Router；
- 不新增第二个全局研究 orchestrator；
- 不把“热门/下载多”当能力质量证据；
- 不把外部论文/Skill 的历史结果当当前赛题 deciding evidence。

## Outcome

本轮新增两个真正独立的局部能力：`causal-inference` 与 `experimental-design`；补强一个已有 Tool：`paper-search`。其余候选优先映射到已有 Skill/reference，维持 `minimal-primary-first`，避免 registry 膨胀。
