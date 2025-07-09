#!/usr/bin/env bash
set -euo pipefail

# Production build: prefix links with your repo name
python3 src/main.py "/static-site-generator/"

echo "✅  Site generated to ./docs (ready for GitHub Pages)."
