#!/bin/bash

#DEPLOY DURABLE FUNCTION

set -e
#GET AWS ACCOUNT ID
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

#DECLARE VARIABLES
FUNCTION_NAME="fn-Fraud-Detection"
LAYER_NAME="lr-FraudDetection"
REGION="us-east-2"
ROLE_NAME="durable-function-execution-role"
BUCKET_NAME="durable-functions-$ACCOUNT_ID"
BUILD_LAYER=true #IF LAYER WAS ALREADY BUILT AND NO DEPENDENCY CHANGES, YOU CAN SET TO FALSE TO SKIP REBUILDING THE LAYER


###########################################################################################################
##########################          DO NOT MODIFY THE SCRIPT BEYOND HERE            #######################
###########################################################################################################

# SAVE CURRENT DIRECTORY
SCRIPT_DIR=$(pwd)

cd FraudDetection-Agent
./deploy.sh | tee /tmp/agent-deploy.log
AGENT_DEPLOY_EXIT_CODE=${PIPESTATUS[0]}

# ALWAYS RETURN TO ORIGINAL DIRECTORY
cd "$SCRIPT_DIR"

# CHECK IF AGENT DEPLOY SUCCEEDED
if [ $AGENT_DEPLOY_EXIT_CODE -ne 0 ]; then
  echo "❌ Agent deployment failed with exit code: $AGENT_DEPLOY_EXIT_CODE"
  exit 1
fi

# EXTRACT THE RUNTIME ARN FROM OUTPUT
AGENT_RUNTIME_ARN=$(grep "AGENT_RUNTIME_ARN=" /tmp/agent-deploy.log | cut -d'=' -f2)
AGENT_REGION=$(grep "AGENT_REGION=" /tmp/agent-deploy.log | cut -d'=' -f2)

echo "🚀 Deploying $FUNCTION_NAME Function in $REGION..."
echo ""


#CHECK IF S3 BUCKET EXISTS, CREATE IT IF IT DOESN'T
echo "🪣 Checking S3 bucket..."

# CHECK IF BUCKET EXISTS IN ANY REGION
BUCKET_EXISTS=false
if aws s3api head-bucket --bucket $BUCKET_NAME 2>/dev/null; then
  BUCKET_EXISTS=true
  # GET BUCKET REGION
  BUCKET_REGION=$(aws s3api get-bucket-location --bucket $BUCKET_NAME --query 'LocationConstraint' --output text)
  if [ "$BUCKET_REGION" = "None" ] || [ -z "$BUCKET_REGION" ]; then
    BUCKET_REGION="us-east-1"
  fi
  
  if [ "$BUCKET_REGION" != "$REGION" ]; then
    echo "⚠️  Bucket exists in $BUCKET_REGION but Lambda is in $REGION"
    echo "⚠️  Using region-specific bucket name..."
    BUCKET_NAME="durable-functions-bucket-$ACCOUNT_ID-$REGION"
    echo "🔄 New bucket name: $BUCKET_NAME"
    BUCKET_EXISTS=false
  else
    echo "✅ Bucket exists: $BUCKET_NAME in $REGION"
  fi
fi

