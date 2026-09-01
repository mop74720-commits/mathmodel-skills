# mathmodel-skills

## v0.1.12：局部路线反驳与 flip/fallback

保持 50-event 边界，不增加 contest-route-selection Skill。强化 `model-selection / model-challenge / model-comparison`：复杂度必须有 baseline 缺陷与 deciding evidence 支撑；增加 strongest objection、rejected alternative、refutation test、flip condition 和 fallback trigger/action。全局选题仍由 Coach + Selection Workspace 处理。

数学建模竞赛的第二层 Skill Hub。它不决定比赛时间线、模型冻结时点或团队优先级；这些属于 `mathmodel-pro` Coach。它负责在收到明确局部任务或事件后，路由到最小必要的 Role / Skill / Tool / QA，并把结构化结果交还给真实 Competition Repo。

## v0.1.12：50 个事件驱动 Skill + 18 算法族 + 7 个质量择优 Tool

v0.1.12 以 v0.1.10 的集成审计修复为基线，选择性吸收一条 ScholarSkill 定向增强分支中的高价值科研质量协议：数据合同/泄漏审计、决策性实验合同、不确定性预算、写作前 citation planning 与 provenance bundle。保留 v0.1.10 的 50-event 边界、动态 validator、replay reproducibility 和百万行 XLSX streaming；不恢复越权 `competition-strategy`。

设计原则：

- 不引入固定 01→12 阶段链；仍由事件路由。
- 不使用页数、图数、统一百分比扰动等伪硬指标。
- Skill 不拥有比赛阶段/时间/提交决策权，仍归 Coach。
- QA 返回证据化 PASS/WARN/FAIL/NOT_INDEPENDENTLY_VERIFIED，不用主观总分代替问题。
- 论文/结果关键数字优先绑定 Final Run 与 Claim-Evidence Map。






## v0.1.12 Targeted Research-Quality Integration

- `data-audit`：增加 row-unit/data contract、missingness pattern、六类 leakage 与 split integrity。
- `experiment-manager`：增加 `EXPLORATORY / CONFIRMATORY` 与 decision-bearing Experiment Contract。
- `robustness`：增加 uncertainty budget，分离数据/参数/结构/场景/算法/数值不确定性。
- `claim-evidence`：增加写作前 citation purpose planning，继续区分外部文献与本地运行证据。
- `reproducibility`：在 v0.1.10 的 manifest/verify/replay 语义上新增 provenance bundle；hash 仍只证明工件身份，不等同科学正确性。
- 保留 `references/scholarskill-selection-2026-08-31.*` 作为吸收裁决记录；不安装大规模外部 registry，不新增 Router event。

## v0.1.10 Rehearsal Integration Patch（保留）

- 移除越权的 first-class `competition-strategy`；全局竞赛策略归 Coach，官方规则提取仍由 `competition-rules` 负责。
- `validate_hub.py` 不再硬编码 Skill 数量，而是校验 Skill 文件、trigger、registry path、registry version 的双向一致性。
- Reproducibility 明确拆分 `artifact_integrity` 与 `replay_reproducibility`，并修复 `--cwd` 下相对输入/产物路径解析。
- CSV/JSON 可选 semantic fingerprint，允许小数舍入后的语义重放检查，与字节级 exact hash 分开报告。
- XLSX 新增 large-file read-only streaming/summary 模式，用于百万行级附件，不把工作簿编辑逻辑强加给只读审计。
- 根 SKILL / VERSION / registry / README 版本统一。

## v0.1.7 Deep Upstream Selection

- 新增 `OFFICIAL_RULES_NEEDED -> problem/competition-rules`，把官方规则、官方建议、用户要求和内部质量目标分开，生成 `mathmodel-competition-rules/v1`。
- `references/model-composition-patterns.md` 把常见组合模式从“题型→算法捷径”改成“结构信号→候选组合→必需证据→失效条件”。
- MATLAB 升级为一等实现后端：新增 `matlab-implementation.md`、`check_matlab_env.m`，复现 manifest v2 支持 `--runtime matlab` 与工具箱版本。
- Figure 新增三份深度 guide：选图与证据、视觉编码与布局、误导与最终尺寸 review；仍不规定固定图数。
- 上游覆盖矩阵中 XiaoMa 的“常见模式”“MATLAB规范”“论文格式规范”从 PARTIAL 提升为 FULL/TRANSFORMED；Figure 深度知识从方法论覆盖升级为显式按需参考。
- 当前 XiaoMa 35 个审计项为 `22 FULL + 10 TRANSFORMED + 1 PARTIAL + 2 EXCLUDED`；唯一 PARTIAL 是“章节模板”，因 Hub 有意保持 claim-evidence 驱动结构，不固定通用章节顺序。

