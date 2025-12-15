#!/bin/bash

# DEPLOY FRAUD DETECTION AGENT TO AWS BEDROCK AGENTCORE

set -e

# DECLARE VARIABLES
AGENT_RUNTIME_NAME="fraud_risk_scorer"  # Must match pattern: [a-zA-Z][a-zA-Z0-9_]{0,47}
REGION="us-east-1"  # bedrock-agentcore-control is available in us-east-1
RUNTIME="python3.11"
ROLE_NAME="bedrock-agentcore-runtime-fraud-role"
ECR_REPO_NAME="fraud-risk-scorer"


###########################################################################################################
##########################          DO NOT MODIFY THE SCRIPT BEYOND HERE            #######################
###########################################################################################################



echo "🤖 Deploying $AGENT_RUNTIME_NAME Agent to AWS Bedrock AgentCore"
echo "================================================================"
echo ""

# GET AWS ACCOUNT ID
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
echo "📋 Account ID: $ACCOUNT_ID"
echo "📋 Region: $REGION"
echo ""

# CREATE ECR REPOSITORY IF IT DOESN'T EXIST
echo "🐳 Checking ECR repository..."
if ! aws ecr describe-repositories --repository-names $ECR_REPO_NAME --region $REGION >/dev/null 2>&1; then
  echo "📝 Creating ECR repository: $ECR_REPO_NAME"
  aws ecr create-repository \
    --repository-name $ECR_REPO_NAME \
    --region $REGION >/dev/null
  echo "✅ ECR repository created"
else
  echo "✅ ECR repository exists"
fi

ECR_URI="$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$ECR_REPO_NAME"
echo "📋 ECR URI: $ECR_URI"
echo ""

# BUILD DOCKER IMAGE
echo "📦 Building Docker image..."

# CHECK FOR DOCKERFILE 
if [ ! -f Dockerfile ]; then
  echo " Dockerfile does not exist. Please ensure the Dockerfile exists and try again."
  exit 1
fi

# LOGIN TO ECR
echo "🔐 Logging in to ECR..."
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ECR_URI
echo "✅ Logged in to ECR"
echo ""

# BUILD AND PUSH IMAGE
echo "🏷️ Tagging and pushing image..."
docker buildx create --use
docker buildx build --platform linux/arm64 -t $ECR_URI:latest --push .
echo "✅ Docker image built and pushed to ECR"
echo ""


# CREATE/CHECK IAM ROLE FOR AGENTCORE RUNTIME
echo "🔐 Checking IAM role for AgentCore Runtime..."
ROLE_ARN="arn:aws:iam::$ACCOUNT_ID:role/$ROLE_NAME"

if ! aws iam get-role --role-name $ROLE_NAME >/dev/null 2>&1; then
  echo "📝 Creating IAM role: $ROLE_NAME"
  
  # CREATE THE ROLE
  aws iam create-role \
    --role-name $ROLE_NAME \
    --assume-role-policy-document '{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "AssumeRolePolicy",
          "Effect": "Allow",
          "Principal": {
            "Service": [
              "bedrock-agentcore.amazonaws.com"
            ]
          },
          "Action": "sts:AssumeRole",
          "Condition": {
            "StringEquals": {
                "aws:SourceAccount": '"$ACCOUNT_ID"'
            },
            "ArnLike": {
                "aws:SourceArn": "arn:aws:bedrock-agentcore:'"$REGION"':'"$ACCOUNT_ID"':*"
            }
          }
        }
      ]
    }' >/dev/null
  
  sleep 3

  # ATTACH POLICIES
  aws iam attach-role-policy \
    --role-name $ROLE_NAME \
    --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly
  
  # ADD INLINE POLICY FOR ECS TASK EXECUTION AND CLOUDWATCH LOGS
  aws iam put-role-policy \
    --role-name $ROLE_NAME \
    --policy-name AgentCoreRuntimePolicy \
    --policy-document '{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "BedrockModelInvocation",
          "Effect": "Allow",
          "Action": [
            "bedrock:InvokeModel",
            "bedrock:InvokeModelWithResponseStream"
          ],
          "Resource": [
            "arn:aws:bedrock:*::foundation-model/*",
            "arn:aws:bedrock:'"$REGION"':'"$ACCOUNT_ID"':*"
            ]
        },
        {
          "Sid": "GetAgentAccessToken",
          "Effect": "Allow",
          "Action": [
            "bedrock-agentcore:GetWorkloadAccessToken",
            "bedrock-agentcore:GetWorkloadAccessTokenForJWT",
            "bedrock-agentcore:GetWorkloadAccessTokenForUserId"
          ],
          "Resource": [
            "arn:aws:bedrock-agentcore:'"$REGION"':'"$ACCOUNT_ID"':workload-identity-directory/default",
            "arn:aws:bedrock-agentcore:'"$REGION"':'"$ACCOUNT_ID"':workload-identity-directory/default/workload-identity/agentName-*"
            ]
        },
        {
          "Sid" : "ECRToken",
          "Effect": "Allow",
          "Action": [
            "ecr:BatchGetImage",
            "ecr:GetDownloadUrlForLayer"
          ],
          "Resource": ["arn:aws:ecr:'"$REGION"':'"$ACCOUNT_ID"':repository/*"]
        },
        {
          "Sid" : "ECRImageAccess",
          "Effect": "Allow",
          "Action": [
            "ecr:GetAuthorizationToken"
          ],
          "Resource": ["*"]
        },
        {
          "Sid" : "CreateCloudWatchLogGroup",
          "Effect": "Allow",
          "Action": [
            "logs:CreateLogGroup",
            "logs:DescribeLogStreams"
          ],
          "Resource": ["arn:aws:logs:'"$REGION"':'"$ACCOUNT_ID"':log-group:/aws/bedrock-agentcore/runtimes/*"]
        },
        {
          "Sid" : "ViewCloudWatchLogGroup",
          "Effect": "Allow",
          "Action": ["logs:DescribeLogGroups"],
          "Resource": "arn:aws:logs:'"$REGION"':'"$ACCOUNT_ID"':log-group:*"
        },

        {
          "Sid" : "CreateCloudWatchLogs",
          "Effect": "Allow",
          "Action": [
            "logs:CreateLogStream",
            "logs:PutLogEvents"
          ],
          "Resource": ["arn:aws:logs:'"$REGION"':'"$ACCOUNT_ID"':log-group:/aws/bedrock-agentcore/runtimes/*:log-stream:*"]
        },
        {
          "Sid" : "XrayObservability",
          "Effect": "Allow",
          "Action": [
            "xray:PutTraceSegments",
            "xray:PutTelemetryRecords",
            "xray:GetSamplingRules",
            "xray:GetSamplingTargets"
          ],
          "Resource": ["*"]
        },
        {
          "Sid" : "PutCloudWatchMetrics",
          "Effect": "Allow",
          "Action": [
            "cloudwatch:PutMetricData"
          ],
          "Resource": ["*"],
          "Condition": {
            "StringEquals": {
                "cloudwatch:namespace": "bedrock-agentcore"
                }
            }
        }
      ]
    }'
  
  echo "✅ IAM role created"
  echo "⏳ Waiting 5 seconds for IAM role to propagate..."
  sleep 5
