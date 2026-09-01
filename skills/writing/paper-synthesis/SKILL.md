---
name: paper-synthesis
trigger: PAPER_SYNTHESIS_NEEDED
description: 把完整 Competition Repo 中的已验证证据选择性合成为竞赛论文正文，明确正文/附录/支撑材料边界，避免把仓库打印成论文。
---

# paper-synthesis

## Trigger

- 事件：`PAPER_SYNTHESIS_NEEDED`。
- 当模型、结果和部分验证已可用于写作，但现有材料仍是 Repo/实验/审计碎片，尚未形成高质量论文叙事时调用。
- 不要求所有问题都已最终冻结；只对已有稳定证据合成，未稳定内容保留为缺口。

## Scope

负责“证据选择与论文叙事设计”，不是重新建模，也不是官方格式审计。必须遵守 `references/paper-quality-contract.md`。

## Inputs

- 问题合同与题面事实
- 模型合同
- Final/候选稳定 Run 与结果分析
- Claim-Evidence Map
- 关键图表
- 已有论文草稿（如有）
- 官方结构/篇幅规则（若已核验）

## Procedure

1. 先把 Repo 信息分成 `main-text / appendix / support-only / omit` 四类；Repo 完整性不能自动转化为正文长度。
2. 为每个子问题确定一个直接答案和最小充分证据链：问题 → 模型机制 → 结果 → 表图/验证 → 含义/边界。
3. 识别跨问题共享的变量、数据处理、模型机制和验证，只在首次出现处完整说明，后文引用。
4. 选择最能帮助评委比较和理解的关键表图；不为了“看起来丰富”增加重复图。
5. 将实验日志、内部审计、Run 路径、AI 使用详情、完整 provenance、调试过程等默认留在 Repo/支撑材料；官方明确要求进入论文时放到最小必要位置或隔离附录。
6. 设计正文叙事顺序，使读者先看到问题、核心机制和答案，再看到必要细节；不要按 Repo 目录顺序写论文。
7. 为尚未稳定的数字或结论标记证据缺口，不写伪 Final 文本。
8. 生成正文草稿/结构后，做一次“如果删除这一段会不会影响理解或证据”测试；无影响的内容进入压缩候选。

## Outputs

- 主正文结构与可直接撰写的 synthesis draft
- `main-text / appendix / support-only / omit` 内容映射
- 每问核心 claim-evidence 闭环
- 关键图表位置与用途
- 尚未稳定/缺证据项

## Checks

- 正文不是 Competition Repo 的逐目录转写
- 每问的直接答案可快速定位
- 关键模型机制和关键结果均有足够证据
- Audit/governance/provenance 语言没有无必要进入正文
- 正文、附录、支撑材料边界清楚
- 不使用固定页数/图数作为通用质量门槛

## Failure

- 关键 claim 无证据：转 `CLAIM_UNSUPPORTED`
- 结果本身未稳定：转 `FINAL_RESULT_NEEDS_REVIEW`
- 已有正文主要问题是冗长和补丁化：转 `PAPER_TOO_BLOATED`
- 需要最终评委扫读：转 `PAPER_JUDGE_REVIEW_NEEDED`

## Handoff

返回合成后的正文权威路径和内容映射；是否立即继续写作、验证或改模型由 Coach 决定。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
