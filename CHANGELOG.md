# Changelog

## 0.1.11 — Paper Quality Repair

- 新增 `paper-synthesis`：明确 Repo→paper 的选择性压缩与 main/appendix/support 分层。
- 新增 `editorial-compression`：处理正文膨胀、算法百科、重复、审计化/合规补丁污染。
- 新增 `judge-review`：有限注意力评委扫读、5-minute map、scan friction；不使用虚构评分表。
- `paper-review` 收窄为 scientific/semantic review，避免把数学正确性、编辑质量、合规问题混成一个总评。
- `final-review` 增加 compliance overlay 非退化检查：合规修改不得无必要破坏正文叙事和渲染质量。
- writing role、outline、result-writing、abstract、technical-style、visualization-review 同步 paper-quality contract。
- 新增 `references/paper-quality-contract.md` 与 `scripts/validate_paper_quality.py`。
- SkillHub 现为 53 个事件驱动 Skill；新增能力仍按需调用，不形成论文固定流水线。


## 0.1.10

- 强化 `OFFICIAL_RULES_NEEDED` 到固定 Competition Repo 规则位置。
- final-review 将规则核验、AI 披露真实性、论文附录源程序、独立支撑材料一致性纳入最终审计。
- 不新增全局策略 Skill，不改变 50 个局部事件边界。

### Integration-audit fixes

- 全系统演练与集成审计修复版。
- 移除越权 `competition-strategy` first-class Skill，恢复 50 个局部事件 Skill。
- validator 改为 registry/Skill 双向动态一致性检查并校验版本。
- reproducibility 拆分 artifact integrity / replay reproducibility，修正 cwd 相对路径，支持 CSV/JSON semantic fingerprint。
- XLSX 增加百万行级只读 streaming/summary。

## 0.1.8

- 减法优化：降低 Skill 重复。
- 增加 claim-evidence Figure 映射与 benchmark 压力测试规范。
- 曾加入 `competition-strategy`；集成审计证明其越过 Coach/Hub 边界，因此在 0.1.10 回退为 Coach-owned strategy。

## 0.1.7

- 第二轮按同能力质量深挖，不扩张 Coach/Hub 总架构。
- 新增 `OFFICIAL_RULES_NEEDED` / `problem/competition-rules`，总事件 Skill 从 49 增至 50；官方硬约束、官方建议、用户要求、内部目标分级记录。
- 新增 `competition-rule-profile.md` 与 `templates/competition-rules.yaml`，避免固定页数/图数/字数被误当永久官方规则。
- 新增 `model-composition-patterns.md`：11 类组合模式以结构签名、候选组合、证据、失效条件表达，明确禁止“题型→固定算法”捷径。
- MATLAB 成为一等实现后端：新增 MATLAB 专项规范与 feature-scoped 环境报告脚本；run manifest 升级 v2，支持任意 runtime 和 dependency 版本。
- Figure 增加选图与证据、视觉编码与布局、误导/最终尺寸 review 三份深度 guide。
- 新增 `validate_profiles.py`；原 18 算法族、7 Tool、72 上游审计行保持兼容。

## 0.1.6

- 纠正“只补缺失项”的合并策略，改为对 Hub / Han / XiaoMa **同能力逐项比较后择优**。
- 新增 `references/overlap-quality-selection.md/.csv` 与 `algorithm-depth-selection.md`，明确每类重叠能力的 winner、融合项和主动排除项。
- 三个 Role 保留 Hub 权限外壳，但补强建模前置合同、数值稳健性/复现、证据写作/自审与英文论文参考。
- Figure 独立增强为多文件/glob、raster/SVG/PDF、可配置 DPI/尺寸、丰富数据剖析、source 与灰度 QA。
- LaTeX 独立增强为 generic/CJK init、bibliography-aware build、资源/ref 检查、字体/PDF 审计、显式规则阈值与 provenance。
- XLSX 采用融合：保留原工作簿/公式审计，新增显式 LibreOffice 重算到新文件。
- Paper Search 采用融合：保留 OpenAlex + Crossref 公共双源，增加 DOI/高阈值模糊题名去重、年份/引用过滤和透明相关性排序。
- DOCX/PDF 依据能力边界独立补强只读 QA；由于上游对应目录含限制性许可，明确不复制/派生其源码或模板。
- 工具验证扩展为 22 个实现文件；原有 49 事件 / 18 算法族 / 72 上游覆盖行保持结构兼容。
## 0.1.5

