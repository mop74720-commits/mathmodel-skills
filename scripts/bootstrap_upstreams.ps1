$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Upstream = Join-Path $Root "upstream"
New-Item -ItemType Directory -Force -Path $Upstream | Out-Null

function Sync-Repo($Name, $Url, $Commit) {
  $Path = Join-Path $Upstream $Name
  if (-not (Test-Path (Join-Path $Path ".git"))) {
    git clone $Url $Path
  } else {
    git -C $Path fetch --all --tags --prune
  }
  git -C $Path checkout --detach $Commit
  $Actual = (git -C $Path rev-parse HEAD).Trim()
  if ($Actual -ne $Commit) { throw "$Name commit mismatch: $Actual" }
  Write-Host "$Name OK $Actual"
}

Sync-Repo "xiaoma" "https://github.com/XiaoMaColtAI/math-modeling-skill.git" "e5d9313420d519f18ed1429d52d95fe0a72ae944"
Sync-Repo "han" "https://github.com/han69611/math-modeling-skills.git" "b5b98aebcb25ff89a99ea1cbb52b31ccab5040ca"
python (Join-Path $Root "scripts/verify_upstreams.py")
