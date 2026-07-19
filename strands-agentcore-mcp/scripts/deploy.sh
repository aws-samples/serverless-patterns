#!/usr/bin/env bash
# =============================================================================
# deploy.sh — One-command deploy for strands-agentcore-mcp (AWS SAM)
#
# Usage:
#   ./scripts/deploy.sh
#
# Prerequisites: AWS SAM CLI + pip3 (Python 3.12). No Docker required —
# the build is Docker-free via the root Makefile's BuildMethod: makefile
# targets, which run the two-step pip3 manylinux install during `sam build`.
#
# What it does (in order):
#   1. Build the SAM application (sam build — Docker-free, Makefile-driven)
#   2. Deploy the SAM application (sam deploy — reads samconfig.toml)
#   3. Read stack outputs
#   4. Create or update the AgentCore MCP Target (boto3) + synchronize
#   5. Seed DynamoDB with sample products
#   6. Create Cognito test user
#   7. Generate scripts/test.sh with baked-in deployment values
# =============================================================================
set -euo pipefail

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
REGION="us-east-1"
STACK_NAME="agentcore-mcp"
TEMPLATE_FILE="infrastructure/template.yaml"

# Test user credentials (baked into generated test.sh)
TEST_USERNAME="testuser"
TEST_PASSWORD="TestPass123!"
TEST_EMAIL="testuser@example.com"

# PID-based temp files — macOS-compatible (no mktemp suffix templates)
TMP_STACK_OUTPUT="/tmp/agentcore-mcp.$$.stack-output.json"

# ---------------------------------------------------------------------------
# Cleanup trap — runs on exit (success or failure)
# ---------------------------------------------------------------------------
cleanup() {
  rm -rf \
    "$TMP_STACK_OUTPUT" \
    2>/dev/null || true
}
trap cleanup EXIT

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
log() { echo "[deploy] $*"; }
die() { echo "[deploy] ERROR: $*" >&2; exit 1; }

# ---------------------------------------------------------------------------
# STEP 1: Build the SAM application (Requirement 2.1, 10.1)
#
# Docker-free: each function declares Metadata.BuildMethod: makefile, so
# `sam build` invokes the root Makefile's build-<FunctionLogicalId> targets,
# which run the proven two-step pip3 manylinux install. No --use-container,
# no Docker daemon required.
# ---------------------------------------------------------------------------
log "Step 1: Building SAM application..."
sam build --template "$TEMPLATE_FILE"
log "Build complete."

# ---------------------------------------------------------------------------
# STEP 2: Deploy the SAM application (Requirement 10.1, 10.2)
#
# All deploy parameters (stack name, region, capabilities, resolve_s3,
# parameter_overrides, fail_on_empty_changeset=false) live in samconfig.toml,
# so no flags are passed here. SAM handles create-vs-update automatically and
# tolerates no-op changesets.
# ---------------------------------------------------------------------------
log "Step 2: Deploying SAM application (stack '$STACK_NAME')..."
sam deploy
log "Deploy complete."

# ---------------------------------------------------------------------------
# Read stack outputs
#
# Prefer `sam list stack-outputs` (Requirement 12.2); fall back to
# `aws cloudformation describe-stacks` if `sam list` fails or is unavailable.
# The two sources produce different JSON shapes:
#   - sam list stack-outputs: a flat array of {OutputKey, OutputValue}
#   - describe-stacks:        an object with Stacks[0].Outputs (same item shape)
# The parser below detects which shape it received and extracts accordingly.
# ---------------------------------------------------------------------------
log "Reading stack outputs..."
if sam list stack-outputs \
     --stack-name "$STACK_NAME" \
     --region "$REGION" \
     --output json \
     > "$TMP_STACK_OUTPUT" 2>/dev/null; then
  log "  Read outputs via 'sam list stack-outputs'."
else
  log "  'sam list stack-outputs' unavailable — falling back to describe-stacks."
  aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --region "$REGION" \
    > "$TMP_STACK_OUTPUT"
