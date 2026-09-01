---
name: tool-reproducibility
description: 生成/验证轻量运行 manifest，并按实际功能检查依赖；只记录复现所需信息，不采集秘密环境变量。
---

# Reproducibility Tool

用于 `experiment-manager`、`implementation` 和 Final Run 证据绑定。

## Commands

```bash
python tools/reproducibility/scripts/run_manifest.py doctor --features data visualization optimization
python tools/reproducibility/scripts/run_manifest.py create --output results/run-manifest.json --run-id q2-final --command "python q2.py --config configs/q2.json" --seed 42 --input data/input.xlsx --artifact results/q2.csv --package numpy --package scipy
python tools/reproducibility/scripts/run_manifest.py verify results/run-manifest.json
```

`create` 记录 UTC 时间、平台/Python、Git commit/dirty（若存在）、指定 package 版本、指定输入/产物 SHA-256、seed 与唯一复现命令。它不会转储完整环境变量或凭据。

`doctor` 只检查用户声明将使用的 feature profile，不要求仓库全量依赖一次性安装。

`verify` 重新计算已记录文件的哈希，发现文件缺失或内容变化时返回非零状态。
