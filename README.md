# mathmodel-skills

数学建模竞赛的第二层 Skill Hub。它不决定比赛时间线、模型冻结时点或团队优先级；这些属于 `mathmodel-pro` Coach。它负责在收到明确局部任务或事件后，路由到最小必要的 Role / Skill / Tool / QA，并把结构化结果交还给真实 Competition Repo。

## v0.1.5：49 个事件驱动 Skill + 18 算法族 + 7 个可执行 Tool

v0.1.5 在 v0.1.4 的事件驱动架构上做选择性上游补强：新增 MCM/ICM 英文化 Skill；增加求解稳健性与算法 playbook；新增可复现运行 Tool；增强 Figure 源码/灰度 QA 与 LaTeX build provenance。仍不恢复固定阶段链、固定图数/页数或主观评分。

设计原则：

- 不引入固定 01→12 阶段链；仍由事件路由。
- 不使用页数、图数、统一百分比扰动等伪硬指标。
- Skill 不拥有比赛阶段/时间/提交决策权，仍归 Coach。
- QA 返回证据化 PASS/WARN/FAIL/NOT_INDEPENDENTLY_VERIFIED，不用主观总分代替问题。
- 论文/结果关键数字优先绑定 Final Run 与 Claim-Evidence Map。


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


## v0.1.4 Tool Layer（v0.1.5 继续增强）

- PDF：结构审计、SHA-256、页尺寸/文本/图片统计、带页码嵌入文本抽取；不默认 OCR。
- XLSX：工作表/行列/表头/公式/错误单元格/合并区域审计，以及受限行读取；不伪造 Excel 公式重算。
- Figure：CSV/TSV 数据剖析、raster/SVG/PDF 图文件机械审计、matplotlib 多格式导出 helper；v0.1.5 增加绘图源码静态 QA 与灰度/对比度 QA。
- DOCX：OOXML/OMML、修订、批注、媒体和残留 LaTeX 标记审计；LibreOffice→PDF→PNG 真实渲染 QA。
- LaTeX：`doctor / init-cjk / build / bind / validate`；v0.1.5 增加 build provenance JSON 与 fatal/warning 分层，已用 XeLaTeX 真实 smoke。
- Paper Search：OpenAlex + Crossref 双源检索与 DOI/题名去重；关键主张仍需回到 DOI/出版机构原页面。
- Reproducibility：按 feature 检查实际依赖，创建/验证 run manifest，绑定命令、seed、版本和指定输入/产物哈希。

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
python tests/tool_smoke.py
```
