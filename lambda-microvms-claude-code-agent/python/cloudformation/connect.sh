#!/bin/bash
# connect.sh — Open an interactive shell into the Lambda MicroVM
#
# Requires: websocat (https://github.com/vi/websocat), AWS CLI
#
# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

set -euo pipefail

MICROVM_ID="${1:?Usage: $0 <microvm-id>}"
AWS_REGION="us-east-2"
TOKEN_TTL="30"

# ── Check prerequisites ──────────────────────────────────────────────────────
command -v websocat >/dev/null 2>&1 || {
    echo "ERROR: websocat not found."
    echo ""
    echo "Install it (single static binary, no runtime deps):"
    echo "  brew install websocat                          # macOS (Homebrew)"
    echo "  cargo install websocat                         # Rust (any platform)"
    echo "  scoop install websocat                         # Windows (Scoop)"
    echo "  # or download from https://github.com/vi/websocat/releases"
    exit 1
}

# ── Resolve the MicroVM endpoint ─────────────────────────────────────────────
echo "Resolving MicroVM endpoint..."
MVM_ENDPOINT=$(aws lambda-microvms get-microvm \
  --microvm-identifier "${MICROVM_ID}" \
  --region "${AWS_REGION}" \
  --query 'endpoint' --output text)

if [ -z "${MVM_ENDPOINT}" ] || [ "${MVM_ENDPOINT}" = "None" ]; then
    echo "ERROR: Could not resolve endpoint for ${MICROVM_ID}."
    echo "       Is the MicroVM running? Check with:"
    echo "       aws lambda-microvms get-microvm --microvm-identifier ${MICROVM_ID} \\"
    echo "         --region ${AWS_REGION}"
    exit 1
fi

# ── Generate a shell auth token ──────────────────────────────────────────────
echo "Generating shell auth token (${TOKEN_TTL} min TTL)..."
TOKEN=$(aws lambda-microvms create-microvm-shell-auth-token \
  --microvm-identifier "${MICROVM_ID}" \
  --expiration-in-minutes "${TOKEN_TTL}" \
  --region "${AWS_REGION}" \
  --query 'authToken."X-aws-proxy-auth"' --output text)

if [ -z "${TOKEN}" ] || [ "${TOKEN}" = "None" ]; then
    echo "ERROR: Failed to generate shell auth token."
    echo "       Make sure the MicroVM has SHELL_INGRESS attached."
    exit 1
fi

# ── Connect (raw terminal mode — like SSH) ───────────────────────────────────
echo "Connecting to wss://${MVM_ENDPOINT}/ ..."
echo "(Type 'exit' or press Ctrl+\\ to disconnect)"
echo ""

# Put local terminal in raw mode (no echo, no buffering) then restore on exit.
# This is the documented websocat pattern for interactive shell access.
cleanup() { stty sane 2>/dev/null; }
trap cleanup EXIT INT TERM
stty raw -echo

websocat "wss://${MVM_ENDPOINT}/" \
  --protocol "lambda-microvms,lambda-microvms.authentication.${TOKEN}" \
  -b

cleanup
