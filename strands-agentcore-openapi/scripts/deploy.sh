#!/usr/bin/env bash
# =============================================================================
# OpenAPI Agent Gateway — Deployment Script (AWS SAM)
#
# Creates the API Key credential provider (which cannot be defined in the
# template), then builds and deploys the stack with AWS SAM in a single pass.
#
# Usage:
#   ./scripts/deploy.sh \
#     --environment-name dev \
#     --weather-api-key YOUR_WEATHERAPI_KEY \
#     --region us-east-1 \
#     --model-id us.anthropic.claude-sonnet-4-5-20250929-v1:0
# =============================================================================
set -e

# -------------------------------------------------------
# Defaults
# -------------------------------------------------------
REGION="us-east-1"
ENVIRONMENT_NAME=""
WEATHER_API_KEY=""
MODEL_ID="us.anthropic.claude-sonnet-4-5-20250929-v1:0"
TEMPLATE_FILE="template.yaml"
CAPABILITIES="CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND"

# -------------------------------------------------------
# Parse arguments
# -------------------------------------------------------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --environment-name)
      ENVIRONMENT_NAME="$2"
      shift 2
      ;;
    --weather-api-key)
      WEATHER_API_KEY="$2"
      shift 2
      ;;
    --region)
      REGION="$2"
      shift 2
      ;;
    --model-id)
      MODEL_ID="$2"
      shift 2
      ;;
    *)
      echo "Unknown parameter: $1"
      echo "Usage: $0 --environment-name NAME --weather-api-key KEY [--region REGION] [--model-id MODEL_ID]"
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

if [[ -z "$WEATHER_API_KEY" ]]; then
  echo "ERROR: --weather-api-key is required"
  exit 1
fi

if ! command -v sam > /dev/null 2>&1; then
  echo "ERROR: AWS SAM CLI is not installed."
  echo "       Install it: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html"
  exit 1
fi

STACK_NAME="${ENVIRONMENT_NAME}-openapi-agent-gateway"
WEATHER_SECRET_NAME="${ENVIRONMENT_NAME}/weatherapi-key"
LAMBDA_FUNCTION_NAME="${ENVIRONMENT_NAME}-agent-lambda"

echo "============================================="
echo " OpenAPI Agent Gateway Deployment (AWS SAM)"
echo "============================================="
echo " Environment : ${ENVIRONMENT_NAME}"
echo " Region      : ${REGION}"
echo " Stack       : ${STACK_NAME}"
echo " Model       : ${MODEL_ID}"
echo "============================================="

get_output() {
  aws cloudformation describe-stacks \
    --stack-name "${STACK_NAME}" \
    --region "${REGION}" \
    --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" \
    --output text
}

# =============================================================================
# Step 1: Create/update Secrets Manager secret for WeatherAPI key
# =============================================================================
echo ""
echo ">>> Step 1: Creating/updating WeatherAPI key secret..."

if aws secretsmanager describe-secret --secret-id "${WEATHER_SECRET_NAME}" --region "${REGION}" > /dev/null 2>&1; then
  echo "    Updating existing secret..."
  aws secretsmanager put-secret-value \
    --secret-id "${WEATHER_SECRET_NAME}" \
    --secret-string "${WEATHER_API_KEY}" \
    --region "${REGION}" > /dev/null
else
  echo "    Creating secret..."
  aws secretsmanager create-secret \
    --name "${WEATHER_SECRET_NAME}" \
    --description "WeatherAPI.com API key for ${ENVIRONMENT_NAME}" \
    --secret-string "${WEATHER_API_KEY}" \
    --region "${REGION}" > /dev/null
fi

WEATHER_SECRET_ARN=$(aws secretsmanager describe-secret \
  --secret-id "${WEATHER_SECRET_NAME}" \
  --region "${REGION}" \
  --query 'ARN' --output text)

echo "    Secret ARN: ${WEATHER_SECRET_ARN}"

# =============================================================================
# Step 2: Create/update the API Key credential provider
#
# This is independent of the CloudFormation stack, so we create it first and
# feed its ARN into a single SAM deploy. Requires AWS CLI 2.28+.
# =============================================================================
echo ""
echo ">>> Step 2: Creating/updating credential provider..."

CRED_PROVIDER_NAME="${ENVIRONMENT_NAME}-weatherapi-key"
CRED_PROVIDER_ARN=""

