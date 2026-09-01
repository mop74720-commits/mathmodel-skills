# Changelog

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
