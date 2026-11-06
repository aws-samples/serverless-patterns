#!/usr/bin/env bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# Generate the Python Protobuf bindings from proto/order_placed.proto.
#
# The bindings (common/gen/order_placed_pb.py) are a BUILD ARTIFACT — they are
# git-ignored, so a fresh clone must run this once before publishing or testing.
#
# Prerequisites (see README): a Python venv with the codegen toolchain installed
#   python3 -m venv .venv
#   ./.venv/bin/pip install -r publisher/requirements.txt   # protobuf-py (runtime)
#   ./.venv/bin/pip install protoc-gen-py buf-bin            # codegen (dev only)
#
# Usage:
#   scripts/generate.sh
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_BIN="${HERE}/.venv/bin"

if [ ! -x "${VENV_BIN}/buf" ] || [ ! -x "${VENV_BIN}/protoc-gen-py" ]; then
  echo "error: codegen tools not found in ${VENV_BIN}." >&2
  echo "Install them into the sample's venv first:" >&2
  echo "  python3 -m venv .venv" >&2
  echo "  ./.venv/bin/pip install -r publisher/requirements.txt" >&2
  echo "  ./.venv/bin/pip install protoc-gen-py buf-bin" >&2
  exit 1
fi

mkdir -p "${HERE}/common/gen"

# buf invokes the protoc-gen-py plugin by finding it on PATH, so put the venv
# bin first. Run from the sample root so the buf.gen.yaml paths resolve.
echo "Generating Protobuf bindings into common/gen/ ..."
cd "${HERE}"
PATH="${VENV_BIN}:${PATH}" "${VENV_BIN}/buf" generate --template proto/buf.gen.yaml

# Make the generated dir an importable package.
touch "${HERE}/common/gen/__init__.py"

echo "Done. Generated:"
ls -1 "${HERE}/common/gen/"
