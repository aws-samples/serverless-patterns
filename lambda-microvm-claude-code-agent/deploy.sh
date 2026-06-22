#!/bin/bash
# deploy.sh — Deploy the Lambda MicroVM Claude Code Agent
#
# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

set -euo pipefail

AWS_REGION="${AWS_REGION:-us-east-2}"
ACCOUNT_ID="${ACCOUNT_ID:-$(aws sts get-caller-identity --query Account --output text)}"
S3_BUCKET="${S3_BUCKET:-microvm-artifacts-${ACCOUNT_ID}}"
IMAGE_NAME="claude-code-agent"
STACK_NAME="microvm-${IMAGE_NAME}"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
S3_KEY="deployments/${IMAGE_NAME}-${TIMESTAMP}.zip"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== Lambda MicroVM Claude Code Agent ==="
echo "Region:  ${AWS_REGION}"
echo "Account: ${ACCOUNT_ID}"
echo "Stack:   ${STACK_NAME}"
echo ""

# ── Step 1: S3 bucket ────────────────────────────────────────────────────────
echo ">>> Step 1: Ensuring S3 bucket..."
if ! aws s3api head-bucket --bucket "${S3_BUCKET}" 2>/dev/null; then
    aws s3 mb "s3://${S3_BUCKET}" --region "${AWS_REGION}"
fi

# ── Step 2: Package and upload ───────────────────────────────────────────────
echo ">>> Step 2: Packaging source..."
cd "${SCRIPT_DIR}/src"
zip -r /tmp/app.zip .
aws s3 cp /tmp/app.zip "s3://${S3_BUCKET}/${S3_KEY}" --region "${AWS_REGION}"
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
  --region "${AWS_REGION}"

# ── Step 4: Get outputs ──────────────────────────────────────────────────────
IMAGE_ARN=$(aws cloudformation describe-stacks \
  --stack-name "${STACK_NAME}" --region "${AWS_REGION}" \
  --query 'Stacks[0].Outputs[?OutputKey==`ImageArn`].OutputValue' --output text)
EXEC_ROLE_ARN=$(aws cloudformation describe-stacks \
  --stack-name "${STACK_NAME}" --region "${AWS_REGION}" \
  --query 'Stacks[0].Outputs[?OutputKey==`ExecutionRoleArn`].OutputValue' --output text)

echo "    Image: ${IMAGE_ARN}"
echo "    Role:  ${EXEC_ROLE_ARN}"

# ── Step 5: Run MicroVM with SHELL_INGRESS ───────────────────────────────────
echo ">>> Step 5: Running MicroVM..."
LAUNCH=$(aws lambda-microvms run-microvm \
  --image-identifier "${IMAGE_ARN}" \
  --execution-role-arn "${EXEC_ROLE_ARN}" \
  --ingress-network-connectors '["arn:aws:lambda:'"${AWS_REGION}"':aws:network-connector:aws-network-connector:SHELL_INGRESS"]' \
  --idle-policy '{"maxIdleDurationSeconds":3600,"suspendedDurationSeconds":1800,"autoResumeEnabled":true}' \
  --logging '{"cloudWatch":{"logGroup":"/aws/lambda-microvms/'"${IMAGE_NAME}"'"}}' \
  --region "${AWS_REGION}")

MICROVM_ID=$(echo "${LAUNCH}" | python3 -c "import sys,json; print(json.load(sys.stdin)['microvmId'])" 2>/dev/null || \
             echo "${LAUNCH}" | grep -o '"microvmId":"[^"]*"' | cut -d'"' -f4)
MICROVM_EP=$(echo "${LAUNCH}" | python3 -c "import sys,json; print(json.load(sys.stdin)['endpoint'])" 2>/dev/null || \
             echo "${LAUNCH}" | grep -o '"endpoint":"[^"]*"' | cut -d'"' -f4)

echo ""
echo "=== Deployment Complete ==="
echo ""
echo "MicroVM ID: ${MICROVM_ID}"
echo "Endpoint:   https://${MICROVM_EP}"
echo ""
echo "Connect (interactive shell):"
echo "  ./connect.sh ${MICROVM_ID}"