else
  echo "✅ Role exists: $ROLE_NAME"
fi
echo ""

# 🚀 CREATE/UPDATE AGENT RUNTIME
echo "🚀 Deploying AgentCore Runtime..."

# CHECK IF AGENT RUNTIME EXISTS BY LISTING ALL RUNTIMES
RUNTIME_EXISTS=false
AGENT_RUNTIME_ID=""

# LIST RUNTIMES AND FIND OURS BY NAME
RUNTIME_LIST=$(aws bedrock-agentcore-control list-agent-runtimes \
  --region $REGION \
  --output json 2>/dev/null || echo '{"agentRuntimes":[]}')

RUNTIME_INFO=$(echo "$RUNTIME_LIST" | jq -r ".agentRuntimes[] | select(.agentRuntimeName==\"$AGENT_RUNTIME_NAME\")")
AGENT_RUNTIME_ID=$(echo "$RUNTIME_INFO" | jq -r '.agentRuntimeId // empty')

if [ -n "$AGENT_RUNTIME_ID" ]; then
  RUNTIME_EXISTS=true
  echo "🔄 Agent runtime exists (ID: $AGENT_RUNTIME_ID), updating..."
else
  echo "📝 Creating new agent runtime..."
fi

if [ "$RUNTIME_EXISTS" = true ]; then
  # UPDATE EXISTING RUNTIME
  aws bedrock-agentcore-control update-agent-runtime \
    --agent-runtime-id $AGENT_RUNTIME_ID \
    --agent-runtime-artifact "containerConfiguration={containerUri=$ECR_URI:latest}" \
    --role-arn $ROLE_ARN \
    --network-configuration "networkMode=PUBLIC" \
    --description "Fraud risk scoring agent runtime" \
    --region $REGION >/dev/null
  
  echo "✅ Agent runtime updated successfully!"
else
  # CREATE NEW RUNTIME
  RUNTIME_RESPONSE=$(aws bedrock-agentcore-control create-agent-runtime \
    --agent-runtime-name $AGENT_RUNTIME_NAME \
    --agent-runtime-artifact "containerConfiguration={containerUri=$ECR_URI:latest}" \
    --role-arn $ROLE_ARN \
    --network-configuration "networkMode=PUBLIC" \
    --description "Fraud risk scoring agent runtime" \
    --region $REGION \
    --output json)
  
  AGENT_RUNTIME_ID=$(echo "$RUNTIME_RESPONSE" | jq -r '.agentRuntimeId')
  echo "✅ Agent runtime created with ID: $AGENT_RUNTIME_ID"
fi

echo ""

# WAIT FOR DEFAULT ENDPOINT TO BECOME AVAILABLE
echo "⏳ Waiting for DEFAULT endpoint to become available..."
echo "   (This can take up to 2 minutes)"

