#!/usr/bin/env bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# Read the deployed resources and publish one Avro OrderPlaced event.
#
# The bus and the Glue registry both come from the CloudFormation stack outputs.
#
# Usage:
#   scripts/run_publish.sh [stack-name] [region] [order-id]
#
# Requires: scripts/deploy.sh already run, and the publisher's Python deps
# installed (pip install -r publisher/requirements.txt).
set -euo pipefail

STACK_NAME="${1:-avro-eventbridge-sample}"
# Region resolution order: positional arg, then $AWS_REGION / $AWS_DEFAULT_REGION,
# then the region configured in your AWS CLI profile. Nothing is hardcoded.
REGION="${2:-${AWS_REGION:-${AWS_DEFAULT_REGION:-$(aws configure get region 2>/dev/null || true)}}}"
ORDER_ID="${3:-order-$(date +%s)}"

if [ -z "${REGION}" ]; then
  echo "error: no AWS region set. Pass one as the 2nd argument, export AWS_REGION," >&2
  echo "       or set a default with 'aws configure'." >&2
  exit 1
fi

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

get_output() {
  aws cloudformation describe-stacks \
    --stack-name "${STACK_NAME}" --region "${REGION}" \
    --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text
}

REGISTRY_ARN="$(get_output SchemaRegistryArn)"
LOG_GROUP="$(get_output ConsumerLogGroup)"
BUS_ARN="$(get_output EventBusArn)"

if [ "${BUS_ARN}" = "None" ] || [ -z "${BUS_ARN}" ]; then
  echo "error: EventBusArn not found in stack '${STACK_NAME}'. Run scripts/deploy.sh first." >&2
  exit 1
fi

echo "Bus:      ${BUS_ARN}"
echo "Registry: ${REGISTRY_ARN}"
echo "Publishing orderId=${ORDER_ID}..."

# Pick a Python interpreter: prefer the sample's virtualenv, then python3, then
# python. $PYTHON can override. Whichever is used must have boto3 + fastavro.
if [ -n "${PYTHON:-}" ]; then
  PYBIN="${PYTHON}"
elif [ -x "${HERE}/.venv/bin/python" ]; then
  PYBIN="${HERE}/.venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
  PYBIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYBIN="python"
else
  echo "error: no Python interpreter found. Install Python 3 and the publisher deps:" >&2
  echo "  python3 -m venv .venv && ./.venv/bin/pip install -r publisher/requirements.txt" >&2
  exit 1
fi

if ! "${PYBIN}" -c "import boto3, fastavro" >/dev/null 2>&1; then
  echo "error: ${PYBIN} is missing boto3 and/or fastavro. Install them with:" >&2
  echo "  ${PYBIN} -m pip install -r publisher/requirements.txt" >&2
  echo "(or create the venv: python3 -m venv .venv && ./.venv/bin/pip install -r publisher/requirements.txt)" >&2
  exit 1
fi

BUS_ARN="${BUS_ARN}" REGISTRY_ARN="${REGISTRY_ARN}" AWS_REGION="${REGION}" \
  "${PYBIN}" "${HERE}/publisher/publish.py" --order-id "${ORDER_ID}"

echo
echo "Give delivery a few seconds, then check the delivered event in CloudWatch:"
echo "  aws logs tail '${LOG_GROUP}' --region ${REGION} --since 5m --format short"
