---
name: linear-integer-optimization
trigger: ALGO_LINEAR_INTEGER
description: 处理线性规划、整数规划、混合整数规划、0-1决策、资源分配、选址与离散调度。
---

# linear-integer-optimization

## Trigger

- 事件：`ALGO_LINEAR_INTEGER`。
- 通常由 `model-selection` 在识别问题结构后路由；用户直接点名该算法族时也可调用。
- 本 Skill 只决定该算法族内的技术路线，不决定比赛阶段、时间预算、是否冻结或提交。

## Scope

当目标函数和主要约束可线性表达，且存在连续/整数/二元决策时，用本 Skill 选择 LP/MILP 建模与求解策略。它不负责比赛优先级，也不以“用了整数规划”本身作为创新。

## Inputs

- 已冻结或接近冻结的 model contract
- 决策变量类型、目标函数、全部约束和单位
- 规模信息：变量/约束数量、离散维度、稀疏性
- 是否存在逻辑条件、固定成本、容量、时间窗等结构
- 可用求解器与时间/内存约束

## Procedure

1. 把自然语言约束逐条翻译成变量域、线性等式/不等式，并单独列出二元逻辑。先检查 maximize/minimize 符号、上下界和 Big-M 的方向。
2. 判断是否可用纯 LP。若整数性只来自最终展示或可安全舍入，不要过早升级 MILP；若整数性影响可行性，则必须显式保留。
3. 对逻辑条件优先使用 indicator constraint、SOS 或紧的线性化；只有确有必要时使用 Big-M，并从题面边界推导尽可能紧的 M，记录来源。
4. 建立可解释的 LP/MILP Baseline。对大规模组合问题，再考虑分解、列生成、拉格朗日松弛、局部搜索或启发式作为求解层改进，而不是改掉原优化目标。
5. 运行可行性预检：变量界是否冲突、容量是否足够、流量/需求是否守恒、固定成本与启用变量是否绑定。必要时先求 feasibility model 或最小约束冲突集。
6. 求解后必须独立回代所有关键约束，并报告最大违反量、整数性误差、objective 重算值和 solver gap；solver 的 success/status 不能替代回代。
7. 若使用启发式或近似算法，保留 MILP 小规模实例作为校准基准；声明“当前最好可得解”而非无证据的全局最优。

## Decision Rules

- 若 LP relaxation 已经给出整数解，优先保留更简单的 formulation，不为了“整数规划感”人为增加二元变量。
- 若逻辑约束可由网络结构/全酉矩阵自然保证整数性，应利用结构而不是额外 Big-M。
- 若 MIP gap 长时间不降，先区分“找到可行解困难”还是“证明下界困难”：前者需要改善初始可行解/模型结构，后者可考虑更紧 formulation、cuts 或分解。
- 固定成本、启用变量、最小批量等常见逻辑应检查正反两个方向，避免只写 `x <= My` 却漏掉必要的下界或业务条件。

## Validation Design

1. 构造一个手工可枚举的小实例，确认 objective 和约束方向。
2. 对最终解运行独立 checker，而不是复用建模表达式同一段代码，以降低“同错同验”风险。
3. 若求解器给出最优证书，记录 gap、bound、停止原因；若因时间限制终止，区分 incumbent objective 与 best bound。
4. 对关键整数边界做 ±1 的邻域检查，判断结果是否由单个脆弱阈值驱动。
5. 对成本/容量参数做离散敏感性时，每次都重新求整数模型，不对整数解直接做连续导数解释。

## Outputs

- 变量—约束—目标的规范化模型表
- LP/MILP/近似求解路线选择及理由
- 线性化或 Big-M 推导记录
- 求解后约束回代与 objective 重算结果
- 规模/求解风险及必要的 fallback

## Checks

- 每个离散决策都对应明确变量域
- Big-M 或线性化有可解释上界，不用任意超大常数
- 最大化/最小化符号与 solver 接口一致
- 整数舍入不会破坏可行性；若会，禁止事后硬舍入
- 报告 gap 时说明其定义与停止条件

## Failure

- 模型 infeasible：转 `SOLVER_FAILED`，优先定位约束冲突
- 线性表达失真或关键关系本质非线性：转 `ALGO_NONLINEAR_OPT` 或回到 `MODEL_UNCERTAIN`
- 多个 formulation 都可行但性能差异需实测：转 `MODELS_NEED_COMPARISON`

## Handoff

模型结构确定后通常转 `MODEL_CONTRACT_MISSING`；实现阶段转 `IMPLEMENT_MODEL`。

统一回执：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。算法 Skill 可以建议下一事件，但不能替 Coach 做阶段或资源决策。
