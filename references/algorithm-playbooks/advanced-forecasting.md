# Advanced Forecasting Playbook — Prophet / Boosting / Ensemble

用于 `time-series` 已建立 chronological baseline 后，评估 Prophet、tree boosting 与模型融合是否有真实增益。复杂模型必须在 rolling/expanding validation 中证明价值。

## 1. Prophet 类趋势—季节模型

适合趋势可分段、季节性明确、节假日/事件有解释且时间序列长度足以识别这些成分的业务序列。

- changepoint flexibility 必须通过留后验证选择；过多变点会追随噪声。
- seasonality period 必须有时间语义，不能只因频谱有峰就自动加入。
- holiday/event regressors 只能使用预测时点可知的信息。
- 与 seasonal-naive、ETS/ARIMA 类简单模型公平比较。

## 2. Boosting Forecasting

XGBoost/LightGBM 等本质是监督学习器，需要显式构造 lag、rolling statistics、calendar/exogenous features。

1. 每个特征检查在预测时点是否可获得，严格防 target leakage。
2. rolling mean/std 等只能使用过去窗口；不能先对全序列计算后再切分。
3. 用 expanding/rolling origin 重训或模拟真实部署流程。
4. 调参只能在训练/验证历史窗口内进行；最终测试窗口不可参与 feature/parameter 选择。
5. 解释特征重要性时不写成因果。

## 3. Ensemble / Stacking

- 简单平均/加权平均先于复杂 stacking，只有误差互补证据存在时才融合。
- 权重必须从验证窗口估计，不能按测试集表现反向调权。
- Stacking 的 meta-learner 训练必须使用 out-of-fold / rolling out-of-sample predictions，禁止用 base learner 的训练内预测。
- 模型高度相关时，融合可能只增加复杂度；报告单模型与 ensemble 的增益及稳定性。

## 4. 评价协议

- 至少保留 naive / seasonal-naive baseline。
- 按 horizon 分层报告 MAE/RMSE/MAPE 或任务真正关心的损失；零值/小值时谨慎使用 MAPE。
- 需要区间时检查 empirical coverage 和 interval width，不只画阴影。
- 结构突变前后分别观察误差，避免平均指标掩盖失效期。
- 若预测用于下游优化，把预测误差/区间传播到决策，检查更复杂预测是否真的改变决策质量。

## 5. 失效条件

- Prophet/boosting/ensemble 不稳定或不优于简单 baseline：删除复杂层。
- 外生变量未来不可获得：不得用于真正预测。
- 数据量不足以支持大量 lag/seasonal/interaction 特征：简化模型。
- 只提升训练拟合而 rolling validation 无提升：判为过拟合。

论文不应以“用了 XGBoost/Prophet/Stacking”为贡献；应报告为什么结构适配、相对 baseline 的 out-of-sample 增益、误差边界和实际决策价值。
