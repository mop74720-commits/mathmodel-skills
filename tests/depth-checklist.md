# Depth checklist

人工抽查重点：

1. `model-selection` 能输出 Baseline + 主候选 + 条件备选，而不是算法堆砌。
2. `solver-debug` 明确区分模型/实现/数值/solver 配置根因。
3. `numerical-check` 包含离散/容差收敛、结构残差与随机误差。
4. `sensitivity` 不使用固定 ±10% 作为硬规则，离散参数不会套微分敏感度。
5. `robustness` 检查最终决策稳定性与失效边界。
6. `claim-evidence` 的摘要数字必须回到 Final Run。
7. `paper-review` 不使用虚构总评分作为审稿结论。
8. `final-review` 明确当届官方规则优先，并实际审最终渲染。
9. 所有 Skill 只能推荐事件，不得改变比赛 stage/priority。
