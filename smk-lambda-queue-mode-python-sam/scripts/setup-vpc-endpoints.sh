#!/usr/bin/env bash
# setup-vpc-endpoints.sh — Create VPC interface endpoints required for Queue mode
#
# ESM pollers run in private subnets and require three VPC endpoints:
#   lambda  — to invoke the Lambda function
#   sts     — to obtain temporary credentials
#   sqs     — to write failed records to the OnFailure DLQ
#
# IMPORTANT: All three are required. Missing the SQS endpoint causes a silent
# connection error — the ESM stays Enabled/OK but Lambda stops being invoked
# after the first batch when a failed record triggers a DLQ write.
#
# This script is idempotent — it skips endpoints that already exist.
#
# Usage (Path A — full deploy, resolves VPC from kafka-queue-network stack):
#   ./scripts/setup-vpc-endpoints.sh --region <region> --profile <profile>
#
# Usage (Path B/C — BYO VPC, provide values directly):
#   ./scripts/setup-vpc-endpoints.sh --region <region> --profile <profile> \
#     --vpc-id vpc-xxx \
#     --subnet-ids "subnet-a,subnet-b,subnet-c" \
#     --security-group-id sg-xxx
#
# If your VPC already has these endpoints, this script will skip them.

set -euo pipefail

REGION="${AWS_DEFAULT_REGION:-us-east-1}"
PROFILE="${AWS_PROFILE:-default}"
NETWORK_STACK="kafka-queue-network"
VPC_ID=""
SUBNET_IDS=""
SG_ID=""

while [[ $# -gt 0 ]]; do
  case $1 in
    --region)           REGION="$2";   shift 2 ;;
    --profile)          PROFILE="$2";  shift 2 ;;
    --vpc-id)           VPC_ID="$2";   shift 2 ;;
    --subnet-ids)       SUBNET_IDS="$2"; shift 2 ;;
    --security-group-id) SG_ID="$2";  shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

echo "=== Setting up VPC endpoints ==="
echo "  Region:  $REGION"
echo "  Profile: $PROFILE"
echo ""

# ── Resolve from stack outputs if not provided ────────────────
if [ -z "$VPC_ID" ]; then
  echo "Resolving VPC config from stack $NETWORK_STACK..."
  get_output() {
    aws cloudformation describe-stacks \
      --stack-name "$NETWORK_STACK" --profile "$PROFILE" --region "$REGION" \
      --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" \
      --output text
  }
  VPC_ID=$(get_output "VpcId")
  SUBNET_A=$(get_output "PrivateSubnetA")
  SUBNET_B=$(get_output "PrivateSubnetB")
  SUBNET_C=$(get_output "PrivateSubnetC")
  SG_ID=$(get_output "LambdaSecurityGroupId")
  SUBNET_IDS="$SUBNET_A $SUBNET_B $SUBNET_C"
else
  echo "Using provided VPC config..."
  # Convert comma-separated to space-separated for aws CLI
  SUBNET_IDS="${SUBNET_IDS//,/ }"
fi

echo "  VPC:     $VPC_ID"
echo "  Subnets: $SUBNET_IDS"
echo "  SG:      $SG_ID"
echo ""

# ── Create endpoints ─────────────────────────────────────────
for SVC in lambda sts sqs; do
  EXISTING=$(aws ec2 describe-vpc-endpoints \
    --profile "$PROFILE" --region "$REGION" \
    --filters \
      "Name=service-name,Values=com.amazonaws.$REGION.$SVC" \
      "Name=vpc-id,Values=$VPC_ID" \
      "Name=vpc-endpoint-state,Values=available,pending" \
    --query 'VpcEndpoints[0].VpcEndpointId' \
    --output text 2>/dev/null)

  if [ "$EXISTING" = "None" ] || [ -z "$EXISTING" ]; then
    echo "Creating $SVC endpoint..."
    EPID=$(aws ec2 create-vpc-endpoint \
      --vpc-id "$VPC_ID" \
      --service-name "com.amazonaws.$REGION.$SVC" \
      --vpc-endpoint-type Interface \
      --subnet-ids $SUBNET_IDS \
      --security-group-ids "$SG_ID" \
      --private-dns-enabled \
      --profile "$PROFILE" --region "$REGION" \
      --query 'VpcEndpoint.VpcEndpointId' \
      --output text)
    echo "  Created: $EPID"
  else
    echo "$SVC endpoint already exists: $EXISTING (skipping)"
  fi
done

echo ""
echo "All VPC endpoints in place. Wait ~30s for endpoints to become available,"
echo "then run ./scripts/create-esm.sh to create the Queue mode ESM."
