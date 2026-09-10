#!/bin/bash
# deploy.sh -- Deploy the AWS Lambda MicroVM Codex CLI Agent
#
# Overridable with environment variables:
#   AWS_REGION         target Region (default: the AWS CLI's configured Region)
#   ACCOUNT_ID         AWS account (default: resolved from the current credentials)
#   AWS_PARTITION      AWS partition, e.g. aws or aws-us-gov (default: resolved from the current credentials)
#   IMAGE_NAME         MicroVM image name; also derives the stack name (default: codex-cli-agent)
#   S3_BUCKET          artifact bucket (default: microvm-artifacts-<account>-<region>)
#   MODEL_ID           Amazon Bedrock model for Codex, unprefixed (default: template default)
#   MCP_ENDPOINT       AWS MCP Server endpoint (default: template default)
#   MEMORY_MIB         MicroVM memory floor in MiB (default: template default)
#   MAX_DURATION       MicroVM hard lifetime in seconds (default: 28800, i.e. 8 hours)
#   IDLE_SECONDS       idle time before the MicroVM suspends (default: 3600)
#   SUSPENDED_SECONDS  time suspended before the MicroVM terminates (default: 1800)
#
# The Region is never baked into the image: the platform supplies AWS_REGION to
# the MicroVM and app.py renders the Codex config from it at runtime.
#
# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
IMAGE_NAME="${IMAGE_NAME:-codex-cli-agent}"
STACK_NAME="microvm-${IMAGE_NAME}"

AWS_REGION="${AWS_REGION:-$(aws configure get region 2>/dev/null || true)}"
if [ -z "${AWS_REGION}" ]; then
    echo "ERROR: No AWS Region configured. Set one and retry:"
    echo "  export AWS_REGION=us-east-2"
    exit 1
fi

# Account and partition both come from the caller identity ARN
# (arn:<partition>:sts::<account>:...), so the script needs no hardcoded
# partition and works unchanged in Regions outside the standard one.
CALLER_ARN="$(aws sts get-caller-identity --query Arn --output text)"
ACCOUNT_ID="${ACCOUNT_ID:-$(printf '%s' "${CALLER_ARN}" | cut -d: -f5)}"
AWS_PARTITION="${AWS_PARTITION:-$(printf '%s' "${CALLER_ARN}" | cut -d: -f2)}"
# Region is part of the bucket name: bucket names are global but buckets are
# regional, so a fixed name breaks the second Region you deploy into.
S3_BUCKET="${S3_BUCKET:-microvm-artifacts-${ACCOUNT_ID}-${AWS_REGION}}"
S3_KEY="deployments/${IMAGE_NAME}-$(date +%Y%m%d-%H%M%S).zip"

# Only pass parameters the caller actually set, so the template's own defaults
# stay authoritative.
PARAM_OVERRIDES=(
    "S3Bucket=${S3_BUCKET}"
    "S3Key=${S3_KEY}"
    "ImageName=${IMAGE_NAME}"
)
if [ -n "${MODEL_ID:-}" ]; then
    PARAM_OVERRIDES+=("ModelId=${MODEL_ID}")
fi
if [ -n "${MCP_ENDPOINT:-}" ]; then
    PARAM_OVERRIDES+=("McpEndpoint=${MCP_ENDPOINT}")
fi
if [ -n "${MEMORY_MIB:-}" ]; then
    PARAM_OVERRIDES+=("MemoryMiB=${MEMORY_MIB}")
fi

echo "=== AWS Lambda MicroVM Codex CLI Agent ==="
echo "Region:  ${AWS_REGION}"
echo "Account: ${ACCOUNT_ID}"
echo "Stack:   ${STACK_NAME}"
echo "Bucket:  ${S3_BUCKET}"
echo ""

# -- Step 1: Amazon S3 bucket -------------------------------------------------
echo ">>> Step 1: Ensuring Amazon S3 bucket..."
if ! aws s3api head-bucket --bucket "${S3_BUCKET}" --region "${AWS_REGION}" 2>/dev/null; then
    aws s3 mb "s3://${S3_BUCKET}" --region "${AWS_REGION}"
fi

