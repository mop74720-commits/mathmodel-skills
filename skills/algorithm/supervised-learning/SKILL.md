---
name: supervised-learning
trigger: ALGO_SUPERVISED_LEARNING
description: 处理回归、分类、排序及结构化数据的监督学习模型选择与验证。
---

# supervised-learning

## Trigger

- 事件：`ALGO_SUPERVISED_LEARNING`。
- 通常由 `model-selection` 在识别问题结构后路由；用户直接点名该算法族时也可调用。
- 本 Skill 只决定该算法族内的技术路线，不决定比赛阶段、时间预算、是否冻结或提交。

## Scope

当存在明确标签/响应变量并希望预测或解释时使用。重点是泄漏、数据切分、校准和解释，而非追求模型堆砌。

## Inputs

- X/y 定义与数据来源
- 样本量、特征数、类别比例
- 分组/时间/个体重复结构
- 评价指标和业务代价
- 解释性与部署约束

## Procedure

1. 先确定任务是回归、二分类、多分类、序数或排序；建立简单 Baseline（均值/多数类/线性或 logistic）。
2. 识别泄漏边界：同一主体重复记录应 group split，时间数据应 time split，任何目标后验特征必须排除。
3. 按规模和结构选择少数候选：线性/正则化、树模型、SVM、boosting 等；复杂深度模型仅在数据量和结构真正支持时考虑。
4. 所有预处理放入训练 pipeline，交叉验证中每折独立 fit；特征选择同样不能先看全数据。
5. 分类除 accuracy 外根据不平衡程度检查 precision/recall/F1/PR-AUC/ROC-AUC，并在概率决策时检查 calibration；回归检查误差分布和异方差。
6. 使用 repeated CV/分层或分组 CV（按问题结构）估计不确定性；测试集只做最终一次评估。
7. 解释时区分预测相关性与因果关系；特征重要性需说明方法及其偏差，避免把 SHAP 等解释工具写成因果证明。

## Decision Rules

- 样本量相对特征数较小时，优先正则化与低复杂度模型；不要把特征数多误认为“适合深度学习”。
- 类别极不平衡时，先根据决策代价定义阈值和指标，再决定重采样/类权重；不要仅为平衡数据而改变真实先验。
- 存在主体重复、医院/学校/设备分组时，split 必须在主体/组层面进行，否则验证会严重乐观。
- 若目标是解释变量影响而非预测，统计模型和不确定性可能比纯预测模型更合适。

## Validation Design

1. 把完整 pipeline 放进 CV：缺失处理、编码、标准化、特征选择和模型都只在训练折 fit。
2. 报告 fold 分布而不仅是平均分。
3. 分类概率模型检查 reliability/calibration；阈值根据验证集或代价函数决定。
4. 对高性能模型做简单模型对照，判断增益是否值得复杂度。
5. 对关键特征做 permutation/ablation，检查模型是否依赖可疑代理变量或泄漏字段。

## Outputs

- 切分与防泄漏合同
- Baseline + 少数候选
- 交叉验证与指标设计
- 最终泛化结果及不确定性
- 解释性与限制说明

## Checks

- 切分单位与真实使用场景一致
- 预处理只在训练折 fit
- 类别不平衡时未只看 accuracy
- 测试集未用于调参
- 解释不越界为因果结论

## Failure

- 样本太小/高维导致方差过大：考虑正则化、降维或统计模型
- 标签质量差：返回 `DATA_UNKNOWN` 或假设审查
- 性能对 split 高度敏感：转 `RESULT_UNSTABLE`

## Handoff

候选比较转 `MODELS_NEED_COMPARISON`；结果稳定后转 `RESULT_NEEDS_INTERPRETATION`。

统一回执：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。算法 Skill 可以建议下一事件，但不能替 Coach 做阶段或资源决策。
