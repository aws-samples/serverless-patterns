#!/usr/bin/env bash
# Packages the agent for AgentCore Runtime direct code deployment and uploads it to S3.
# AgentCore runs the code on Linux ARM64 with Python 3.13, so the dependencies
# are downloaded as manylinux aarch64 wheels, whatever machine you build on.
#
# Usage: ./build.sh <bucket-name>
# Prints the S3 key to pass to sam deploy as AgentCodeKey.
set -euo pipefail

BUCKET="${1:?usage: ./build.sh <bucket-name>}"
cd "$(dirname "$0")"

rm -rf .build && mkdir -p .build/package
# A throwaway virtual environment keeps the build isolated from your own Python packages.
python3 -m venv .build/venv
.build/venv/bin/python -m pip install --quiet --disable-pip-version-check \
  --target .build/package \
  --platform manylinux2014_aarch64 \
  --implementation cp \
  --python-version 3.13 \
  --only-binary=:all: \
  --requirement agent/requirements.txt
cp agent/main.py .build/package/

(cd .build/package && zip -qr ../agent.zip .)

# A new key for each build, so that sam deploy picks up the new code.
HASH=$(shasum -a 256 .build/agent.zip | cut -c1-12)
KEY="sfn-bedrock-agentcore-callback/agent-${HASH}.zip"
aws s3 cp --quiet .build/agent.zip "s3://${BUCKET}/${KEY}"
echo "${KEY}"
