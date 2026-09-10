---
name: literature-evidence
version: 0.1.13
event: LITERATURE_EVIDENCE_NEEDED
description: 把已找到的文献候选转成可审计 Method Card，核对方法前提、所需数据、可迁移部分、失败模式和证据定位；不把文献方法直接当作当前题证据。
---

# Literature Evidence

## Purpose

用于“搜到论文以后，判断这篇论文到底能不能影响当前建模决策”。输出不是摘要堆积，而是少量可追溯的 Method Card。

本 Skill 不负责全局选题，不替代 `model-selection`，也不允许因为某篇论文使用某方法就机械采用该方法。

## Inputs

至少需要：

- 当前 question / problem contract；
- 当前数据画像或已知字段/变量；
- 一个或多个文献候选（标题、DOI/URL、摘要或全文证据）；
- 当前 deciding unknown 或需要判断的候选方法。

若只有检索词而没有文献候选，可先调用 `tools/paper-search`；检索成功只代表拿到候选，不代表已经核验方法。

## Procedure

1. **确认证据层级**
   - 区分 `FULLTEXT_VERIFIED / ABSTRACT_ONLY / METADATA_ONLY`。
   - 拿不到全文时必须明确降级，禁止假装读过正文。

2. **提取问题结构**
   - 文献解决的实际任务是什么；
   - 输入、输出、变量类型、时间/空间/网络结构是什么；
   - 与当前题结构相同和不同的地方分别是什么。

3. **提取方法合同**
   - 方法/算法；
   - 关键假设；
   - required data / parameters；
   - 训练、求解或校准条件；
   - 文献自己的 validation / benchmark；
   - 已声明的 limitation 或可推导的适用边界。

4. **做迁移检查**
   - `transferable_parts`：当前题可以借用的机制、建模结构、验证方式、baseline 或计算策略；
   - `non_transferable_parts`：当前题缺变量、尺度不同、假设冲突、评价口径不同或证据不足的部分；
   - `failure_modes`：如果迁移，最值得提前做的 refutation test。

5. **绑定证据定位**
   - 每个关键方法主张尽量记录 section/page/table/equation/figure 或摘要字段；
   - DOI、URL、作者年份等只证明来源身份，不替代具体证据定位。

6. **给出 decision role**
   只能使用：
   - `CANDIDATE_PRIOR`：值得进入候选，但尚未被当前题验证；
   - `PROBE_HINT`：提示最有信息量的当前题 probe；
   - `VALIDATION_PATTERN`：可迁移其验证设计；
   - `BACKGROUND_ONLY`：只作背景；
   - `REJECT_FOR_CURRENT_TASK`：当前题条件不满足。

7. **写入/更新 Method Card**
   推荐遵循 `references/method-card-contract.md`。若 Competition Repo 提供 `references/method_cards/`，每篇/每种方法单独保存；不要把几十篇论文塞进一张表。

## Method Card minimum fields

```yaml
card_id:
source:
evidence_level:
problem_structure:
method:
assumptions:
required_data:
transferable_parts:
non_transferable_parts:
failure_modes:
validation_pattern:
evidence_locator:
decision_role:
current_task_status: CANDIDATE | ADAPTED | ADOPTED | REJECTED
reason:
```

## Handoff

- 方法值得进入当前候选 -> `MODEL_UNCERTAIN` / `model-selection`
- 两条路线需要真实公平比较 -> `MODELS_NEED_COMPARISON`
- 方法需要小规模实现验证 -> `IMPLEMENT_MODEL`，并由 Coach 决定是否作为 `pilot_run`
- 文献暴露了当前题意/数据解释错误 -> 返回 Coach，触发 evidence reconciliation；不要由本 Skill 自行修改正式题意
- 论文主张需要引用绑定 -> `CLAIM_UNSUPPORTED`

## QA / Failure conditions

以下任一情况不得把 Method Card 标为 `ADOPTED`：

- 只看标题/元数据，却写出正文不存在的前提或结果；
- 关键 required data 在当前题不存在且没有可辩护替代；
- 把文献中的性能、阈值、参数或结论直接当成当前题事实；
- 迁移后没有当前题 validation / probe；
- 无法区分文献实际证据与模型自己的推测。

## Boundary

文献是 external evidence/prior；当前比赛的 deciding evidence 仍应来自题面、附件、官方来源和当前可复现实验。该设计选择性吸收 `zhou2030109-glitch/Remit` 的 method-card / literature-to-model feedback 思想，并按本 Hub 的局部事件边界独立重写。