MAX_WAIT_TIME=120  # 2 minutes
WAIT_INTERVAL=10   # 10 seconds
ELAPSED_TIME=0
ENDPOINT_FOUND=false

# INITIAL WAIT AFTER AGENT CREATION
sleep 10
ELAPSED_TIME=10

while [ $ELAPSED_TIME -le $MAX_WAIT_TIME ]; do
  echo "   Checking for endpoint... (${ELAPSED_TIME}s elapsed)"
  
  # GET ENDPOINT DETAILS
  ENDPOINT_INFO=$(aws bedrock-agentcore-control list-agent-runtime-endpoints \
    --agent-runtime-id $AGENT_RUNTIME_ID \
    --region $REGION \
    --output json 2>/dev/null || echo '{"runtimeEndpoints":[]}')
  
  # CHECK FOR DEFAULT ENDPOINT
  DEFAULT_ENDPOINT=$(echo "$ENDPOINT_INFO" | jq -r '.runtimeEndpoints[] | select(.name=="DEFAULT")')
  
  if [ -n "$DEFAULT_ENDPOINT" ]; then
    ENDPOINT_STATUS=$(echo "$DEFAULT_ENDPOINT" | jq -r '.status // empty')
    
    if [ "$ENDPOINT_STATUS" = "READY" ]; then
      echo "✅ DEFAULT endpoint is READY!"
      ENDPOINT_FOUND=true
      ENDPOINT_DATA="$DEFAULT_ENDPOINT"
      ENDPOINT_ARN=$(echo "$ENDPOINT_DATA" | jq -r '.agentRuntimeEndpointArn // empty')
      ENDPOINT_ID=$(echo "$ENDPOINT_DATA" | jq -r '.id // empty')
      break
    else
      echo "   DEFAULT endpoint found but status is: $ENDPOINT_STATUS"
    fi
  fi
  
  # WAIT BEFORE NEXT CHECK
  if [ $ELAPSED_TIME -lt $MAX_WAIT_TIME ]; then
    sleep $WAIT_INTERVAL
    ELAPSED_TIME=$((ELAPSED_TIME + WAIT_INTERVAL))
  else
    break
  fi
done

if [ "$ENDPOINT_FOUND" = false ]; then
  echo "⚠️  DEFAULT endpoint not ready after ${MAX_WAIT_TIME}s"
  echo "   You may need to wait longer and check manually:"
  echo "   aws bedrock-agentcore-control list-agent-runtime-endpoints \\"
  echo "     --agent-runtime-id $AGENT_RUNTIME_ID \\"
  echo "     --region $REGION"
fi


echo ""
echo "✅ Deployment complete!"
echo ""
echo "📋 Agent Runtime Details:"
echo "   Name: $AGENT_RUNTIME_NAME"
echo "   ID: $AGENT_RUNTIME_ID"
echo "   Region: $REGION"
echo "   Container: $ECR_URI:latest"
echo ""

# GET RUNTIME ARN
RUNTIME_ARN=$(echo "$ENDPOINT_DATA" | jq -r '.agentRuntimeArn // empty')

echo ""
echo "🧪 To test the agent:"
if [ -n "$RUNTIME_ARN" ]; then
  # CREATE TEST PAYLOAD FILE
  echo '{"amount": 5000}' > test-payload.json
  echo "   # Test payload created in test-payload.json"
  echo ""
  echo "   # Option 1: Using file (recommended):"
  echo "   aws bedrock-agentcore invoke-agent-runtime \\"
  echo "     --agent-runtime-arn $RUNTIME_ARN \\"
  echo "     --qualifier $ENDPOINT_ID \\"
  echo "     --payload fileb://test-payload.json \\"
  echo "     --content-type application/json \\"
  echo "     --accept application/json \\"
  echo "     --region $REGION \\"
  echo "     response.json"
  echo ""
  echo "   # Option 2: Direct with base64 encoding:"
  echo "   aws bedrock-agentcore invoke-agent-runtime \\"
  echo "     --agent-runtime-arn $RUNTIME_ARN \\"
  echo "     --qualifier $ENDPOINT_ID \\"
  echo "     --payload \"\$(echo -n '{\"input\":{\"amount\": 5000}}' | base64)\" \\"
  echo "     --content-type application/json \\"
  echo "     --accept application/json \\"
  echo "     --region $REGION \\"
  echo "     response.json"
  echo ""
  echo "   # Then view the response:"
  echo "   cat response.json"
else
  echo "   # Endpoint not fully configured - check endpoint status"
  echo "   aws bedrock-agentcore-control list-agent-runtime-endpoints \\"
  echo "     --agent-runtime-id $AGENT_RUNTIME_ID \\"
  echo "     --region $REGION"
fi
echo ""
# OUTPUT RUNTIME ARN FOR PARENT SCRIPT TO CAPTURE
echo "AGENT_RUNTIME_ARN=$RUNTIME_ARN"
echo "AGENT_REGION=$REGION"