- 选择性吸收当前上游高价值能力，不恢复固定阶段总流程。
- 新增 `ENGLISH_PAPER_NEEDED` / `writing/english-paper`，总事件 Skill 49 个，算法族仍 18 个。
- 新增 `references/solver-robustness.md` 与 4 个算法 playbook：模糊综合评价、网络搜索/路由、分类 baseline、随机启发式优化。
- 新增 `tools/reproducibility`：按 feature 检查依赖；创建/验证 run manifest，绑定命令、seed、Git/运行时/依赖版本和指定输入/产物 SHA-256。
- Figure Tool 新增绘图源码静态 QA 与 raster 灰度/对比度 QA。
- LaTeX Tool 新增 build provenance JSON、engine 版本、耗时与 fatal/warning 分层。
- Paper Review 增加快速评阅路径与关键结论证据密度检查，但不规定固定图数。
- 修复 `registry.yaml` 版本仍停留在 0.1.3 的一致性问题。
- 主动不吸收 Han Legacy/12 阶段、paper-score/project-manager，以及 XiaoMa 固定图数/页数/平台插件和不明确许可证代码的直接复制。

## 0.1.4

- 六个 Tool 从纯契约升级为可执行核心：PDF、XLSX、Figure、DOCX、LaTeX、Paper Search。
- 新增 PDF 结构审计/页码文本抽取；XLSX 工作簿审计/受限读取。
- 新增 Figure 数据剖析、图文件检查和 matplotlib 导出 helper。
- 新增 DOCX OOXML/OMML 审计与真实 LibreOffice 页面渲染。
- 新增 LaTeX doctor/init-cjk/build/bind/validate，并实际通过 XeLaTeX smoke。
- 新增 OpenAlex + Crossref 双源学术检索与 DOI/题名去重；不复制上游 AnySearch 实现。
- 增加 `validate_tools.py` 与 `tool_smoke.py`；coverage matrix 将 figure/paper-search/latex/pdf 更新为 TRANSFORMED，DOCX/XLSX 保持 PARTIAL。
- 48 个事件 Skill 和 18 个算法族保持不变，Coach/Hub 权限边界不变。

## 0.1.3

- 新增 Upstream Coverage Matrix，对 XiaoMa 与 Han 共 72 个重要条目逐项标记 FULL / TRANSFORMED / PARTIAL / EXCLUDED。
- 新增 `domain-context`、`model-challenge`、`technical-style` 三个专项 Skill。
- 新增 6 个算法 Skill：灰色预测、DEA/效率分析、排队、系统动力学、元胞自动机、博弈论。
- 总 Skill 数由 39 增至 48；算法族由 12 增至 18。
- `model-selection` 增加领域上下文与 6 个新算法族 dispatch。
- 明确剩余最大缺口是 XiaoMa 的 figure/docx/latex/paper_search/xlsx/pdf 具体工具实现，而非核心建模方法论。
- 继续主动排除固定阶段链、主观总评分、逐阶段审批和平台专用封装。

## 0.1.2

- 新增 12 个 algorithm-family Skill，覆盖优化、网络、预测、机器学习、评价、动力学、随机、统计和几何。
- `model-selection` 增加结构化 `ALGO_*` dispatch，不再承担全部算法细节。
- 新增 `algorithm-dispatch.md` 和更完整的 `algorithm-index.md`。
- 新增算法路由测试；保持 Coach 对阶段、优先级、冻结和提交的唯一调度权。
- 未引入固定页数/图数/模型数、固定扰动比例或强制用户审批。


## 0.1.1

- Deepened all 27 event-driven Skills from generic contracts into executable local workflows.
- Added domain-specific procedures, checks, failure routing and handoff logic for each Skill.
- Preserved every v0.1.0 event name/path and Coach-vs-Hub authority boundary.
- Removed fixed percentage sensitivity assumptions and arbitrary quantity targets from detailed procedures.
- Strengthened Final Run, Run Ledger, Claim-Evidence, numerical verification and independent review semantics.
- Expanded router scenario coverage to all 27 events and added a Skill Depth Map.

## 0.1.0

- 建立 XiaoMa 风格的 Router / Role / Tool / QA 骨架，但重新编写内容。
- 吸收 Han 的假设设计、模型选择、实验管理、结果分析、创新、Reviewer、Verify 等局部能力思想。
- 建立 27 个事件驱动专项 Skill。
- 删除固定 12 阶段链、固定图数/篇幅、逐阶段审批和无 Subagent 即全局阻断。
- 明确 Coach > Hub 的调度权边界。
- 新增 registry、QA contract、router scenarios 和结构校验脚本。
