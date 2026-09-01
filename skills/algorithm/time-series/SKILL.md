---
name: time-series
trigger: ALGO_TIME_SERIES
description: 处理时间序列预测、趋势季节性、滚动预测、时序回归与不确定性区间。
---

# time-series

## Trigger

- 事件：`ALGO_TIME_SERIES`。
- 通常由 `model-selection` 在识别问题结构后路由；用户直接点名该算法族时也可调用。
- 本 Skill 只决定该算法族内的技术路线，不决定比赛阶段、时间预算、是否冻结或提交。

## Scope

用于数据按时间有序且目标是预测未来、估计趋势或描述动态依赖。核心原则是时间顺序不可被随机切分破坏。

## Inputs

- 时间索引、采样频率、缺失/不规则间隔
- 预测 horizon 与评价时点
- 目标变量及可用外生变量
- 历史长度、季节周期候选
- 是否需要区间预测

## Procedure

1. 先画时间轴并核对频率、缺口、异常和结构突变。明确预测时点真正可获得哪些特征。
2. 建立 naive、last value、seasonal naive 等时间序列 Baseline；复杂模型必须在同一滚动评估口径下超过 Baseline。
3. 按数据特征考虑 ETS/ARIMA/状态空间、回归+滞后、树模型或深度时序模型；样本较短时优先低自由度模型。
4. 训练/验证/测试按时间切分，调参使用 rolling/expanding window；任何 scaler、插值规则和特征工程只从训练可见信息拟合。
5. 检查平稳性、季节性、残差自相关和结构突变，但不要把统计检验当机械前置门槛；根据模型假设解释其意义。
6. 评价同时报告与 horizon 对应的 MAE/RMSE/MAPE 或业务指标；含零值时谨慎使用 MAPE。
7. 若需要区间，使用模型原生区间、bootstrap 或 conformal 等可验证方法，并检查覆盖率而非只展示带状图。

## Decision Rules

- 若预测 horizon 很短且序列强惯性，naive baseline 往往很强；复杂模型必须证明增益而不是只展示拟合曲线。
- 多变量时序的外生特征必须在预测时点可获得；未来天气预报与未来真实天气是两种不同信息条件。
- 高频数据中的强周期可先通过季节 naive/傅里叶项处理，不必直接上深度网络。
- 结构突变明显时，应考虑分段、状态切换或最近窗口，不把全部历史一视同仁。

## Validation Design

1. 采用能覆盖多个预测起点的 rolling-origin evaluation；窗口数量由数据长度和结论稳定性决定，避免单次切分偶然性。
2. 按 horizon 分层报告误差，避免平均指标掩盖远期崩溃。
3. 检查残差随时间、季节、预测值大小是否有系统模式。
4. 比较 naive/seasonal naive，若复杂模型没有稳定超过，应优先保留简单模型。
5. 区间预测检查经验覆盖率与平均宽度，过宽区间即使覆盖高也不代表实用。

## Outputs

- 时间切分与信息可见性合同
- Baseline 与候选时序模型
- 滚动验证方案
- 点预测与必要的区间预测
- 残差/稳定性诊断

## Checks

- 没有随机打乱未来样本
- 标准化/插值无未来泄漏
- Baseline 同口径比较
- 预测 horizon 与评价窗口一致
- 区间预测有覆盖率或校准证据

## Failure

- 结构突变导致历史规律失效：转 `RESULT_UNSTABLE` 或场景建模
- 特征高度外生且未来不可知：回到问题合同重新界定预测可用信息
- 样本太少无法支持复杂模型：降级到低复杂度/贝叶斯/灰色类候选并说明限制

## Handoff

候选需比较时转 `MODELS_NEED_COMPARISON`；路线确定后转 `MODEL_CONTRACT_MISSING`。

统一回执：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。算法 Skill 可以建议下一事件，但不能替 Coach 做阶段或资源决策。
