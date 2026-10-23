#!/bin/bash
# connect.sh -- Open an interactive shell into the Codex CLI AWS Lambda MicroVM
#
# Usage: ./connect.sh <microvm-id> [region]
#
# The Region is resolved from the argument, then AWS_REGION, then the AWS CLI's
# own configured Region. Nothing is hardcoded, so this script does not have to be
# edited to work in a second Region.
#
# Requires: websocat (https://github.com/vi/websocat), AWS CLI v2
#
# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

set -euo pipefail

MICROVM_ID="${1:?Usage: $0 <microvm-id> [region]}"
AWS_REGION="${2:-${AWS_REGION:-$(aws configure get region 2>/dev/null || true)}}"
TOKEN_TTL="${TOKEN_TTL:-30}"

if [ -z "${AWS_REGION}" ]; then
    echo "ERROR: Could not determine an AWS Region."
    echo "       Pass one explicitly:  $0 ${MICROVM_ID} us-east-2"
    echo "       Or export it:         export AWS_REGION=us-east-2"
    exit 1
fi

# -- Check prerequisites ------------------------------------------------------
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

# -- Resolve the MicroVM endpoint ---------------------------------------------
echo "Resolving MicroVM endpoint in ${AWS_REGION}..."
MVM_ENDPOINT=$(aws lambda-microvms get-microvm \
  --microvm-identifier "${MICROVM_ID}" \
  --region "${AWS_REGION}" \
  --query 'endpoint' --output text)

if [ -z "${MVM_ENDPOINT}" ] || [ "${MVM_ENDPOINT}" = "None" ]; then
    echo "ERROR: Could not resolve endpoint for ${MICROVM_ID} in ${AWS_REGION}."
    echo "       Is the MicroVM running? Check with:"
    echo "       aws lambda-microvms get-microvm --microvm-identifier ${MICROVM_ID} \\"
    echo "         --region ${AWS_REGION}"
    exit 1
fi

# -- Generate a shell auth token ----------------------------------------------
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

# -- Connect (raw terminal mode, like SSH) ------------------------------------
echo "Connecting to wss://${MVM_ENDPOINT}/ ..."
echo ""
echo "To DISCONNECT, run this from another local terminal:"
echo "    pkill -f websocat"
echo ""
echo "Typing 'exit' ends the remote shell but the server keeps the WebSocket"
echo "open, so the session appears to hang; it drops on its own after the ping"
echo "timeout below. Ctrl+C and Ctrl+\\ do not disconnect either, because raw"
echo "mode forwards them to the remote shell. pkill is the clean way out."
echo ""

# Raw mode so the remote TUI receives keystrokes directly. A consequence is that
# the local shell no longer turns Ctrl+C / Ctrl+\ into signals here. Teardown
# therefore relies on this EXIT trap, which runs however websocat ends -- most
# reliably when it is killed from another terminal (pkill -f websocat) -- and
# restores the local terminal.
cleanup() { stty sane 2>/dev/null; }
trap cleanup EXIT
stty raw -echo

# The MicroVM shell agent does not close the WebSocket when the remote shell
# exits, so there is no client-side keystroke that ends the session cleanly. The
# ping timeout is the backstop: if the connection goes half-open (including after
# typing 'exit'), websocat gives up instead of hanging forever.
websocat "wss://${MVM_ENDPOINT}/" \
  --protocol "lambda-microvms,lambda-microvms.authentication.${TOKEN}" \
  --ping-interval 20 --ping-timeout 60 \
  -b
