#!/bin/bash
# deploy.sh — Deploy the AWS Lambda MicroVMs Code Server infrastructure
#
# This script handles first-time setup:
#   1. Creates an S3 bucket for artifacts
#   2. Packages and uploads the source code
#   3. Deploys the CloudFormation stack (IAM roles + MicroVM image build)
#
# After infrastructure is ready, it hands off to connect.sh which
# launches a MicroVM, gets an auth token, and starts the local proxy.
#
# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

set -euo pipefail

AWS_REGION="${AWS_REGION:-us-east-2}"
AWS_PROFILE="${AWS_PROFILE:-}"
ACCOUNT_ID="${ACCOUNT_ID:-$(aws sts get-caller-identity --query Account --output text)}"
S3_BUCKET="${S3_BUCKET:-microvm-artifacts-${ACCOUNT_ID}}"
IMAGE_NAME="code-server"
STACK_NAME="lambda-microvm-${IMAGE_NAME}"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
S3_KEY="deployments/${IMAGE_NAME}-${TIMESTAMP}.zip"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Build AWS CLI base args
AWS_ARGS=(--region "${AWS_REGION}")
if [[ -n "${AWS_PROFILE}" ]]; then
    AWS_ARGS+=(--profile "${AWS_PROFILE}")
fi

echo "=== AWS Lambda MicroVMs Code Server — Deploy ==="
echo "Region:  ${AWS_REGION}"
echo "Account: ${ACCOUNT_ID}"
echo "Stack:   ${STACK_NAME}"
[[ -n "${AWS_PROFILE}" ]] && echo "Profile: ${AWS_PROFILE}"
echo ""

# ── Step 1: S3 bucket ────────────────────────────────────────────────────────
echo ">>> Step 1: Ensuring S3 bucket..."
if ! aws s3api head-bucket --bucket "${S3_BUCKET}" "${AWS_ARGS[@]}" >/dev/null 2>&1; then
    aws s3 mb "s3://${S3_BUCKET}" "${AWS_ARGS[@]}"
fi

# ── Step 2: Package and upload ───────────────────────────────────────────────
echo ">>> Step 2: Packaging source..."
cd "${SCRIPT_DIR}/src"
zip -r /tmp/app.zip .
aws s3 cp /tmp/app.zip "s3://${S3_BUCKET}/${S3_KEY}" "${AWS_ARGS[@]}"
rm -f /tmp/app.zip
cd - > /dev/null
echo "    Uploaded to s3://${S3_BUCKET}/${S3_KEY}"

# ── Step 3: Deploy CloudFormation stack (IAM + image build) ──────────────────
echo ">>> Step 3: Deploying CloudFormation stack..."
aws cloudformation deploy \
  --template-file "${SCRIPT_DIR}/template.yaml" \
  --stack-name "${STACK_NAME}" \
  --parameter-overrides \
      S3Bucket="${S3_BUCKET}" \
      S3Key="${S3_KEY}" \
      ImageName="${IMAGE_NAME}" \
  --capabilities CAPABILITY_NAMED_IAM \
  "${AWS_ARGS[@]}"

# ── Step 4: Verify outputs ───────────────────────────────────────────────────
IMAGE_ARN=$(aws cloudformation describe-stacks \
  --stack-name "${STACK_NAME}" "${AWS_ARGS[@]}" \
  --query 'Stacks[0].Outputs[?OutputKey==`ImageArn`].OutputValue' --output text)

echo ""
echo "=== Infrastructure Ready ==="
echo "    Image: ${IMAGE_ARN}"
echo ""

# ── Step 5: Hand off to connect.sh ───────────────────────────────────────────
echo ">>> Launching MicroVM and connecting..."
echo ""

CONNECT_ARGS=(--region "${AWS_REGION}" --stack "${STACK_NAME}")
if [[ -n "${AWS_PROFILE}" ]]; then
    CONNECT_ARGS+=(--profile "${AWS_PROFILE}")
fi

exec "${SCRIPT_DIR}/connect.sh" "${CONNECT_ARGS[@]}"
echo "    --query 'authToken.\"X-aws-proxy-auth\"' --output text)"
echo ""
echo "  python3 proxy.py \"https://${MICROVM_EP}\" \"\$TOKEN\""
