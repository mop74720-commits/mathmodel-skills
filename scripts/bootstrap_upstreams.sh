#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$ROOT/upstream"

sync_repo() {
  local name="$1" url="$2" commit="$3" path="$ROOT/upstream/$name"
  if [ ! -d "$path/.git" ]; then
    git clone "$url" "$path"
  else
    git -C "$path" fetch --all --tags --prune
  fi
  git -C "$path" checkout --detach "$commit"
  actual="$(git -C "$path" rev-parse HEAD)"
  [ "$actual" = "$commit" ] || { echo "$name commit mismatch: $actual" >&2; exit 1; }
  echo "$name OK $actual"
}

sync_repo xiaoma https://github.com/XiaoMaColtAI/math-modeling-skill.git e5d9313420d519f18ed1429d52d95fe0a72ae944
sync_repo han https://github.com/han69611/math-modeling-skills.git b5b98aebcb25ff89a99ea1cbb52b31ccab5040ca
python3 "$ROOT/scripts/verify_upstreams.py"
