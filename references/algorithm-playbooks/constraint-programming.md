# Constraint Programming Playbook

Constraint Programming / CP-SAT 适合逻辑组合、排程、资源冲突、all-different、可选区间等离散约束高度结构化的问题。它与 MILP 有重叠，但建模原语和求解机制不同。

## 1. 何时优先考虑

- 大量逻辑条件、互斥/先后关系、interval scheduling、NoOverlap、cumulative resource。
- 决策主要是整数/布尔，目标相对简单，但可行性结构复杂。
- Big-M 线性化导致弱松弛、巨大 M 或模型难维护。

若目标/约束天然线性、LP relaxation 很强且规模可控，MILP 仍是首选 Baseline。

## 2. 建模规则

1. 明确整数尺度。CP-SAT 以整数为核心，连续量离散化时必须记录尺度与误差。
2. 优先使用原生 global constraints：AllDifferent、NoOverlap、Cumulative、Element、Circuit 等；不要把它们手工展开成大量脆弱 pairwise 约束。
3. 可选任务使用 presence literal / optional interval；逻辑蕴含保持双向业务语义，避免只编码一个方向。
4. 调度问题明确 start/end/duration、资源容量、precedence 与 calendar；单位必须统一。
5. 搜索参数、时间限制和随机 seed 可记录，但不要靠调参替代模型修正。

## 3. 与 MILP 的公平比较

- 使用同一问题合同和可行性 checker。
- 报告求解时间、best objective、best bound/gap（若后端提供）、首次可行解时间。
- CP-SAT 找到 feasible 不代表最优；达到时间上限时区分 FEASIBLE 与 OPTIMAL。
- 对小实例做枚举或 MILP 精确交叉验证。

## 4. 常见失败

- 把实数成本粗暴乘常数取整，导致目标排序改变。
- 时间单位过细造成域巨大；过粗又损失可行方案。
- 只写 pairwise 不冲突，漏掉资源总容量。
- 通过巨量 reified constraints 模拟本来有 global constraint 的结构。

## 5. 回退

若存在关键连续非线性变量，评估 decomposition、hybrid CP/MIP 或回到相应优化 Skill；不要把所有连续问题强行离散成 CP。