# -- Step 2: Package and upload -----------------------------------------------
# Built in a temp directory that is always removed, so a failed upload leaves
# nothing behind.
echo ">>> Step 2: Packaging source..."
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT
ZIP_PATH="${TMP_DIR}/${IMAGE_NAME}.zip"
# Exclusions keep local build droppings out of the artifact, so the image build
# gets the same context regardless of what has been run in src/ locally.
( cd "${SCRIPT_DIR}/src" && zip -qr "${ZIP_PATH}" . \
    -x '*__pycache__*' -x '*.pyc' -x '.DS_Store' -x '*/.DS_Store' )
aws s3 cp "${ZIP_PATH}" "s3://${S3_BUCKET}/${S3_KEY}" --region "${AWS_REGION}"
echo "    Uploaded to s3://${S3_BUCKET}/${S3_KEY}"

# -- Step 3: Deploy AWS CloudFormation stack (IAM + image build) --------------
echo ">>> Step 3: Deploying AWS CloudFormation stack (image build takes a few minutes)..."
aws cloudformation deploy \
  --template-file "${SCRIPT_DIR}/template.yaml" \
  --stack-name "${STACK_NAME}" \
  --parameter-overrides "${PARAM_OVERRIDES[@]}" \
  --capabilities CAPABILITY_IAM \
  --region "${AWS_REGION}"

# -- Step 4: Read stack outputs ------------------------------------------------
stack_output() {
    aws cloudformation describe-stacks \
      --stack-name "${STACK_NAME}" --region "${AWS_REGION}" \
      --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text
}

IMAGE_ARN=$(stack_output ImageArn)
EXEC_ROLE_ARN=$(stack_output ExecutionRoleArn)
RESOLVED_MODEL=$(stack_output ModelId)
RESOLVED_MCP=$(stack_output McpEndpoint)

echo "    Image: ${IMAGE_ARN}"
echo "    Role:  ${EXEC_ROLE_ARN}"
echo "    Model: ${RESOLVED_MODEL}"
echo "    MCP:   ${RESOLVED_MCP}"

# -- Step 5: Run the MicroVM with SHELL_INGRESS -------------------------------
# A MicroVM has a hard lifetime that is independent of the idle policy: when it
# expires the VM is terminated mid-session with
#   stateReason: "MicroVM exceeded maximum lifetime."
# even if it was active a second earlier, and no amount of resuming extends it.
# The service default is short enough to interrupt a real session, so this asks
# for 8 hours, a full working day. Lower it for a firmer cost ceiling than
# cleanup.sh gives you. The service enforces its own default and maximum for this
# value and rejects a request above the maximum; check the AWS Lambda MicroVMs
# documentation for the current limits rather than this comment.
MAX_DURATION="${MAX_DURATION:-28800}"
# Idle policy: suspend after IDLE_SECONDS without traffic, resume automatically
# when traffic returns, terminate after SUSPENDED_SECONDS in the suspended state.
IDLE_SECONDS="${IDLE_SECONDS:-3600}"
SUSPENDED_SECONDS="${SUSPENDED_SECONDS:-1800}"
echo ">>> Step 5: Running MicroVM (max lifetime ${MAX_DURATION}s, idle ${IDLE_SECONDS}s, suspended ${SUSPENDED_SECONDS}s)..."
read -r MICROVM_ID MICROVM_EP < <(aws lambda-microvms run-microvm \
  --image-identifier "${IMAGE_ARN}" \
  --execution-role-arn "${EXEC_ROLE_ARN}" \
  --ingress-network-connectors '["arn:'"${AWS_PARTITION}"':lambda:'"${AWS_REGION}"':aws:network-connector:aws-network-connector:SHELL_INGRESS"]' \
  --idle-policy '{"maxIdleDurationSeconds":'"${IDLE_SECONDS}"',"suspendedDurationSeconds":'"${SUSPENDED_SECONDS}"',"autoResumeEnabled":true}' \
  --maximum-duration-in-seconds "${MAX_DURATION}" \
  --logging '{"cloudWatch":{"logGroup":"/aws/lambda-microvms/'"${IMAGE_NAME}"'"}}' \
  --region "${AWS_REGION}" \
  --query '[microvmId, endpoint]' --output text)

echo ""
echo "=== Deployment Complete ==="
echo ""
echo "MicroVM ID: ${MICROVM_ID}"
echo "Endpoint:   https://${MICROVM_EP}"
echo ""
echo "Connect (interactive shell):"
echo "  ./connect.sh ${MICROVM_ID} ${AWS_REGION}"
echo ""
echo "Tear everything down:"
echo "  MICROVM_ID=${MICROVM_ID} AWS_REGION=${AWS_REGION} ./cleanup.sh"
