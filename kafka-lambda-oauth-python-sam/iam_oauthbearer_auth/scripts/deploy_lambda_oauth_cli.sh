#!/bin/bash
# =============================================================================
# Deploy the Java Kafka consumer as a Lambda function with a SELF-MANAGED KAFKA
# event source using IAM Outbound Identity Federation (IAM_OAUTHBEARER_AUTH),
# via the AWS CLI.
#
# The Lambda poller mints an AWS web-identity (OIDC) token from its execution
# role and presents it to the brokers over SASL/OAUTHBEARER. There is no external
# identity provider and no OAuth client secret. AWS SAM does not support this
# auth type, so this uses `aws lambda create-event-source-mapping` directly.
#
# Reuses the same Python consumer (app.lambda_handler) and writes messages to DynamoDB.
#
# -----------------------------------------------------------------------------
# PREREQUISITES:
#   1. Your account is ALLOWLISTED for the self-managed Kafka ESM auth types.
#   2. Outbound web identity federation is ENABLED for the account (this script
#      calls enable-outbound-web-identity-federation; it is idempotent).
#   3. The brokers expose a SASL_SSL / OAUTHBEARER listener validating the AWS STS
#      OIDC issuer with audience == OUTBOUND_AUDIENCE (the CloudFormation stack
#      configures this).
# NOTE (under development): the sts:GetWebIdentityToken / outbound-federation APIs
# are not finalized; adjust the CLI calls here and in the broker config if needed.
# =============================================================================
set -euo pipefail
export AWS_PAGER=""
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
STACK_NAME="${STACK_NAME:-kafka-iam-oauth}"
# Lambda-side resource names are derived from the stack name, so two stacks in the
# same account and region (for example the Java and Python versions of this
# pattern) never overwrite each other's function, role, secrets, or table.
FUNCTION_NAME="${FUNCTION_NAME:-${STACK_NAME}-consumer}"
RUNTIME="${RUNTIME:-python3.13}"
HANDLER="app.lambda_handler"
ZIP_PATH="${ZIP_PATH:-$PATTERN_DIR/kafka_event_consumer_function/function.zip}"
TOPIC="${TOPIC:-${KAFKA_TOPIC:-KafkaIamOAuthBearerLambdaTopic}}"
CONSUMER_GROUP="${CONSUMER_GROUP:-lambda-iam-oauth-consumer}"
POLLER_GROUP="${POLLER_GROUP:-${CONSUMER_GROUP}-cell1}"
BATCH_SIZE="${BATCH_SIZE:-10}"
DDB_TABLE_NAME="${DDB_TABLE_NAME:-${STACK_NAME}-messages}"
if [ ${#FUNCTION_NAME} -gt 59 ]; then
  echo "ERROR: FUNCTION_NAME '$FUNCTION_NAME' is longer than 59 characters (IAM role names, which"
  echo "       add '-role', max out at 64). Set FUNCTION_NAME to something shorter."
  exit 1
fi

# Brokers' SASL_SSL / OAUTHBEARER listener (:9092 in this pattern).
BOOTSTRAP_SERVERS="${BOOTSTRAP_SERVERS:-10.0.1.10:9092,10.0.2.10:9092,10.0.3.10:9092}"

# Broker CA trust anchor (still SASL_SSL): pass an ARN or a PEM file path.
SERVER_CA_SECRET_ARN="${SERVER_CA_SECRET_ARN:-}"
BROKER_CA_CERT_FILE="${BROKER_CA_CERT_FILE:-/home/ec2-user/kafka.crt}"

# ---------------------- Discover config from the stack -----------------------
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
OUTBOUND_AUDIENCE="${OUTBOUND_AUDIENCE:-$(get_output OutboundAudience)}"
OUTBOUND_AUDIENCE="${OUTBOUND_AUDIENCE:-kafka-cluster}"
[ -n "$SUBNET1" ] && [ -n "$SG_ID" ] || { echo "ERROR: could not resolve subnets/SG from stack $STACK_NAME; set SUBNET1..3 and SG_ID"; exit 1; }

# Ensure the account has outbound web identity federation enabled (idempotent).
aws iam enable-outbound-web-identity-federation 2>/dev/null || true

# ------------------------- Broker CA trust-anchor secret ---------------------
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
if [ -z "$SERVER_CA_SECRET_ARN" ]; then
  [ -n "$BROKER_CA_CERT_FILE" ] && [ -f "$BROKER_CA_CERT_FILE" ] || {
    echo "ERROR: set SERVER_CA_SECRET_ARN, or BROKER_CA_CERT_FILE (PEM) to create it"; exit 1; }
  echo "Creating/updating broker CA trust-anchor secret (field 'certificate')..."
  SERVER_CA_SECRET_ARN=$(ensure_secret "${FUNCTION_NAME}-broker-ca" \
    "$(jq -n --arg c "$(cat "$BROKER_CA_CERT_FILE")" '{certificate:$c}')")
fi

# ----------------------------- Package the zip -------------------------------
# The consumer only needs app.py; boto3 is provided by the Lambda Python runtime.
if [ ! -f "$ZIP_PATH" ]; then
  echo "Packaging consumer zip..."
  ( cd "$PATTERN_DIR/kafka_event_consumer_function" && rm -f function.zip && zip -q function.zip app.py )
fi

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

# (Re)apply policies every run. The poller creates ENIs, reads the broker-CA
# secret, and mints an AWS web-identity token via sts:GetWebIdentityToken.
aws iam put-role-policy --role-name "$ROLE_NAME" --policy-name kafka-esm-access --policy-document "{
  \"Version\":\"2012-10-17\",\"Statement\":[
    {\"Effect\":\"Allow\",\"Action\":[\"ec2:CreateNetworkInterface\",\"ec2:DescribeNetworkInterfaces\",\"ec2:DeleteNetworkInterface\",\"ec2:DescribeSecurityGroups\",\"ec2:DescribeSubnets\",\"ec2:DescribeVpcs\"],\"Resource\":\"*\"},
    {\"Effect\":\"Allow\",\"Action\":[\"sts:GetWebIdentityToken\"],\"Resource\":\"*\"},
    {\"Effect\":\"Allow\",\"Action\":[\"secretsmanager:GetSecretValue\"],\"Resource\":[\"$SERVER_CA_SECRET_ARN\"]}
  ]}"
aws iam put-role-policy --role-name "$ROLE_NAME" --policy-name dynamodb-write --policy-document "{
  \"Version\":\"2012-10-17\",\"Statement\":[
    {\"Effect\":\"Allow\",\"Action\":[\"dynamodb:PutItem\",\"dynamodb:BatchWriteItem\"],\"Resource\":\"$DDB_TABLE_ARN\"}
  ]}"

# Grant the poller READ on the topic + consumer groups. The poller's web-identity
# token subject is its execution role ARN, so that is the Kafka principal. ACLs
# are set over the brokers' internal PLAINTEXT listener (ANONYMOUS is a broker
# super user there), which requires this to run on the client EC2 instance.
KAFKA_HOME="${KAFKA_HOME:-/home/ec2-user/kafka}"
INTERNAL_BOOTSTRAP="${INTERNAL_BOOTSTRAP:-$(echo "$BOOTSTRAP_SERVERS" | sed 's/:9092/:9094/g')}"
if [ -x "$KAFKA_HOME/bin/kafka-acls.sh" ]; then
  echo "Granting poller principal READ (User:$ROLE_ARN) via the internal listener..."
  "$KAFKA_HOME"/bin/kafka-acls.sh --bootstrap-server "$INTERNAL_BOOTSTRAP" --add --allow-principal "User:$ROLE_ARN" --operation Read --topic "$TOPIC" 2>/dev/null || true
  "$KAFKA_HOME"/bin/kafka-acls.sh --bootstrap-server "$INTERNAL_BOOTSTRAP" --add --allow-principal "User:$ROLE_ARN" --operation Read --group '*' 2>/dev/null || true
else
  echo "NOTE: kafka-acls.sh not found; grant the poller READ manually (principal User:$ROLE_ARN)."
fi

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

BS_JSON=$(python3 -c "import json,sys;print(json.dumps([s for s in sys.argv[1].split(',') if s]))" "$BOOTSTRAP_SERVERS")

# ------------------------- Create the event source mapping -------------------
EXISTING_ESM=$(aws lambda list-event-source-mappings --region "$REGION" --function-name "$FUNCTION_NAME" \
  --query "EventSourceMappings[?Topics[0]=='$TOPIC'].UUID | [0]" --output text 2>/dev/null)
if [ -n "$EXISTING_ESM" ] && [ "$EXISTING_ESM" != "None" ]; then
  echo "Event source mapping already exists for topic $TOPIC ($EXISTING_ESM); skipping create."
  echo "Delete it first if you need to recreate: aws lambda delete-event-source-mapping --uuid $EXISTING_ESM"
  exit 0
fi
echo "Creating self-managed Kafka event source mapping (IAM_OAUTHBEARER_AUTH)..."
# IAM Outbound: auth entry is a flag (no URI); OAUTHBEARER_AUDIENCE is required.
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
    {\"Type\":\"IAM_OAUTHBEARER_AUTH\"},
    {\"Type\":\"OAUTHBEARER_AUDIENCE\",\"URI\":\"$OUTBOUND_AUDIENCE\"},
    {\"Type\":\"SERVER_ROOT_CA_CERTIFICATE\",\"URI\":\"$SERVER_CA_SECRET_ARN\"}
  ]" \
  --provisioned-poller-config "{\"PollerGroupName\":\"$POLLER_GROUP\",\"MinimumPollers\":1,\"MaximumPollers\":1}" \
  --starting-position TRIM_HORIZON \
  --batch-size "$BATCH_SIZE"; then esm_created=true; break; fi
  echo "  ESM create attempt $attempt failed (often IAM role/policy propagation); retrying in 15s..."; sleep 15
done
[ "$esm_created" = true ] || { echo "ERROR: event source mapping not created after retries"; exit 1; }

echo
echo "Done. Watch the mapping reach Enabled:"
echo "  aws lambda list-event-source-mappings --region $REGION --function-name $FUNCTION_NAME \\"
echo "    --query 'EventSourceMappings[].[UUID,State,LastProcessingResult]' --output table"
echo "Then produce messages (scripts/producer_send.sh $TOPIC 10) and check CloudWatch logs + DynamoDB ($DDB_TABLE_NAME)."
