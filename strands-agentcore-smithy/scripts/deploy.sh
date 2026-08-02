#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# AgentCore Smithy Bedrock - Deployment Script
# ============================================================
# Orchestrates the full deployment lifecycle:
#   1. Validate CloudFormation template
#   2. Upload Smithy model to S3
#   3. Deploy CloudFormation stack (create or update)
#   4. Package Lambda code (two-step pip3 install)
#   5. Deploy Lambda code (S3 fallback if >50MB)
#   6. Create Cognito test user
#   7. Generate scripts/test.sh
# ============================================================

STACK_NAME="${STACK_NAME:-agentcore-smithy-bedrock}"
REGION="${AWS_REGION:-us-east-1}"
TEMPLATE_PATH="infrastructure/cloudformation-template.yaml"
TEST_USERNAME="testuser"
TEST_PASSWORD="TestPass123!"

echo "============================================================"
echo "Deploying stack: ${STACK_NAME} in region: ${REGION}"
echo "============================================================"

# ============================================================
# Step 1: Validate CloudFormation template
# ============================================================
echo ""
echo ">>> Step 1: Validating CloudFormation template..."
aws cloudformation validate-template \
    --template-body "file://${TEMPLATE_PATH}" \
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
# Step 2: Deploy CloudFormation stack (create or update)
# ============================================================
echo ""
echo ">>> Step 3: Deploying CloudFormation stack..."

STACK_STATUS=$(aws cloudformation describe-stacks \
    --stack-name "${STACK_NAME}" \
    --region "${REGION}" \
    --query "Stacks[0].StackStatus" \
    --output text 2>&1 || true)

if echo "${STACK_STATUS}" | grep -qi "does.not.exist\|DOES_NOT_EXIST"; then
    echo "Stack does not exist. Creating..."
    aws cloudformation create-stack \
        --stack-name "${STACK_NAME}" \
        --template-body "file://${TEMPLATE_PATH}" \
        --capabilities CAPABILITY_NAMED_IAM \
        --region "${REGION}"

    echo "Waiting for stack creation to complete..."
    aws cloudformation wait stack-create-complete \
        --stack-name "${STACK_NAME}" \
        --region "${REGION}"
    echo "Stack creation complete."
elif echo "${STACK_STATUS}" | grep -q "ROLLBACK_COMPLETE"; then
    echo "Stack is in ROLLBACK_COMPLETE state. Deleting before re-creating..."
    aws cloudformation delete-stack \
        --stack-name "${STACK_NAME}" \
        --region "${REGION}"
    aws cloudformation wait stack-delete-complete \
        --stack-name "${STACK_NAME}" \
        --region "${REGION}"
    echo "Old stack deleted. Creating fresh stack..."
    aws cloudformation create-stack \
        --stack-name "${STACK_NAME}" \
        --template-body "file://${TEMPLATE_PATH}" \
        --capabilities CAPABILITY_NAMED_IAM \
        --region "${REGION}"

    echo "Waiting for stack creation to complete..."
    aws cloudformation wait stack-create-complete \
        --stack-name "${STACK_NAME}" \
        --region "${REGION}"
    echo "Stack creation complete."
else
    echo "Stack exists (status: ${STACK_STATUS}). Updating..."
    UPDATE_OUTPUT=$(aws cloudformation update-stack \
        --stack-name "${STACK_NAME}" \
        --template-body "file://${TEMPLATE_PATH}" \
        --capabilities CAPABILITY_NAMED_IAM \
        --region "${REGION}" 2>&1 || true)

    if echo "${UPDATE_OUTPUT}" | grep -q "No updates are to be performed"; then
        echo "No updates are to be performed. Continuing..."
    else
        echo "Waiting for stack update to complete..."
        aws cloudformation wait stack-update-complete \
            --stack-name "${STACK_NAME}" \
            --region "${REGION}"
        echo "Stack update complete."
    fi
fi


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
# Step 3: Package Lambda code (two-step pip3 install)
# ============================================================
echo ""
echo ">>> Step 4: Packaging Lambda code..."

PACKAGE_DIR=$(mktemp -d)
echo "Using temp directory: ${PACKAGE_DIR}"

# Copy source code
cp -r src "${PACKAGE_DIR}/"

# Step 3a: Install binary packages with platform targeting
echo "Installing binary dependencies (step 1 of 2)..."
pip3 install \
    --target "${PACKAGE_DIR}" \
    --platform manylinux2014_x86_64 \
    --python-version 3.12 \
    --only-binary=:all: \
    -r requirements.txt

# Step 3b: Install pure Python packages that may have been skipped
echo "Installing pure Python dependencies (step 2 of 2)..."
pip3 install \
    --target "${PACKAGE_DIR}" \
    --platform manylinux2014_x86_64 \
    --python-version 3.12 \
    --only-binary=:all: \
    --no-deps \
    requests urllib3 charset-normalizer idna certifi PyJWT cryptography cffi

# Create zip package
ZIP_FILE="/tmp/lambda-package-$$.zip"
rm -f "${ZIP_FILE}"
echo "Creating zip package..."
(cd "${PACKAGE_DIR}" && zip -r "${ZIP_FILE}" . -x "__pycache__/*" "*/__pycache__/*")

# ============================================================
# Step 4: Deploy Lambda code (S3 fallback if >50MB)
# ============================================================
echo ""
echo ">>> Step 5: Deploying Lambda code..."

# Get file size (macOS and Linux compatible)
ZIP_SIZE=$(stat -f%z "${ZIP_FILE}" 2>/dev/null || stat -c%s "${ZIP_FILE}")
MAX_SIZE=$((50 * 1024 * 1024))

echo "Package size: ${ZIP_SIZE} bytes"

if [ "${ZIP_SIZE}" -gt "${MAX_SIZE}" ]; then
    echo "Package exceeds 50MB. Using S3 fallback..."
    S3_BUCKET="${STACK_NAME}-lambda-packages"
    S3_KEY="lambda-package.zip"

    aws s3 mb "s3://${S3_BUCKET}" --region "${REGION}" 2>/dev/null || true
    aws s3 cp "${ZIP_FILE}" "s3://${S3_BUCKET}/${S3_KEY}" --region "${REGION}"

    aws lambda update-function-code \
        --function-name "${LAMBDA_FUNCTION_NAME}" \
        --s3-bucket "${S3_BUCKET}" \
        --s3-key "${S3_KEY}" \
        --region "${REGION}" > /dev/null
else
    echo "Package under 50MB. Uploading directly..."
    aws lambda update-function-code \
        --function-name "${LAMBDA_FUNCTION_NAME}" \
        --zip-file "fileb://${ZIP_FILE}" \
        --region "${REGION}" > /dev/null
fi

echo "Lambda code deployed successfully."

# Cleanup temp files
rm -rf "${PACKAGE_DIR}"
rm -f "${ZIP_FILE}"


# ============================================================
# Step 5: Create Cognito test user
# ============================================================
echo ""
echo ">>> Step 6: Creating Cognito test user..."

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
# Step 7: Generate test script (scripts/test.sh)
# ============================================================
echo ""
echo ">>> Step 7: Generating test script..."

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
