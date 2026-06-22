#!/bin/bash
# deploy.sh — Deploy a Lambda MicroVM from a pre-built ECR image
#
# Flow: CloudFormation (IAM + ECR + image) → docker build/push → run-microvm
#
# Requires: Docker with buildx, AWS CLI
#
# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

set -euo pipefail

AWS_REGION="${AWS_REGION:-us-east-2}"
ACCOUNT_ID="${ACCOUNT_ID:-$(aws sts get-caller-identity --query Account --output text)}"
S3_BUCKET="${S3_BUCKET:-microvm-artifacts-${ACCOUNT_ID}}"
IMAGE_NAME="from-ecr"
ECR_REPO="microvm-from-ecr"
STACK_NAME="microvm-${IMAGE_NAME}"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
S3_KEY="deployments/${IMAGE_NAME}-${TIMESTAMP}.zip"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ECR_URI="${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}"

echo "=== Lambda MicroVM from ECR ==="
echo "Region:   ${AWS_REGION}"
echo "Account:  ${ACCOUNT_ID}"
echo "Stack:    ${STACK_NAME}"
echo "ECR Repo: ${ECR_URI}"
echo ""

# ── Step 1: S3 bucket ────────────────────────────────────────────────────────
echo ">>> Step 1: Ensuring S3 bucket..."
if ! aws s3api head-bucket --bucket "${S3_BUCKET}" 2>/dev/null; then
    aws s3 mb "s3://${S3_BUCKET}" --region "${AWS_REGION}"
fi

# ── Step 2: Build and push Docker image to ECR ───────────────────────────────
echo ">>> Step 2: Building and pushing Docker image to ECR..."
aws ecr describe-repositories --repository-names "${ECR_REPO}" --region "${AWS_REGION}" >/dev/null 2>&1 || \
  aws ecr create-repository --repository-name "${ECR_REPO}" --region "${AWS_REGION}" >/dev/null

aws ecr get-login-password --region "${AWS_REGION}" | \
  docker login --username AWS --password-stdin "${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"

docker buildx build --platform linux/arm64 --push --provenance=false \
  -t "${ECR_URI}:latest" "${SCRIPT_DIR}/src"
echo "    Pushed ${ECR_URI}:latest"

# ── Step 3: Create thin zip (FROM ecr) and upload ────────────────────────────
echo ">>> Step 3: Creating thin zip artifact..."
TMPDIR=$(mktemp -d)
cat > "${TMPDIR}/Dockerfile" <<EOF
FROM ${ECR_URI}:latest
EOF
cd "${TMPDIR}"
zip /tmp/app.zip Dockerfile
cd - > /dev/null
rm -rf "${TMPDIR}"
aws s3 cp /tmp/app.zip "s3://${S3_BUCKET}/${S3_KEY}" --region "${AWS_REGION}"
rm -f /tmp/app.zip
echo "    Uploaded to s3://${S3_BUCKET}/${S3_KEY}"

# ── Step 4: Deploy CloudFormation stack (IAM + image build) ──────────────────
echo ">>> Step 4: Deploying CloudFormation stack..."
aws cloudformation deploy \
  --template-file "${SCRIPT_DIR}/template.yaml" \
  --stack-name "${STACK_NAME}" \
  --parameter-overrides \
      S3Bucket="${S3_BUCKET}" \
      S3Key="${S3_KEY}" \
      ImageName="${IMAGE_NAME}" \
  --capabilities CAPABILITY_NAMED_IAM \
  --region "${AWS_REGION}"

# ── Step 5: Get outputs and run ──────────────────────────────────────────────
IMAGE_ARN=$(aws cloudformation describe-stacks \
  --stack-name "${STACK_NAME}" --region "${AWS_REGION}" \
  --query 'Stacks[0].Outputs[?OutputKey==`ImageArn`].OutputValue' --output text)
ROLE_ARN=$(aws cloudformation describe-stacks \
  --stack-name "${STACK_NAME}" --region "${AWS_REGION}" \
  --query 'Stacks[0].Outputs[?OutputKey==`BuildRoleArn`].OutputValue' --output text)

echo "    Image: ${IMAGE_ARN}"

echo ">>> Step 5: Running MicroVM..."
LAUNCH=$(aws lambda-microvms run-microvm \
  --image-identifier "${IMAGE_ARN}" \
  --execution-role-arn "${ROLE_ARN}" \
  --idle-policy '{"maxIdleDurationSeconds":900,"suspendedDurationSeconds":300,"autoResumeEnabled":true}' \
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
echo "Test:"
echo "  TOKEN=\$(aws lambda-microvms create-microvm-auth-token \\"
echo "    --microvm-identifier ${MICROVM_ID} --expiration-in-minutes 30 \\"
echo "    --allowed-ports '[{\"port\":8080}]' \\"
echo "    --region ${AWS_REGION} \\"
echo "    --query 'authToken.\"X-aws-proxy-auth\"' --output text)"
echo ""
echo "  curl \"https://${MICROVM_EP}/\" -H \"X-aws-proxy-auth: \$TOKEN\""
