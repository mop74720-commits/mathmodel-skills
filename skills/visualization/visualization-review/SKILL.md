---
name: visualization-review
trigger: FIGURE_WEAK
description: 从证据表达和实际出版尺寸审查图表：可读性、统计口径、尺度、颜色、冗余和误导风险。
---

# visualization-review

## Trigger

- 事件：`FIGURE_WEAK`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

既看“好不好看”，更看“图有没有正确表达结论”。默认审查最终候选图，不要求所有探索图都达到出版质量。

## Inputs

- 实际图文件（优先 PNG/PDF/SVG 渲染）
- Figure Contract 或预期 claim
- 正文预计尺寸
- 数据/统计口径说明

## Procedure

1. 在论文预计物理尺寸下查看实际渲染，不只看大屏放大图；检查字体、线宽、标记和图例。
2. 核对 claim：读者只看图+图注能否得到正确结论；图是否暗示了数据并不支持的因果、趋势或显著性。
3. 检查尺度和统计：轴范围、对数轴、双轴、归一化、误差条、箱线定义、样本量、排序是否会误导。
4. 检查视觉层级：主数据是否突出，网格/装饰/阴影是否抢占注意力，多面板是否有明确主次。
5. 检查灰度和常见色觉缺陷下的可区分性；只有颜色不同但线型相同的关键曲线要修。
6. 检查裁切、遮挡、文字溢出、分辨率/矢量文本和中文/数学字体。
7. 检查与全文的一致性：同一变量颜色、名称、单位和小数精度是否在多图中漂移。

## Outputs

- 按 P0/P1/P2 分类的图表问题
- 需要重画的最小修改清单
- 可保留/应删的重复图建议

## Checks

- 实际打开并检查最终图
- 统计口径与数据一致
- 没有只凭美学评分
- 主结论在灰度/小尺寸下仍清楚

## Failure

- 图的数据本身有问题：转 `RESULT_NEEDS_INTERPRETATION`/`NUMERICAL_SUSPECT`
- 图缺证据：转 `CLAIM_UNSUPPORTED`
- 只是需要新图：转 `FIGURE_NEEDED`

## Handoff

返回审查结果；是否替换正文图由 writing/Coach 决定。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
