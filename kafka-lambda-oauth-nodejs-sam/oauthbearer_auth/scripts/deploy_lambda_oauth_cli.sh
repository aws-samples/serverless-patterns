#!/bin/bash
# =============================================================================
# Deploy the Node.js Kafka consumer as a Lambda function with a SELF-MANAGED KAFKA
# event source using SASL/OAUTHBEARER (OAuth 2.0 client-credentials) auth, via
# the AWS CLI.
#
# AWS SAM does not yet support the OAUTHBEARER auth type for self-managed Kafka
# event sources, so this script uses `aws lambda create-event-source-mapping`
# directly (per the "Kafka OAuth & IAM Testing Manual").
#
# It reuses the same Node.js consumer as the SAM path (app.lambdaHandler).
#
# -----------------------------------------------------------------------------
# PREREQUISITES (these are NOT created by this script and are assumed to exist):
#   1. Your AWS account is ALLOWLISTED for the new self-managed Kafka ESM auth
#      types (OAUTHBEARER_AUTH). Otherwise create-event-source-mapping fails.
#   2. The brokers expose a SASL_SSL / OAUTHBEARER listener (e.g. :9093) with a
#      TLS server certificate. The Lambda poller connects over TLS and validates
#      the broker cert against SERVER_ROOT_CA_CERTIFICATE. (The pattern's default
#      cluster listens SASL_PLAINTEXT on :9092 - add a TLS listener first.)
#   3. A Cognito app client with the client_credentials grant, a user-pool
#      domain, and a resource server + scope (e.g. kafka/consume). The broker's
#      JWKS validator must accept these tokens (no audience is present).
#
# This script CAN create the two Secrets Manager secrets for you (see CREATE
# secret sections) if you pass the raw values instead of pre-made ARNs.
# =============================================================================
set -euo pipefail
export AWS_PAGER=""   # don't pipe CLI output through a pager (less/vi)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PATTERN_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# ---------------------------- Configuration ---------------------------------
# Pick up STACK_NAME, AWS_REGION, and the rest of the values the client instance's
# user data recorded at boot, so this script works without any exports. Anything
# already set in your environment takes precedence.
ENV_FILE="${KAFKA_OAUTH_ENV:-/home/ec2-user/kafka_oauth.env}"
if [ -f "$ENV_FILE" ]; then
  while IFS='=' read -r key value; do
    key="${key#export }"
    if [ -n "$key" ] && [ -z "${!key:-}" ]; then export "$key=$value"; fi
  done < <(grep -E '^export [A-Za-z_][A-Za-z0-9_]*=' "$ENV_FILE")
fi

