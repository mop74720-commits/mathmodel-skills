---
name: tool-reproducibility
description: 记录运行合同，并明确区分 artifact integrity 与 replay reproducibility；支持 Python/MATLAB/其他 runtime、cwd 相对路径和 CSV/JSON 数值语义指纹。
---

# Reproducibility Tool — v0.1.11

## Two different claims

1. **artifact_integrity**：当前文件是否仍与记录时完全相同。`verify` 只证明这一点。
2. **replay_reproducibility**：重新执行记录命令后，产物是否重新得到相同结果。`replay` 才检查这一点。

绝不把 hash verify PASS 写成“代码可复现”。

## Create

相对 `--input` / `--artifact` 路径按 `--cwd` 解析：

```bash
python tools/reproducibility/scripts/run_manifest.py create \
  --output results/run-manifest.json \
  --run-id q2-final \
  --cwd . \
  --command "python src/q2/main.py" \
  --seed 42 \
  --input data/processed/q2.csv \
  --artifact results/q2.csv \
  --semantic-decimals 10 \
  --package numpy --package scipy
```

`--semantic-decimals` 只对 CSV/JSON 建立可选数值 canonical fingerprint。它用于容忍最后几位浮点漂移，不取代 exact SHA-256。

## Verify artifact integrity

```bash
python tools/reproducibility/scripts/run_manifest.py verify results/run-manifest.json
```

输出明确标记 `check_type=artifact_integrity`。

## Replay

```bash
python tools/reproducibility/scripts/run_manifest.py replay results/run-manifest.json --timeout 600
```

可能状态：

- `EXACT_MATCH`：重新运行后的产物字节级一致；
- `SEMANTIC_MATCH`：exact hash 不同，但配置的 CSV/JSON 数值 canonical fingerprint 一致；
- `MISMATCH`：重放结果不满足已记录合同；
- `INPUT_DRIFT`：输入在重放前已经改变，默认不继续。

## Boundary

- semantic fingerprint 是工程复现工具，不替代科学误差分析；真正允许的容差应来自模型/数值语义。
- 对随机并行算法，必要时记录 deterministic/canonical Final Run，并把更广泛的随机稳健性放在 `robustness` Skill。
- 不采集秘密环境变量。
