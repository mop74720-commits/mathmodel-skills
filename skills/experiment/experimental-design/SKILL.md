---
name: experimental-design
trigger: EXPERIMENT_DESIGN_NEEDED
description: 为物理、仿真或数据实验设计最小但可判别的随机化、重复、区组、因子筛选与响应面方案，控制混杂并绑定确认性决策规则。
---

# experimental-design

## Trigger

- 事件：`EXPERIMENT_DESIGN_NEEDED`。
- 当需要决定“实验/仿真该怎么安排才能回答问题”，而不是仅仅记录已经跑过的实验时调用。
- 用户明确要求 DOE、factorial design、blocking、replication、randomization、response surface、power/sample-size 或多因素交互实验时可直接调用。

## Scope

本 Skill 负责局部实验设计，不承担比赛时间线和全局资源调度。覆盖物理实验、计算实验/仿真、模型对比实验与数据采集设计。重点是让每次运行都能区分主要效应、交互、随机误差和混杂，而不是机械增加实验数量。

它与 `experiment-manager` 的边界：本 Skill 决定**怎么设计实验**；`experiment-manager` 负责**怎么登记、追踪和冻结实验身份**。

## Inputs

- 当前 question / hypothesis / decision
- response / primary metric 与允许的 secondary metrics
- 可控 factors、候选 levels/ranges
- nuisance variables / blocking variables
- 物理、预算、伦理、软件或求解器约束
- 预期效应量/噪声信息（若有）
- 可并行度、重复成本和失败成本
- 已有 pilot / baseline 结果

## Procedure

1. **定义决策性问题**：先写清本实验要区分哪两个或多个解释/模型，primary response 是什么，什么结果会改变下一步。没有 decision role 的实验不应优先占用预算。
2. **划分变量角色**：将变量分成 controlled factor、nuisance/blocking factor、response、covariate、不可控随机源。防止把数据生成后的结果变量当作实验因子。
3. **建立简单 Baseline 设计**：单因素试验可用于初步单调性/尺度探索，但若怀疑交互，不能把 OFAT 当最终设计。
4. **选择设计族**：
   - 因子少且预算允许：full factorial。
   - 因子多、先筛主要因素：fractional factorial / screening design，并记录 alias/confounding。
   - 已找到关键连续因素且需要局部优化：response surface / central composite / Box-Behnken 等候选。
   - 高成本仿真或实验：使用 space-filling / sequential design；只有明确收益时再引入 surrogate/adaptive 方案。
5. **随机化、重复与区组**：
   - 可随机化的运行顺序默认随机化；
   - 对批次、机器、日期、场地、初始状态等系统差异做 blocking；
   - replication 用于估计随机误差，而不是把同一 deterministic run 复制多次冒充独立样本。
6. **样本量/重复数**：优先根据目标精度、最小有意义效应和噪声估计做 power/precision 设计；复杂或非标准统计量可用 simulation-based power。未知噪声时先小 pilot 再更新。
7. **随机仿真实验**：显式记录 seed；模型 A/B 比较时在适用情况下使用 paired seeds / common random numbers 减小比较方差，同时避免把共享随机数误当独立重复。
8. **冻结 confirmatory contract**：确认性实验开始前冻结 primary metric、factor ranges、run count/stop rule、失败定义、排除规则和分析方法。探索性调参必须与确认性证据分开。
9. **预设失败和回退**：传感器饱和、求解失败、运行超时、模型不可识别、交互过强、随机误差过大等都要有处理规则，不在看完结果后临时挑“最好看”的子集。

## Decision Rules

- 只验证单个参数的局部敏感性，优先 `NEED_SENSITIVITY`，不必启用完整 DOE。
- 需要估计真实干预的因果效应时，与 `ALGO_CAUSAL_INFERENCE` 组合；随机化设计优先于事后统计修补。
- 多个模型公平比较但因子结构不复杂时，可直接 `MODELS_NEED_COMPARISON`，不强行上 factorial/RSM。
- 因子数量远大于预算时先 screening，不要直接做高阶响应面。
- 对 deterministic solver，重复相同输入不会增加统计信息；应扰动有科学含义的场景/初值/数值设置。
- 任何固定“至少 N 次”“固定 ±10%”都不是通用规则；范围和重复数必须来自题目尺度、噪声、计算成本或官方约束。

## Validation Design

1. 检查 randomization/blocking 是否实际执行，运行顺序与批次效应是否可追溯。
2. 对 factorial/screening 设计检查 rank、alias 与可估计效应，避免把混杂项单独解释。
3. 用 replicate/pilot 估计 pure error 或运行波动；报告置信区间/预测区间，而非只报均值。
4. 检查残差、异方差、非线性和强交互；必要时变换 response 或升级响应面/非线性模型。
5. confirmatory 结果按预先冻结的 primary metric 和规则判读；探索性发现标记为 hypothesis-generating。
6. 高成本 sequential design 记录每轮 acquisition/选择依据，防止事后只保留成功轨迹。
7. 关键结论需在独立重复、holdout 场景或额外确认点上复核。

## Outputs

- Experimental Design Contract
- factors / levels / ranges / blocks / randomization
- run matrix 或生成规则
- replication / sample-size rationale
- primary metric / analysis plan
- exploratory vs confirmatory 标记
- stop/failure/exclusion rules
- expected information gain / deciding evidence
- handoff 给 experiment-manager 的运行登记字段

## Checks

- 每个实验都有明确 question、response 和 decision role
- 因子、协变量、干扰变量角色没有混淆
- 随机化/重复/区组有明确理由
- 设计能估计想解释的主要效应或交互
- 没有在看结果后偷偷修改 primary metric/停止规则
- 随机实验的 seed、重复和比较配对方式可追溯
- 实验数量不是由任意固定阈值决定

## Failure

- 关键 factor/range 没有物理或领域依据：转 `DOMAIN_CONTEXT_NEEDED` / `ASSUMPTION_WEAK`。
- 设计矩阵无法区分关键效应：返回 `MODEL_UNCERTAIN` 并简化因素或增加信息量更高的运行。
- pilot 显示噪声远大于可检测效应：重新估算 power/precision，必要时降级目标。
- 需要估计因果效应但处理分配/对照定义不清：转 `ALGO_CAUSAL_INFERENCE`。
- 设计已确定但实验身份/结果追踪混乱：转 `EXPERIMENTS_UNTRACKED`。

## Handoff

设计冻结后转 `EXPERIMENTS_UNTRACKED` / `experiment-manager` 建立运行身份并执行；参数局部扰动转 `NEED_SENSITIVITY`；多场景稳定性转 `RESULT_UNSTABLE`；真实处理效应估计转 `ALGO_CAUSAL_INFERENCE`；实验需要代码实现转 `IMPLEMENT_MODEL`。

统一回执：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。本 Skill 只负责实验设计，不替 Coach 决定全局比赛资源和截止时间。
