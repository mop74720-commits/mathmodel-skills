---
name: network-routing
trigger: ALGO_NETWORK_ROUTING
description: 处理图论、最短路、最大流、匹配、TSP/VRP、运输网络和动态路由。
---

# network-routing

## Trigger

- 事件：`ALGO_NETWORK_ROUTING`。
- 通常由 `model-selection` 在识别问题结构后路由；用户直接点名该算法族时也可调用。
- 本 Skill 只决定该算法族内的技术路线，不决定比赛阶段、时间预算、是否冻结或提交。

## Scope

当实体可抽象为节点/边，目标依赖路径、流、连通性、匹配或路由时使用。先确认图语义，再选算法。

## Inputs

- 节点、边、方向性和权重定义
- 容量、需求、时间窗、车辆/资源限制
- 是否允许负权、回路、多路径或动态权重
- 目标：距离/成本/时间/风险/服务水平
- 网络规模与是否需要精确最优

## Procedure

1. 先定义图：有向/无向、单图/多层图、边权单位、容量和可达性。不要仅因为有“地点”就自动套最短路。
2. 按结构分流：非负单源最短路可用 Dijkstra；存在负权需 Bellman-Ford 等；全源路径、最大流/最小割、匹配分别选择对应算法。
3. 运输/路由若含车辆容量、时间窗、服务顺序或多仓库，明确是 TSP/VRP 的哪种变体；建立最简单可行 Baseline。
4. 精确 MILP 中显式处理 flow conservation、capacity、subtour elimination、time window；启发式中仍需用同一可行性检查器复核。
5. 检查网络预处理是否改变问题：道路距离与欧氏距离不能混用；不可达边不能用大常数伪造为正常边而不记录。
6. 动态路由要定义重规划时点和信息可见性，避免使用未来信息。
7. 输出路径后独立重算总成本、节点访问、容量、时间窗和守恒，必要时在小规模实例与精确解对照。

## Decision Rules

- “最短距离”与“最低费用”不是同一个边权；若运费分段或路径风险非线性，应先把真实成本映射到边/路径，再决定能否用 shortest path。
- 多商品流、车辆路由和普通最短路不可混为一类；节点访问一次、车辆容量、时间窗会把问题提升为组合优化。
- 动态网络中，边权更新的时间粒度必须与决策时点一致，防止使用事件发生后的信息优化事件发生前的路径。
- 若图很稠密但实际几何限制明显，可先做合法邻接生成，避免把“不可能走的边”交给 solver 再靠大罚值压制。

## Validation Design

1. 对路径结果逐边检查边是否存在、方向是否合法。
2. 独立累加距离/费用，核对 solver objective。
3. VRP/TSP 检查每个客户访问次数、车辆起终点、容量和时间窗。
4. 构造小网络与手工/枚举答案比较。
5. 对不可达节点、零容量、相同距离多最优等边界场景做测试，确认 tie-breaking 不影响论文主结论。

## Outputs

- 图语义合同
- 算法/模型族选择
- 可行性检查器定义
- 路径/流结果和独立重算
- 网络特有风险：不可达、子回路、容量、时间窗

## Checks

- 方向、权重、容量单位明确
- 负权时未错误使用 Dijkstra
- TSP/VRP 有子回路处理
- 每个流节点满足守恒或题面允许的源汇条件
- 动态算法无未来信息泄漏

## Failure

- 约束组合使 MILP 规模过大：转 `NEED_LOW_RISK_IMPROVEMENT` 寻找分解/启发式
- 路径结果违反容量/时间窗：转 `SOLVER_FAILED` 或实现审查
- 几何边界而非网络拓扑是核心：转 `ALGO_GEOMETRY`

## Handoff

建模路线确定后转 `MODEL_CONTRACT_MISSING`；实现后常接 `FINAL_RESULT_NEEDS_REVIEW`。

统一回执：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。算法 Skill 可以建议下一事件，但不能替 Coach 做阶段或资源决策。