REGION="${AWS_REGION:-us-west-2}"
STACK_NAME="${STACK_NAME:-kafka-oauth}"                    # CFN stack for VPC/subnet/SG discovery
# Lambda-side resource names are derived from the stack name, so two stacks in the
# same account and region (for example the Java and Python versions of this
# pattern) never overwrite each other's function, role, secrets, or table.
FUNCTION_NAME="${FUNCTION_NAME:-${STACK_NAME}-consumer}"
RUNTIME="${RUNTIME:-nodejs22.x}"
HANDLER="app.lambdaHandler"
ZIP_PATH="${ZIP_PATH:-$PATTERN_DIR/kafka_event_consumer_function/function.zip}"
TOPIC="${TOPIC:-${KAFKA_TOPIC:-KafkaOAuthBearerLambdaTopic}}"
CONSUMER_GROUP="${CONSUMER_GROUP:-lambda-oauth-consumer}"
POLLER_GROUP="${POLLER_GROUP:-${CONSUMER_GROUP}-cell1}"    # must be a fresh name per VPC + event source type
BATCH_SIZE="${BATCH_SIZE:-10}"
DDB_TABLE_NAME="${DDB_TABLE_NAME:-${STACK_NAME}-messages}"   # the function writes each message here
if [ ${#FUNCTION_NAME} -gt 59 ]; then
  echo "ERROR: FUNCTION_NAME '$FUNCTION_NAME' is longer than 59 characters (IAM role names, which"
  echo "       add '-role', max out at 64). Set FUNCTION_NAME to something shorter."
  exit 1
fi

# Bootstrap servers = the brokers' SASL_SSL / OAUTHBEARER listener (:9092 in this pattern).
BOOTSTRAP_SERVERS="${BOOTSTRAP_SERVERS:-10.0.1.10:9092,10.0.2.10:9092,10.0.3.10:9092}"

# --- OAuth client-credentials secret: pass an existing ARN, OR raw values, OR
#     leave blank to auto-discover the client_credentials app client from the stack ---
OAUTH_SECRET_ARN="${OAUTH_SECRET_ARN:-}"
OAUTH_CLIENT_ID="${OAUTH_CLIENT_ID:-}"
OAUTH_CLIENT_SECRET="${OAUTH_CLIENT_SECRET:-}"
OAUTH_TOKEN_ENDPOINT="${OAUTH_TOKEN_ENDPOINT:-}"          # https://<domain>.auth.<region>.amazoncognito.com/oauth2/token
OAUTH_SCOPE="${OAUTH_SCOPE:-}"

# --- Broker CA trust anchor secret: pass an existing ARN, OR a PEM file path.
#     Defaults to the cert the client instance fetched from the S3 cache. ---
SERVER_CA_SECRET_ARN="${SERVER_CA_SECRET_ARN:-}"
BROKER_CA_CERT_FILE="${BROKER_CA_CERT_FILE:-/home/ec2-user/kafka.crt}"

# ---------------------- Discover VPC config from the stack -------------------
get_output() {
  aws cloudformation describe-stacks --region "$REGION" --stack-name "$STACK_NAME" \
    --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text 2>/dev/null || true
}
# Fail loudly if the stack can't be found. Without this check, a wrong STACK_NAME
# or AWS_REGION makes the lookups below fail inside variable assignments, and
# 'set -e' exits the script silently.
if ! aws cloudformation describe-stacks --region "$REGION" --stack-name "$STACK_NAME" >/dev/null 2>&1; then
  echo "ERROR: CloudFormation stack '$STACK_NAME' not found in region $REGION."
  echo "       Set STACK_NAME and AWS_REGION to match your stack, for example:"
  echo "       STACK_NAME=<your-stack-name> AWS_REGION=<region> bash $0"
  exit 1
fi
SUBNET1="${SUBNET1:-$(get_output PrivateSubnetOne)}"
SUBNET2="${SUBNET2:-$(get_output PrivateSubnetTwo)}"
SUBNET3="${SUBNET3:-$(get_output PrivateSubnetThree)}"
SG_ID="${SG_ID:-$(get_output KafkaBrokerSecurityGroupId)}"
[ -n "$SUBNET1" ] && [ -n "$SG_ID" ] || { echo "ERROR: could not resolve subnets/SG from stack $STACK_NAME; set SUBNET1..3 and SG_ID"; exit 1; }

# Auto-discover the OAuth client-credentials app client from the stack.
USER_POOL_ID="${USER_POOL_ID:-$(get_output CognitoUserPoolId)}"
OAUTH_CLIENT_ID="${OAUTH_CLIENT_ID:-$(get_output PollerClientId)}"
OAUTH_TOKEN_ENDPOINT="${OAUTH_TOKEN_ENDPOINT:-$(get_output OAuthTokenEndpoint)}"
OAUTH_SCOPE="${OAUTH_SCOPE:-$(get_output OAuthScope)}"
OAUTH_SCOPE="${OAUTH_SCOPE:-kafka/consume}"
if [ -z "$OAUTH_SECRET_ARN" ] && [ -z "$OAUTH_CLIENT_SECRET" ] && [ -n "$USER_POOL_ID" ] && [ -n "$OAUTH_CLIENT_ID" ]; then
  echo "Fetching poller app-client secret from Cognito..."
  OAUTH_CLIENT_SECRET=$(aws cognito-idp describe-user-pool-client --region "$REGION" \
    --user-pool-id "$USER_POOL_ID" --client-id "$OAUTH_CLIENT_ID" \
    --query 'UserPoolClient.ClientSecret' --output text)
fi

# ------------------------- Create secrets if needed --------------------------
# Create the secret if it does not exist, otherwise update it in place, and
# return its ARN (so re-runs are idempotent - secrets outlive the CFN stack).
ensure_secret() {  # name  secret-string  ->  prints ARN
  local name="$1" value="$2" arn
  arn=$(aws secretsmanager describe-secret --region "$REGION" --secret-id "$name" --query ARN --output text 2>/dev/null || true)
  if [ -n "$arn" ] && [ "$arn" != "None" ]; then
    aws secretsmanager put-secret-value --region "$REGION" --secret-id "$name" --secret-string "$value" >/dev/null
    echo "$arn"
  else
    aws secretsmanager create-secret --region "$REGION" --name "$name" --secret-string "$value" --query 'ARN' --output text
  fi
}

if [ -z "$OAUTH_SECRET_ARN" ]; then
  [ -n "$OAUTH_CLIENT_ID" ] && [ -n "$OAUTH_CLIENT_SECRET" ] && [ -n "$OAUTH_TOKEN_ENDPOINT" ] || {
    echo "ERROR: set OAUTH_SECRET_ARN, or OAUTH_CLIENT_ID + OAUTH_CLIENT_SECRET + OAUTH_TOKEN_ENDPOINT to create it"; exit 1; }
  echo "Creating/updating OAuth client-credentials secret..."
  OAUTH_SECRET_ARN=$(ensure_secret "${FUNCTION_NAME}-oauth-creds" \
    "{\"oauthClientId\":\"$OAUTH_CLIENT_ID\",\"oauthClientSecret\":\"$OAUTH_CLIENT_SECRET\",\"oauthTokenEndpointUrl\":\"$OAUTH_TOKEN_ENDPOINT\"}")
fi

if [ -z "$SERVER_CA_SECRET_ARN" ]; then
  [ -n "$BROKER_CA_CERT_FILE" ] && [ -f "$BROKER_CA_CERT_FILE" ] || {
    echo "ERROR: set SERVER_CA_SECRET_ARN, or BROKER_CA_CERT_FILE (PEM) to create it"; exit 1; }
  echo "Creating/updating broker CA trust-anchor secret (field 'certificate')..."
  SERVER_CA_SECRET_ARN=$(ensure_secret "${FUNCTION_NAME}-broker-ca" \
    "$(jq -n --arg c "$(cat "$BROKER_CA_CERT_FILE")" '{certificate:$c}')")
fi

# ---------------------------- Package the zip --------------------------------
# The handler uses only the AWS SDK v3 (already in the Lambda Node.js runtime),
# so the deployment package is just app.mjs + package.json.
echo "Packaging consumer zip..."
( cd "$PATTERN_DIR/kafka_event_consumer_function" && rm -f function.zip && zip -q function.zip app.mjs package.json )

# ---------------------------- DynamoDB table ---------------------------------
if ! aws dynamodb describe-table --region "$REGION" --table-name "$DDB_TABLE_NAME" >/dev/null 2>&1; then
  echo "Creating DynamoDB table $DDB_TABLE_NAME (topicPartition [HASH], offset [RANGE])..."
  aws dynamodb create-table --region "$REGION" --table-name "$DDB_TABLE_NAME" \
    --attribute-definitions AttributeName=topicPartition,AttributeType=S AttributeName=offset,AttributeType=N \
    --key-schema AttributeName=topicPartition,KeyType=HASH AttributeName=offset,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST >/dev/null
  aws dynamodb wait table-exists --region "$REGION" --table-name "$DDB_TABLE_NAME"
fi
DDB_TABLE_ARN=$(aws dynamodb describe-table --region "$REGION" --table-name "$DDB_TABLE_NAME" --query 'Table.TableArn' --output text)

# ---------------------------- Execution role ---------------------------------
ROLE_NAME="${ROLE_NAME:-${FUNCTION_NAME}-role}"
if ! aws iam get-role --role-name "$ROLE_NAME" >/dev/null 2>&1; then
  echo "Creating execution role $ROLE_NAME..."
  aws iam create-role --role-name "$ROLE_NAME" \
    --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}]}' >/dev/null
  aws iam attach-role-policy --role-name "$ROLE_NAME" \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
  echo "Waiting for role to propagate..."; sleep 15
