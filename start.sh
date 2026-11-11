#!/usr/bin/env bash
# Scary Drama Prop Looper - Linux / macOS Startup Script
set -e

# Change to script directory
cd "$(dirname "$0")"

# Ensure python3 is available
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required. Please install python3 (e.g., sudo apt install python3)"
    exit 1
fi

echo "========================================================"
echo "  SCARY DRAMA PROP - TERMINAL LOOP"
echo "  Press Ctrl+C at any time to exit"
echo "========================================================"
echo ""

python3 loop.py "$@"
