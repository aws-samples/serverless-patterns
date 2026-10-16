#!/usr/bin/env bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# Build and deploy the ordered synchronous-Lambda sample (TypeScript) — entirely
# with CloudFormation. The event bus and the FIFO, synchronous subscriber are
# AWS::EventsV2::* resources in the template, so there is no separate CLI step.
# SAM builds the TypeScript consumer with esbuild.
#
# Account- and region-agnostic: pass any region; nothing is hardcoded.
#
# Usage:
#   scripts/deploy.sh [stack-name] [region]
set -euo pipefail

STACK_NAME="${1:-lambda-sync-eventbridge-sample}"
# Region resolution order: positional arg, then $AWS_REGION / $AWS_DEFAULT_REGION,
# then the region configured in your AWS CLI profile. Nothing is hardcoded.
REGION="${2:-${AWS_REGION:-${AWS_DEFAULT_REGION:-$(aws configure get region 2>/dev/null || true)}}}"
if [ -z "${REGION}" ]; then
  echo "error: no AWS region set. Pass one as the 2nd argument, export AWS_REGION," >&2
  echo "       or set a default with 'aws configure'." >&2
  exit 1
fi

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE="${HERE}/infra/template.yaml"

echo "Building the consumer Lambda (esbuild)..."
sam build --template "${TEMPLATE}" --region "${REGION}"

echo "Deploying stack '${STACK_NAME}' in ${REGION}..."
sam deploy \
  --stack-name "${STACK_NAME}" \
  --region "${REGION}" \
  --capabilities CAPABILITY_NAMED_IAM \
  --no-confirm-changeset \
  --no-fail-on-empty-changeset \
  --resolve-s3

BUS_ARN="$(aws cloudformation describe-stacks \
  --stack-name "${STACK_NAME}" --region "${REGION}" \
  --query "Stacks[0].Outputs[?OutputKey=='EventBusArn'].OutputValue" --output text)"

echo
echo "Deploy complete."
echo "  Event bus ARN : ${BUS_ARN}"
echo
echo "Publish an ordered sequence:  scripts/run_publish.sh ${STACK_NAME} ${REGION}"
echo "  (add a count:               scripts/run_publish.sh ${STACK_NAME} ${REGION} 8 )"