# CREATE BUCKET IF IT DOESN'T EXIST
if [ "$BUCKET_EXISTS" = false ]; then
  if aws s3 ls "s3://$BUCKET_NAME" 2>&1 | grep -q 'NoSuchBucket'; then
    echo "📦 Creating S3 bucket: $BUCKET_NAME in $REGION"
    
    # RETRY LOGIC FOR BUCKET CREATION
    MAX_RETRIES=3
    RETRY_COUNT=0
    BUCKET_CREATED=false
    
    while [ $RETRY_COUNT -lt $MAX_RETRIES ] && [ "$BUCKET_CREATED" = false ]; do
      if [ $RETRY_COUNT -gt 0 ]; then
        echo "⏳ Waiting 10 seconds before retry $RETRY_COUNT/$MAX_RETRIES..."
        sleep 10
      fi
      
      #CREATE BUCKET WITH APPROPRIATE LOCATION CONSTRAINT
      if [ "$REGION" = "us-east-1" ]; then
        if aws s3api create-bucket --bucket $BUCKET_NAME --region $REGION 2>/dev/null; then
          BUCKET_CREATED=true
        fi
      else
        if aws s3api create-bucket \
          --bucket $BUCKET_NAME \
          --region $REGION \
          --create-bucket-configuration LocationConstraint=$REGION 2>/dev/null; then
          BUCKET_CREATED=true
        fi
      fi
      
      RETRY_COUNT=$((RETRY_COUNT + 1))
    done
    
    if [ "$BUCKET_CREATED" = false ]; then
      echo "❌ Failed to create bucket after $MAX_RETRIES attempts"
      echo "💡 The bucket might be in the process of being deleted. Please wait a few minutes and try again."
      exit 1
    fi
    
    #ENABLE VERSIONING (RECOMMENDED FOR LAMBDA DEPLOYMENTS)
    echo "📚 Enabling versioning..."
    aws s3api put-bucket-versioning \
      --bucket $BUCKET_NAME \
      --versioning-configuration Status=Enabled \
      --region $REGION
    
    echo "✅ Bucket created: $BUCKET_NAME"
  else
    echo "✅ Bucket exists: $BUCKET_NAME"
  fi
fi


#BUILD LAMBDA LAYER WITH NODE_MODULES
if $BUILD_LAYER = true; then 
  echo "📦 Building Lambda layer with dependencies..."
  cd FraudDetection-Lambda

  #CLEAN PREVIOUS BUILDS
  echo "🧹 Cleaning directory...."
  rm -rf node_modules && rm -rf layer && rm -rf layer.zip || true

  #INSTALL DEPENDENCIES
  echo "📥 Installing dependencies..."
  npm install --silent

  #CREATE LAYER STRUCTURE (LAMBDA LAYERS REQUIRE NODEJS/NODE_MODULES PATH)
  echo "🏗️  Creating layer structure..."
  mkdir -p layer/nodejs
  cp -r node_modules layer/nodejs/

  #CREATE LAYER ZIP
  echo "🗜️ Creating layer package..."
  cd layer
  zip -qr ../layer.zip .
  cd ..
  LAYER_SIZE=$(ls -lh layer.zip | awk '{print $5}')
  echo "✅ Layer package created: $LAYER_SIZE"

  #UPLOAD LAYER TO S3
  LAYER_S3_KEY="layers/$LAYER_NAME.zip"
  echo "⬆️  Uploading layer to S3..."
  aws s3 cp layer.zip s3://$BUCKET_NAME/$LAYER_S3_KEY --region $REGION
  echo "✅ Layer uploaded to s3://$BUCKET_NAME/$LAYER_S3_KEY"

  #CHECK IF LAYER EXISTS AND CREATE/UPDATE
  echo "🔍 Checking if layer exists..."
  LAYER_ARN=""
  if aws lambda list-layer-versions --layer-name $LAYER_NAME --region $REGION --query 'LayerVersions[0].LayerVersionArn' --output text 2>/dev/null | grep -q "arn:aws:lambda"; then
    echo "Layer exists, publishing new version..."
  else
    echo "Creating new layer..."
  fi

  #PUBLISH LAYER VERSION
  echo "🚀 Publishing layer"
  LAYER_ARN=$(aws lambda publish-layer-version \
    --layer-name $LAYER_NAME \
    --description "Node modules for Fraud Detection durable function" \
    --content S3Bucket=$BUCKET_NAME,S3Key=$LAYER_S3_KEY \
    --compatible-runtimes nodejs24.x \
    --region $REGION \
    --query 'LayerVersionArn' \
    --output text)

  echo "✅ Layer published: $LAYER_ARN"
  echo ""

  #CLEAN UP LAYER ARTIFACTS
  echo "🧹 Cleaning directory...."
  rm -rf layer
  cd ..

