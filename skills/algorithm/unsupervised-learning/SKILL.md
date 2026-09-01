---
name: unsupervised-learning
trigger: ALGO_UNSUPERVISED_LEARNING
description: 处理聚类、降维、异常结构发现与无标签模式提取。
---

# unsupervised-learning

## Trigger

- 事件：`ALGO_UNSUPERVISED_LEARNING`。
- 通常由 `model-selection` 在识别问题结构后路由；用户直接点名该算法族时也可调用。
- 本 Skill 只决定该算法族内的技术路线，不决定比赛阶段、时间预算、是否冻结或提交。

## Scope

当没有可靠标签，需要发现群组、低维结构或异常模式时使用。聚类不是自动“分群”，必须验证稳定性和业务/题意可解释性。

## Inputs

- 特征定义、单位与尺度
- 样本量与维度
- 是否存在混合类型变量
- 希望得到的结构：簇/嵌入/异常
- 后续用途和可解释性需求

## Procedure

1. 先明确无监督任务的用途：压缩、可视化、分群还是异常检测。若只是为了后续监督模型，不要把聚类结果包装成独立科学结论。
2. 检查尺度、偏态、离群点和类别变量编码。距离型方法前必须确认距离度量有意义。
3. 建立简单 Baseline，如标准化后的 k-means/PCA，并根据形状、密度、概率结构考虑 hierarchical、DBSCAN、GMM 等。
4. 聚类数不得只靠单一 elbow。结合 silhouette、稳定性重采样、信息准则和实际解释；DBSCAN 等密度法检查参数敏感性。
5. PCA/降维报告方差解释和载荷；t-SNE/UMAP 等主要用于可视化时，不把二维距离当原空间定量证据。
6. 做稳定性测试：重采样、初始化、尺度方案变化后簇是否保持；给出簇映射或一致性度量。
7. 最终解释每个簇的差异需回到原始变量，不只展示彩色散点。

## Decision Rules

- k-means 默认欧氏球状簇；如果簇形状非凸、密度差异大或噪声多，应考虑层次/密度/概率模型。
- 聚类数是模型选择问题，不是论文必须给出的固定整数；如果证据显示无清晰簇结构，应允许结论为“数据呈连续谱”。
- 降维用于解释时优先可解释线性方法；用于可视化时可用非线性嵌入，但限制其定量解释。
- 聚类前标准化是否合理取决于单位与语义；某些物理量本来就应有更大权重，不能机械 z-score。

## Validation Design

1. 对不同 seed/重采样重复聚类并做簇对齐。
2. 比较不同合理尺度处理后的结构。
3. 对 cluster profile 回到原始特征统计，不只看嵌入图。
4. 检查极少数离群点是否决定整个分群。
5. 若簇将用于后续决策，验证不同聚类方案是否改变最终决策，而不是只优化 silhouette。

## Outputs

- 距离/尺度/编码合同
- Baseline 与候选方法
- 簇数或降维维数选择证据
- 稳定性结果
- 原始变量层面的结构解释

## Checks

- 距离度量与变量类型相容
- 聚类不依赖单次初始化
- 二维嵌入未被误当因果或真实几何距离
- 簇标签有原变量解释
- 异常点处理有记录

## Failure

- 簇结构不稳定：不要强行分群，返回 `RESULT_UNSTABLE`
- 其实存在明确标签：转 `ALGO_SUPERVISED_LEARNING`
- 问题本质为多指标排序而非聚类：转 `ALGO_MULTI_CRITERIA`

## Handoff

需要结果解释转 `RESULT_NEEDS_INTERPRETATION`；需要比较算法转 `MODELS_NEED_COMPARISON`。

统一回执：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。算法 Skill 可以建议下一事件，但不能替 Coach 做阶段或资源决策。
