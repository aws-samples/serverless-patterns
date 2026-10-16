#!/bin/bash
# =============================================================================
# Deploy the Node.js Kafka consumer as a Lambda function with a SELF-MANAGED KAFKA
# event source using IAM_AUTH, via the AWS CLI.
#
# The MSK cluster (IAM auth) is declared to Lambda as a SELF-MANAGED event source
# pointed at its IAM bootstrap endpoint (:9098) with the IAM_AUTH flag (per the
# "Kafka OAuth & IAM Testing Manual", Route B). The poller authenticates with the
# function's execution role via SASL/AWS_MSK_IAM - no secret, no trust anchor.
# AWS SAM does not support this auth type, so we use the AWS CLI directly.
#
# Reuses the same Node.js consumer (app.mjs); it writes messages to DynamoDB.
#
# PREREQUISITE: your account is ALLOWLISTED for the self-managed Kafka ESM auth types.
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
STACK_NAME="${STACK_NAME:-kafka-iam}"
# Lambda-side resource names are derived from the stack name, so two stacks in the
# same account and region (for example the Java and Python versions of this
# pattern) never overwrite each other's function, role, secrets, or table.
FUNCTION_NAME="${FUNCTION_NAME:-${STACK_NAME}-consumer}"
RUNTIME="${RUNTIME:-nodejs22.x}"
HANDLER="app.lambdaHandler"
ZIP_PATH="${ZIP_PATH:-$PATTERN_DIR/kafka_event_consumer_function/function.zip}"
TOPIC="${TOPIC:-${KAFKA_TOPIC:-KafkaIamLambdaTopic}}"
CONSUMER_GROUP="${CONSUMER_GROUP:-lambda-iam-consumer}"
POLLER_GROUP="${POLLER_GROUP:-${CONSUMER_GROUP}-cell1}"
BATCH_SIZE="${BATCH_SIZE:-10}"
DDB_TABLE_NAME="${DDB_TABLE_NAME:-${STACK_NAME}-messages}"
if [ ${#FUNCTION_NAME} -gt 59 ]; then
  echo "ERROR: FUNCTION_NAME '$FUNCTION_NAME' is longer than 59 characters (IAM role names, which"
  echo "       add '-role', max out at 64). Set FUNCTION_NAME to something shorter."
  exit 1
fi

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
SG_ID="${SG_ID:-$(get_output MSKSecurityGroupId)}"
MSK_CLUSTER_ARN="${MSK_CLUSTER_ARN:-$(get_output MSKClusterArn)}"
[ -n "$SUBNET1" ] && [ -n "$SG_ID" ] && [ -n "$MSK_CLUSTER_ARN" ] || { echo "ERROR: could not resolve subnets/SG/cluster from stack $STACK_NAME"; exit 1; }

# IAM bootstrap brokers (:9098)
BOOTSTRAP_SERVERS="${BOOTSTRAP_SERVERS:-$(aws kafka get-bootstrap-brokers --region "$REGION" --cluster-arn "$MSK_CLUSTER_ARN" --query 'BootstrapBrokerStringSaslIam' --output text)}"
[ -n "$BOOTSTRAP_SERVERS" ] || { echo "ERROR: could not resolve IAM bootstrap brokers"; exit 1; }

# kafka-cluster:* resource ARNs (cluster name is <stack>-cluster)
CLUSTER_RES="arn:aws:kafka:${REGION}:$(aws sts get-caller-identity --query Account --output text):cluster/${STACK_NAME}-cluster/*"
TOPIC_RES="${CLUSTER_RES/:cluster\//:topic\/}"
GROUP_RES="${CLUSTER_RES/:cluster\//:group\/}"

# ------------------------------ Package the zip ------------------------------
# The consumer only uses the AWS SDK v3 (already in the Lambda Node.js runtime),
# so the deployment package is just app.mjs (+ package.json).
if [ ! -f "$ZIP_PATH" ]; then
  echo "Packaging consumer zip..."
  ( cd "$PATTERN_DIR/kafka_event_consumer_function" && rm -f function.zip && zip -q function.zip app.mjs package.json )
fi

# ---------------------------- DynamoDB table ---------------------------------
if ! aws dynamodb describe-table --region "$REGION" --table-name "$DDB_TABLE_NAME" >/dev/null 2>&1; then
  echo "Creating DynamoDB table $DDB_TABLE_NAME..."
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

# The poller creates ENIs and authenticates to MSK with the execution role's
# IAM identity (SASL/AWS_MSK_IAM): grant read access on the cluster/topic/group.
aws iam put-role-policy --role-name "$ROLE_NAME" --policy-name kafka-esm-access --policy-document "{
  \"Version\":\"2012-10-17\",\"Statement\":[
    {\"Effect\":\"Allow\",\"Action\":[\"ec2:CreateNetworkInterface\",\"ec2:DescribeNetworkInterfaces\",\"ec2:DeleteNetworkInterface\",\"ec2:DescribeSecurityGroups\",\"ec2:DescribeSubnets\",\"ec2:DescribeVpcs\"],\"Resource\":\"*\"},
    {\"Effect\":\"Allow\",\"Action\":[\"kafka-cluster:Connect\",\"kafka-cluster:DescribeCluster\"],\"Resource\":\"$CLUSTER_RES\"},
    {\"Effect\":\"Allow\",\"Action\":[\"kafka-cluster:DescribeTopic\",\"kafka-cluster:ReadData\"],\"Resource\":\"$TOPIC_RES\"},
    {\"Effect\":\"Allow\",\"Action\":[\"kafka-cluster:AlterGroup\",\"kafka-cluster:DescribeGroup\"],\"Resource\":\"$GROUP_RES\"}
  ]}"
aws iam put-role-policy --role-name "$ROLE_NAME" --policy-name dynamodb-write --policy-document "{
  \"Version\":\"2012-10-17\",\"Statement\":[
    {\"Effect\":\"Allow\",\"Action\":[\"dynamodb:PutItem\",\"dynamodb:BatchWriteItem\"],\"Resource\":\"$DDB_TABLE_ARN\"}
  ]}"

# ------------------------- Create/update the function ------------------------
if aws lambda get-function --region "$REGION" --function-name "$FUNCTION_NAME" >/dev/null 2>&1; then
  aws lambda update-function-code --region "$REGION" --function-name "$FUNCTION_NAME" --zip-file "fileb://$ZIP_PATH" >/dev/null
  aws lambda wait function-updated-v2 --region "$REGION" --function-name "$FUNCTION_NAME" 2>/dev/null || sleep 10
  aws lambda update-function-configuration --region "$REGION" --function-name "$FUNCTION_NAME" \
    --environment "Variables={DYNAMODB_TABLE_NAME=$DDB_TABLE_NAME}" >/dev/null
else
  aws lambda create-function --region "$REGION" --function-name "$FUNCTION_NAME" \
    --runtime "$RUNTIME" --role "$ROLE_ARN" --handler "$HANDLER" \
    --zip-file "fileb://$ZIP_PATH" --timeout 60 --memory-size 512 \
    --environment "Variables={DYNAMODB_TABLE_NAME=$DDB_TABLE_NAME}" >/dev/null
fi
aws lambda wait function-active-v2 --region "$REGION" --function-name "$FUNCTION_NAME" 2>/dev/null || sleep 10

BS_JSON=$(node -e "console.log(JSON.stringify(process.argv[1].split(',').filter(Boolean)))" "$BOOTSTRAP_SERVERS")

# ------------------------- Create the event source mapping -------------------
EXISTING_ESM=$(aws lambda list-event-source-mappings --region "$REGION" --function-name "$FUNCTION_NAME" \
  --query "EventSourceMappings[?Topics[0]=='$TOPIC'].UUID | [0]" --output text 2>/dev/null)
if [ -n "$EXISTING_ESM" ] && [ "$EXISTING_ESM" != "None" ]; then
  echo "Event source mapping already exists for topic $TOPIC ($EXISTING_ESM); skipping create."
  exit 0
fi
echo "Creating self-managed Kafka event source mapping (IAM_AUTH)..."
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
    {\"Type\":\"IAM_AUTH\"}
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
