#!/bin/bash
# connect.sh — Connect to an existing (or new) Lambda MicroVM Code Server
#
# This script handles the full "get me connected" lifecycle:
#   1. Finds the image/role from the deployed CloudFormation stack
#   2. Looks for a RUNNING or SUSPENDED MicroVM — reuses it if found
#   3. If none available, launches a new MicroVM and waits for RUNNING
#   4. Gets a fresh auth token
#   5. Starts the local proxy and opens the browser
#
# Usage:
#   ./connect.sh              # Uses defaults (us-east-2, default profile)
#   ./connect.sh --region us-west-2 --profile my-profile
#
# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

set -euo pipefail

# ── Configuration ────────────────────────────────────────────────────────────
AWS_REGION="${AWS_REGION:-us-east-2}"
AWS_PROFILE="${AWS_PROFILE:-}"
IMAGE_NAME="code-server"
STACK_NAME="lambda-microvm-${IMAGE_NAME}"
PROXY_PORT="${PROXY_PORT:-8080}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Parse optional CLI args
while [[ $# -gt 0 ]]; do
    case "$1" in
        --region)  AWS_REGION="$2"; shift 2 ;;
        --profile) AWS_PROFILE="$2"; shift 2 ;;
        --port)    PROXY_PORT="$2"; shift 2 ;;
        --stack)   STACK_NAME="$2"; shift 2 ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

# Build AWS CLI base args
AWS_ARGS=(--region "${AWS_REGION}")
if [[ -n "${AWS_PROFILE}" ]]; then
    AWS_ARGS+=(--profile "${AWS_PROFILE}")
fi

echo "=== Lambda MicroVM Code Server — Connect ==="
echo "Region:  ${AWS_REGION}"
echo "Stack:   ${STACK_NAME}"
[[ -n "${AWS_PROFILE}" ]] && echo "Profile: ${AWS_PROFILE}"
echo ""

# ── Step 1: Get stack outputs ────────────────────────────────────────────────
echo ">>> Looking up stack outputs..."
IMAGE_ARN=$(aws cloudformation describe-stacks \
    --stack-name "${STACK_NAME}" "${AWS_ARGS[@]}" \
    --query 'Stacks[0].Outputs[?OutputKey==`ImageArn`].OutputValue' --output text)
EXEC_ROLE_ARN=$(aws cloudformation describe-stacks \
    --stack-name "${STACK_NAME}" "${AWS_ARGS[@]}" \
    --query 'Stacks[0].Outputs[?OutputKey==`ExecutionRoleArn`].OutputValue' --output text)

if [[ -z "${IMAGE_ARN}" || "${IMAGE_ARN}" == "None" ]]; then
    echo "ERROR: Stack '${STACK_NAME}' not found or missing outputs."
    echo "       Run deploy.sh first to set up the infrastructure."
    exit 1
fi
echo "    Image: ${IMAGE_ARN}"

# ── Step 2: Find an active MicroVM ──────────────────────────────────────────
echo ">>> Checking for existing MicroVMs..."
ACTIVE_VM=$(aws lambda-microvms list-microvms "${AWS_ARGS[@]}" --output json \
    | python3 -c "
import sys, json
data = json.load(sys.stdin)
for vm in data.get('items', []):
    if vm.get('imageArn') == '${IMAGE_ARN}' and vm.get('state') in ('RUNNING', 'SUSPENDED'):
        print(vm['microvmId'])
        break
" 2>/dev/null || echo "")

if [[ -n "${ACTIVE_VM}" ]]; then
    MICROVM_ID="${ACTIVE_VM}"
    echo "    Found active MicroVM: ${MICROVM_ID}"

    # Get endpoint
    MICROVM_EP=$(aws lambda-microvms get-microvm \
        --microvm-identifier "${MICROVM_ID}" "${AWS_ARGS[@]}" \
        --query 'endpoint' --output text)
    STATE=$(aws lambda-microvms get-microvm \
        --microvm-identifier "${MICROVM_ID}" "${AWS_ARGS[@]}" \
        --query 'state' --output text)
    echo "    State:    ${STATE}"
    echo "    Endpoint: ${MICROVM_EP}"

    if [[ "${STATE}" == "SUSPENDED" ]]; then
        echo "    (MicroVM will auto-resume on first request)"
    fi
else
    # ── Step 3: Launch a new MicroVM ─────────────────────────────────────────
    echo "    No active MicroVM found. Launching a new one..."
    IMAGE_NAME=$(echo "${IMAGE_ARN}" | grep -o '[^:]*$')

    LAUNCH=$(aws lambda-microvms run-microvm \
        --image-identifier "${IMAGE_ARN}" \
        --execution-role-arn "${EXEC_ROLE_ARN}" \
        --ingress-network-connectors '["arn:aws:lambda:'"${AWS_REGION}"':aws:network-connector:aws-network-connector:HTTP_INGRESS"]' \
        --egress-network-connectors '["arn:aws:lambda:'"${AWS_REGION}"':aws:network-connector:aws-network-connector:INTERNET_EGRESS"]' \
        --idle-policy '{"maxIdleDurationSeconds":3600,"suspendedDurationSeconds":1800,"autoResumeEnabled":true}' \
        --logging '{"cloudWatch":{"logGroup":"/aws/lambda-microvms/'"${IMAGE_NAME}"'"}}' \
        "${AWS_ARGS[@]}" --output json)

    MICROVM_ID=$(echo "${LAUNCH}" | python3 -c "import sys,json; print(json.load(sys.stdin)['microvmId'])")
    MICROVM_EP=$(echo "${LAUNCH}" | python3 -c "import sys,json; print(json.load(sys.stdin)['endpoint'])")
    echo "    MicroVM ID: ${MICROVM_ID}"
    echo "    Endpoint:   ${MICROVM_EP}"

    # Wait for RUNNING
    echo -n "    Waiting for RUNNING"
    for i in $(seq 1 30); do
        STATE=$(aws lambda-microvms get-microvm \
            --microvm-identifier "${MICROVM_ID}" "${AWS_ARGS[@]}" \
            --query 'state' --output text)
        if [[ "${STATE}" == "RUNNING" ]]; then
            echo " ✓"
            break
        fi
        echo -n "."
        sleep 2
    done

    if [[ "${STATE}" != "RUNNING" ]]; then
        echo ""
        echo "ERROR: MicroVM did not reach RUNNING state (current: ${STATE})"
        exit 1
    fi
fi

# ── Step 4: Get auth token ───────────────────────────────────────────────────
echo ">>> Getting auth token..."
TOKEN=$(aws lambda-microvms create-microvm-auth-token \
    --microvm-identifier "${MICROVM_ID}" \
    --expiration-in-minutes 60 \
    --allowed-ports allPorts={} \
    "${AWS_ARGS[@]}" \
    --query 'authToken."X-aws-proxy-auth"' --output text)

if [[ -z "${TOKEN}" || "${TOKEN}" == "None" ]]; then
    echo "ERROR: Failed to get auth token. Check your credentials."
    exit 1
fi
echo "    Token: ${TOKEN:0:16}... (expires in 60 min)"

# ── Step 5: Start proxy ─────────────────────────────────────────────────────
echo ""
echo ">>> Starting local proxy on port ${PROXY_PORT}..."
echo ""
exec python3 "${SCRIPT_DIR}/proxy.py" "https://${MICROVM_EP}" "${TOKEN}" --port "${PROXY_PORT}"
