---
name: causal-inference
trigger: ALGO_CAUSAL_INFERENCE
description: 处理干预/处理—结果、反事实与政策效应问题；先做因果识别，再选择估计器，强调 DAG、混杂、重叠、设计诊断和安慰剂/敏感性检验。
---

# causal-inference

## Trigger

- 事件：`ALGO_CAUSAL_INFERENCE`。
- 当题目明确询问“某干预是否导致结果变化”“政策效应是多少”“控制混杂后处理效应是否仍存在”“处理组与对照组如何构造反事实”等问题时调用。
- 只有相关性、预测准确率或普通组间差异时，不应为了显得高级而自动升级到因果推断。

## Scope

本 Skill 负责从因果问题定义、识别假设到估计与诊断的局部技术路线。覆盖随机试验与常见观察性设计：协变量调整、匹配/倾向评分、IPW/AIPW、双重差分（DiD）、回归不连续（RDD）、工具变量（IV）和合成控制等。它不把某个估计器名称当作“已经识别”，也不把观察数据中的相关性包装成因果结论。

## Inputs

- 因果问题：处理/暴露 `T`、结果 `Y`、分析单位与时间索引
- 目标 estimand：ATE / ATT / CATE 或题目定义的政策效应
- 处理分配机制与可用对照
- 处理前协变量、潜在混杂、可能的中介与碰撞变量
- 时间结构、政策实施点、阈值/规则、空间或网络干扰信息
- 数据覆盖、缺失、测量误差与抽样机制
- 可用领域知识、文献 Method Card 与当前假设登记

## Procedure

1. **先写因果问题而不是先选算法**：明确 `T → Y` 的决策含义、分析单位、处理时点、潜在结果/反事实，以及最终要报告的 estimand。
2. **画最小因果结构**：用 DAG 或等价结构列出 pre-treatment confounders、mediators、colliders、selection variables。禁止把处理后的变量无脑当控制变量。
3. **识别优先于估计**：说明为什么目标效应在现有设计下可识别。检查 consistency/SUTVA、exchangeability 或设计特有假设、positivity/overlap；若存在群体/网络干扰，显式声明标准 SUTVA 是否失效。
4. **先建立非因果 Baseline**：描述性差异或调整回归可作为参照，用于展示“仅相关”与“满足识别假设后的效应估计”之间的差别。
5. **按设计选择最小充分方法**：
   - 已随机分配：优先按随机化设计分析，并保留随机化/分层信息。
   - 观察性协变量充分：回归调整、matching、propensity score、IPW；需要稳健性时考虑 doubly robust / AIPW。
   - 明确处理前后 + 处理/对照组：在平行趋势可辩护时考虑 DiD/event study。
   - 明确阈值决定处理：在局部连续性与无操纵条件可辩护时考虑 RDD。
   - 存在影响处理但只通过处理影响结果的外生工具：在排除限制等条件可辩护时考虑 IV。
   - 单一/少数干预单位 + 可构造供体池：考虑 synthetic control，并检查 pre-treatment fit。
6. **做设计特异诊断**：overlap/balance、pre-trend、阈值密度与协变量连续性、第一阶段强度、合成控制处理前拟合等。估计器“跑出来”不等于识别成立。
7. **做反驳与敏感性**：placebo/falsification、不同合理控制集、不同带宽/匹配口径、未观测混杂敏感性、负对照（若适用）。记录什么证据会让因果措辞降级为关联性结论。
8. **只报告与识别强度相称的结论**：给效应量、区间/不确定性、目标人群和外推边界；若只能识别局部效应，不外推成全体平均效应。

## Decision Rules

- **关联问题**：若题目只问预测/关联，转 `ALGO_STATISTICAL_INFERENCE` 或 `ALGO_SUPERVISED_LEARNING`。
- **干预问题但无法识别**：不要用更复杂估计器掩盖缺口；返回 `ASSUMPTION_WEAK` / `MODEL_UNCERTAIN`，并明确“当前数据只能支持关联”。
- **DiD**：没有可信处理前趋势或存在明显差异性提前反应时，不把标准 DiD 当默认答案。
- **RDD**：阈值附近存在排序/操纵或协变量断点时，需要重新审查识别。
- **IV**：工具相关性不足、排除限制无依据或单调性不合理时，不使用 IV。
- **Propensity methods**：倾向评分不能修复未观测混杂；严重缺乏 overlap 时应缩小 estimand/目标人群或改变设计。
- **Synthetic control**：处理前拟合差或供体被同一干预污染时，不把处理后差异解释为可信政策效应。

## Validation Design

1. 报告处理/对照样本与关键协变量的可比性；加权/匹配后检查 balance 和有效样本量。
2. 检查 overlap/positivity；展示极端权重、修剪或目标人群变化对结论的影响。
3. DiD 做 pre-trend / event-study 与 placebo timing；RDD 做 bandwidth、kernel、polynomial order、density/manipulation 与协变量连续性检查。
4. IV 检查 first-stage strength，并把排除限制作为不可由数据单独证明的关键假设；必要时做弱工具稳健推断。
5. 合成控制报告 pre-treatment fit、placebo units/time 与供体敏感性。
6. 对主要 estimand 做至少一种 falsification / placebo 或 unmeasured-confounding sensitivity；若结论易翻转，降级措辞。
7. 若有随机化或准实验的已知 ground truth，可通过 simulation/recovery 检查实现链，区分设计错、估计错与代码错。

## Outputs

- Causal Question / estimand
- DAG 或最小因果结构与变量角色
- identification assumptions 与可验证/不可验证边界
- Baseline 与主估计路线
- design diagnostics
- effect estimate + uncertainty
- falsification / placebo / sensitivity 结果
- strongest identification risk、flip condition 与 fallback

## Checks

- 因果措辞与识别假设匹配，没有把相关性写成因果
- 控制变量是按因果角色选择，而不是“能放进去的都控制”
- treatment/post-treatment 时间顺序明确
- overlap/positivity 与样本支持范围已检查
- 方法特有假设和诊断齐全
- 结论没有超出 estimand 与样本外推边界
- 至少有一个反驳/安慰剂/敏感性检查

## Failure

- 因果方向/变量角色无法确定：转 `PROBLEM_AMBIGUOUS` 或 `DOMAIN_CONTEXT_NEEDED`。
- 识别依赖无法辩护的强假设：转 `ASSUMPTION_WEAK`，并将结论降级。
- 重叠严重不足、阈值操纵、平行趋势失败或工具变量过弱：返回 `MODEL_UNCERTAIN`，选择替代 estimand/设计。
- 实现结果对数值/代码细节异常敏感：转 `NUMERICAL_SUSPECT` / `IMPLEMENT_MODEL`。
- 需要专门设计可控实验来识别效应：转 `EXPERIMENT_DESIGN_NEEDED`。

## Handoff

识别与估计合同稳定后转 `MODEL_CONTRACT_MISSING`；需要实际实现转 `IMPLEMENT_MODEL`；需要设计干预/仿真实验转 `EXPERIMENT_DESIGN_NEEDED`；结论对假设或设计敏感时转 `NEED_SENSITIVITY` / `RESULT_UNSTABLE`；需要引用外部因果方法证据时转 `LITERATURE_EVIDENCE_NEEDED`。

统一回执：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。本 Skill 可以建议下一事件，但不能替 Coach 决定比赛阶段或题目优先级。
