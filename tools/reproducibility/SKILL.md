---
name: tool-reproducibility
description: 记录运行合同，区分 artifact integrity、replay reproducibility 与 provenance bundle integrity；支持 Python/MATLAB/其他 runtime、cwd 相对路径和 CSV/JSON 数值语义指纹。
---

# Reproducibility Tool — v0.1.12

## Three different claims

1. **artifact_integrity**：当前 manifest 中记录的输入/产物是否仍与记录时完全相同。`verify` 只证明这一点。
2. **replay_reproducibility**：重新执行记录命令后，产物能否重新得到相同结果。`replay` 才检查这一点。
3. **provenance_bundle_integrity**：manifest、Run Ledger、规则 profile、Claim-Evidence Map 等被 bundle 引用的证据索引是否仍是同一份文件。`verify-bundle` 只证明索引工件身份。

绝不把 hash verify PASS 写成“代码可复现”或“科学结论正确”。

## Create manifest

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

`--semantic-decimals` 只对 CSV/JSON 建立可选数值 canonical fingerprint。它用于识别最后几位浮点漂移，不取代 exact SHA-256，也不自动定义科学允许误差。

## Verify artifact integrity

```bash
python tools/reproducibility/scripts/run_manifest.py verify results/run-manifest.json
```

输出 `check_type=artifact_integrity`。

## Replay

```bash
python tools/reproducibility/scripts/run_manifest.py replay results/run-manifest.json --timeout 600
```

可能状态：

- `EXACT_MATCH`：重新运行后的产物字节级一致；
- `SEMANTIC_MATCH`：exact hash 不同，但配置的 CSV/JSON 数值 canonical fingerprint 一致；
- `MISMATCH`：重放结果不满足已记录合同；
- `INPUT_DRIFT`：输入在重放前已经改变，默认不继续。

## Provenance bundle

对 Confirmatory / Final Run，可把关键证据索引绑定为轻量 bundle：

```bash
python tools/reproducibility/scripts/run_manifest.py bundle \
  --manifest results/run-manifest.json \
  --output results/provenance-bundle.json \
  --cwd . \
  --ledger runs/RUN_LEDGER.csv \
  --rule-profile rules/RULE_PROFILE.json \
  --claim-evidence audit/CLAIM_EVIDENCE_MAP.csv \
  --status final

python tools/reproducibility/scripts/run_manifest.py verify-bundle \
  results/provenance-bundle.json
```

Bundle 不保存 API key、token、秘密环境变量或完整机器快照。推荐合同见 `references/provenance-bundle.md`。

## Boundary

- semantic fingerprint 是工程复现工具，不替代数值误差、统计误差或模型不确定性分析。
- provenance bundle 是证据索引，不替代 Run Ledger、Claim-Evidence Map 或 Final Review。
- 对随机并行算法，必要时记录 deterministic/canonical Final Run，并把更广泛的随机稳健性放在 `robustness` Skill。
- 不采集秘密环境变量。