fi

# Parse outputs into shell variables.
# Write the Python script to a temp file to avoid shell brace-expansion issues
# with dict comprehensions inside eval "$(...)".
TMP_PARSE_PY="/tmp/agentcore-mcp.$$.parse.py"
cat > "$TMP_PARSE_PY" << 'PYEOF'
import json, sys

data = json.load(open(sys.argv[1]))

# Detect source shape:
#   - sam list stack-outputs -> a list of {OutputKey, OutputValue}
#   - describe-stacks        -> {'Stacks': [{'Outputs': [...]}]}
if isinstance(data, list):
    raw_outputs = data
elif isinstance(data, dict) and 'Stacks' in data:
    raw_outputs = data['Stacks'][0].get('Outputs', [])
else:
    raw_outputs = data.get('Outputs', []) if isinstance(data, dict) else []

outputs = {}
for o in raw_outputs:
    outputs[o['OutputKey']] = o['OutputValue']

keys = [
    'AgentLambdaName',
    'McpServerLambdaName',
    'CognitoUserPoolId',
    'CognitoClientId',
    'McpApiInvokeUrl',
    'GatewayUrl',
    'ProductTableName',
    'GatewayId',
]
for k in keys:
    v = outputs.get(k, '')
    v_escaped = v.replace("'", "'\\''")
    print(f"{k}='{v_escaped}'")
PYEOF

eval "$(python3 "$TMP_PARSE_PY" "$TMP_STACK_OUTPUT")"
rm -f "$TMP_PARSE_PY"

log "  AgentLambdaName:     $AgentLambdaName"
log "  McpServerLambdaName: $McpServerLambdaName"
log "  CognitoUserPoolId:   $CognitoUserPoolId"
log "  CognitoClientId:     $CognitoClientId"
log "  McpApiInvokeUrl:     $McpApiInvokeUrl"
log "  GatewayUrl:          $GatewayUrl"
log "  ProductTableName:    $ProductTableName"
log "  GatewayId:           $GatewayId"

# ---------------------------------------------------------------------------
# STEP 5b: Create or update the AgentCore MCP Target
#
# McpTarget is NOT in the CloudFormation template because AgentCore probes
# tools/list during target creation — the placeholder Lambda would return a
# non-MCP response causing a Forbidden error. We create it here after the
# real Lambda code is deployed.
#
# We use the AWS CLI (bedrock-agentcore-control) to create/update the target.
# ---------------------------------------------------------------------------
log "Step 5b: Creating/updating AgentCore MCP Target..."

# GatewayId is read from the stack outputs above (first-class output).
GATEWAY_ID="$GatewayId"

log "  Gateway ID: $GATEWAY_ID"
log "  MCP Endpoint: $McpApiInvokeUrl"

MCP_ENDPOINT="$McpApiInvokeUrl"
TMP_TARGET_OUTPUT="/tmp/agentcore-mcp.$$.target-output.json"

# Check if target already exists
EXISTING_TARGET_ID=$(aws bedrock-agentcore-control list-gateway-targets \
  --gateway-identifier "$GATEWAY_ID" \
  --region "$REGION" \
  --query "items[?name=='mcp-server-target'].targetId" \
  --output text 2>/dev/null || echo "")

if [ -z "$EXISTING_TARGET_ID" ] || [ "$EXISTING_TARGET_ID" = "None" ]; then
  log "  Creating new MCP target..."
  # Use boto3 directly — the AWS CLI's local schema validation rejects
  # iamCredentialProvider even though the service requires it for mcpServer targets.
  TMP_TARGET_PY="/tmp/agentcore-mcp.$$.target.py"
  cat > "$TMP_TARGET_PY" << PYEOF
import boto3, sys, json

