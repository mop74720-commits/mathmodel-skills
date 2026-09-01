# Classification Baseline Playbook

候选算法的目的不是“多试几个模型”，而是建立机制互补、可公平验证的少量 baseline。

| Model | Useful when | Main risks / checks |
|---|---|---|
| Logistic regression | 需要透明线性概率基线、样本相对较少 | 标准化、共线性、正则化、阈值与校准 |
| Decision tree | 需要可解释非线性规则 | 深度/叶样本控制，防止高方差 |
| KNN | 局部相似性有意义、维度不高 | 必须尺度处理；高维距离失效；推理成本 |
| Naive Bayes | 特征生成机制近似条件独立或文本/计数特征 | 独立性假设与概率校准 |
| SVM | 中小样本、边界复杂 | 特征尺度、核/超参、概率输出并非天然校准 |
| Random forest / boosting | 表格数据非线性与交互明显 | 调参泄漏、类别不平衡、解释边界 |

所有模型共用同一 split、预处理 pipeline、评价指标和测试集；时间/组结构优先决定切分方式。测试集不参与模型选择。类别不平衡时根据决策代价选择 PR/recall/precision/F1/AUC/阈值，而不是只看 accuracy。
