#!/usr/bin/env bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# Tear down the sample. The event bus and subscriber are part of the
# CloudFormation stack (AWS::EventsV2::*), so deleting the stack removes them.
# The consumer's CloudWatch Logs log group is created by Lambda on first
# invocation, not by the stack, so it is deleted separately afterwards.
#
# Usage:
#   scripts/teardown.sh [stack-name] [region]
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

# Read the log group name from the stack output before the stack is gone, so a
# custom AppName is honored. Fall back to the default name if the lookup fails.
LOG_GROUP="$(aws cloudformation describe-stacks --stack-name "${STACK_NAME}" --region "${REGION}" \
  --query "Stacks[0].Outputs[?OutputKey=='ConsumerLogGroup'].OutputValue" --output text 2>/dev/null || true)"
if [ -z "${LOG_GROUP}" ] || [ "${LOG_GROUP}" = "None" ]; then
  LOG_GROUP="/aws/lambda/sync-orders-consumer"
fi

echo "Deleting stack ${STACK_NAME}..."
aws cloudformation delete-stack --stack-name "${STACK_NAME}" --region "${REGION}"
aws cloudformation wait stack-delete-complete --stack-name "${STACK_NAME}" --region "${REGION}"

# Delete after the stack so the function can't recreate the log group.
echo "Deleting log group ${LOG_GROUP}..."
if ! aws logs delete-log-group --log-group-name "${LOG_GROUP}" --region "${REGION}" 2>/dev/null; then
  echo "Log group ${LOG_GROUP} not found (the function may never have run); skipping."
fi
echo "Teardown complete."
