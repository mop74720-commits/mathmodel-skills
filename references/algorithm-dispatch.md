# Algorithm Dispatch Contract

`model-selection` 负责判断模型族；必要时先用 `DOMAIN_CONTEXT_NEEDED` 补领域机制；`skills/algorithm/*` 负责该族内部的算法选择和验证设计。当前共 **21 个算法族入口**；具体算法名优先通过 `references/algorithm-depth-selection.md` 与 `references/algorithm-playbooks/*` 渐进加载。

标准链：

```text
MODEL_UNCERTAIN
  -> model-selection
  -> [DOMAIN_CONTEXT_NEEDED if needed]
  -> ALGO_* (one primary)
  -> [one depth playbook if evidence requires]
  -> MODEL_CONTRACT_MISSING
  -> IMPLEMENT_MODEL
```

这不是固定 stage workflow。若用户已经明确算法族，可以直接从 `ALGO_*` 开始；若 model contract 已冻结，也可以跳过算法层。

算法 Skill 不得：
- 决定比赛优先级或剩余时间分配；
- 强制固定模型数量、图数量、扰动比例；
- 因为没有独立 reviewer 就宣布整场 BLOCKED；
- 通过更改题意或假设来让算法“更好跑”；
- 把 XGBoost、Prophet、NSGA-II、VIKOR、GA/PSO 等具体方法名无条件升级成一级路由。

算法 Skill 必须：
- 至少给出一个 baseline 或可校准参照；
- 说明适用条件和失败模式；
- 设计能区分“模型错/实现错/数值错”的检查；
- 把约束、seed、split、步长、权重、prior、采样率等影响结论的参数纳入可追溯输出；
- 复杂方法只有在 baseline 暴露了结构性缺口后升级，并写出 deciding evidence / failure condition / fallback。
