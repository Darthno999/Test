#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$ROOT_DIR/.venv"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required. Install with: sudo apt update && sudo apt install -y python3 python3-venv python3-pip"
  exit 1
fi

if ! command -v google-chrome >/dev/null 2>&1 \
  && ! command -v google-chrome-stable >/dev/null 2>&1 \
  && ! command -v chromium-browser >/dev/null 2>&1 \
  && ! command -v chromium >/dev/null 2>&1; then
  echo "Chrome/Chromium not detected. Install with:"
  echo "  sudo apt update && sudo apt install -y chromium-browser"
  exit 1
fi

if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"
python -m pip install --upgrade pip
python -m pip install -r "$ROOT_DIR/requirements.txt"
python "$ROOT_DIR/auto_swipe.py"