client = boto3.client('bedrock-agentcore-control', region_name=sys.argv[1])
resp = client.create_gateway_target(
    gatewayIdentifier=sys.argv[2],
    name='mcp-server-target',
    description='MCP target pointing at the API Gateway HTTPS endpoint',
    credentialProviderConfigurations=[{
        'credentialProviderType': 'GATEWAY_IAM_ROLE',
        'credentialProvider': {
            'iamCredentialProvider': {
                'service': 'execute-api'
            }
        }
    }],
    targetConfiguration={
        'mcp': {
            'mcpServer': {
                'endpoint': sys.argv[3]
            }
        }
    }
)
print(json.dumps({'targetId': resp.get('targetId', '')}))
PYEOF
  python3 "$TMP_TARGET_PY" "$REGION" "$GATEWAY_ID" "$MCP_ENDPOINT" > "$TMP_TARGET_OUTPUT"
  rm -f "$TMP_TARGET_PY"
  TARGET_ID=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1])).get('targetId',''))" "$TMP_TARGET_OUTPUT")
  log "  MCP target created (targetId: $TARGET_ID)."
else
  log "  Updating existing MCP target ($EXISTING_TARGET_ID)..."
  TMP_TARGET_PY="/tmp/agentcore-mcp.$$.target.py"
  cat > "$TMP_TARGET_PY" << PYEOF
import boto3, sys, json

client = boto3.client('bedrock-agentcore-control', region_name=sys.argv[1])
resp = client.update_gateway_target(
    gatewayIdentifier=sys.argv[2],
    targetId=sys.argv[3],
    name='mcp-server-target',
    description='MCP target pointing at the API Gateway HTTPS endpoint',
    credentialProviderConfigurations=[{
        'credentialProviderType': 'GATEWAY_IAM_ROLE',
        'credentialProvider': {
            'iamCredentialProvider': {
                'service': 'execute-api'
            }
        }
    }],
    targetConfiguration={
        'mcp': {
            'mcpServer': {
                'endpoint': sys.argv[4]
            }
        }
    }
)
print(json.dumps({'targetId': resp.get('targetId', '')}))
PYEOF
  python3 "$TMP_TARGET_PY" "$REGION" "$GATEWAY_ID" "$EXISTING_TARGET_ID" "$MCP_ENDPOINT" > "$TMP_TARGET_OUTPUT"
  rm -f "$TMP_TARGET_PY"
  TARGET_ID="$EXISTING_TARGET_ID"
  log "  MCP target updated."
fi

# Synchronize the target so the gateway indexes the tools from the MCP server.
# Without this, tools/list returns 0 tools and the agent has nothing to call.
log "  Synchronizing MCP target to index tools..."
TMP_SYNC_PY="/tmp/agentcore-mcp.$$.sync.py"
cat > "$TMP_SYNC_PY" << PYEOF
import boto3, sys, json, time

client = boto3.client('bedrock-agentcore-control', region_name=sys.argv[1])
gateway_id = sys.argv[2]
target_id = sys.argv[3]

# Wait for target to reach a stable state before synchronizing
print("  Waiting for target to reach stable state...", flush=True)
for _ in range(36):  # up to 3 minutes
    resp = client.get_gateway_target(
        gatewayIdentifier=gateway_id,
        targetId=target_id
    )
    status = resp.get('status', '')
    print(f"  Target status: {status}", flush=True)
    if status not in ('CREATING', 'UPDATING', 'SYNCHRONIZING'):
        break
    time.sleep(5)

# Trigger synchronization
print("  Triggering synchronization...", flush=True)
client.synchronize_gateway_targets(
    gatewayIdentifier=gateway_id,
    targetIdList=[target_id]
)

# Poll until sync completes
for _ in range(36):  # up to 3 minutes
    resp = client.get_gateway_target(
        gatewayIdentifier=gateway_id,
        targetId=target_id
    )
    status = resp.get('status', '')
    reasons = resp.get('statusReasons', [])
    print(f"  Target status: {status}", flush=True)
    if status not in ('SYNCHRONIZING', 'CREATING', 'UPDATING'):
        if reasons:
            print(f"  Status reasons: {reasons}", flush=True)
        break
    time.sleep(5)

