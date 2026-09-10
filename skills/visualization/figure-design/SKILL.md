---
name: figure-design
trigger: FIGURE_NEEDED
description: 围绕一个明确主张选择最小充分图型、统计口径和版面结构，让图成为证据而不是装饰。
---

# figure-design

## Trigger

- 事件：`FIGURE_NEEDED`。
- 用户明确点名本能力时也可直接调用。
- 本 Skill 只解决局部问题；比赛阶段、时间预算、是否放弃某题仍由 Coach 决定。

## Scope

本 Skill 设计图的语义与数据契约，不以“至少几张图”为目标。每张图必须能回答一个读者问题。

## Inputs

- 要支持的 claim
- 数据字段及单位
- 目标论文尺寸/媒介
- 已有图或视觉约束（如有）

## Procedure

1. 先写一句图要证明/展示的 claim；如果一句话说不清，先拆 claim 而不是堆多面板。
2. 识别变量结构和**证据任务**（分布、比较、关系、趋势、构成、不确定性、性能、空间/网络等）。按需读取 `references/figure-guides/selection-and-evidence.md`；同一批数据因 claim 不同可以选择不同图型。
3. 检查样本支持、配对/重复测量、过度平滑、过度聚合等风险；样本弱时优先暴露原始点，而不是机械套箱线/KDE。
4. 确定统计口径：均值/中位数、置信区间/分位数、样本量、归一化、基准线、误差定义；图中数值必须由代码计算。
5. 设计主次层级：主结论放最显眼位置，辅助面板只在能解释机制时加入；不要把不同重要性的面板机械等分。
6. 定义坐标轴单位、范围、零点、对数尺度和排序规则；截断坐标必须有合理理由并避免夸大差异。
7. 规划颜色/线型/标记使彩色、灰度、常见色觉缺陷下仍可区分；尽量避免仅靠颜色编码。
8. 写出图注必须包含的最少信息：对象、场景、统计口径、误差条含义、关键参数。

## Deep references

- `references/figure-guides/selection-and-evidence.md`：claim × 变量结构 × 样本支持选图。
- `references/figure-guides/encoding-and-layout.md`：视觉通道、轴、区间、多面板与导出。
- `references/figure-guides/pitfalls-and-review.md`：统计/视觉误导与最终尺寸攻击清单。

## Outputs

- Figure Contract：claim、数据、图型、统计口径、轴/单位、图注要求
- 必要时的多面板布局草图
- 若合同已足够执行，handoff 推荐 `FIGURE_RENDER_NEEDED`

## Checks

- 图型与数据类型匹配
- 一个图有一个主结论
- 误差条/区间定义明确
- 坐标尺度不误导
- 没有为满足数量而生成重复图

## Failure

- 无法用现有数据支持 claim：转 `CLAIM_UNSUPPORTED`
- 图已经生成但可读性弱：转 `FIGURE_WEAK`
- 需要表达算法/决策流程而不是数据关系：转 `FLOWCHART_NEEDED`

## Handoff

Figure Contract 冻结后转 `FIGURE_RENDER_NEEDED` 执行成图；是否纳入正文由 writing/Coach 决定。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。

## Tool Routing

合同冻结前可用 `tools/figure/scripts/profile_data.py` 复核数据形态；实际成图由 `figure-render` 调 `render_figure.py` 或项目专用绘图脚本；成图后用 `check_figure.py` / `visual_qa.py` 做机械审计。机械 PASS 不替代实际读图。