else
  echo "⏭️  Skipping layer build..."
  echo "🔍 Getting existing layer ARN..."
  
  # GET THE LATEST LAYER VERSION ARN
  LAYER_ARN=$(aws lambda list-layer-versions \
    --layer-name $LAYER_NAME \
    --region $REGION \
    --query 'LayerVersions[0].LayerVersionArn' \
    --output text 2>/dev/null)
  
  if [ -z "$LAYER_ARN" ] || [ "$LAYER_ARN" = "None" ]; then
    echo "❌ Layer '$LAYER_NAME' not found in region $REGION"
    echo "💡 Set BUILD_LAYER=true to create the layer first"
    exit 1
  fi
  
  echo "✅ Found existing layer: $LAYER_ARN"
  echo ""
  
  # INSTALL DEPENDENCIES FOR TYPESCRIPT COMPILATION (WILL BE REMOVED AFTER BUILD)
  cd FraudDetection-Lambda
  echo "📥 Installing dependencies for TypeScript compilation..."
  npm install --silent
  cd ..
fi

# 🔨 BUILD LAMBDA FUNCTION CODE (WITHOUT NODE_MODULES)
echo "🔨 Building Lambda function code..."
cd FraudDetection-Lambda

# 🧹 CLEAN BUILD ARTIFACTS
rm -rf dist && rm -f function.zip

# COMPILE TYPESCRIPT
tsc
echo "✅ TypeScript compiled"

# 📦 CREATE FUNCTION DEPLOYMENT PACKAGE (WITHOUT NODE_MODULES - THEY'RE IN THE LAYER)
echo "📦 Creating function deployment package..."
cd dist
zip -qr ../function.zip .
cd ..
zip -r ../function.zip package.json
PACKAGE_SIZE=$(ls -lh function.zip | awk '{print $5}')
echo "✅ Function package created: $PACKAGE_SIZE (dependencies in layer)"

# 🧹 CLEAN UP NODE_MODULES (NOT NEEDED IN DEPLOYMENT PACKAGE)
echo "🧹 Cleaning up node_modules..."
rm -rf node_modules && rm -rf package-lock.json
cd ..

#UPLOAD FUNCTION TO S3
S3_KEY="functions/$FUNCTION_NAME.zip"
echo "⬆️  Uploading function to S3..."
aws s3 cp FraudDetection-Lambda/function.zip s3://$BUCKET_NAME/$S3_KEY --region $REGION
echo "✅ Function uploaded to s3://$BUCKET_NAME/$S3_KEY"
echo ""

#CHECK IF IAM EXECUTION ROLE EXISTS, CREATE IF IT DOESN'T
echo "� Checking if IAM execution role exists..."
if aws iam get-role --role-name $ROLE_NAME >/dev/null 2>&1; then
  echo "✅ Role exists: $ROLE_NAME"
  ROLE_ARN="arn:aws:iam::$ACCOUNT_ID:role/$ROLE_NAME"

else
  echo "📝 Creating IAM execution role: $ROLE_NAME"
  
  # CREATE THE ROLE
  ROLE=$(aws iam create-role \
    --role-name $ROLE_NAME \
    --assume-role-policy-document '{"Version": "2012-10-17", "Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}' \
    --output text)
  
  echo "✅ Role created"
  
  # EXTRACT ROLE ARN
  ROLE_ARN=$(echo "$ROLE" | grep -Eo 'arn:aws:iam::[0-9]{12}:role/[^[:space:]]+')
  echo "📋 Role ARN: $ROLE_ARN"
  
  # ATTACH BASIC EXECUTION POLICY
  echo "📎 Attaching basic execution policy..."
  aws iam attach-role-policy \
    --role-name $ROLE_NAME \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
  
  # ADD DURABLE EXECUTION POLICY
  echo "📎 Adding durable execution policy..."
  aws iam put-role-policy \
    --role-name $ROLE_NAME \
    --policy-name LambdaDurableExecutionPolicy \
    --policy-document "{\"Version\": \"2012-10-17\",\"Statement\": [{\"Sid\": \"AWSLambdaDurableExecutionRole\",\"Effect\": \"Allow\",\"Action\": [\"lambda:CheckpointDurableExecution\",\"lambda:GetDurableExecutionState\"],\"Resource\": \"arn:aws:lambda:$REGION:$ACCOUNT_ID:function:$FUNCTION_NAME:*\"}]}"
  
