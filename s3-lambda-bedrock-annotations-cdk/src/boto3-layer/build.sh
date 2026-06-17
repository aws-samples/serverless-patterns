#!/bin/bash
# Build boto3 layer with S3 Annotations support
set -e
cd "$(dirname "$0")"
rm -rf python
pip install -r requirements.txt -t python --quiet
echo "Layer built: $(python -c 'import importlib.metadata; print(importlib.metadata.version("boto3"))' 2>/dev/null || pip show boto3 2>/dev/null | grep Version)"
