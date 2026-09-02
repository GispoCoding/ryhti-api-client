#!/bin/bash
# Copies a generated client (public | xroad) into src/ and docs/, then post-processes
# and formats it. Run from the project root.
set -euo pipefail

api_dir=${1:?usage: $0 public|xroad}

cp -rf .generated/$api_dir/ryhti_api_client/models src/ryhti_api_client/
cp -rf .generated/$api_dir/ryhti_api_client/${api_dir}_api src/ryhti_api_client/
cp -rf .generated/$api_dir/ryhti_api_client/docs ./
# cp -rf .generated/$api_dir/ryhti_api_client/test ./
find .generated/$api_dir/ryhti_api_client -maxdepth 1 -type f -exec cp -f {} src/ryhti_api_client/ \;

# Replace the generated oneOf wrapper classes with pydantic discriminated unions
uv run python "$(dirname "$0")/fix_discriminated_unions.py"

uv run ruff check --fix --extend-fixable=F841,F401 src/ryhti_api_client
uv run ruff format src/ryhti_api_client
