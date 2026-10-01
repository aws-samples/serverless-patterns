#!/usr/bin/env bash
# =============================================================================
# AgentCore API Gateway Weather Agent — Deployment Script (AWS SAM)
#
# Deploys the full stack in the correct order, handling resources that cannot
# be created via CloudFormation (the AgentCore credential provider).
#
# Uses AWS SAM: `sam build` packages the Lambda code + dependencies, and
# `sam deploy` provisions the stack and uploads the code in one step.
#
# Usage:
#   ./scripts/deploy.sh \
#     --environment-name dev \
#     --region us-east-1 \
#     --s3-bucket my-deploy-bucket
# =============================================================================
set -e

# -------------------------------------------------------
# Defaults
# -------------------------------------------------------
REGION="us-east-1"
S3_BUCKET=""
ENVIRONMENT_NAME=""
BEDROCK_MODEL_ID="us.anthropic.claude-sonnet-4-6"
TEMPLATE_FILE="infrastructure/template.yaml"

# -------------------------------------------------------
# Parse arguments
# -------------------------------------------------------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --environment-name)
      ENVIRONMENT_NAME="$2"
      shift 2
      ;;
    --region)
      REGION="$2"
      shift 2
      ;;
    --s3-bucket)
      S3_BUCKET="$2"
      shift 2
      ;;
    --bedrock-model-id)
      BEDROCK_MODEL_ID="$2"
      shift 2
      ;;
    *)
      echo "Unknown parameter: $1"
      echo "Usage: $0 --environment-name NAME [--region REGION] [--s3-bucket BUCKET] [--bedrock-model-id MODEL_ID]"
      exit 1
      ;;
  esac
done

# -------------------------------------------------------
# Validate required parameters
# -------------------------------------------------------
if [[ -z "$ENVIRONMENT_NAME" ]]; then
  echo "ERROR: --environment-name is required"
  exit 1
fi

if ! command -v sam > /dev/null 2>&1; then
  echo "ERROR: AWS SAM CLI is not installed."
  echo "       Install it: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html"
  exit 1
fi

STACK_NAME="${ENVIRONMENT_NAME}-weather-agent"
APIGW_SECRET_NAME="${ENVIRONMENT_NAME}/apigw-api-key"
LAMBDA_FUNCTION_NAME="${ENVIRONMENT_NAME}-weather-agent"
BUILD_DIR=".aws-sam/build"

echo "============================================="
echo " AgentCore Weather Agent Deployment (SAM)"
echo "============================================="
echo " Environment : ${ENVIRONMENT_NAME}"
echo " Region      : ${REGION}"
echo " Stack       : ${STACK_NAME}"
echo " Model       : ${BEDROCK_MODEL_ID}"
echo " S3 Bucket   : ${S3_BUCKET:-<none — sam managed (--resolve-s3)>}"
echo "============================================="

# -------------------------------------------------------
# Helper: run `sam deploy` with the given parameter overrides.
# Reuses the already-built artifacts in .aws-sam/build.
#
#   sam_deploy "<parameter-overrides>"
# -------------------------------------------------------
sam_deploy() {
  local param_overrides="$1"
  local s3_args

  if [[ -n "${S3_BUCKET}" ]]; then
    s3_args="--s3-bucket ${S3_BUCKET} --s3-prefix ${STACK_NAME}"
  else
    s3_args="--resolve-s3"
  fi

  sam deploy \
    --template-file "${BUILD_DIR}/template.yaml" \
    --stack-name "${STACK_NAME}" \
    --region "${REGION}" \
    --capabilities CAPABILITY_NAMED_IAM \
    --no-confirm-changeset \
    --no-fail-on-empty-changeset \
    ${s3_args} \
    --parameter-overrides ${param_overrides}
}

# =============================================================================
# Step 1: Validate SAM template
# =============================================================================
echo ""
echo ">>> Step 1: Validating SAM template..."
sam validate \
  --template-file "${TEMPLATE_FILE}" \
  --region "${REGION}"
echo "    Template validation passed."

# =============================================================================
# Step 2: Create/update Secrets Manager secrets
#
# Only the API Gateway key secret is needed — it holds the API key the
# AgentCore credential provider uses to call API Gateway. The Open-Meteo
# backend requires no key, so there is no downstream API secret.
# =============================================================================
echo ""
echo ">>> Step 2: Creating/updating Secrets Manager secrets..."

# --- Placeholder APIGW key secret ---
if aws secretsmanager describe-secret --secret-id "${APIGW_SECRET_NAME}" --region "${REGION}" > /dev/null 2>&1; then
  echo "    APIGW key secret already exists (will update after stack deploy)."
