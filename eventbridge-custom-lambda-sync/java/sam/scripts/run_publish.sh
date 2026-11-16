#!/usr/bin/env bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# Publish an ordered sequence of OrderPlaced events (one event group) with the
# AWS CLI, then show where to watch them being processed in order.
#
# Every event shares one SystemMetadata.EventGroupId and carries an increasing
# seq, so the FIFO subscriber orders them and, invoking the consumer
# synchronously, processes them one at a time, in sequence. The IAM action
# needed is events:PutEvents on the bus (the prefix is events:, never eventsv2:).
#
# Usage:
#   scripts/run_publish.sh [stack-name] [region] [count]
#
#   count  number of ordered events to publish (default 5).
#
# Requires: the stack deployed (scripts/deploy.sh or sam deploy) and the AWS CLI
# v2.37.3 or later, signed in to the account that owns the stack.
set -euo pipefail

STACK_NAME="${1:-lambda-sync-eventbridge-sample}"
# Region resolution order: positional arg, then $AWS_REGION / $AWS_DEFAULT_REGION,
# then the region configured in your AWS CLI profile. Nothing is hardcoded.
REGION="${2:-${AWS_REGION:-${AWS_DEFAULT_REGION:-$(aws configure get region 2>/dev/null || true)}}}"
COUNT="${3:-5}"

if [ -z "${REGION}" ]; then
  echo "error: no AWS region set. Pass one as the 2nd argument, export AWS_REGION," >&2
  echo "       or set a default with 'aws configure'." >&2
  exit 1
fi
if ! [[ "${COUNT}" =~ ^[0-9]+$ ]] || [ "${COUNT}" -lt 1 ]; then
  echo "error: count must be a whole number >= 1 (got '${COUNT}')." >&2
  exit 1
fi

get_output() {
  aws cloudformation describe-stacks \
    --stack-name "${STACK_NAME}" --region "${REGION}" \
    --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text
}

APP_NAME="$(get_output AppName)"
LOG_GROUP="$(get_output ConsumerLogGroup)"
BUS_ARN="$(get_output EventBusArn)"
if [ "${BUS_ARN}" = "None" ] || [ -z "${BUS_ARN}" ]; then
  echo "error: EventBusArn not found in stack '${STACK_NAME}'. Run scripts/deploy.sh first." >&2
  exit 1
fi

# One group per run, so each run is ordered independently of earlier runs.
GROUP="order-group-$(date +%s)"

echo "AppName: ${APP_NAME}"
echo "Bus: ${BUS_ARN}"
echo "Publishing ${COUNT} ordered events in group '${GROUP}'..."

for ((seq = 1; seq <= COUNT; seq++)); do
  ORDER_ID="$(printf '%s-%03d' "${GROUP}" "${seq}")"
  # The order record. PutEvents takes Detail as a JSON string, so it is escaped
  # once more when embedded in the entry below.
  DETAIL="$(printf '{"orderId":"%s","orderGroup":"%s","seq":%d,"customerId":"cust-987","amount":%d.0,"currency":"USD","placedAt":"%s"}' \
    "${ORDER_ID}" "${GROUP}" "${seq}" "$((100 + seq))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)")"
  ENTRY="$(printf '[{"Source":"com.example.orders","DetailType":"OrderPlaced","Detail":"%s","SystemMetadata":{"EventGroupId":"%s"}}]' \
    "${DETAIL//\"/\\\"}" "${GROUP}")"

  # One event per call so each seq gets its own confirmed result. The CLI
  # retries throttling on its own.
  RESULT="$(aws eventsv2 put-events \
    --event-bus-arn "${BUS_ARN}" --region "${REGION}" \
    --entries "${ENTRY}" \
    --query 'Entries[0].[SuccessCode, EventId, ErrorCode, ErrorMessage]' \
    --output text)"
  read -r SUCCESS EVENT_ID ERROR_CODE ERROR_MESSAGE <<< "${RESULT}"
  if [ "${ERROR_CODE}" != "None" ]; then
    echo "error: seq=${seq} orderId=${ORDER_ID} failed: ${ERROR_CODE} ${ERROR_MESSAGE}" >&2
    exit 1
  fi
  echo "Published seq=${seq} orderId=${ORDER_ID} -> SuccessCode=${SUCCESS} EventId=${EVENT_ID}"
done

echo
echo "Give it a few seconds, then watch the consumer process the group in order:"
echo "  aws logs tail '${LOG_GROUP}' --region ${REGION} --since 5m --format short"
echo "The 'Processing order ... seq=' lines should appear in order 1..${COUNT}."
