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

# GET THE FUNCTION ARN
echo "🔍 Getting function arn..."
FUNCTION_ARN="arn:aws:lambda:$REGION:$ACCOUNT_ID:function:$FUNCTION_NAME"

if [ -z "$FUNCTION_ARN" ] || [ "$FUNCTION_ARN" = "None" ]; then
    echo "❌ Lambda function was not found. Please run ./deploy-sam.sh first."
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
INVOKE_OUTPUT=$(aws lambda invoke \
    --function-name "$FUNCTION_ARN:\$LATEST" \
    --payload "$PAYLOAD" \
    --region $REGION \
    response.json 2>&1)

echo ""
echo "✅ Function invoked successfully!"
echo ""

# EXTRACT DURABLE EXECUTION ARN FROM OUTPUT
DURABLE_EXECUTION_ARN=$(echo "$INVOKE_OUTPUT" | jq -r '.DurableExecutionArn // empty' 2>/dev/null)

# DISPLAY RESPONSE PAYLOAD
echo "📊 Response:"
echo "$INVOKE_OUTPUT"
echo ""

if [ -f "response.json" ]; then
    echo "📄 Response file content:"
    cat response.json
    echo ""
    rm -f response.json
fi

if [ ! -z "$DURABLE_EXECUTION_ARN" ]; then
    echo "🔗 Durable Execution ARN:"
    echo "   $DURABLE_EXECUTION_ARN"
    echo ""
    echo "📝 Durable Execution ARN (for monitoring):"
    echo "   This execution can be monitored through CloudWatch logs"
    echo "   Note: Use custom durable-lambda CLI if available for detailed execution info"
    echo ""
fi

echo ""
echo "🔍 View CloudWatch Logs:"
echo "   aws logs tail /aws/lambda/$FUNCTION_NAME --region $REGION --follow"
echo ""
