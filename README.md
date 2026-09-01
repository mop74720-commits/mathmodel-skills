# mathmodel-skills v0.2.0 — upstream-preserving edition

定位：第二层 Skill Hub。保留 XiaoMaColtAI/math-modeling-skill 与 han69611/math-modeling-skills 的原始仓库内容，不在本包内重写或替换上游文件；本包只提供本地 bootstrap、固定提交、路由 overlay 与 Coach 接口。

## 为什么采用 upstream + overlay

两个上游当前仓库元数据未声明许可证。本包不重新分发其完整源码/文档，而是在你的本机通过 Git 从原仓库取得原内容。这样：

- 上游内容保持原样；
- 可精确固定到已审阅提交；
- 我们的规则仅作为 overlay，不污染上游；
- 后续可单独更新某个 upstream 并重新审计。

## 一键初始化

Windows PowerShell：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap_upstreams.ps1
```

macOS / Linux：

```bash
bash ./scripts/bootstrap_upstreams.sh
```

完成后：

```text
mathmodel-skills-v0.2.0/
├── SKILL.md
├── registry.yaml
├── overlay/
├── references/
├── scripts/
└── upstream/
    ├── xiaoma/   # XiaoMa 原仓库，固定提交
    └── han/      # Han 原仓库，固定提交
```

## 固定版本

- XiaoMaColtAI/math-modeling-skill: `e5d9313420d519f18ed1429d52d95fe0a72ae944`
- han69611/math-modeling-skills: `b5b98aebcb25ff89a99ea1cbb52b31ccab5040ca`

如需更新上游，修改 `upstream-lock.json` 后重新运行 bootstrap，并重新审核差异。
