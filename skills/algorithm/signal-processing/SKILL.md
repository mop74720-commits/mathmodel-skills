---
name: signal-processing
trigger: ALGO_SIGNAL_PROCESSING
description: 处理采样信号的频域/时频分析、滤波、去噪与特征提取，强调采样定理、谱泄漏、边界效应和独立验证。
---

# signal-processing

## Trigger

- 事件：`ALGO_SIGNAL_PROCESSING`。
- 当数据本质是按时间/空间采样的连续信号，问题依赖周期、频率、瞬态、能量分布、去噪或时频特征时调用。
- 用户点名 FFT、PSD、STFT、小波、滤波、频谱分析时也可调用，但先确认这些方法对应题目证据需求。

## Scope

覆盖离散采样信号的预处理、FFT/功率谱、STFT、wavelet、数字滤波和由信号提取的统计特征。它不替代普通时间序列预测：若目标是预测未来值且频谱只是辅助特征，应与 `ALGO_TIME_SERIES` 或 `ALGO_SUPERVISED_LEARNING` 组合。

## Inputs

- 采样值、时间戳/空间坐标与采样频率
- 单位、传感器量程和缺失/饱和信息
- 目标：周期识别、去噪、事件检测、特征提取或重构
- 预期频段/物理时间尺度（若有依据）
- 下游模型和允许的相位/幅值失真

## Procedure

1. 审计采样合同：确认采样是否等间隔、采样频率是否足以覆盖目标频带，并检查时间戳漂移、缺失、重复点和传感器饱和。
2. 建立原始信号 Baseline，先做时域统计、趋势和异常检查；去均值、去趋势、标准化等操作必须记录且说明是否改变物理解释。
3. 频域分析前检查 Nyquist 条件和 aliasing 风险；FFT/PSD 选择窗口长度、window function 与重叠时说明频率分辨率和谱泄漏权衡。
4. 平稳周期问题优先 FFT/Welch PSD；频率随时间变化或瞬态问题考虑 STFT / wavelet。不要因为小波“更高级”就默认使用。
5. 滤波时根据目标频带选低通/高通/带通/notch，记录截止频率、阶数和相位特性；零相位离线滤波不能冒充实时因果处理。
6. Wavelet 分解需说明母小波、尺度/层数和边界处理；只保留能解释或改善下游指标的系数/特征。
7. 所有去噪/滤波结果都与原始信号和合成/已知频率基准对照，确认没有把真实事件、峰值或相位结构滤掉。
8. 若提取频域/时频特征供分类/回归，训练测试切分必须先于任何从全数据学习参数的预处理，防止 leakage。

## Decision Rules

- 主要问题是未来预测：优先 `ALGO_TIME_SERIES`，信号处理只做有证据的特征工程。
- 稳定单频/窄带结构：FFT/PSD 通常比 wavelet 更简单且可解释。
- 强瞬态、chirp 或局部频率变化：STFT/wavelet 才有明显结构优势。
- 非等间隔采样不能直接按普通 FFT 解释频率轴；先重采样或采用适合不规则采样的方法并验证失真。
- 去噪后指标改善但原始物理峰被削弱时，应优先保留科学解释而非追求平滑视觉效果。

## Validation Design

1. 用合成正弦/多频信号验证频率轴、幅值归一化和窗函数实现。
2. 检查不同 window / segment length 下主频是否稳定，报告频率分辨率。
3. 滤波前后比较能量、峰值、相位和边界段，识别 ringing / edge effect。
4. Wavelet/STFT 改变参数后关键时频结论是否稳定。
5. 下游任务中使用严格 split，比较“不用信号特征”的 Baseline，证明新增处理确有决策价值。
6. 若有真实已知事件/机械频率/工频等参考，核对估计峰与领域事实是否一致。

## Outputs

- 采样与单位合同
- 时域 Baseline 与预处理记录
- 频域/时频方法及参数依据
- 主频、带宽、能量或时频特征
- 滤波/去噪前后对照
- 稳定性、aliasing、边界效应与适用范围

## Checks

- 频率轴和单位正确
- 未违反采样定理而无说明
- 窗函数/重叠/归一化可复现
- 滤波没有使用未来数据冒充实时方法
- wavelet 边界效应已检查
- 特征工程没有跨训练/验证集泄漏

## Failure

- 采样频率不足导致不可恢复 aliasing：返回 `DATA_UNKNOWN` / 降低可声明频带。
- 结果高度依赖窗口、尺度或滤波参数：转 `RESULT_UNSTABLE`。
- 目标本质是预测/分类而非信号结构：转 `ALGO_TIME_SERIES` / `ALGO_SUPERVISED_LEARNING`。
- 数值实现的幅值/频率基准不通过：转 `NUMERICAL_SUSPECT`。

## Handoff

特征/信号路线确定后转 `MODEL_CONTRACT_MISSING` 或 `IMPLEMENT_MODEL`；需检验参数稳定性时转 `NEED_SENSITIVITY`。

统一回执：`status / inputs_used / outputs_written / key_findings / risks / qa_status / handoff`。算法 Skill 可以建议下一事件，但不能替 Coach 做阶段或资源决策。
