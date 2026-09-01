---
name: english-paper
trigger: ENGLISH_PAPER_NEEDED
description: 将已验证的中文/双语建模内容转换为适合 MCM/ICM 等英文建模论文的技术英文，同时保持公式、数字、单位、引用与证据链不变。
---

# english-paper

## Trigger

- 事件：`ENGLISH_PAPER_NEEDED`。
- 用户明确要求把已完成的建模论文转换为英文竞赛论文时可直接调用。
- 本 Skill 负责技术英文化，不替代当届官方格式规则检查。

## Scope

目标是把已经冻结的模型、结果和论证关系写成清晰、紧凑、可核验的英文，而不是逐句直译中文，也不是为了规避任何 AI 检测。公式、关键数字、单位、图表编号、引用和结论强度不得在英文化过程中被擅自改变。

## Inputs

- 已验证的中文正文或双语稿
- Claim-Evidence Map / Final Run
- 符号表、术语表、图表与参考文献
- 目标竞赛当届官方模板/规则（如涉及格式）

## Procedure

1. 先冻结事实层：建立术语—符号—单位—数字对照表；对每个关键结论标出其公式、表图或运行证据。英文化只改表达，不改这些事实锚点。
2. 按“逻辑关系”而非中文语序重写：每段优先呈现 claim → method/evidence → quantitative result → implication/limitation，避免长串名词化和逐字翻译。
3. 统一术语：同一模型、变量、约束、评价指标只保留一个主英文名称；首次出现时定义，后文不随意换同义词。
4. 处理时态与语态：题目事实/模型定义通常用一般现在时；已执行实验与获得结果通常用过去时；避免为了“学术感”过度使用被动语态。
5. 数学语言保持严格：区分 estimate/predict/simulate/optimize/prove；只有有最优性证据时才写 optimal/global optimum；相关性不得改写为 causality。
6. 摘要和结论做英文独立压缩：优先保留问题、核心方法、关键定量结果、验证/价值；删除中文论文中常见的背景复述和空泛总结。
7. 对图表标题、坐标轴、表头、注释、交叉引用做同一术语校验；数字、有效位、百分号、单位必须与权威结果一致。
8. 最后做双向一致性审计：抽取英文稿中的关键数字/公式引用/模型名，与原稿和 Final Run 对照；任何语义增强必须有新证据，否则回退。

## Outputs

- 英文正文或指定章节
- 术语/符号一致性表
- 关键数字与引用一致性检查结果
- 仍需人工确认的竞赛格式或措辞风险

## Checks

- 公式、数字、单位、引用没有因翻译变化
- 术语在全文中一致
- 摘要中的定量结论可追到 Final Run
- 未把“更好/稳定/最优/显著”等弱证据结论升级为强断言
- 英文段落按论证关系组织，而非机械逐句翻译

## Failure

- 原稿存在未冻结数字或证据冲突：转 `CLAIM_UNSUPPORTED` / `FINAL_RESULT_NEEDS_REVIEW`
- 原稿数学定义本身不清楚：转 `MODEL_CONTRACT_MISSING`
- 仅涉及最终官方格式：转 `PRE_SUBMISSION`

## Handoff

英文稿完成后推荐 `PAPER_NEEDS_ATTACK` 做独立语义审稿，再由 `PRE_SUBMISSION` 核验当届官方格式。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
