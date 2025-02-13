#!/bin/bash

set -euo pipefail

cd "$(dirname "$0")"

python3 -m uv pip compile "pyproject.toml" --python=3.8 --extra "dev" > requirements.txt
