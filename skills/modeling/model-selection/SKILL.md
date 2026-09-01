---
name: model-selection
trigger: MODEL_UNCERTAIN
description: 基于问题结构、数据条件、可解释性、求解成本和验证能力选择 Baseline + 主候选 + 必要备选。
---

# model-selection

## Trigger

- 事件：`MODEL_UNCERTAIN`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

选择的是“模型族和求解路线”，不是堆算法名称。重点是让候选与题目结构匹配，并保留一个可快速跑通的 Baseline。

## Inputs

- 问题合同
- 数据审计
- 假设登记
- 现有 baseline/历史结果（如有）
- 可用算力和软件约束

## Procedure

1. 先判定每个子问题的主类型：优化、预测、评价、分类/聚类、机理/仿真、图网络或混合类型；混合题拆成组件而不是硬贴单标签。
2. 建立 Baseline：应简单、可解释、可快速复现，用于判断复杂方案是否真的带来收益；Baseline 不等于“低质量模型”。
3. 生成少数真正独立的候选模型族。候选之间若只差超参数或同一机制的近似阶次，按一个模型族处理。
4. 逐个检查适用条件：所需数据、变量类型、约束表达能力、样本量、可辨识性、计算复杂度、是否能在剩余环境中实现、可用验证方式。
5. 对候选给出定性证据矩阵：适配度、实现风险、验证成本、解释性、潜在增益。不要用无依据的 0-100“综合分”冒充客观评价。
6. 识别失败模式和退出条件，例如 MILP 规模爆炸、时间序列泄漏、机理参数不可辨识、神经网络样本不足。
7. 给出推荐顺序：Baseline、首选、仅在特定条件下才值得尝试的备选，并说明触发条件。
8. 若问题结构已足够明确，不要继续在本 Skill 内展开算法细节，而是路由到最小必要的 algorithm Skill：
   - 线性/整数/0-1/资源分配 → `ALGO_LINEAR_INTEGER`
   - 连续非线性/非凸优化 → `ALGO_NONLINEAR_OPT`
   - 图、流、路径、TSP/VRP → `ALGO_NETWORK_ROUTING`
   - 时间序列预测 → `ALGO_TIME_SERIES`
   - 有标签回归/分类 → `ALGO_SUPERVISED_LEARNING`
   - 聚类/降维 → `ALGO_UNSUPERVISED_LEARNING`
   - 多指标评价/排序 → `ALGO_MULTI_CRITERIA`
   - ODE/状态空间 → `ALGO_ODE_DYNAMICS`
   - PDE/空间场 → `ALGO_PDE_DYNAMICS`
   - Monte Carlo/Markov/随机模拟 → `ALGO_STOCHASTIC_SIM`
   - 假设检验/参数推断 → `ALGO_STATISTICAL_INFERENCE`
   - 几何/碰撞/空间重建 → `ALGO_GEOMETRY`。
   混合题允许一个主 algorithm Skill + 一个必要的 secondary，不要一次加载整套算法库。

## Outputs

- 模型候选表
- Baseline/首选/备选及理由
- 每个候选的失败模式和验证方案
- 需要进一步比较时的公平比较协议草案

## Checks

- 至少有一个可运行 Baseline
- 候选模型与题面目标和数据结构有直接联系
- 没有把复杂度当创新性
- 没有承诺“全局最优/高精度”而无验证依据

## Failure

- 候选优劣需要数据跑分才能裁决：转 `MODELS_NEED_COMPARISON`
- 已选路线但数学合同未冻结：转 `MODEL_CONTRACT_MISSING`
- 模型都依赖高风险假设：返回 `ASSUMPTION_WEAK`

## Handoff

推荐下一事件优先是匹配的 `ALGO_*` 事件；若算法族已经确定且无需进一步展开，再转 `MODEL_CONTRACT_MISSING` 或 `MODELS_NEED_COMPARISON`。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
