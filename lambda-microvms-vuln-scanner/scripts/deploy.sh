#!/bin/bash
# deploy.sh — Vulnerability scanning tool on AWS Lambda MicroVMs
#
# Builds the scanner MicroVM image declaratively via CloudFormation
# (AWS::Lambda::MicrovmImage). This script:
#   1. Ensures a staging S3 bucket exists.
#   2. Fetches the Trivy (ARM64) binary into the MicroVM app build context and
#      zips the app (Dockerfile + app.py + hooks.py + start.sh + trivy).
#   3. Uploads the artifact to S3.
#   4. Deploys the CloudFormation stack, which builds the MicroVM image and
#      creates the IAM build/execution roles and the log group.
#
# Launching a MicroVM and running a scan is a runtime step — see the README.
#
# Usage:
#   ./scripts/deploy.sh [stack-name] [region]
# Example:
#   ./scripts/deploy.sh vuln-scanner us-east-1
#
# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
MICROVM_APP_DIR="$PROJECT_ROOT/src/microvm-app"

STACK_NAME="${1:-vuln-scanner}"
REGION="${2:-${AWS_REGION:-$(aws configure get region)}}"
ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
STAGING_BUCKET="${STACK_NAME}-staging-${ACCOUNT_ID}"
ARTIFACT_KEY="microvm-app/artifact.zip"
TRIVY_VERSION="${TRIVY_VERSION:-0.74.0}"

echo "============================================"
echo "Deploying Lambda MicroVMs vulnerability scanner"
echo "============================================"
echo "Stack:          $STACK_NAME"
echo "Region:         $REGION"
echo "Account:        $ACCOUNT_ID"
echo "Staging Bucket: $STAGING_BUCKET"
echo ""

# ── Step 1: staging bucket ───────────────────────────────────────────────────
echo "--- Step 1: Ensure staging bucket ---"
if ! aws s3api head-bucket --bucket "$STAGING_BUCKET" --region "$REGION" 2>/dev/null; then
  echo "Creating staging bucket: $STAGING_BUCKET"
  if [ "$REGION" = "us-east-1" ]; then
    aws s3api create-bucket --bucket "$STAGING_BUCKET" --region "$REGION"
  else
    aws s3api create-bucket --bucket "$STAGING_BUCKET" --region "$REGION" \
      --create-bucket-configuration "LocationConstraint=$REGION"
  fi
  aws s3api put-public-access-block --bucket "$STAGING_BUCKET" --region "$REGION" \
    --public-access-block-configuration \
    "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
  # A newly created bucket is not always immediately reachable; wait for it.
  echo "Waiting for staging bucket to become reachable..."
  for _ in $(seq 1 30); do
    aws s3api head-bucket --bucket "$STAGING_BUCKET" --region "$REGION" 2>/dev/null && break
    sleep 2
  done
else
  echo "Staging bucket already exists: $STAGING_BUCKET"
fi
echo ""

# ── Step 2: package the MicroVM app (Trivy fetched at package time) ──────────
# The image build sandbox has no general internet egress, so the Trivy binary
# is fetched here (on your machine) and baked into the artifact. The Trivy
# vulnerability database is downloaded by the running MicroVM at scan time.
echo "--- Step 2: Package MicroVM app (fetching Trivy ${TRIVY_VERSION}) ---"
curl -sfL -o /tmp/trivy.tgz \
  "https://github.com/aquasecurity/trivy/releases/download/v${TRIVY_VERSION}/trivy_${TRIVY_VERSION}_Linux-ARM64.tar.gz"
tar -xzf /tmp/trivy.tgz -C "$MICROVM_APP_DIR" trivy
rm -f /tmp/trivy.tgz

ARTIFACT_ZIP="/tmp/microvm-artifact.zip"
rm -f "$ARTIFACT_ZIP"
( cd "$MICROVM_APP_DIR" && zip -qr "$ARTIFACT_ZIP" Dockerfile app.py hooks.py start.sh trivy )
rm -f "$MICROVM_APP_DIR/trivy"   # keep the repo binary-free
echo "Created: $ARTIFACT_ZIP"
echo ""

# ── Step 3: upload the artifact ──────────────────────────────────────────────
echo "--- Step 3: Upload artifact ---"
aws s3 cp "$ARTIFACT_ZIP" "s3://$STAGING_BUCKET/$ARTIFACT_KEY" --region "$REGION"
rm -f "$ARTIFACT_ZIP"
echo ""

# ── Step 4: deploy the stack (builds the image; allow several minutes) ───────
echo "--- Step 4: Deploy CloudFormation stack (image build runs inside the stack) ---"
aws cloudformation deploy \
  --template-file "$PROJECT_ROOT/template.yaml" \
  --stack-name "$STACK_NAME" \
  --region "$REGION" \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides \
    StackLabel="$STACK_NAME" \
    StagingBucket="$STAGING_BUCKET" \
    ArtifactKey="$ARTIFACT_KEY" \
  --no-fail-on-empty-changeset
echo ""

# ── Outputs ──────────────────────────────────────────────────────────────────
echo "=== Deployment Complete ==="
aws cloudformation describe-stacks --stack-name "$STACK_NAME" --region "$REGION" \
  --query 'Stacks[0].Outputs' --output table

IMAGE_ARN=$(aws cloudformation describe-stacks --stack-name "$STACK_NAME" --region "$REGION" \
  --query 'Stacks[0].Outputs[?OutputKey==`MicroVMImageArn`].OutputValue' --output text)
EXECUTION_ROLE_ARN=$(aws cloudformation describe-stacks --stack-name "$STACK_NAME" --region "$REGION" \
  --query 'Stacks[0].Outputs[?OutputKey==`MicroVMExecutionRoleArn`].OutputValue' --output text)

echo ""
echo "To launch a scanner MicroVM and run a scan, export these and follow the README:"
echo ""
echo "  export REGION=\"$REGION\""
echo "  export STACK_NAME=\"$STACK_NAME\""
echo "  export IMAGE_ARN=\"$IMAGE_ARN\""
echo "  export EXECUTION_ROLE_ARN=\"$EXECUTION_ROLE_ARN\""
echo ""
