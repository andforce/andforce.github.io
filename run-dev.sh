#!/usr/bin/env bash
set -euo pipefail

if ! command -v python3 >/dev/null 2>&1; then
  echo "本地预览需要 Python 3，请先安装。" >&2
  exit 1
fi

cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
port="${PORT:-8000}"
printf '本地预览：http://127.0.0.1:%s（Ctrl+C 停止）\n' "$port"
exec python3 -m http.server "$port" --bind 127.0.0.1