## v0.1.6 Same-capability Quality Selection（v0.1.7 保留）

这次不是“上游有什么新东西就补什么”，而是对**重叠能力**逐项裁决。完整矩阵见 `references/overlap-quality-selection.md`。核心结果：

- Han 的题意分析、假设、模型选择、实验、Reviewer/Verify 等重叠项：当前 Hub 的事件合同、失败分流和证据门禁整体更好，继续以 Hub 为主，只抽取少量删除/替换/解释类启发式。
- XiaoMa 的三角色细则：其建模前置检查、数值稳健性、复现、自审和英文写作深度更好；v0.1.7 保留 Hub 的角色外壳，新增按需深度参考。
- 算法：Hub 的 18 个原子 Skill 继续负责“何时用/何时不用/怎么验”；深度算法知识只作为 reference/playbook，不把大百科变成第二个 Router。
- Figure/LaTeX：上游能力目标明显胜出，v0.1.7 独立重实现更完整 QA。
- XLSX/Paper Search：双方各有优势，采用融合。
- DOCX/PDF：上游能力更广，但相关目录存在限制性许可；本包只做独立只读 QA 实现，不复制或派生其代码。

## v0.1.5 Selective Upstream Refresh

本轮不是“同步整个原仓库”，而是按 Hub 边界选择可复用能力并独立重写：

- `ENGLISH_PAPER_NEEDED` → `writing/english-paper`：MCM/ICM 技术英文化、术语/数字/公式/引用一致性。
- `references/solver-robustness.md`：稳定计算、尺度/条件、solver 匹配、多起点、收敛、资源降级与跨环境复现。
- 4 个算法 playbook：模糊综合评价、A*/TSP/Chinese Postman、分类 baseline、随机启发式规范。
- `tools/reproducibility`：feature-scoped dependency doctor + run manifest create/verify。
- Figure：增加 plotting-source 静态 QA 与灰度/对比度 raster QA。
- LaTeX：build 自动生成 provenance JSON，并把 fatal 与排版 warning 分开。
- Paper Review：增加“摘要→子问题结论→关键表图→方法回溯”的快速评阅可定位性检查。

明确不纳入：Han 的 12 阶段/Legacy 重复入口、主观 paper-score/project-manager；XiaoMa 的固定图数/篇幅目标、平台专用 DSH 封装、任何许可证不明确的上游脚本直接复制。

## v0.1.3 新增缺口补齐

- `DOMAIN_CONTEXT_NEEDED` → `domain-context`：9 类常见领域机制/陷阱/评价口径。
- `MODEL_NEEDS_CHALLENGE` → `model-challenge`：简化、替换、去掉、解释测试。
- `WRITING_STYLE_WEAK` → `technical-style`：技术表达去模板化，但不以“规避 AI 检测”为目标。
- 新增 6 个算法族：灰色预测、DEA/效率、排队、系统动力学、元胞自动机、博弈论。
- 新增 `references/upstream-coverage-matrix.md` 和 CSV，对两个上游共 72 个重要条目逐项映射。


## Tool Layer（v0.1.7 质量择优增强）

