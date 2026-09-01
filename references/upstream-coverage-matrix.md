# Upstream Coverage Matrix

本矩阵用于回答“两个上游到底吸收了什么”。状态不是版权/文件复制状态，而是**能力与方法论覆盖状态**。

基线：
- XiaoMa: `XiaoMaColtAI/math-modeling-skill` commit `e5d9313420d519f18ed1429d52d95fe0a72ae944`。
- Han: `han69611/math-modeling-skills` commit `b5b98aebcb25ff89a99ea1cbb52b31ccab5040ca`。
- 本仓库：`mathmodel-skills v0.1.3`。

状态定义：`FULL`=核心能力已落入可调用 Skill；`TRANSFORMED`=吸收但按 Coach/Hub 边界改造；`PARTIAL`=只吸收方法/接口，具体工具或细节仍缺；`EXCLUDED`=主动不吸收。

## 摘要

- **XiaoMaColtAI/math-modeling-skill@e5d9313**：TRANSFORMED 4，FULL 18，PARTIAL 11，EXCLUDED 2。
- **han69611/math-modeling-skills@b5b98ae**：TRANSFORMED 6，EXCLUDED 9，FULL 21，PARTIAL 1。

v0.1.3 新补：`domain-context`、`model-challenge`、`technical-style`、`grey-forecasting`、`efficiency-analysis`、`queueing`、`system-dynamics`、`cellular-automata`、`game-theory`。

## XiaoMaColtAI/math-modeling-skill@e5d9313