if aws bedrock-agentcore-control list-api-key-credential-providers --region "${REGION}" > /dev/null 2>&1; then
  EXISTING_ARN=$(aws bedrock-agentcore-control list-api-key-credential-providers \
    --region "${REGION}" \
    --query "credentialProviders[?name=='${CRED_PROVIDER_NAME}'].credentialProviderArn" \
    --output text 2>/dev/null)

  if [[ -n "${EXISTING_ARN}" && "${EXISTING_ARN}" != "None" ]]; then
    echo "    Updating existing credential provider..."
    if aws bedrock-agentcore-control update-api-key-credential-provider \
      --name "${CRED_PROVIDER_NAME}" \
      --api-key "${WEATHER_API_KEY}" \
      --region "${REGION}" > /dev/null 2>&1; then
      CRED_PROVIDER_ARN="${EXISTING_ARN}"
      echo "    Credential provider updated."
    else
      echo "    WARNING: update failed. Deleting and recreating..."
      aws bedrock-agentcore-control delete-api-key-credential-provider \
        --name "${CRED_PROVIDER_NAME}" \
        --region "${REGION}" > /dev/null 2>&1 || true
      sleep 3
    fi
  fi

  if [[ -z "${CRED_PROVIDER_ARN}" || "${CRED_PROVIDER_ARN}" == "None" ]]; then
    echo "    Creating credential provider via CLI..."
    CRED_PROVIDER_ARN=$(aws bedrock-agentcore-control create-api-key-credential-provider \
      --name "${CRED_PROVIDER_NAME}" \
      --api-key "${WEATHER_API_KEY}" \
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

if [[ -z "${CRED_PROVIDER_ARN}" || "${CRED_PROVIDER_ARN}" == "None" ]]; then
  CRED_PROVIDER_ARN=""
  echo ""
  echo "    WARNING: Could not create the credential provider automatically."
  echo "    The stack will deploy WITHOUT the WeatherAPI Gateway Target."
  echo "    Create it via the Console (Bedrock -> AgentCore -> Identity -> Outbound Auth,"
  echo "    type 'API Key', name '${CRED_PROVIDER_NAME}'), then re-run this script."
fi

# =============================================================================
# Step 3: Build with SAM
# =============================================================================
echo ""
echo ">>> Step 3: Building with SAM..."

# The Agent function uses a Makefile build (see src/Makefile) that installs
# Linux manylinux wheels via pip's --platform flag — no Docker required.
sam build --template-file "${TEMPLATE_FILE}"

echo "    Build complete."

# =============================================================================
# Step 4: Deploy with SAM (single pass)
# =============================================================================
echo ""
echo ">>> Step 4: Deploying stack '${STACK_NAME}'..."

PARAM_OVERRIDES=(
  "EnvironmentName=${ENVIRONMENT_NAME}"
  "WeatherApiKeySecretArn=${WEATHER_SECRET_ARN}"
  "BedrockModelId=${MODEL_ID}"
)
# Only pass CredentialProviderArn when we actually have one — SAM rejects an
# empty parameter value, and omitting it lets the template default ('') apply,
# which skips the Gateway Target via the HasCredentialProvider condition.
if [[ -n "${CRED_PROVIDER_ARN}" ]]; then
  PARAM_OVERRIDES+=("CredentialProviderArn=${CRED_PROVIDER_ARN}")
fi

sam deploy \
  --stack-name "${STACK_NAME}" \
  --region "${REGION}" \
  --capabilities ${CAPABILITIES} \
  --resolve-s3 \
  --no-confirm-changeset \
  --no-fail-on-empty-changeset \
  --parameter-overrides "${PARAM_OVERRIDES[@]}"

echo "    Deployment complete."

GATEWAY_ID=$(get_output "GatewayId")
USER_POOL_ID=$(get_output "CognitoUserPoolId")
USER_POOL_CLIENT_ID=$(get_output "CognitoClientId")
LAMBDA_ARN=$(get_output "AgentLambdaArn")

echo ""
echo "    Stack Outputs:"
echo "      Gateway ID   : ${GATEWAY_ID}"
echo "      User Pool ID : ${USER_POOL_ID}"
echo "      Client ID    : ${USER_POOL_CLIENT_ID}"
echo "      Lambda ARN   : ${LAMBDA_ARN}"

# Save stack outputs for other scripts
mkdir -p deployment
cat > deployment/stack_outputs.json << EOF
{
  "GatewayId": "${GATEWAY_ID}",
  "CognitoUserPoolId": "${USER_POOL_ID}",
  "CognitoClientId": "${USER_POOL_CLIENT_ID}",
  "AgentLambdaArn": "${LAMBDA_ARN}"
}
EOF
echo "    Outputs saved to deployment/stack_outputs.json"

# =============================================================================
# Step 5: Create test user
# =============================================================================
echo ""
echo ">>> Step 5: Creating test user..."

TEST_USERNAME="testuser@example.com"
TEST_PASSWORD="TestPassword123!"

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
    --user-attributes Name=email,Value="${TEST_USERNAME}" Name=email_verified,Value=true \
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
# Step 6: Generate test script
# =============================================================================
echo ""
echo ">>> Step 6: Generating test script..."

TEST_SCRIPT="scripts/test.sh"
mkdir -p scripts

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

echo "Getting access token..."
ACCESS_TOKEN=$(aws cognito-idp initiate-auth \
  --auth-flow USER_PASSWORD_AUTH \
  --client-id "${CLIENT_ID}" \
  --auth-parameters USERNAME="${USERNAME}",PASSWORD="${PASSWORD}" \
  --region "${REGION}" \
  --query 'AuthenticationResult.AccessToken' --output text)

if [[ -z "${ACCESS_TOKEN}" || "${ACCESS_TOKEN}" == "None" ]]; then
  echo "ERROR: Failed to get access token"
  exit 1
fi

echo "Token obtained (${#ACCESS_TOKEN} chars)"

PROMPT="${1:-What is the weather in London, UK?}"
echo "Invoking agent with: ${PROMPT}"

PAYLOAD=$(python3 -c "
import json
inner = json.dumps({'prompt': '${PROMPT}'})
outer = json.dumps({'body': inner, 'headers': {'Authorization': 'Bearer ${ACCESS_TOKEN}'}})
print(outer)
")

aws lambda invoke \
  --function-name "${FUNCTION_NAME}" \
  --region "${REGION}" \
  --cli-binary-format raw-in-base64-out \
  --payload "${PAYLOAD}" \
  /tmp/response.json > /dev/null

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

# =============================================================================
# Done
# =============================================================================
echo ""
echo "============================================="
echo " Deployment Complete!"
echo "============================================="
echo ""
echo " Test the agent:"
echo ""
echo "   ./scripts/test.sh"
echo "   ./scripts/test.sh 'What is the weather in Paris, France?'"
echo ""
