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
# Stack name and region default to the values `sam deploy --guided` saved in
# samconfig.toml, so after a guided deploy no arguments are needed.
#
# Requires: the stack already deployed with `sam deploy`, a JDK 21+, and Maven.
# The publisher is run from the shaded jar (built with `mvn clean package` if not
# already present).
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SAMCONFIG="${HERE}/samconfig.toml"

# Read a key (e.g. stack_name, region) from samconfig.toml. SAM CLI may save a
# key under [default.deploy.parameters] or [default.global.parameters], so the
# deploy section wins and the global section is the fallback. Prints nothing if
# the file or key is absent.
samconfig_get() {
  [ -f "${SAMCONFIG}" ] || return 0
  awk -v key="$1" '
    /^\[/ { section = $0; next }
    $1 == key && (section == "[default.deploy.parameters]" || section == "[default.global.parameters]") {
      val = $0
      sub(/^[^=]*=[[:space:]]*/, "", val)
      gsub(/^"|"[[:space:]]*$/, "", val)
      if (section == "[default.deploy.parameters]") deploy = val
      else global = val
    }
    END { print (deploy != "" ? deploy : global) }
  ' "${SAMCONFIG}"
}

STACK_NAME="${1:-$(samconfig_get stack_name)}"
# Region resolution order: positional arg, then samconfig.toml, then
# $AWS_REGION / $AWS_DEFAULT_REGION, then the region in your AWS CLI profile.
REGION="${2:-$(samconfig_get region)}"
REGION="${REGION:-${AWS_REGION:-${AWS_DEFAULT_REGION:-$(aws configure get region 2>/dev/null || true)}}}"
ORDER_ID="${3:-order-$(date +%s)}"

if [ -z "${STACK_NAME}" ]; then
  echo "error: no stack name. Run 'sam deploy --guided' (which saves it to samconfig.toml)," >&2
  echo "       or pass the stack name as the 1st argument." >&2
  exit 1
fi

if [ -z "${REGION}" ]; then
  echo "error: no AWS region set. Pass one as the 2nd argument, export AWS_REGION," >&2
  echo "       or set a default with 'aws configure'." >&2
  exit 1
fi

get_output() {
  aws cloudformation describe-stacks \
    --stack-name "${STACK_NAME}" --region "${REGION}" \
    --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text
}

REGISTRY_ARN="$(get_output SchemaRegistryArn)"
LOG_GROUP="$(get_output ConsumerLogGroup)"
BUS_ARN="$(get_output EventBusArn)"

if [ "${BUS_ARN}" = "None" ] || [ -z "${BUS_ARN}" ]; then
  echo "error: EventBusArn not found in stack '${STACK_NAME}' (${REGION})." >&2
  echo "       Deploy it first with 'sam build && sam deploy --guided --capabilities CAPABILITY_NAMED_IAM'." >&2
  exit 1
fi

# Build the shaded jar if it is not already present. Use `clean` so a prior
# `sam build` (which writes into target/) can't leave a stale incremental state
# that breaks the compile.
JAR="${HERE}/target/eventbridge-custom-avro-sam-java-1.0.0.jar"
if [ ! -f "${JAR}" ]; then
  echo "Building the publisher jar (mvn clean package)..."
  (cd "${HERE}" && mvn -q -DskipTests clean package)
fi

echo "Stack:    ${STACK_NAME} (${REGION})"
echo "Bus:      ${BUS_ARN}"
echo "Registry: ${REGISTRY_ARN}"
echo "Publishing orderId=${ORDER_ID}..."

BUS_ARN="${BUS_ARN}" REGISTRY_ARN="${REGISTRY_ARN}" AWS_REGION="${REGION}" \
  java -jar "${JAR}" --order-id "${ORDER_ID}"

echo
echo "Give delivery a few seconds, then check the delivered event in CloudWatch:"
echo "  aws logs tail '${LOG_GROUP}' --region ${REGION} --since 5m --format short"
