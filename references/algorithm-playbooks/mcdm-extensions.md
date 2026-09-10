# MCDM Extensions Playbook — VIKOR / GRA

用于 `multi-criteria-evaluation` 已确认任务确实是多指标评价后，按结构选择 VIKOR 或 Grey Relational Analysis。它们不是默认比 TOPSIS“更高级”的替代品。

## 1. VIKOR

VIKOR 适合需要在群体效用与最差指标遗憾之间做 compromise ranking 的场景。

1. 明确正/负向指标、归一化和权重来源。
2. 计算各指标 best/worst reference，再得到 group utility `S_i` 与 individual regret `R_i`。
3. compromise 指标 `Q_i` 中参数 `v` 表示群体效用相对个体遗憾的偏好，不应机械固定后不解释。
4. 检查 acceptable advantage / stability 条件；若不满足，应允许给出 compromise set，而不是强行唯一第一名。
5. 对 `v`、权重、归一化和极端值做 rank sensitivity。

## 2. Grey Relational Analysis

GRA 适合比较多个方案/序列与参考序列的形态接近程度，尤其在样本有限、尺度不同但趋势关系重要时作为评价工具。

1. 参考序列必须有语义依据，不应直接选“所有指标最大值”而无解释。
2. 归一化方式与指标方向保持一致。
3. 计算差异序列、全局最小/最大差异与 grey relational coefficient。
4. distinguishing coefficient `rho` 是方法参数，默认值只能作为起点，关键排序需做敏感性。
5. 聚合 relational grade 时权重来源与其他 MCDM 一样需要审计。

## 3. 与 TOPSIS / AHP 的边界

- 距离理想点是核心：TOPSIS 更自然。
- 层级主观判断和专家偏好是核心：AHP 可用于权重，但必须做一致性和敏感性。
- 强调最大遗憾与折中：VIKOR 更合适。
- 强调参考序列形态接近：GRA 更合适。

## 4. 共同验证

- 指标方向、归一化、权重 provenance 完整。
- 删去/加入一个指标、改变合理权重后排名是否稳定。
- 检查 top alternatives 的实际分差，不把 0.001 的排序差异包装成显著优劣。
- 至少与等权或简单综合分 Baseline 对照。
- 若不同 MCDM 方法给出不同第一名，应报告模型依赖，而不是挑符合预期的一种。

输出应包含方法选择理由、参数/权重、排序、近邻方案差距、敏感性和结论稳定区。