fi

# ADD BEDROCK AGENTCORE INVOKE POLICY (ALWAYS RUN, WHETHER ROLE IS NEW OR EXISTING)
echo "📎 Adding/Updating Bedrock AgentCore invoke policy..."
aws iam put-role-policy \
  --role-name $ROLE_NAME \
  --policy-name BedrockAgentCoreInvokePolicy \
  --policy-document '{"Version": "2012-10-17","Statement": [{"Sid": "InvokeAgentRuntime","Effect": "Allow","Action": ["bedrock-agentcore:InvokeAgentRuntime"],"Resource": ["'"$AGENT_RUNTIME_ARN"'/*","'"$AGENT_RUNTIME_ARN"'"]}]}'

echo "✅ IAM role configured successfully"
echo ""

echo "⏳ Waiting 10 seconds for IAM role to propagate..."
sleep 10

# 🔍 CHECK IF FUNCTION EXISTS
echo "🔍 Checking if function exists..."
if aws lambda get-function --function-name $FUNCTION_NAME --region $REGION >/dev/null 2>&1; then
  echo "Function exists, updating code instead..."
  aws lambda update-function-code \
    --function-name $FUNCTION_NAME \
    --s3-bucket $BUCKET_NAME \
    --s3-key $S3_KEY \
    --region $REGION \
    --query 'FunctionArn' \
    --output text

  sleep 3
  

  # UPDATE ENVIRONMENT VARIABLES
  echo "🔧 Updating environment variables..."
  aws lambda update-function-configuration \
    --function-name $FUNCTION_NAME \
    --environment "Variables={AGENT_RUNTIME_ARN=$AGENT_RUNTIME_ARN,AGENT_REGION=$AGENT_REGION}" \
    --region $REGION >/dev/null
  

  echo "📋 Publishing new version..."
  FUNCTION_ARN=$(aws lambda publish-version \
    --function-name $FUNCTION_NAME \
    --region $REGION \
    --query 'FunctionArn' \
    --output text)
  
  echo "✅ Function updated!"
  echo ""
  echo "📋 Function ARN: $FUNCTION_ARN"
  rm -f function.zip
  exit 0
fi

# 🚀 CREATE DURABLE FUNCTION WITH LAYER
echo "🚀 Creating durable function with SDK layer..."
aws lambda create-function \
  --function-name $FUNCTION_NAME \
  --runtime nodejs24.x \
  --role arn:aws:iam::$ACCOUNT_ID:role/$ROLE_NAME \
  --handler index.handler \
  --code S3Bucket=$BUCKET_NAME,S3Key=$S3_KEY \
  --environment "Variables={AGENT_RUNTIME_ARN=$AGENT_RUNTIME_ARN,AGENT_REGION=$AGENT_REGION}" \
  --layers $LAYER_ARN \
  --durable-config '{"ExecutionTimeout":600,"RetentionPeriodInDays":7}' \
  --timeout 120 \
  --memory-size 128 \
  --region $REGION \
  --query 'FunctionArn' \
  --output text

echo ""
echo "⏳ Waiting for function to be ready..."
sleep 5

# 📋 PUBLISH VERSION
echo "📋 Publishing version..."
FUNCTION_ARN=$(aws lambda publish-version \
  --function-name $FUNCTION_NAME \
  --region $REGION \
  --query 'FunctionArn' \
  --output text)

