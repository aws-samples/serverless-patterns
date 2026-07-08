#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# AgentCore Smithy Bedrock - Deployment Script (AWS SAM)
# ============================================================
# Orchestrates the full deployment lifecycle with AWS SAM:
#   1. Validate the SAM template
#   2. Upload the official Smithy model to S3
#   3. Build the Lambda with SAM (Makefile build — no Docker)
#   4. Deploy the stack with SAM
#   5. Create a Cognito test user
#   6. Generate scripts/test.sh
# ============================================================

STACK_NAME="${STACK_NAME:-agentcore-smithy-bedrock}"
REGION="${AWS_REGION:-us-east-1}"
TEMPLATE_PATH="infrastructure/template.yaml"
TEST_USERNAME="testuser"
TEST_PASSWORD="TestPass123!"

echo "============================================================"
echo "Deploying stack: ${STACK_NAME} in region: ${REGION}"
echo "============================================================"

# ============================================================
# Step 1: Validate the SAM template
# ============================================================
echo ""
echo ">>> Step 1: Validating SAM template..."
sam validate \
    --template-file "${TEMPLATE_PATH}" \
    --region "${REGION}" > /dev/null
echo "Template validation successful."

# ============================================================
# Step 2: Upload official Smithy model to S3
# ============================================================
echo ""
echo ">>> Step 2: Uploading Bedrock Runtime Smithy model to S3..."
SMITHY_BUCKET="${STACK_NAME}-smithy-models"
SMITHY_MODEL_URL="https://raw.githubusercontent.com/aws/api-models-aws/main/models/bedrock-runtime/service/2023-09-30/bedrock-runtime-2023-09-30.json"
SMITHY_MODEL_FILE="/tmp/bedrock-runtime-2023-09-30.json"

curl -sL "${SMITHY_MODEL_URL}" -o "${SMITHY_MODEL_FILE}"
aws s3 mb "s3://${SMITHY_BUCKET}" --region "${REGION}" 2>/dev/null || true
aws s3 cp "${SMITHY_MODEL_FILE}" "s3://${SMITHY_BUCKET}/bedrock-runtime-2023-09-30.json" --region "${REGION}"
echo "Smithy model uploaded to s3://${SMITHY_BUCKET}/bedrock-runtime-2023-09-30.json"

# ============================================================
# Step 3: Build the Lambda with SAM (Makefile build, no Docker)
# ============================================================
echo ""
echo ">>> Step 3: Building Lambda with SAM (Makefile build)..."
sam build \
    --template-file "${TEMPLATE_PATH}"
echo "SAM build complete."

# ============================================================
# Step 4: Deploy the stack with SAM
# ============================================================
echo ""
echo ">>> Step 4: Deploying stack with SAM..."
sam deploy \
    --stack-name "${STACK_NAME}" \
    --region "${REGION}" \
    --capabilities CAPABILITY_NAMED_IAM \
    --resolve-s3 \
    --no-confirm-changeset \
    --no-fail-on-empty-changeset \
    --parameter-overrides "GatewayName=smithy-bedrock-gateway"
echo "SAM deploy complete."

# ============================================================
# Retrieve stack outputs
# ============================================================
echo ""
echo ">>> Retrieving stack outputs..."

GATEWAY_ID=$(aws cloudformation describe-stacks \
    --stack-name "${STACK_NAME}" \
    --region "${REGION}" \
    --query "Stacks[0].Outputs[?OutputKey=='GatewayId'].OutputValue" \
    --output text)

COGNITO_USER_POOL_ID=$(aws cloudformation describe-stacks \
    --stack-name "${STACK_NAME}" \
    --region "${REGION}" \
    --query "Stacks[0].Outputs[?OutputKey=='CognitoUserPoolId'].OutputValue" \
    --output text)

COGNITO_CLIENT_ID=$(aws cloudformation describe-stacks \
    --stack-name "${STACK_NAME}" \
    --region "${REGION}" \
    --query "Stacks[0].Outputs[?OutputKey=='CognitoClientId'].OutputValue" \
    --output text)

LAMBDA_FUNCTION_NAME=$(aws cloudformation describe-stacks \
    --stack-name "${STACK_NAME}" \
    --region "${REGION}" \
    --query "Stacks[0].Outputs[?OutputKey=='LambdaFunctionName'].OutputValue" \
    --output text)

echo "Gateway ID: ${GATEWAY_ID}"
echo "Cognito User Pool ID: ${COGNITO_USER_POOL_ID}"
echo "Cognito Client ID: ${COGNITO_CLIENT_ID}"
echo "Lambda Function: ${LAMBDA_FUNCTION_NAME}"

