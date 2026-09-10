---
name: model-selection
trigger: MODEL_UNCERTAIN
description: 基于问题结构、数据条件、工程风险和决定性证据选择 Baseline + 主候选 + 必要备选，并明确反驳、翻转与回退条件。
---

# model-selection

## Trigger

- 事件：`MODEL_UNCERTAIN`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

选择的是“模型族和求解路线”，不是堆算法名称。重点是让候选与题目结构匹配，并用最小必要证据决定复杂度。Baseline 是默认比较锚点；若理论结构/可辨识性尚未澄清，可先建立最小证明性结果而不是为形式强行编码。

## Inputs

- 问题合同
- 数据审计
- 假设登记
- 现有 baseline/历史结果（如有）
- 可用算力和软件约束

## Procedure

1. 先判定每个子问题的主类型：优化、预测、评价、分类/聚类、机理/仿真、图网络、统计/贝叶斯、因果/反事实、信号/时频、个体仿真或混合类型；混合题拆成组件而不是硬贴单标签。若赛题属于明显专业领域且领域机制会改变变量、约束或评价口径，先发出 `DOMAIN_CONTEXT_NEEDED`，再做最终模型取舍。
2. 在生成候选前，可按需读取 `references/model-composition-patterns.md` 做**结构模式识别**。模式只用于提出候选组合及其必需证据，禁止把“样本小/指标多/规模大”等弱线索直接映射为固定算法。若一级算法族已明确但需要选择具体方法，再按 `references/algorithm-depth-selection.md` 加载一个必要 playbook，不预加载整套算法百科。
3. 建立 Baseline 或最小证明性结果：应简单、可解释，用于判断复杂方案是否真的带来收益；若当前关键未知是可辨识性、参数来源、因果识别或硬约束，应先解决该未知，再决定是否值得实现 Baseline。
4. 只在存在真实选择不确定性时生成少数独立候选模型族。低不确定性时允许 `baseline + primary`；不要为了“至少两个模型”制造无意义备选。候选若只差超参数或同一机制近似阶次，按一个模型族处理。
5. 逐个检查适用条件：所需数据、变量类型、约束表达能力、样本量、可辨识性/可识别性、计算复杂度、是否能在剩余环境中实现、可用验证方式。
6. 对候选给出定性证据矩阵：适配度、实现风险、验证成本、解释性、潜在增益。不要用无依据的 0-100“综合分”冒充客观评价。
7. 对主候选写出 `strongest_objection / rejected_alternatives / refutation_tests / deciding_evidence / flip_condition`：不仅说明为什么选，还要说明什么证据会让更简单或不同路线重新成为首选。
8. 给出推荐顺序与结构化 fallback：`trigger + action`；deadline 仅在 Coach 的真实剩余时间判断需要时加入，Skill 不自带固定 Day-1/Day-2 时间门槛。
9. 若问题结构已足够明确，不要继续在本 Skill 内展开算法细节，而是路由到最小必要的 algorithm Skill：
   - 线性/整数/0-1/资源分配 → `ALGO_LINEAR_INTEGER`
   - 连续非线性/非凸优化 → `ALGO_NONLINEAR_OPT`
   - 图、流、路径、TSP/VRP → `ALGO_NETWORK_ROUTING`
   - 时间序列预测 → `ALGO_TIME_SERIES`
   - 小样本、信息不完全且趋势平滑的灰色预测候选 → `ALGO_GREY_FORECAST`
   - 有标签回归/分类 → `ALGO_SUPERVISED_LEARNING`
   - 聚类/降维 → `ALGO_UNSUPERVISED_LEARNING`
   - 多指标评价/排序 → `ALGO_MULTI_CRITERIA`
   - 多投入—多产出相对效率/前沿 → `ALGO_EFFICIENCY_ANALYSIS`
   - ODE/状态空间 → `ALGO_ODE_DYNAMICS`
   - PDE/空间场 → `ALGO_PDE_DYNAMICS`
   - Monte Carlo/Markov/随机模拟 → `ALGO_STOCHASTIC_SIM`
   - 到达—服务—等待/拥堵 → `ALGO_QUEUEING`
   - 库存—流量—反馈—延迟 → `ALGO_SYSTEM_DYNAMICS`
   - 空间格点+局部更新规则 → `ALGO_CELLULAR_AUTOMATA`
   - 多主体策略互动 → `ALGO_GAME_THEORY`
   - 假设检验/参数推断 → `ALGO_STATISTICAL_INFERENCE`
   - 明确干预/处理—结果、政策效应、反事实或混杂控制 → `ALGO_CAUSAL_INFERENCE`
   - 几何/碰撞/空间重建 → `ALGO_GEOMETRY`
   - 先验—似然—后验、层级/部分池化、后验预测 → `ALGO_BAYESIAN_MODELING`
   - 采样信号的频域/时频、滤波、去噪 → `ALGO_SIGNAL_PROCESSING`
   - 异质自主个体、环境/网络交互与涌现 → `ALGO_AGENT_BASED_MODELING`
   混合题允许一个主 algorithm Skill + 一个必要的 secondary，不要一次加载整套算法库。

## Outputs

- 模型候选表
- Baseline/首选/必要备选及理由
- strongest objection / rejected alternatives / refutation tests
- deciding evidence / flip condition
- fallback trigger + action
- 需要进一步比较时的公平比较协议草案

## Checks

- 有可解释的 Baseline/最小证明性结果，或明确说明为什么当前应先澄清更上游结构
- 候选模型与题面目标和数据结构有直接联系
- 因果问题在选择估计器前已先检查识别条件
- 没有把复杂度当创新性
- 没有承诺“全局最优/高精度/因果效应”而无验证依据
- 没有把具体算法名直接升级成一级路由，除非它对应独立的问题结构和验证合同

## Failure

- 候选优劣需要数据跑分才能裁决：转 `MODELS_NEED_COMPARISON`
- 已选路线但数学合同未冻结：转 `MODEL_CONTRACT_MISSING`
- 模型都依赖高风险假设：返回 `ASSUMPTION_WEAK`
- 因果问题没有可辩护的识别策略：优先转 `ALGO_CAUSAL_INFERENCE` 做 identification audit，而不是直接套回归

## Handoff

推荐下一事件优先是 `DOMAIN_CONTEXT_NEEDED`（若领域机制尚未核清）或匹配的 `ALGO_*` 事件；候选模型形成后、若需要检查复杂度和创新真实性，可转 `MODEL_NEEDS_CHALLENGE`。算法族已经确定且无需进一步展开时，再转 `MODEL_CONTRACT_MISSING` 或 `MODELS_NEED_COMPARISON`。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