else
  echo "    Creating placeholder APIGW key secret..."
  aws secretsmanager create-secret \
    --name "${APIGW_SECRET_NAME}" \
    --description "API Gateway API key for AgentCore credential provider (${ENVIRONMENT_NAME})" \
    --secret-string "PLACEHOLDER_WILL_BE_UPDATED" \
    --region "${REGION}" > /dev/null
fi

APIGW_SECRET_ARN=$(aws secretsmanager describe-secret \
  --secret-id "${APIGW_SECRET_NAME}" \
  --region "${REGION}" \
  --query 'ARN' --output text)
echo "    APIGW secret ARN: ${APIGW_SECRET_ARN}"

# =============================================================================
# Step 3: Build the SAM application
#
# The Agent Lambda uses a Makefile custom build (BuildMethod: makefile in the
# template). The Makefile downloads prebuilt manylinux wheels so binary
# dependencies (cryptography, cffi) match the Lambda runtime on any host OS —
# no Docker and no local python3.12 required.
# =============================================================================
echo ""
echo ">>> Step 3: Building SAM application..."
sam build --template-file "${TEMPLATE_FILE}"
echo "    Build complete."

# =============================================================================
# Step 4: Initial deploy (without credential provider)
# =============================================================================
echo ""
echo ">>> Step 4: Deploying stack '${STACK_NAME}' (initial)..."
sam_deploy "EnvironmentName=${ENVIRONMENT_NAME} BedrockModelId=${BEDROCK_MODEL_ID}"
echo "    Stack deployment complete."

# Retrieve stack outputs
get_output() {
  aws cloudformation describe-stacks \
    --stack-name "${STACK_NAME}" \
    --region "${REGION}" \
    --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" \
    --output text
}

GATEWAY_ID=$(get_output "GatewayId")
REST_API_ID=$(get_output "RestApiId")
API_KEY_ID=$(get_output "ApiKeyId")
USER_POOL_ID=$(get_output "UserPoolId")
USER_POOL_CLIENT_ID=$(get_output "UserPoolClientId")
COGNITO_JWKS_URL=$(get_output "CognitoJwksUrl")
LAMBDA_ARN=$(get_output "AgentLambdaArn")
API_ENDPOINT_URL=$(get_output "ApiEndpointUrl")

echo ""
echo "    Stack Outputs:"
echo "      Gateway ID        : ${GATEWAY_ID}"
echo "      REST API ID       : ${REST_API_ID}"
echo "      API Key ID        : ${API_KEY_ID}"
echo "      User Pool ID      : ${USER_POOL_ID}"
echo "      Client ID         : ${USER_POOL_CLIENT_ID}"
echo "      JWKS URL          : ${COGNITO_JWKS_URL}"
echo "      Lambda ARN        : ${LAMBDA_ARN}"
echo "      API Endpoint      : ${API_ENDPOINT_URL}"

# =============================================================================
# Step 5: Retrieve API Gateway key value and update Secrets Manager
# =============================================================================
echo ""
echo ">>> Step 5: Retrieving API Gateway key value..."

API_KEY_VALUE=$(aws apigateway get-api-key \
  --api-key "${API_KEY_ID}" \
  --include-value \
  --region "${REGION}" \
  --query 'value' --output text)

if [[ -z "${API_KEY_VALUE}" || "${API_KEY_VALUE}" == "None" ]]; then
  echo "ERROR: Failed to retrieve API Gateway key value."
  exit 1
fi

echo "    API key retrieved successfully."

echo ""
echo ">>> Step 6: Updating Secrets Manager with real API Gateway key..."
aws secretsmanager put-secret-value \
  --secret-id "${APIGW_SECRET_NAME}" \
  --secret-string "${API_KEY_VALUE}" \
  --region "${REGION}" > /dev/null
echo "    APIGW key secret updated."

# =============================================================================
# Step 7: Create/update credential provider (CLI or manual)
#
# The AgentCore credential provider is provisioned via CLI between stack
# operations: the API key only exists after the initial deploy, and its ARN
# must be fed back into the stack via a follow-up deploy (Step 7b).
# =============================================================================
echo ""
echo ">>> Step 7: Creating/updating credential provider..."

CRED_PROVIDER_NAME="${ENVIRONMENT_NAME}-weather-apigw-key"
CRED_PROVIDER_ARN=""

