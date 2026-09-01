---
name: tool-reproducibility
description: 生成/验证轻量运行 manifest，并按实际功能检查依赖；v0.1.7 增加 MATLAB/非 Python runtime 记录，同时不采集秘密环境变量。
---

# Reproducibility Tool

用于 `experiment-manager`、`implementation` 和 Final Run 证据绑定。

## Commands

Python：

```bash
python tools/reproducibility/scripts/run_manifest.py doctor --features data visualization optimization
python tools/reproducibility/scripts/run_manifest.py create \
  --output results/run-manifest.json \
  --run-id q2-final \
  --command "python q2.py --config configs/q2.json" \
  --seed 42 \
  --input data/input.xlsx \
  --artifact results/q2.csv \
  --package numpy --package scipy
python tools/reproducibility/scripts/run_manifest.py verify results/run-manifest.json
```

MATLAB 或其他 runtime：

```bash
python tools/reproducibility/scripts/run_manifest.py create \
  --output results/run-manifest.json \
  --run-id q2-matlab \
  --runtime matlab \
  --runtime-version R2025b \
  --dependency "Optimization Toolbox=25.2" \
  --command 'matlab -batch "main(42)"' \
  --seed 42 \
  --input data/input.csv \
  --artifact results/q2.csv
```

## Contract

`create` 生成 `mathmodel-run-manifest/v2`，记录：

- UTC 时间、run id、唯一复现命令；
- runtime 名称/版本；
- 执行 manifest 脚本的 host Python/platform；
- Git commit/dirty（若存在）；
- 指定 Python package 与通用 `name=version` dependency；
- 指定输入/产物 SHA-256；
- seed 与显式 notes。

它不会转储完整环境变量、token、密钥或系统秘密。

`doctor` 只检查用户声明会用到的 feature；`matlab` feature 只检查 MATLAB executable 是否存在。MATLAB 工具箱的精确检查由 `roles/coding/scripts/check_matlab_env.m` 完成。

`verify` 同时兼容 v1/v2 manifest，重新计算已记录输入与产物哈希；文件缺失或内容变化返回非零状态。
