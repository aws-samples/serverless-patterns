#!/usr/bin/env bash
# Builds dist/supervisor.zip (Dockerfile + linux/arm64 supervisor binary).
# Local only; terraform apply uploads it and builds the image.
set -euo pipefail

cd "$(dirname "$0")"

ARCH="${ARCH:-arm64}"       # must match CpuConfigurations in main.tf (ARM_64)
DIST="dist"
STAGE="$DIST/stage"

echo ">> cleaning"
rm -rf "$DIST"
mkdir -p "$STAGE"

echo ">> cross-compiling supervisor for linux/$ARCH"
( cd supervisor && CGO_ENABLED=0 GOOS=linux GOARCH="$ARCH" \
  go build -trimpath -ldflags="-s -w" -o "../$STAGE/supervisor" . )

echo ">> staging Dockerfile"
cp Dockerfile "$STAGE/Dockerfile"

echo ">> packaging $DIST/supervisor.zip"
# Fixed timestamps and -X make the zip deterministic, so terraform only
# rebuilds the image on a real change.
touch -t 8001010000 "$STAGE/supervisor" "$STAGE/Dockerfile"
# -j: both files at the zip root, where Lambda and the Dockerfile COPY expect them.
( cd "$STAGE" && zip -X -j -q "../supervisor.zip" supervisor Dockerfile )

echo ">> done:"
ls -la "$DIST/supervisor.zip"
unzip -l "$DIST/supervisor.zip"