fi
ROLE_ARN=$(aws iam get-role --role-name "$ROLE_NAME" --query 'Role.Arn' --output text)

# (Re)apply the role policies on every run so they always reference the CURRENT
# secret ARNs and table (secrets/table can be recreated across stack redeploys).
# Self-managed Kafka ESM: the poller creates ENIs in the VPC and reads the OAuth
# + CA secrets on the execution role's behalf.
aws iam put-role-policy --role-name "$ROLE_NAME" --policy-name kafka-esm-access --policy-document "{
  \"Version\":\"2012-10-17\",\"Statement\":[
    {\"Effect\":\"Allow\",\"Action\":[\"ec2:CreateNetworkInterface\",\"ec2:DescribeNetworkInterfaces\",\"ec2:DeleteNetworkInterface\",\"ec2:DescribeSecurityGroups\",\"ec2:DescribeSubnets\",\"ec2:DescribeVpcs\"],\"Resource\":\"*\"},
    {\"Effect\":\"Allow\",\"Action\":[\"secretsmanager:GetSecretValue\"],\"Resource\":[\"$OAUTH_SECRET_ARN\",\"$SERVER_CA_SECRET_ARN\"]}
  ]}"

# Allow the function to write messages to the DynamoDB table.
aws iam put-role-policy --role-name "$ROLE_NAME" --policy-name dynamodb-write --policy-document "{
  \"Version\":\"2012-10-17\",\"Statement\":[
    {\"Effect\":\"Allow\",\"Action\":[\"dynamodb:PutItem\",\"dynamodb:BatchWriteItem\"],\"Resource\":\"$DDB_TABLE_ARN\"}
  ]}"

