#!/usr/bin/env bash
# =============================================================================
# terminate.sh — Tear down all resources for strands-agentcore-mcp
#
# Usage:
#   ./scripts/terminate.sh
#
# What it does (in order):
#   1. Delete the MCP Gateway Target (created outside CloudFormation)
#   2. Delete the CloudFormation stack (all other resources)
#   3. Wait for stack deletion to complete
#   4. Clean up the generated test.sh
# =============================================================================
set -euo pipefail

REGION="us-east-1"
STACK_NAME="agentcore-mcp"

log() { echo "[terminate] $*"; }
die() { echo "[terminate] ERROR: $*" >&2; exit 1; }

# ---------------------------------------------------------------------------
# STEP 1: Delete the MCP Gateway Target
#
# The target was created outside CloudFormation (via boto3 in deploy.sh)
# because AgentCore probes tools/list during CFN creation — the placeholder
# Lambda would fail that probe. So we must delete it manually here.
# ---------------------------------------------------------------------------
log "Step 1: Deleting AgentCore MCP Gateway Target..."

python3 - <<'PYEOF'
import boto3, sys

client = boto3.client('bedrock-agentcore-control', region_name='us-east-1')

# Find the gateway by name pattern from stack outputs
try:
    # Get gateway ID from CloudFormation stack output
    cfn = boto3.client('cloudformation', region_name='us-east-1')
    resp = cfn.describe_stacks(StackName='agentcore-mcp')
    outputs = {o['OutputKey']: o['OutputValue'] for o in resp['Stacks'][0].get('Outputs', [])}
    gateway_url = outputs.get('GatewayUrl', '')
    # Extract gateway ID from URL: https://<gateway-id>.gateway.bedrock-agentcore...
    gateway_id = gateway_url.replace('https://', '').split('.')[0]
    if not gateway_id:
        print('  No GatewayUrl output found — skipping target deletion')
        sys.exit(0)
    print(f'  Gateway ID: {gateway_id}')
except Exception as e:
    print(f'  Could not get stack outputs: {e} — skipping target deletion')
    sys.exit(0)

# List and delete all targets on this gateway
try:
    targets = client.list_gateway_targets(gatewayIdentifier=gateway_id)
    items = targets.get('items', [])
    if not items:
        print('  No targets found')
    for target in items:
        target_id = target['targetId']
        name = target.get('name', target_id)
        print(f'  Deleting target: {name} ({target_id})')
        client.delete_gateway_target(
            gatewayIdentifier=gateway_id,
            targetId=target_id
        )
        print(f'  Deleted: {name}')
except Exception as e:
    print(f'  Warning: could not delete targets: {e}')
PYEOF

log "  Gateway targets deleted."

# ---------------------------------------------------------------------------
# STEP 2: Delete the CloudFormation stack
# ---------------------------------------------------------------------------
log "Step 2: Deleting CloudFormation stack '$STACK_NAME'..."

# Check if stack exists first
TMP_ERR="/tmp/agentcore-mcp.$$.terminate-err.txt"
if ! aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --region "$REGION" \
    > /dev/null \
    2> "$TMP_ERR"; then
  if grep -qi "does not exist\|DOES_NOT_EXIST" "$TMP_ERR"; then
    log "  Stack '$STACK_NAME' does not exist — nothing to delete."
    rm -f "$TMP_ERR"
  else
    cat "$TMP_ERR" >&2
    rm -f "$TMP_ERR"
    die "Unexpected error checking stack '$STACK_NAME'"
  fi
else
  rm -f "$TMP_ERR"
  aws cloudformation delete-stack \
    --stack-name "$STACK_NAME" \
    --region "$REGION"

  log "  Waiting for stack deletion to complete (this may take a few minutes)..."
  aws cloudformation wait stack-delete-complete \
    --stack-name "$STACK_NAME" \
    --region "$REGION"
  log "  Stack '$STACK_NAME' deleted."
fi

# ---------------------------------------------------------------------------
# STEP 3: Clean up CloudWatch Log Groups
# ---------------------------------------------------------------------------
log "Step 3: Cleaning up CloudWatch Log Groups..."
for LOG_GROUP in \
  "/aws/lambda/${STACK_NAME}-agent" \
  "/aws/lambda/${STACK_NAME}-mcp-server"; do
  if aws logs describe-log-groups \
      --log-group-name-prefix "$LOG_GROUP" \
      --region "$REGION" \
      --query 'logGroups[0].logGroupName' \
      --output text 2>/dev/null | grep -q "$LOG_GROUP"; then
    aws logs delete-log-group \
      --log-group-name "$LOG_GROUP" \
      --region "$REGION" 2>/dev/null || true
    log "  Deleted log group: $LOG_GROUP"
  else
    log "  Log group not found: $LOG_GROUP — skipping."
  fi
done

# ---------------------------------------------------------------------------
# STEP 4: Clean up S3 deploy bucket (if it exists)
# ---------------------------------------------------------------------------
log "Step 4: Cleaning up S3 deploy bucket (if exists)..."
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text --region "$REGION" 2>/dev/null || echo "")
if [ -n "$ACCOUNT_ID" ]; then
  S3_BUCKET="${ACCOUNT_ID}-${STACK_NAME}-deploy"
  if aws s3api head-bucket --bucket "$S3_BUCKET" --region "$REGION" 2>/dev/null; then
    log "  Emptying and deleting s3://$S3_BUCKET..."
    aws s3 rm "s3://${S3_BUCKET}" --recursive --region "$REGION" 2>/dev/null || true
    aws s3api delete-bucket --bucket "$S3_BUCKET" --region "$REGION" 2>/dev/null || true
    log "  Deleted s3://$S3_BUCKET"
  else
    log "  S3 bucket $S3_BUCKET does not exist — skipping."
  fi
else
  log "  Could not determine account ID — skipping S3 cleanup."
fi

# ---------------------------------------------------------------------------
# STEP 4: Clean up generated scripts
# ---------------------------------------------------------------------------
log "Step 5: Cleaning up generated files..."
rm -f scripts/test.sh
log "  Removed scripts/test.sh"

# ---------------------------------------------------------------------------
# Done
# ---------------------------------------------------------------------------
log ""
log "============================================================"
log "Termination complete!"
log "============================================================"
log ""
log "All resources have been deleted:"
log "  - AgentCore Gateway Target"
log "  - CloudFormation stack (Lambda, API Gateway, DynamoDB,"
log "    Cognito, IAM roles, AgentCore Gateway)"
log "  - CloudWatch Log Groups"
log "  - S3 deploy bucket (if it existed)"
log "  - Generated scripts/test.sh"
log ""
log "To redeploy: ./scripts/deploy.sh"
log ""
