---
name: figure-render
trigger: FIGURE_RENDER_NEEDED
description: 按已冻结 Figure Contract 把真实数据渲染成可复现的科研图；优先标准化可执行后端，复杂图退回项目专用绘图脚本，不改写科学主张。
---

# figure-render

## Trigger

- 事件：`FIGURE_RENDER_NEEDED`。
- `figure-design` 已给出 Figure Contract，而当前缺口是“把合同真正画出来”时调用。
- 用户明确要求根据现有数据和已确定图型直接生成图时也可调用。

## Scope

本 Skill 负责从 Figure Contract 到实际图文件的执行层。它不重新选择模型、不发明统计口径、不为了美观改变数据，也不以固定图数为目标。

## Inputs

- 已冻结 Figure Contract：claim、字段、单位、图型、统计口径、轴/尺度、图注要求
- 权威数据文件或 Final/候选 Run 输出
- 目标输出目录
- 目标媒介/最终尺寸；若当届规则或期刊规范已核验，一并提供
- 后端偏好（Python / MATLAB，可选）

## Procedure

1. 逐项核对 Figure Contract 与数据字段，缺字段、单位冲突或统计口径未定义时停止，不自行补猜。
2. 需要聚合、归一化、排序、区间或误差条时，所有转换必须在绘图代码中显式计算并可回溯到原始列；禁止手工改数。
3. 标准图优先调用 `tools/figure/scripts/render_figure.py`：line、scatter、bar、hist、box、heatmap、errorbar。标准 CLI 无法表达的多面板、空间、网络、Pareto、相图、3D 曲面等，生成 `PROJECT_ROOT` 下的专用 Python/MATLAB 绘图脚本，并复用 `export_figure.py`。
4. 输出尺寸直接按最终使用尺寸设置；轴标签必须包含必要单位。只有 Figure Contract 明确要求时才使用 log 轴、截断轴、聚合或参考线。
5. 分组图默认同时使用形状/线型/marker 等冗余编码；不得靠“颜色看起来好看”掩盖类别不可辨识。
6. 统计标记、显著性、置信区间、误差条和拟合线只能来自真实计算；没有对应计算证据就不画。
7. 至少输出一个矢量格式（优先 SVG/PDF，取决于论文链）和一个 raster 预览；DPI/尺寸阈值由实际交付目标决定，不写死成科学真值。
8. 运行 `validate_source.py` 检查绘图源码，`check_figure.py` 检查导出文件；需要灰度/对比度检查时运行 `visual_qa.py`。
9. 实际打开最终尺寸图检查裁切、遮挡、图例、字号、轴范围、标签和视觉误导。发现问题修改绘图代码后重渲，禁止只修 PNG。
10. 记录输入数据路径、绘图脚本/命令、关键 Figure Contract 字段和输出文件；若图来自 Final Run，保留 Run 对应关系。

## Outputs

- 实际可打开的 SVG/PDF/PNG 图文件
- 对应项目绘图脚本或可复现 CLI 命令
- render receipt：输入数据、Figure Contract 摘要、输出路径、机械 QA 状态
- 若无法忠实实现合同，返回精确阻塞项

## Checks

- 图中数据可回溯到权威输入
- 图型、轴、统计口径与 Figure Contract 一致
- 不存在手工改数、虚构误差条/显著性或未说明聚合
- 最终尺寸下可读
- 矢量/raster 输出可打开，机械 QA 无阻断错误
- 图的主结论没有在渲染阶段被偷换

## Failure

- Figure Contract 本身不清楚或图型不合适：返回 `FIGURE_NEEDED`
- 当前数据不能支持 claim：返回 `CLAIM_UNSUPPORTED`
- 标准渲染器能力不足：创建项目专用绘图脚本，不把复杂图硬塞进通用 CLI
- 已成功生成但视觉/证据表达仍弱：转 `FIGURE_WEAK`

## Handoff

渲染完成后建议 `FIGURE_WEAK` / `visualization-review` 做最终尺寸语义复审；是否纳入论文由 writing/Coach 决定。

统一回执字段：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。Skill 可以建议下一个事件，但不能自行切换比赛阶段。