- PDF：结构/SHA/page/font/text/image/vector/bounds 审计、带页码文本抽取、页面真实渲染；只读且不默认 OCR。
- XLSX：工作表/行列/表头/公式/错误/合并区域审计、受限读取、百万行级只读 streaming，以及显式 LibreOffice 重算到新文件；不宣称等价于全部 Excel 专有函数。
- Figure：CSV/TSV/XLSX 丰富数据剖析、multi-path raster/SVG/PDF 机械审计、matplotlib 导出、源码静态 QA 与灰度/对比度 QA。
- DOCX：OOXML/OMML、样式、关系、修订、批注、fields/hyperlinks、媒体和残留 LaTeX 审计；模板格式摘要和 LibreOffice→PNG 真实渲染 QA。
- LaTeX：`doctor / init / init-cjk / build / bind / validate`；含 bibliography、graphics/bib/ref 检查、PDF/font 审计、可选显式规则阈值和 build provenance。
- Paper Search：OpenAlex + Crossref 双源检索，DOI + 高阈值模糊题名去重、年份/引用过滤与透明相关性排序；关键主张仍需回真实论文。
- Reproducibility：按 feature 检查实际依赖；`verify` 只检查 artifact integrity，`replay` 才执行重放；支持 cwd 相对路径与可选 CSV/JSON semantic fingerprint。

工具执行入口见 `tools/README.md`；逐工具实现/边界见 `references/tool-implementation-matrix.md`。

## 定位

```text
mathmodel-pro (Coach)
        |
        |  event + priority + project context
        v
mathmodel-skills (Skill Hub)
        |
        |  role / skill / tool / review
        v
Competition Repo
```

设计来源：

- `XiaoMaColtAI/math-modeling-skill`：吸收角色分工、渐进式加载、SKILL_ROOT/PROJECT_ROOT 分离、独立 reviewer/QA、工具分类等设计思想。
- `han69611/math-modeling-skills`：吸收假设设计、模型选择、实验管理、结果分析、创新、领域知识、模型自挑战、Reviewer、Verify 等细粒度能力思想。

本项目继续采用独立重写而非整仓复制。XiaoMa 当前根目录未见明确 LICENSE；Han 的 README 声明 MIT，但仓库元数据未识别出 license。具体来源与处理见 `UPSTREAM_NOTICE.md`。

## 最重要的边界

1. Coach 决定“现在做什么”；Skill Hub 决定“这个局部问题怎么做”。
2. Skill Hub 不读取比赛小时数来擅自阻断工作。
3. QA 返回 `PASS / WARN / FAIL / NOT_INDEPENDENTLY_VERIFIED`，不越权宣布整个比赛 `BLOCKED`。
4. 不要求固定图数、固定页数、固定模型数；只要求证据覆盖与题目/官方规则一致。
5. 一个事件优先调用一个 Skill；必要时再组合第二个，避免 12 阶段式全链路强制执行。

## 目录

```text
mathmodel-skills/
├── SKILL.md
├── registry.yaml
├── roles/
│   ├── modeling/
│   ├── coding/
│   └── writing/
├── skills/
│   ├── algorithm/
│   ├── domain/
│   ├── problem/
│   ├── modeling/
│   ├── coding/
│   ├── experiment/
│   ├── visualization/
│   ├── writing/
│   └── audit/
├── tools/
│   ├── pdf/
│   ├── xlsx/
│   ├── figure/
│   ├── docx/
│   ├── latex/
│   ├── paper-search/
│   └── reproducibility/
├── qa/
├── references/
├── scripts/
└── tests/
```

## 使用方式

Coach 推荐事件：

```text
MODEL_UNCERTAIN
```

Router 查 `registry.yaml`：

```text
MODEL_UNCERTAIN -> skills/modeling/model-selection
```

该 Skill 只完成模型选择，返回：候选、Baseline、适用条件、风险、验证方案和下一步 handoff。它不会自行推进“编程阶段”。

## 校验

```bash
python scripts/validate_hub.py
python scripts/validate_algorithm_routing.py
python scripts/validate_scenarios.py
python scripts/validate_upstream_coverage.py
python scripts/validate_tools.py
python scripts/validate_profiles.py
python tests/tool_smoke.py
```


## v0.1.10 Official submission closure（保留）

- `competition-rules` 统一落盘到 Competition Repo 的 `rules/OFFICIAL_RULES.md` + `RULE_PROFILE.json`。
- `final-review` 在规则未核验时硬阻止 submission-ready 结论，但不阻塞前期科学工作。
- AI 披露增加真实性约束：缺模型版本/关键交互等历史证据时明确 BLOCKED，不允许补造。
- 正式支撑材料与论文附录源程序一致性进入 final-review。