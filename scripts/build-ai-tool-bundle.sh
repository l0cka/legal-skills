#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
exec python3 -I "$root/scripts/ai_tool_bundle.py" "$@"
