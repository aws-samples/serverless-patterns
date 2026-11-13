#!/usr/bin/env bash
# Delete the stack. Extra arguments are passed to cdk destroy.
set -euo pipefail
cd "$(dirname "$0")"

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install --quiet --disable-pip-version-check -r cdk/requirements.txt

cd cdk
# Hide the jsii warning about Node.js versions it hasn't been tested with.
export JSII_SILENCE_WARNING_UNTESTED_NODE_VERSION=1
# --force deletes the stack, including the S3 bucket and its files, without asking to confirm.
npx --yes aws-cdk destroy --force "$@"
