#!/bin/bash

# INVOKE DURABLE FRAUD DETECTION FUNCTION

# GET AWS ACCOUNT ID
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# FUNCTION CONFIGURATION (matches deploy.sh)
FUNCTION_NAME="fn-Fraud-Detection"
REGION="us-east-2"

echo "🔍 Fraud Detection - Durable Function Invocation"
echo "================================================"
echo ""

# PROMPT FOR TRANSACTION DETAILS
read -p "Enter transaction ID (default: $(date +%s)): " TX_ID
TX_ID=${TX_ID:-$(date +%s)}

read -p "Enter transaction amount in USD (default: 5000.00): " AMOUNT
AMOUNT=${AMOUNT:-5000.00}

read -p "Enter transaction location (default: New York, NY): " LOCATION
LOCATION=${LOCATION:-"New York, NY"}

read -p "Enter vendor name (default: Amazon.com): " VENDOR
VENDOR=${VENDOR:-"Amazon.com"}

read -p "Enter initial fraud score 0-5 (default: 0, leave as 0 to invoke fraud agent): " SCORE
SCORE=${SCORE:-0}

echo ""
echo "📋 Transaction Details:"
echo "   ID: $TX_ID"
echo "   Amount: \$$AMOUNT"
echo "   Location: $LOCATION"
echo "   Vendor: $VENDOR"
echo "   Initial Score: $SCORE"
echo ""

# GET THE LATEST PUBLISHED VERSION ARN
echo "🔍 Getting latest function version..."
FUNCTION_ARN=$(aws lambda list-versions-by-function \
    --function-name $FUNCTION_NAME \
    --region $REGION \
    --query 'Versions[?Version!=`$LATEST`] | [-1].FunctionArn' \
    --output text)

if [ -z "$FUNCTION_ARN" ] || [ "$FUNCTION_ARN" = "None" ]; then
    echo "❌ No published version found. Please run ./deploy.sh first."
    exit 1
fi

echo "✅ Function ARN: $FUNCTION_ARN"
echo ""

# CREATE PAYLOAD
PAYLOAD=$(cat <<EOF
{
    "id": $TX_ID,
    "amount": $AMOUNT,
    "location": "$LOCATION",
    "vendor": "$VENDOR",
    "score": $SCORE
}
EOF
)

echo "🚀 Invoking durable function..."
echo ""

# INVOKE THE FUNCTION
# Note: AWS CLI v2 automatically handles payload encoding, no need to base64 encode
INVOKE_OUTPUT=$(aws lambda invoke \
    --function-name "$FUNCTION_ARN" \
    --payload "$PAYLOAD" \
    --region $REGION \
    /dev/stdout 2>&1)

echo ""
echo "✅ Function invoked successfully!"
echo ""

# EXTRACT DURABLE EXECUTION ARN FROM OUTPUT (it's in the response headers)
DURABLE_EXECUTION_ARN=$(echo "$INVOKE_OUTPUT" | grep -o 'arn:aws:lambda:[^:]*:[^:]*:function:[^/]*/durable-execution/[^/]*/[a-zA-Z0-9-]*' | head -1)

# DISPLAY RESPONSE PAYLOAD (filter out the ARN line)
echo "📊 Response Payload:"
echo "$INVOKE_OUTPUT" | grep -v "arn:aws:lambda" | jq '.' 2>/dev/null || echo "$INVOKE_OUTPUT" | grep -v "arn:aws:lambda"
echo ""

if [ ! -z "$DURABLE_EXECUTION_ARN" ]; then
    echo "🔗 Durable Execution ARN:"
    echo "   $DURABLE_EXECUTION_ARN"
    echo ""
    echo "📝 Useful Commands:"
    echo ""
    echo "   # Get execution details:"
    echo "   aws durable-lambda get-durable-execution \\"
    echo "     --durable-execution-arn '$DURABLE_EXECUTION_ARN' \\"
    echo "     --region $REGION"
    echo ""
    echo "   # Get execution history:"
    echo "   aws durable-lambda get-durable-execution-history \\"
    echo "     --durable-execution-arn '$DURABLE_EXECUTION_ARN' \\"
    echo "     --region $REGION \\"
    echo "     --include-execution-data"
    echo ""
    echo "   # List all executions:"
    echo "   aws durable-lambda list-durable-executions-by-function \\"
    echo "     --function-name $FUNCTION_NAME \\"
    echo "     --region $REGION"
    echo ""
fi

echo ""
echo "🔍 View CloudWatch Logs:"
echo "   aws logs tail /aws/lambda/$FUNCTION_NAME --region $REGION --follow"
echo ""