# ------------------------- Create/update the function ------------------------
if aws lambda get-function --region "$REGION" --function-name "$FUNCTION_NAME" >/dev/null 2>&1; then
  echo "Updating function code..."
  aws lambda update-function-code --region "$REGION" --function-name "$FUNCTION_NAME" \
    --zip-file "fileb://$ZIP_PATH" >/dev/null
  aws lambda wait function-updated-v2 --region "$REGION" --function-name "$FUNCTION_NAME" 2>/dev/null || sleep 10
  aws lambda update-function-configuration --region "$REGION" --function-name "$FUNCTION_NAME" \
    --environment "Variables={DYNAMODB_TABLE_NAME=$DDB_TABLE_NAME}" >/dev/null
else
  echo "Creating function $FUNCTION_NAME..."
  aws lambda create-function --region "$REGION" --function-name "$FUNCTION_NAME" \
    --runtime "$RUNTIME" --role "$ROLE_ARN" --handler "$HANDLER" \
    --zip-file "fileb://$ZIP_PATH" --timeout 60 --memory-size 512 \
    --environment "Variables={DYNAMODB_TABLE_NAME=$DDB_TABLE_NAME}" >/dev/null
fi
aws lambda wait function-active-v2 --region "$REGION" --function-name "$FUNCTION_NAME" 2>/dev/null || sleep 10

# --------- Build the bootstrap-servers JSON array from the CSV list ----------
BS_JSON=$(node -e "process.stdout.write(JSON.stringify(process.argv[1].split(',').filter(Boolean)))" "$BOOTSTRAP_SERVERS")

# ------------------------- Create the event source mapping -------------------
# Skip if a mapping for this function + topic already exists (idempotent re-runs;
# the function code/env are still updated above).
EXISTING_ESM=$(aws lambda list-event-source-mappings --region "$REGION" --function-name "$FUNCTION_NAME" \
  --query "EventSourceMappings[?Topics[0]=='$TOPIC'].UUID | [0]" --output text 2>/dev/null)
if [ -n "$EXISTING_ESM" ] && [ "$EXISTING_ESM" != "None" ]; then
  echo "Event source mapping already exists for topic $TOPIC ($EXISTING_ESM); skipping create."
  echo "Delete it first if you need to recreate: aws lambda delete-event-source-mapping --uuid $EXISTING_ESM"
  exit 0
fi
echo "Creating self-managed Kafka event source mapping (OAUTHBEARER)..."
esm_created=false
for attempt in 1 2 3 4 5 6; do
if aws lambda create-event-source-mapping --region "$REGION" \
  --function-name "$FUNCTION_NAME" \
  --topics "$TOPIC" \
  --self-managed-event-source "{\"Endpoints\":{\"KAFKA_BOOTSTRAP_SERVERS\":$BS_JSON}}" \
  --self-managed-kafka-event-source-config "{\"ConsumerGroupId\":\"$CONSUMER_GROUP\"}" \
  --source-access-configurations "[
    {\"Type\":\"VPC_SUBNET\",\"URI\":\"subnet:$SUBNET1\"},
    {\"Type\":\"VPC_SUBNET\",\"URI\":\"subnet:$SUBNET2\"},
    {\"Type\":\"VPC_SUBNET\",\"URI\":\"subnet:$SUBNET3\"},
    {\"Type\":\"VPC_SECURITY_GROUP\",\"URI\":\"security_group:$SG_ID\"},
    {\"Type\":\"OAUTHBEARER_AUTH\",\"URI\":\"$OAUTH_SECRET_ARN\"},
    {\"Type\":\"OAUTHBEARER_SCOPE\",\"URI\":\"$OAUTH_SCOPE\"},
    {\"Type\":\"SERVER_ROOT_CA_CERTIFICATE\",\"URI\":\"$SERVER_CA_SECRET_ARN\"}
  ]" \
  --provisioned-poller-config "{\"PollerGroupName\":\"$POLLER_GROUP\",\"MinimumPollers\":1,\"MaximumPollers\":1}" \
  --starting-position TRIM_HORIZON \
  --batch-size "$BATCH_SIZE"; then esm_created=true; break; fi
  echo "  ESM create attempt $attempt failed (often IAM role/policy propagation); retrying in 15s..."; sleep 15
done
[ "$esm_created" = true ] || { echo "ERROR: event source mapping not created after retries"; exit 1; }

echo
echo "Done. Watch the mapping reach Enabled and process records:"
echo "  aws lambda list-event-source-mappings --region $REGION --function-name $FUNCTION_NAME \\"
echo "    --query 'EventSourceMappings[].[UUID,State,LastProcessingResult]' --output table"
echo "Then produce messages (scripts/producer_send.sh $TOPIC 10) and check the function's CloudWatch logs."