print(f"Final status: {status}")
PYEOF
python3 "$TMP_SYNC_PY" "$REGION" "$GATEWAY_ID" "$TARGET_ID"
rm -f "$TMP_SYNC_PY"
log "  MCP target synchronized."

rm -f "$TMP_TARGET_OUTPUT"

# ---------------------------------------------------------------------------
# STEP 6: Seed DynamoDB with sample products (Requirement 10.4)
#
# At least three items across at least two categories.
# DynamoDB attribute-value JSON format.
# ---------------------------------------------------------------------------
log "Step 6: Seeding DynamoDB table '$ProductTableName'..."

aws dynamodb put-item \
  --table-name "$ProductTableName" \
  --item '{
    "category":  {"S": "Electronics"},
    "productId": {"S": "ELEC-001"},
    "name":      {"S": "Noise-cancelling Headphones"},
    "price":     {"N": "199.99"}
  }' \
  --region "$REGION"

aws dynamodb put-item \
  --table-name "$ProductTableName" \
  --item '{
    "category":  {"S": "Electronics"},
    "productId": {"S": "ELEC-002"},
    "name":      {"S": "Wireless Keyboard"},
    "price":     {"N": "79.99"}
  }' \
  --region "$REGION"

aws dynamodb put-item \
  --table-name "$ProductTableName" \
  --item '{
    "category":  {"S": "Books"},
    "productId": {"S": "BOOK-001"},
    "name":      {"S": "Clean Code"},
    "price":     {"N": "34.99"}
  }' \
  --region "$REGION"

log "  Seeded 3 products (Electronics x2, Books x1)."

# ---------------------------------------------------------------------------
# STEP 7: Create Cognito test user (Requirement 10.5)
# ---------------------------------------------------------------------------
log "Step 7: Creating Cognito test user '$TEST_USERNAME'..."

# Create user (suppress welcome email)
aws cognito-idp admin-create-user \
  --user-pool-id "$CognitoUserPoolId" \
  --username "$TEST_USERNAME" \
  --user-attributes "Name=email,Value=${TEST_EMAIL}" \
  --message-action SUPPRESS \
  --region "$REGION" \
  > /dev/null 2>&1 || log "  User '$TEST_USERNAME' already exists — skipping create."

# Set permanent password (confirms the user)
aws cognito-idp admin-set-user-password \
  --user-pool-id "$CognitoUserPoolId" \
  --username "$TEST_USERNAME" \
  --password "$TEST_PASSWORD" \
  --permanent \
  --region "$REGION"

log "  Test user '$TEST_USERNAME' is CONFIRMED."

# ---------------------------------------------------------------------------
# STEP 8: Generate scripts/test.sh with baked-in literal values
#
# Rules (Requirements 11.3, 11.4, 11.5):
#   - Use a heredoc + sed substitution (NOT nested echo emitting JSON)
#   - Bake in USER_POOL_ID, CLIENT_ID, AGENT_LAMBDA_NAME, USERNAME, PASSWORD
#   - Accept $1 as optional prompt, fall back to DEFAULT_PROMPT
#   - Obtain ID token via initiate-auth USER_PASSWORD_AUTH
#   - Invoke Agent Lambda with {"jwt": "<id_token>", "prompt": "<prompt>"}
#   - Print the model's final answer
# ---------------------------------------------------------------------------
log "Step 8: Generating scripts/test.sh..."

# Write the template with placeholder tokens
cat > scripts/test.sh <<'EOF'
#!/usr/bin/env bash
# =============================================================================
# test.sh — End-to-end smoke test for strands-agentcore-mcp
#
# Generated by deploy.sh — do not edit manually.
#
# Usage:
#   ./scripts/test.sh                                      # default prompt
#   ./scripts/test.sh 'List all products in Electronics'
#   ./scripts/test.sh 'Get product ELEC-001 details'
#   ./scripts/test.sh 'Add a new product called Widget'
# =============================================================================
set -euo pipefail

