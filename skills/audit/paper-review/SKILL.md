---
name: paper-review
trigger: PAPER_NEEDS_ATTACK
description: 以独立语义审稿视角攻击论文的数学、逻辑、证据、结果一致性和过度宣称；编辑压缩与评委扫读由专门 Skill 负责。
---

# paper-review

## Trigger

- 事件：`PAPER_NEEDS_ATTACK`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

这是 scientific/semantic paper review，不替代格式脚本，也不负责把所有可读性问题都混进同一个审稿。reviewer 默认只读。

## Inputs

- 论文正文/PDF 或可渲染稿
- 问题合同
- 模型合同
- Final Run/Claim-Evidence Map
- 图表与参考文献

## Procedure

1. 检查答题完整性：所有子问题是否真正回答，直接结论能否在正文中定位。
2. 审数学链：公式定义、推导、符号、单位、边界、条件、模型适用性和求解逻辑。
3. 审证据链：关键数字、最优性、显著性、鲁棒性、创新性等表述是否有同等级直接证据。
4. 审一致性：摘要、正文、表图、结论、附录中的模型名、参数、数字、单位是否与 Final/合同一致。
5. 审图表真实性：图是否支持 claim，统计口径、单位、样本量、误差和尺度是否足够；纯视觉编辑问题可转 `FIGURE_WEAK`。
6. 审因果和强表述：避免“证明最优、完全准确、显著提升”等越过证据边界的结论。
7. 检查是否存在正文与附录/支撑材料之间的科学内容漂移，例如代码使用不同参数、附录公式与正文模型不一致。
8. 按 scientific P0/P1/P2 排序并给出页/节/公式/表图位置。若主要问题只是正文过长或评委扫读困难，不在这里无限扩写，分别转 `PAPER_TOO_BLOATED` 或 `PAPER_JUDGE_REVIEW_NEEDED`。

## Outputs

- scientific/semantic 问题矩阵
- P0/P1/P2 分级
- 必须修复与可选增强清单
- 可读性问题的专门路由建议

## Checks

- 问题都有精确位置和证据理由
- 不使用虚构官方评分表打“总分”
- 不因风格偏好判数学错误
- 关键事实与 Final/合同交叉核对
- 不把 compliance/aesthetic/judge 三类问题混成一个总分

## Failure

- scientific P0/P1：FAIL 并回对应 modeling/coding/writing
- 主要是正文膨胀：转 `PAPER_TOO_BLOATED`
- 主要是扫读摩擦：转 `PAPER_JUDGE_REVIEW_NEEDED`
- 缺权威规则：转 `OFFICIAL_RULES_NEEDED`
- 仅 scientific P2：WARN，可由 Coach 决定是否继续优化

## Handoff

返回只读 scientific review 回执；修改后只复审受影响范围。编辑质量与提交合规由专门 Skill 分别处理。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