echo "✅ Function deployed successfully!"
echo ""
echo "📋 Function Details:"
echo "   Name: $FUNCTION_NAME"
echo "   ARN: $FUNCTION_ARN"
echo "   Region: $REGION"
echo "   Layer: $LAYER_ARN"
echo "   Package Size: $PACKAGE_SIZE"
echo ""
echo "🧪 Test the Fraud Detection Function:"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📝 INTERACTIVE TESTING (Recommended)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Use the interactive invoke script:"
echo "   ./invoke-function.sh"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "💰 MANUAL TESTING - Transaction Scenarios"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1️⃣  Low Risk Transaction (Auto-Approve, score < 3):"
echo "   aws durable-lambda invoke \\"
echo "     --function-name '$FUNCTION_ARN' \\"
echo "     --invocation-type Event \\"
echo "     --payload '{\"transactionId\":\"tx-001\",\"amount\":500,\"location\":\"New York\",\"vendor\":\"Amazon\",\"initialScore\":0}' \\"
echo "     --region $REGION \\"
echo "     output-low-risk.json"
echo ""
echo "2️⃣  High Risk Transaction (Send to Fraud, score = 5):"
echo "   aws durable-lambda invoke \\"
echo "     --function-name '$FUNCTION_ARN' \\"
echo "     --invocation-type Event \\"
echo "     --payload '{\"transactionId\":\"tx-002\",\"amount\":10000,\"location\":\"Unknown\",\"vendor\":\"Suspicious Store\",\"initialScore\":0}' \\"
echo "     --region $REGION \\"
echo "     output-high-risk.json"
echo ""
echo "3️⃣  Medium Risk Transaction (Human Verification, score 3-4):"
echo "   aws durable-lambda invoke \\"
echo "     --function-name '$FUNCTION_ARN' \\"
echo "     --invocation-type Event \\"
echo "     --payload '{\"transactionId\":\"tx-003\",\"amount\":6500,\"location\":\"Los Angeles\",\"vendor\":\"Electronics Store\",\"initialScore\":0}' \\"
echo "     --region $REGION \\"
echo "     output-medium-risk.json"
echo ""
echo "   📧 After invocation, retrieve callback IDs from logs and use:"
echo "      ./send-callback.sh"
echo ""
echo "4️⃣  Override Risk Score (Skip Agent, use score 3):"
echo "   aws durable-lambda invoke \\"
echo "     --function-name '$FUNCTION_ARN' \\"
echo "     --invocation-type Event \\"
echo "     --payload '{\"transactionId\":\"tx-004\",\"amount\":1000,\"location\":\"Chicago\",\"vendor\":\"Store\",\"initialScore\":3}' \\"
echo "     --region $REGION \\"
echo "     output-override.json"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 MONITORING & DEBUGGING"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 List all durable executions:"
echo "   aws durable-lambda list-durable-executions-by-function \\"
echo "     --function-name $FUNCTION_NAME \\"
echo "     --region $REGION"
echo ""
echo "🔍 Get execution details (replace <ARN> with execution ARN from invoke output):"
echo "   aws durable-lambda get-durable-execution \\"
echo "     --durable-execution-arn <ARN> \\"
echo "     --region $REGION"
echo ""
echo "📜 View execution history with data:"
echo "   aws durable-lambda get-durable-execution-history \\"
echo "     --durable-execution-arn <ARN> \\"
echo "     --region $REGION \\"
echo "     --include-execution-data"
echo ""
echo "📝 View CloudWatch Logs (real-time):"
echo "   aws logs tail /aws/lambda/$FUNCTION_NAME \\"
echo "     --region $REGION \\"
echo "     --follow"
echo ""
echo "📝 View recent logs (last hour):"
echo "   aws logs tail /aws/lambda/$FUNCTION_NAME \\"
echo "     --region $REGION \\"
echo "     --since 1h"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "💡 RISK SCORE BEHAVIOR"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "   Amount < \$1,000      → Scores 1-2 (Auto-Approved)"
echo "   Amount \$1,000-\$4,999 → Scores 1-4 (Weighted toward lower)"
echo "   Amount \$5,000-\$9,999 → Scores 3-5 (Higher risk)"
echo "   Amount = \$6,500       → Score 3 (Forces human verification)"
echo "   Amount ≥ \$10,000     → Score 5 (Send to Fraud)"
echo ""

# 🧹 CLEANUP
rm -f function.zip

echo "✅ Deployment complete!"