| Upstream item | Status | Our mapping | Decision | Notes |
|---|---|---|---|---|
| SKILL.md / 三阶段总路由 | TRANSFORMED | SKILL.md + registry.yaml | 吸收 | 改为事件驱动 Router；阶段/时间权交给 Coach |
| references/roles/建模手/SKILL.md | FULL | roles/modeling + problem/* + modeling/* | 吸收 | 保留题意/数据/候选/验证设计；取消硬 M1 阻断 |
| 建模手/references/前置合同.md | FULL | skills/modeling/model-contract | 吸收 | 以可执行 model contract 重构 |
| 建模手/references/工作流程.md | TRANSFORMED | problem/* + modeling/* | 吸收 | 拆为事件，不保留阶段顺序 |
| 建模手/references/常见模式.md | PARTIAL | model-selection + algorithm/* | 继续补 | 常见题型已覆盖，具体算法细节仍可继续深化 |
| 建模手/references/建模设计理论.md | FULL | model-selection + model-comparison + model-challenge | 吸收 | 补了 Baseline、失败模式、简化/替换/消融 |
| 建模手/references/质检清单.md | FULL | audit/model-review | 吸收 | 证据化 reviewer，不用阶段硬门禁 |
| references/roles/编程手/SKILL.md | FULL | roles/coding + coding/* + experiment/* | 吸收 | MVP/复现/数值检查被拆成专项能力 |
| 编程手/references/工作流程.md | TRANSFORMED | implementation + mvp-check + result-review | 吸收 | 先 MVP 再扩展保留；是否扩展由 Coach 可覆盖 |
| 编程手/references/MATLAB规范.md | PARTIAL | roles/coding + tools contracts | 按需补 | 语言特定细节未完整复制 |
| 编程手/references/质检清单.md | FULL | audit/mvp-check + result-review + numerical-check | 吸收 | 强调复现、约束、单位、Final Run |
| references/roles/论文手/SKILL.md | FULL | roles/writing + writing/* + audit/* | 吸收 | 证据先行、真实结果、规则优先保留 |
| 论文手/references/写作规范.md | FULL | writing/technical-style + abstract + result-writing | 吸收 | 去模板化但不做“检测器规避” |
| 论文手/references/章节模板.md | PARTIAL | writing/outline | 保留思想 | 不固定章节模板，按问题与证据链组织 |
| 论文手/references/自审框架.md | FULL | audit/paper-review + final-review | 吸收 | 数学/证据/可读性/过度宣称检查 |
| 论文手/references/英文化工作流.md | PARTIAL | roles/writing | 未来可补 | MCM/ICM 英文化尚无独立 Skill |
| 论文手/references/论文格式规范.md | PARTIAL | tools/docx + tools/latex + final-review | 接口吸收 | 具体格式脚本未完整实现 |
| references/Subagent调度.md | TRANSFORMED | qa/protocol.md + reviewer-contract.md | 吸收 | 独立 reviewer 思想保留；无 Subagent 不再全局 BLOCKED |
| references/算法索引.md | FULL | references/algorithm-index.md + algorithm-dispatch.md | 吸收 | 渐进加载与按问题族路由保留 |
| assets/01-优化算法说明.md | FULL | algorithm/linear-integer-optimization + nonlinear-optimization | 吸收 | 优化大类已覆盖 |
| assets/02-预测类算法说明.md | FULL | time-series + supervised-learning + grey-forecasting | 吸收 | v0.1.3 补灰色预测 |
| assets/03-评价类算法说明.md | FULL | multi-criteria-evaluation + efficiency-analysis | 吸收 | v0.1.3 补 DEA/效率分析 |
| assets/04-图论与网络分析算法说明.md | FULL | network-routing | 吸收 | 最短路/流/匹配/TSP-VRP 路由到统一图网络族 |
| assets/05-统计分析与数据处理算法说明.md | FULL | statistical-inference + unsupervised-learning + data-audit | 吸收 | 统计/降维/聚类/预处理均有入口 |
| assets/06-综合类算法说明.md | FULL | stochastic-simulation + ode-dynamics + queueing + system-dynamics + cellular-automata + game-theory | 吸收 | v0.1.3 补排队/系统动力学/CA/博弈 |
| assets/07-机器学习算法说明.md | FULL | supervised-learning + unsupervised-learning | 吸收 | 算法级细分仍可继续向 RF/XGBoost/NN 下钻 |
| tools/figure/SKILL.md 方法论 | FULL | figure-design + visualization-review + tools/figure | 吸收 | 数据剖析→claim→选图→视觉审查逻辑已吸收；固定图数删除 |
| tools/figure/scripts/* | PARTIAL | tools/figure | 未来可补 | 当前 Hub 有工具契约，没有完整脚本实现 |
| tools/paper_search/* | PARTIAL | tools/paper-search | 未来可补 | 有工具接口，未重实现双引擎脚本 |
| tools/docx/* | PARTIAL | tools/docx | 未来可补 | 有工具接口，未重实现完整 OMML/validate 工具链 |
| tools/latex/* | PARTIAL | tools/latex | 未来可补 | 有工具接口，未重实现 doctor/build/bind/validate 全工具链 |
| tools/xlsx/* | PARTIAL | tools/xlsx | 未来可补 | 有工具接口，未重实现全部模板/重算/错误检查脚本 |
| tools/pdf/* | PARTIAL | tools/pdf | 未来可补 | 有工具接口，未重实现全部抽取工具 |
| dsh-plugin/math-modeling-agent/* | EXCLUDED | — | 主动排除 | DeepSeek Harness 平台专用封装，不属于通用 Skill Hub 核心 |
| .github / imgs / star-history / changelog | EXCLUDED | — | 主动排除 | 仓库运营与展示元数据，不影响建模能力 |

## han69611/math-modeling-skills@b5b98ae

| Upstream item | Status | Our mapping | Decision | Notes |
|---|---|---|---|---|
| 00-system | TRANSFORMED | SKILL.md + qa/* | 吸收 | 总规则拆为 Router/QA，审批/阶段权移除 |
| 01-start-mathmodel | EXCLUDED | mathmodel-pro Coach | 主动排除 | 12阶段总流程与 Coach 重复 |
| 02-analysis-modeling | FULL | problem-analysis + model-selection | 吸收 | 赛题分析与建模设计已深化 |
| 03-hypothesis | FULL | problem/hypothesis | 吸收 | 假设理由/影响/验证/失效风险保留 |
| 03-model-selection | FULL | modeling/model-selection + algorithm/* | 吸收并增强 | 由自动决策树升级为 Baseline+候选+算法族 dispatch |
| 04-coding | FULL | coding/implementation | 吸收 | 实现与最小纵向切片 |
| 04-coding-visual | FULL | implementation + figure-design | 拆分吸收 | 代码与图表不再绑死 |
| 05-result-analysis | FULL | experiment/result-analysis | 吸收 | 结果→比较→解释→意义 |
| 05-visualization | FULL | visualization/figure-design | 吸收 | claim 驱动选图 |
| 06-drawio | FULL | visualization/flowchart | 吸收 | 只在真正有流程/决策结构时画图 |
| 06-experiment-manager | FULL | experiment/experiment-manager | 吸收 | Run/commit/参数/seed/淘汰原因可追溯 |
| 07-result-analysis | FULL | experiment/result-analysis + statistical-inference | 吸收 | Baseline/统计检验/异常/迭代逻辑 |
| 07-writing | FULL | writing/* + technical-style | 吸收 | 写作结构与技术语言拆为专项 Skill |
| 08-reviewer-mode | FULL | audit/paper-review | 吸收 | 严格攻击数学/逻辑/证据/可读性 |
| 09-verify | FULL | audit/final-review | 吸收 | 风险优先而非虚构官方评分 |
| 09-writing | FULL | writing/* | 吸收 | 摘要/结果/大纲分别深化 |
| 10-innovation-engine | TRANSFORMED | modeling/innovation | 吸收 | 创新路径保留；主观 Innovation Score 删除 |
| 11-reviewer-mode | FULL | audit/paper-review | 吸收 | 9维审查核心已覆盖 |
| 12-verify | TRANSFORMED | audit/final-review | 吸收 | 风险等级保留；100分制不当作官方评分 |
| 1start-mathmodel | EXCLUDED | covered by v2-derived event skills | 主动排除 | Legacy 5阶段与新版能力重复，不保留重复入口 |
| 2analysis-modeling | EXCLUDED | covered by v2-derived event skills | 主动排除 | Legacy 5阶段与新版能力重复，不保留重复入口 |
| 3coding-visual | EXCLUDED | covered by v2-derived event skills | 主动排除 | Legacy 5阶段与新版能力重复，不保留重复入口 |
| 4drawio | EXCLUDED | covered by v2-derived event skills | 主动排除 | Legacy 5阶段与新版能力重复，不保留重复入口 |
| 5writing | EXCLUDED | covered by v2-derived event skills | 主动排除 | Legacy 5阶段与新版能力重复，不保留重复入口 |
| 6verity | EXCLUDED | covered by v2-derived event skills | 主动排除 | Legacy 5阶段与新版能力重复，不保留重复入口 |
| anti-ai-writing | TRANSFORMED | writing/technical-style | 吸收 | 保留真实技术表达；删除机械禁句和“规避检测”导向 |
| challenge-yourself | FULL | modeling/model-challenge | 吸收 | v0.1.3 补简化/替换/去掉/解释测试 |
| cumcm-paper-writing | FULL | writing/* + audit/paper-review | 吸收 | 结构、模型理由、结果解释、摘要与图表证据均覆盖 |
| domain-knowledge | FULL | domain/domain-context | 吸收 | v0.1.3 补9大领域特有机制/陷阱/指标 |
| innovation-engine | TRANSFORMED | modeling/innovation + model-challenge | 吸收 | 创新路径保留，数字打分删除 |
| latex-cjk-setup | PARTIAL | tools/latex | 未来可补 | 接口存在，具体 CJK 工具链未完整实现 |
| math-modeling | TRANSFORMED | Router + 48 event skills | 吸收 | 综合大 Skill 被拆成渐进加载的专项能力 |
| model-selection | FULL | modeling/model-selection | 吸收并增强 | 增加算法族/领域上下文/失败条件 |
| paper-score | EXCLUDED | audit/paper-review + final-review | 主动排除评分 | 保留风险检查，不保留主观100分 |
| project-manager | EXCLUDED | Competition Repo + mathmodel-pro | 主动排除 | 目录与版本治理属于真实比赛仓库/Coach，不让 Hub 抢权 |
| reviewer-mode | FULL | audit/paper-review | 吸收 | 独立评委视角 |
| visualization-review | FULL | visualization/visualization-review | 吸收 | 可读性/语义/正文对应保留，固定600dpi等改为目标/官方要求驱动 |

## Remaining High-Value Gaps

1. **XiaoMa 工具实现层**仍是最大缺口：`figure/docx/latex/paper_search/xlsx/pdf` 当前主要吸收接口和方法论，未完整重实现其脚本与模板。
2. **MCM/ICM 英文化工作流**目前仅部分存在于 writing role，尚未做成独立事件 Skill。
3. 算法族现在覆盖较完整，但仍可继续从“算法族”下钻到具体算法单元（如 MILP scheduling、VRP、ARIMA/ETS、XGBoost 等）；这属于深化，不属于当前上游覆盖缺失。

## Explicit Non-Goals

- 不恢复 Han 的 12 阶段/Legacy 固定流水线；全局阶段由 Coach 管理。
- 不恢复每阶段必须用户审批、固定图数/页数、无 Subagent 即全局 BLOCKED。
- 不恢复 Innovation Score / paper-score 之类无官方依据的总分作为决策真值。
- 不吸收 XiaoMa 的 DSH 平台专用插件和仓库运营元数据。