# Detect CLI support by listing providers (help command is buggy in some CLI versions)
if aws bedrock-agentcore-control list-api-key-credential-providers --region "${REGION}" > /dev/null 2>&1; then
  # Check if provider already exists
  EXISTING_ARN=$(aws bedrock-agentcore-control list-api-key-credential-providers \
    --region "${REGION}" \
    --query "credentialProviders[?name=='${CRED_PROVIDER_NAME}'].credentialProviderArn" \
    --output text 2>/dev/null)

  if [[ -n "${EXISTING_ARN}" && "${EXISTING_ARN}" != "None" ]]; then
    echo "    Updating existing credential provider with new API key..."
    UPDATE_OUTPUT=$(aws bedrock-agentcore-control update-api-key-credential-provider \
      --name "${CRED_PROVIDER_NAME}" \
      --api-key "${API_KEY_VALUE}" \
      --region "${REGION}" 2>&1) || {
        echo "    WARNING: update-api-key-credential-provider failed. Deleting and recreating..."
        aws bedrock-agentcore-control delete-api-key-credential-provider \
          --name "${CRED_PROVIDER_NAME}" \
          --region "${REGION}" > /dev/null 2>&1 || true
        # Small delay for eventual consistency
        sleep 3
        EXISTING_ARN=""
      }
    if [[ -n "${EXISTING_ARN}" ]]; then
      CRED_PROVIDER_ARN="${EXISTING_ARN}"
      echo "    Credential provider updated: ${CRED_PROVIDER_ARN}"
    fi
  fi

  if [[ -z "${CRED_PROVIDER_ARN}" || "${CRED_PROVIDER_ARN}" == "None" ]]; then
    echo "    Creating credential provider via CLI..."
    CRED_PROVIDER_ARN=$(aws bedrock-agentcore-control create-api-key-credential-provider \
      --name "${CRED_PROVIDER_NAME}" \
      --api-key "${API_KEY_VALUE}" \
      --region "${REGION}" \
      --query 'credentialProviderArn' --output text 2>&1) || {
        echo "    ERROR: Failed to create credential provider: ${CRED_PROVIDER_ARN}"
        CRED_PROVIDER_ARN=""
      }
    if [[ -n "${CRED_PROVIDER_ARN}" && "${CRED_PROVIDER_ARN}" != "None" ]]; then
      echo "    Credential provider created: ${CRED_PROVIDER_ARN}"
    fi
  fi
fi

if [[ -n "${CRED_PROVIDER_ARN}" && "${CRED_PROVIDER_ARN}" != "None" ]]; then
  # Verify the credential provider was updated correctly
  VERIFY_TIME=$(aws bedrock-agentcore-control list-api-key-credential-providers \
    --region "${REGION}" \
    --query "credentialProviders[?name=='${CRED_PROVIDER_NAME}'].lastUpdatedTime" \
    --output text 2>/dev/null)
  echo "    Credential provider verified (last updated: ${VERIFY_TIME})"
  echo ""
  echo ">>> Step 7b: Re-deploying stack with credential provider ARN..."
  sam_deploy "EnvironmentName=${ENVIRONMENT_NAME} BedrockModelId=${BEDROCK_MODEL_ID} CredentialProviderArn=${CRED_PROVIDER_ARN}"
  echo "    Stack updated with credential provider."
else
  echo ""
  echo "============================================="
  echo " MANUAL STEP: Create Credential Provider"
  echo "============================================="
  echo ""
  echo " Your AWS CLI does not support bedrock-agentcore-control."
  echo " Upgrade to AWS CLI 2.28+ or create manually:"
  echo ""
  echo " Option A — Upgrade CLI then run:"
  echo ""
  echo "   aws bedrock-agentcore-control create-api-key-credential-provider \\"
  echo "     --name ${CRED_PROVIDER_NAME} \\"
  echo "     --api-key \$(aws apigateway get-api-key --api-key ${API_KEY_ID} --include-value --region ${REGION} --query 'value' --output text) \\"
  echo "     --region ${REGION}"
  echo ""
  echo " Option B — AWS Console:"
  echo ""
  echo "   1. Open: https://console.aws.amazon.com/bedrock-agentcore/"
  echo "   2. Go to Identity → Outbound Auth"
  echo "   3. Click 'Add OAuth client/API Key' → select 'API Key'"
  echo "   4. Name: ${CRED_PROVIDER_NAME}"
  echo "   5. API Key: (run the command below to get the value)"
  echo "      aws apigateway get-api-key --api-key ${API_KEY_ID} --include-value --region ${REGION} --query 'value' --output text"
  echo ""
  echo " After creating, re-deploy with the credential provider ARN:"
  echo ""
  echo "   sam deploy \\"
  echo "     --template-file ${BUILD_DIR}/template.yaml \\"
  echo "     --stack-name ${STACK_NAME} \\"
  echo "     --capabilities CAPABILITY_NAMED_IAM \\"
  echo "     --region ${REGION} \\"
  echo "     --resolve-s3 \\"
  echo "     --parameter-overrides \\"
  echo "       EnvironmentName=${ENVIRONMENT_NAME} \\"
  echo "       CredentialProviderArn=<YOUR_CREDENTIAL_PROVIDER_ARN>"
  echo ""
  echo "============================================="