# ============================================================
# Step 5: Create Cognito test user
# ============================================================
echo ""
echo ">>> Step 5: Creating Cognito test user..."

aws cognito-idp admin-create-user \
    --user-pool-id "${COGNITO_USER_POOL_ID}" \
    --username "${TEST_USERNAME}" \
    --temporary-password "${TEST_PASSWORD}" \
    --message-action SUPPRESS \
    --region "${REGION}" 2>/dev/null || echo "User may already exist, continuing..."

aws cognito-idp admin-set-user-password \
    --user-pool-id "${COGNITO_USER_POOL_ID}" \
    --username "${TEST_USERNAME}" \
    --password "${TEST_PASSWORD}" \
    --permanent \
    --region "${REGION}"

echo "Cognito test user created (username: ${TEST_USERNAME})."

# ============================================================
# Step 6: Generate test script (scripts/test.sh)
# ============================================================
echo ""
echo ">>> Step 6: Generating test script..."

cat > scripts/test.sh << 'TESTSCRIPT_EOF'
#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# AgentCore Smithy Bedrock - Test Script
# Generated by deploy.sh — do not edit manually
# ============================================================

TESTSCRIPT_EOF

# Append baked-in configuration values (not inside heredoc to allow variable expansion)
cat >> scripts/test.sh << BAKED_VALUES_EOF
REGION="${REGION}"
GATEWAY_ID="${GATEWAY_ID}"
COGNITO_USER_POOL_ID="${COGNITO_USER_POOL_ID}"
COGNITO_CLIENT_ID="${COGNITO_CLIENT_ID}"
LAMBDA_FUNCTION_NAME="${LAMBDA_FUNCTION_NAME}"
TEST_USERNAME="${TEST_USERNAME}"
TEST_PASSWORD="${TEST_PASSWORD}"
BAKED_VALUES_EOF

# Append the rest of the script logic using a non-expanding heredoc
cat >> scripts/test.sh << 'TESTSCRIPT_LOGIC_EOF'

PROMPT="${1:-Use the invoke model tool to ask Claude Haiku to write a short poem about the Beatles}"

echo "============================================================"
echo "Testing AgentCore Smithy Bedrock Agent"
echo "============================================================"
echo "Region: ${REGION}"
echo "Lambda: ${LAMBDA_FUNCTION_NAME}"
echo "Prompt: ${PROMPT}"
echo ""

# Authenticate with Cognito
echo ">>> Authenticating with Cognito..."
AUTH_RESULT=$(aws cognito-idp initiate-auth \
    --auth-flow USER_PASSWORD_AUTH \
    --client-id "${COGNITO_CLIENT_ID}" \
    --auth-parameters USERNAME="${TEST_USERNAME}",PASSWORD="${TEST_PASSWORD}" \
    --region "${REGION}" \
    --query "AuthenticationResult.IdToken" \
    --output text)

ID_TOKEN="${AUTH_RESULT}"
echo "Authentication successful."

# Build the Lambda payload
PAYLOAD_FILE="/tmp/test-payload-$$.json"
rm -f "${PAYLOAD_FILE}"
cat > "${PAYLOAD_FILE}" << PAYLOAD_INNER_EOF
{
    "headers": {
        "Authorization": "Bearer ${ID_TOKEN}"
    },
    "body": {
        "prompt": "${PROMPT}"
    }
}
PAYLOAD_INNER_EOF

# Invoke the Lambda function
echo ""
echo ">>> Invoking Lambda function..."
OUTPUT_FILE="/tmp/test-output-$$.json"
rm -f "${OUTPUT_FILE}"

aws lambda invoke \
    --function-name "${LAMBDA_FUNCTION_NAME}" \
    --payload "file://${PAYLOAD_FILE}" \
    --region "${REGION}" \
    --cli-binary-format raw-in-base64-out \
    "${OUTPUT_FILE}" > /dev/null

echo ""
echo ">>> Response:"
cat "${OUTPUT_FILE}"
echo ""

# Cleanup
rm -f "${PAYLOAD_FILE}" "${OUTPUT_FILE}"

echo ""
echo "============================================================"
echo "Test complete."
echo "============================================================"
TESTSCRIPT_LOGIC_EOF

chmod +x scripts/test.sh
echo "Test script generated at scripts/test.sh"

# ============================================================
# Deployment complete
# ============================================================
echo ""
echo "============================================================"
echo "Deployment complete!"
echo "============================================================"
echo ""
echo "To test the agent, run:"
echo "  ./scripts/test.sh"
echo "  ./scripts/test.sh \"Use the invoke model tool to ask Haiku to write a short poem about the Beatles\""
echo ""
