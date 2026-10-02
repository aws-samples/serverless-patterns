#!/usr/bin/env bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# Build and deploy the Protobuf-on-EventBridge sample — entirely with
# CloudFormation. The event bus and subscriber are now AWS::EventsV2::* resources
# in the template, so there is no separate CLI step.
#
# Usage:
#   scripts/deploy.sh [stack-name] [region]
#
# Requires: AWS SAM CLI, AWS CLI v2, and credentials allowed to create the Glue
# registry/schema, Lambda, IAM role, SQS queue, the eventsv2 bus, and subscriber.
set -euo pipefail

STACK_NAME="${1:-protobuf-eventbridge-sample}"
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

# The publisher imports the generated Protobuf bindings; the Glue schema in the
# template is independent of them, but publishing later needs them, so warn early
# if a fresh clone forgot to generate.
if [ ! -f "${HERE}/common/gen/order_placed_pb.py" ]; then
  echo "note: Protobuf bindings not found (common/gen/order_placed_pb.py)." >&2
  echo "You will need them to publish. Generate with:  scripts/generate.sh" >&2
fi

echo "Building the consumer Lambda..."
sam build --template "${TEMPLATE}" --region "${REGION}"

echo "Deploying stack '${STACK_NAME}' in ${REGION}..."
sam deploy \
  --stack-name "${STACK_NAME}" \
  --region "${REGION}" \
  --capabilities CAPABILITY_NAMED_IAM \
  --no-confirm-changeset \
  --no-fail-on-empty-changeset \
  --resolve-s3

get_output() {
  aws cloudformation describe-stacks \
    --stack-name "${STACK_NAME}" --region "${REGION}" \
    --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text
}

echo
echo "Deploy complete."
echo "  Event bus ARN : $(get_output EventBusArn)"
echo "  Registry ARN  : $(get_output SchemaRegistryArn)"
echo
echo "Publish a test event with:"
echo "  scripts/run_publish.sh ${STACK_NAME} ${REGION}"