fi

# =============================================================================
# Step 8: Create test user
# =============================================================================
echo ""
echo ">>> Step 8: Creating test user..."

TEST_USERNAME="testuser"
TEST_PASSWORD="TestPass123!"

# Check if user already exists
if aws cognito-idp admin-get-user \
    --user-pool-id "${USER_POOL_ID}" \
    --username "${TEST_USERNAME}" \
    --region "${REGION}" > /dev/null 2>&1; then
  echo "    Test user '${TEST_USERNAME}' already exists."
else
  echo "    Creating test user '${TEST_USERNAME}'..."
  aws cognito-idp admin-create-user \
    --user-pool-id "${USER_POOL_ID}" \
    --username "${TEST_USERNAME}" \
    --temporary-password "TempPass123!" \
    --message-action SUPPRESS \
    --region "${REGION}" > /dev/null

  echo "    Setting permanent password..."
  aws cognito-idp admin-set-user-password \
    --user-pool-id "${USER_POOL_ID}" \
    --username "${TEST_USERNAME}" \
    --password "${TEST_PASSWORD}" \
    --permanent \
    --region "${REGION}" > /dev/null

  echo "    Test user created."
fi

# =============================================================================
# Done
# =============================================================================
# Write a test script that can be run directly
TEST_SCRIPT="scripts/test.sh"
cat > "${TEST_SCRIPT}" << 'TESTEOF'
#!/usr/bin/env bash
set -e
TESTEOF

cat >> "${TEST_SCRIPT}" << EOF
CLIENT_ID="${USER_POOL_CLIENT_ID}"
FUNCTION_NAME="${LAMBDA_FUNCTION_NAME}"
REGION="${REGION}"
USERNAME="${TEST_USERNAME}"
PASSWORD="${TEST_PASSWORD}"
EOF

cat >> "${TEST_SCRIPT}" << 'TESTEOF'

echo "Getting ID token..."
ID_TOKEN=$(aws cognito-idp initiate-auth \
  --auth-flow USER_PASSWORD_AUTH \
  --client-id "${CLIENT_ID}" \
  --auth-parameters USERNAME="${USERNAME}",PASSWORD="${PASSWORD}" \
  --region "${REGION}" \
  --query 'AuthenticationResult.IdToken' --output text)

if [[ -z "${ID_TOKEN}" || "${ID_TOKEN}" == "None" ]]; then
  echo "ERROR: Failed to get ID token"
  exit 1
fi
echo "Token obtained (${#ID_TOKEN} chars)"

PROMPT="${1:-What is the weather in London, UK?}"
echo "Invoking agent with: ${PROMPT}"

PAYLOAD=$(python3 -c "
import json
inner = json.dumps({'prompt': '${PROMPT}'})
outer = json.dumps({'body': inner, 'headers': {'Authorization': 'Bearer ${ID_TOKEN}'}})
print(outer)
")

aws lambda invoke \
  --function-name "${FUNCTION_NAME}" \
  --region "${REGION}" \
  --cli-binary-format raw-in-base64-out \
  --payload "${PAYLOAD}" \
  /tmp/response.json

echo ""
echo "=== Response ==="
python3 -c "
import json
with open('/tmp/response.json') as f:
    resp = json.load(f)
if 'body' in resp:
    body = json.loads(resp['body'])
    if 'response' in body:
        print(body['response'])
    elif 'error' in body:
        print(f\"ERROR: {body['error']}\")
    else:
        print(json.dumps(body, indent=2))
else:
    print(json.dumps(resp, indent=2))
"
TESTEOF

chmod +x "${TEST_SCRIPT}"

echo ""
echo "============================================="
echo " Deployment Complete!"
echo "============================================="
echo ""
echo " Test the agent:"
echo ""
echo "   ./scripts/test.sh"
echo "   ./scripts/test.sh 'What is the weather in Liverpool, England?'"
echo ""