# ---------------------------------------------------------------------------
# Baked-in deployment values (substituted by deploy.sh)
# ---------------------------------------------------------------------------
USER_POOL_ID="__USER_POOL_ID__"
CLIENT_ID="__CLIENT_ID__"
AGENT_LAMBDA_NAME="__AGENT_LAMBDA_NAME__"
USERNAME="__USERNAME__"
PASSWORD="__PASSWORD__"
DEFAULT_PROMPT="List all products."
REGION="us-east-1"

# ---------------------------------------------------------------------------
# Accept optional prompt argument
# ---------------------------------------------------------------------------
PROMPT="${1:-$DEFAULT_PROMPT}"

echo "[test] Authenticating as '$USERNAME'..."

# ---------------------------------------------------------------------------
# Obtain ID token via USER_PASSWORD_AUTH
# ---------------------------------------------------------------------------
AUTH_RESULT=$(aws cognito-idp initiate-auth \
  --auth-flow USER_PASSWORD_AUTH \
  --client-id "$CLIENT_ID" \
  --auth-parameters "USERNAME=${USERNAME},PASSWORD=${PASSWORD}" \
  --region "$REGION" \
  --output json)

ID_TOKEN=$(echo "$AUTH_RESULT" | python3 -c "
import json, sys
data = json.load(sys.stdin)
print(data['AuthenticationResult']['IdToken'])
")

echo "[test] Authenticated. Invoking agent with prompt: $PROMPT"

# ---------------------------------------------------------------------------
# Invoke Agent Lambda
# Payload written to a temp file to avoid shell quoting / JSON injection issues
# ---------------------------------------------------------------------------
TMP_PAYLOAD="/tmp/test-payload.$$.json"
TMP_RESPONSE="/tmp/test-response.$$.json"
trap 'rm -f "$TMP_PAYLOAD" "$TMP_RESPONSE"' EXIT

python3 -c "
import json, sys
payload = {'jwt': sys.argv[1], 'prompt': sys.argv[2]}
print(json.dumps(payload))
" "$ID_TOKEN" "$PROMPT" > "$TMP_PAYLOAD"

aws lambda invoke \
  --function-name "$AGENT_LAMBDA_NAME" \
  --payload "fileb://${TMP_PAYLOAD}" \
  --region "$REGION" \
  --cli-binary-format raw-in-base64-out \
  "$TMP_RESPONSE" \
  > /dev/null

echo ""
echo "=== Agent Response ==="
python3 -c "
import json, sys
data = json.load(open(sys.argv[1]))
# AgentResponse dataclass: {success, response, error}
if isinstance(data, dict) and 'response' in data:
    print(data['response'])
else:
    print(json.dumps(data, indent=2))
" "$TMP_RESPONSE"
EOF

# Substitute placeholder tokens with actual deployment values using sed
# (literal string substitution — no nested echo emitting JSON)
sed -i.bak \
  -e "s|__USER_POOL_ID__|${CognitoUserPoolId}|g" \
  -e "s|__CLIENT_ID__|${CognitoClientId}|g" \
  -e "s|__AGENT_LAMBDA_NAME__|${AgentLambdaName}|g" \
  -e "s|__USERNAME__|${TEST_USERNAME}|g" \
  -e "s|__PASSWORD__|${TEST_PASSWORD}|g" \
  scripts/test.sh

# Remove sed backup file
rm -f scripts/test.sh.bak

chmod +x scripts/test.sh
log "  Generated scripts/test.sh"

# ---------------------------------------------------------------------------
# Done
# ---------------------------------------------------------------------------
log ""
log "============================================================"
log "Deployment complete!"
log "============================================================"
log ""
log "Run the smoke test:"
log "  ./scripts/test.sh"
log ""
log "Or with a custom prompt:"
log "  ./scripts/test.sh 'List all products in Electronics'"
log "  ./scripts/test.sh 'Get product ELEC-001 details'"
log ""
