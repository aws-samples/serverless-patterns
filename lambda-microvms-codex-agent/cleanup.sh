#!/bin/bash
# cleanup.sh -- Tear down the AWS Lambda MicroVM Codex CLI Agent
#
# Removes, in order: running MicroVMs, the AWS CloudFormation stack (IAM roles,
# image, log group), and the Amazon S3 artifacts. Prints what it is about to
# delete and asks for confirmation unless FORCE=1.
#
# Overridable with environment variables:
#   AWS_REGION   target Region (default: the AWS CLI's configured Region)
#   ACCOUNT_ID   AWS account (default: resolved from the current credentials)
#   IMAGE_NAME   MicroVM image name; derives the stack name (default: codex-cli-agent)
#   MICROVM_ID   terminate only this MicroVM (default: every MicroVM on the image)
#   S3_BUCKET    artifact bucket (default: microvm-artifacts-<account>-<region>)
#   KEEP_BUCKET  set to 1 to leave the bucket itself in place
#   FORCE        set to 1 to skip the confirmation prompt
#
# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

set -euo pipefail

IMAGE_NAME="${IMAGE_NAME:-codex-cli-agent}"
STACK_NAME="microvm-${IMAGE_NAME}"

AWS_REGION="${AWS_REGION:-$(aws configure get region 2>/dev/null || true)}"
if [ -z "${AWS_REGION}" ]; then
    echo "ERROR: No AWS Region configured. Set one and retry:"
    echo "  export AWS_REGION=us-east-2"
    exit 1
fi

ACCOUNT_ID="${ACCOUNT_ID:-$(aws sts get-caller-identity --query Account --output text)}"
S3_BUCKET="${S3_BUCKET:-microvm-artifacts-${ACCOUNT_ID}-${AWS_REGION}}"

echo "=== Cleanup: AWS Lambda MicroVM Codex CLI Agent ==="
echo "Region:  ${AWS_REGION}"
echo "Account: ${ACCOUNT_ID}"
echo "Stack:   ${STACK_NAME}"
echo "Bucket:  ${S3_BUCKET}"
echo ""

# -- Work out which MicroVMs to terminate --------------------------------------
if [ -n "${MICROVM_ID:-}" ]; then
    TARGETS="${MICROVM_ID}"
else
    # Filter by image server-side, so this only ever terminates VMs belonging to
    # this stack's image. The AWS CLI paginates list-microvms automatically and
    # merges every page into `items`, so no token loop is needed here.
    # Already-terminating VMs are excluded: terminating them again is an error.
    # An empty result is fine; the loop below becomes a no-op.
    IMAGE_ARN=$(aws cloudformation describe-stacks \
      --stack-name "${STACK_NAME}" --region "${AWS_REGION}" \
      --query "Stacks[0].Outputs[?OutputKey=='ImageArn'].OutputValue" \
      --output text 2>/dev/null || true)

    TARGETS=""
    if [ -n "${IMAGE_ARN}" ] && [ "${IMAGE_ARN}" != "None" ]; then
        TARGETS=$(aws lambda-microvms list-microvms --region "${AWS_REGION}" \
          --image-identifier "${IMAGE_ARN}" \
          --query "items[?state!='TERMINATED' && state!='TERMINATING'].microvmId" \
          --output text 2>/dev/null || true)
    else
        echo "NOTE: stack ${STACK_NAME} has no ImageArn output; cannot discover"
        echo "      MicroVMs automatically. Pass MICROVM_ID= explicitly if any"
        echo "      are still running."
    fi
fi

echo "This will delete:"
if [ -n "${TARGETS}" ]; then
    echo "  MicroVMs:        ${TARGETS}"
else
    echo "  MicroVMs:        (none found)"
fi
echo "  CFN stack:       ${STACK_NAME}  (IAM roles, MicroVM image, log group)"
echo "  S3 artifacts:    s3://${S3_BUCKET}/deployments/"
if [ "${KEEP_BUCKET:-0}" != "1" ]; then
    echo "  S3 bucket:       s3://${S3_BUCKET}  (set KEEP_BUCKET=1 to retain)"
fi
echo ""

if [ "${FORCE:-0}" != "1" ]; then
    read -r -p "Proceed? [y/N] " REPLY
    case "${REPLY}" in
        y|Y|yes|YES) ;;
        *) echo "Aborted."; exit 0 ;;
    esac
    echo ""
fi

# -- Step 1: Terminate MicroVMs -----------------------------------------------
# Before the stack, so the image is not deleted from under a running VM.
echo ">>> Step 1: Terminating MicroVMs..."
if [ -z "${TARGETS}" ]; then
    echo "    None to terminate."
else
    for ID in ${TARGETS}; do
        echo "    Terminating ${ID}..."
        aws lambda-microvms terminate-microvm \
          --microvm-identifier "${ID}" \
          --region "${AWS_REGION}" >/dev/null || echo "    WARN: ${ID} could not be terminated (already gone?)"
    done
fi

# -- Step 2: Delete the AWS CloudFormation stack ------------------------------
echo ">>> Step 2: Deleting AWS CloudFormation stack..."
if aws cloudformation describe-stacks --stack-name "${STACK_NAME}" \
     --region "${AWS_REGION}" >/dev/null 2>&1; then
    aws cloudformation delete-stack --stack-name "${STACK_NAME}" --region "${AWS_REGION}"
    echo "    Waiting for delete to complete..."
    aws cloudformation wait stack-delete-complete \
      --stack-name "${STACK_NAME}" --region "${AWS_REGION}"
    echo "    Deleted."
else
    echo "    Stack not found, skipping."
fi

# -- Step 3: Remove Amazon S3 artifacts ---------------------------------------
echo ">>> Step 3: Removing Amazon S3 artifacts..."
if aws s3api head-bucket --bucket "${S3_BUCKET}" --region "${AWS_REGION}" >/dev/null 2>&1; then
    aws s3 rm "s3://${S3_BUCKET}/deployments/" --recursive --region "${AWS_REGION}"
    if [ "${KEEP_BUCKET:-0}" != "1" ]; then
        aws s3 rb "s3://${S3_BUCKET}" --region "${AWS_REGION}"
        echo "    Bucket removed."
    else
        echo "    Bucket retained (KEEP_BUCKET=1)."
    fi
else
    echo "    Bucket not found, skipping."
fi

echo ""
echo "=== Cleanup Complete ==="
