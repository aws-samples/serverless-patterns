#!/usr/bin/env bash
# create-esm.sh — Create a Kafka Queue mode ESM via direct API call
#
# ConsumptionMode: Queue is a pre-release field not yet in the CloudFormation
# or SAM schema. This script creates the ESM by calling the Lambda REST API
# directly using curl with AWS SigV4 signing, bypassing client-side validation.
#
# Prerequisites:
#   - aws CLI configured with appropriate credentials
#   - curl >= 7.75 (for --aws-sigv4 support)
#   - Stacks kafka-queue-network, kafka-queue-broker, kafka-queue-app must be deployed
#
# Usage:
#   ./scripts/create-esm.sh
#   ./scripts/create-esm.sh --region us-west-2 --profile myprofile

set -euo pipefail

# ── Defaults ─────────────────────────────────────────────────
REGION="${AWS_DEFAULT_REGION:-us-east-1}"
PROFILE="${AWS_PROFILE:-default}"
APP_STACK="kafka-queue-app"
BROKER_STACK="kafka-queue-broker"
NETWORK_STACK="kafka-queue-network"
CONSUMER_GROUP_ID="kafka-queue-group-$(date +%s)"
TOPIC="kafka-queue-task-worker"
MIN_POLLERS=2
MAX_POLLERS=10
MAX_RETRY_ATTEMPTS=3

# Parse optional flags
while [[ $# -gt 0 ]]; do
  case $1 in
    --region)     REGION="$2";  shift 2 ;;
    --profile)    PROFILE="$2"; shift 2 ;;
    --topic)      TOPIC="$2";   shift 2 ;;
    --group)      CONSUMER_GROUP_ID="$2"; shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

echo "=== Creating Kafka Queue mode ESM ==="
echo "  Region:        $REGION"
echo "  Profile:       $PROFILE"
echo "  Topic:         $TOPIC"
echo "  Consumer Group: $CONSUMER_GROUP_ID"
echo ""

# ── Resolve values from stack outputs ────────────────────────
get_output() {
  aws cloudformation describe-stacks \
    --stack-name "$1" --profile "$PROFILE" --region "$REGION" \
    --query "Stacks[0].Outputs[?OutputKey=='$2'].OutputValue" \
    --output text
}

echo "Fetching stack outputs..."
WORKER_ARN=$(get_output "$APP_STACK" "WorkerFunctionArn")
DLQ_ARN=$(get_output "$APP_STACK" "TaskWorkerDLQArn")
BOOTSTRAP=$(get_output "$BROKER_STACK" "BootstrapServers")
SUBNET_A=$(get_output "$NETWORK_STACK" "PrivateSubnetA")
SUBNET_B=$(get_output "$NETWORK_STACK" "PrivateSubnetB")
SUBNET_C=$(get_output "$NETWORK_STACK" "PrivateSubnetC")
LAMBDA_SG=$(get_output "$NETWORK_STACK" "LambdaSecurityGroupId")

echo "  Worker ARN:    $WORKER_ARN"
echo "  Bootstrap:     $BOOTSTRAP"
echo "  DLQ ARN:       $DLQ_ARN"
echo ""

# ── Export credentials for curl --aws-sigv4 ──────────────────
echo "Exporting credentials for SigV4 signing..."
unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN
eval "$(aws configure export-credentials --format env --profile "$PROFILE")"

# ── Create ESM via Lambda REST API ───────────────────────────
echo "Creating ESM..."
RESPONSE=$(curl -sS -X POST \
  "https://lambda.$REGION.amazonaws.com/2015-03-31/event-source-mappings/" \
  --aws-sigv4 "aws:amz:$REGION:lambda" \
  --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
  -H "x-amz-security-token: $AWS_SESSION_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"FunctionName\": \"$WORKER_ARN\",
    \"SelfManagedEventSource\": {
      \"Endpoints\": {\"KAFKA_BOOTSTRAP_SERVERS\": [\"$BOOTSTRAP\"]}
    },
    \"SelfManagedKafkaEventSourceConfig\": {
      \"ConsumerGroupId\": \"$CONSUMER_GROUP_ID\",
      \"ConsumptionMode\": \"Queue\"
    },
    \"Topics\": [\"$TOPIC\"],
    \"BatchSize\": 10,
    \"MaximumRetryAttempts\": $MAX_RETRY_ATTEMPTS,
    \"FunctionResponseTypes\": [\"ReportBatchItemFailures\"],
    \"DestinationConfig\": {
      \"OnFailure\": {\"Destination\": \"$DLQ_ARN\"}
    },
    \"ProvisionedPollerConfig\": {
      \"MinimumPollers\": $MIN_POLLERS,
      \"MaximumPollers\": $MAX_POLLERS
    },
    \"MetricsConfig\": {
      \"Metrics\": [\"EventCount\", \"ErrorCount\", \"KafkaMetrics\"]
    },
    \"SourceAccessConfigurations\": [
      {\"Type\": \"VPC_SUBNET\", \"URI\": \"subnet:$SUBNET_A\"},
      {\"Type\": \"VPC_SUBNET\", \"URI\": \"subnet:$SUBNET_B\"},
      {\"Type\": \"VPC_SUBNET\", \"URI\": \"subnet:$SUBNET_C\"},
      {\"Type\": \"VPC_SECURITY_GROUP\", \"URI\": \"security_group:$LAMBDA_SG\"}
    ]
  }")

echo "$RESPONSE" | python3 -c "
import sys, json
r = json.load(sys.stdin)
if 'Type' in r and r.get('Type') == 'User':
    print('ERROR:', r.get('message'))
    sys.exit(1)
print('ESM created!')
print('  UUID:            ', r.get('UUID'))
print('  State:           ', r.get('State'))
print('  ConsumptionMode: ', r.get('SelfManagedKafkaEventSourceConfig',{}).get('ConsumptionMode'))
print('  ProvisionedPollers:', r.get('ProvisionedPollerConfig'))
print()
print('Wait ~60s for State to reach Enabled, then produce records:')
print()
print('  aws lambda invoke \\\\')
print('    --function-name kafka-queue-app-producer \\\\')
print('    --region $REGION --profile $PROFILE \\\\')
print('    --cli-binary-format raw-in-base64-out \\\\')
print('    --payload \'{"count": 20}\' /dev/stdout')
print()
print('Watch logs:')
print('  aws logs tail /aws/lambda/kafka-queue-app-worker --follow \\\\')
print('    --filter-pattern KAFKA_RECORD \\\\')
print('    --region $REGION --profile $PROFILE')
" REGION="$REGION" PROFILE="$PROFILE"
