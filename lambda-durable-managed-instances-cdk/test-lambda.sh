#!/bin/bash

# Test script for Lambda durable function
# Usage: ./test-lambda.sh [profile] [region]

set -e

# Configuration
FUNCTION_NAME="step-wait-step-durable-function"
FUNCTION_VERSION="\$LATEST.PUBLISHED"
PAYLOAD_FILE="events/basic-order.json"
RESPONSE_FILE="response.json"
LOG_GROUP="/aws/lambda/step-wait-step-durable-function"

# Default values
PROFILE="${1:-default}"
REGION="${2:-us-east-2}"

echo "🚀 Testing Lambda durable function..."
echo "Function: $FUNCTION_NAME"
echo "Profile: $PROFILE"
echo "Region: $REGION"
echo

# Check if payload file exists
if [ ! -f "$PAYLOAD_FILE" ]; then
    echo "❌ Error: Payload file $PAYLOAD_FILE not found"
    exit 1
fi

echo "📄 Using payload:"
cat "$PAYLOAD_FILE"
echo

# Invoke Lambda function
echo "⚡ Invoking Lambda function..."
INVOKE_OUTPUT=$(aws lambda invoke \
    --function-name "$FUNCTION_NAME:$FUNCTION_VERSION" \
    --invocation-type Event \
    --payload "file://$PAYLOAD_FILE" \
    --cli-binary-format raw-in-base64-out \
    --region "$REGION" \
    --profile "$PROFILE" \
    "$RESPONSE_FILE" 2>&1)

echo "$INVOKE_OUTPUT"

echo

# Extract durable execution ARN from the invoke output
echo "🔍 Extracting durable execution ARN from output..."
EXECUTION_ARN=$(echo "$INVOKE_OUTPUT" | grep -o 'arn:aws:lambda:[^"]*durable-execution/[^"]*' | head -1)

if [ -n "$EXECUTION_ARN" ]; then
    echo "🔗 Durable Execution ARN:"
    echo "$EXECUTION_ARN"
    echo
else
    echo "⚠️  No durable execution ARN found in invoke output"
    echo "📋 Full invoke output:"
    echo "$INVOKE_OUTPUT"
    echo
fi

# Wait for execution to start
echo "⏳ Waiting 10 seconds for execution to start..."
sleep 10

# Show durable execution history
if [ -n "$EXECUTION_ARN" ]; then
    echo "📜 Durable execution history (initial):"
    aws lambda get-durable-execution-history \
        --durable-execution-arn "$EXECUTION_ARN" \
        --region "$REGION" \
        --profile "$PROFILE" \
        --query 'Events[].{EventType:EventType,Name:Name,Timestamp:EventTimestamp}' \
        --output table || echo "⚠️  Failed to get execution history: $?"
    echo
fi

# Show recent logs
echo "📊 Recent logs (last 2 minutes):"
START_TIME=$(($(date +%s) - 120))000
aws logs filter-log-events \
    --log-group-name "$LOG_GROUP" \
    --start-time "$START_TIME" \
    --region "$REGION" \
    --profile "$PROFILE" \
    --filter-pattern 'INFO' \
    --query 'events[].[timestamp,message]' \
    --output table

# Wait for execution to complete and show final history
if [ -n "$EXECUTION_ARN" ]; then
    echo "⏳ Waiting additional 10 seconds for execution to complete..."
    sleep 10
    
    echo "📜 Final durable execution history:"
    aws lambda get-durable-execution-history \
        --durable-execution-arn "$EXECUTION_ARN" \
        --region "$REGION" \
        --profile "$PROFILE" \
        --query 'Events[].{EventType:EventType,SubType:SubType,Name:Name,Timestamp:EventTimestamp}' \
        --output table || echo "⚠️  Failed to get final execution history: $?"
    echo

    echo "🎯 Durable execution result:"
    aws lambda get-durable-execution \
        --durable-execution-arn "$EXECUTION_ARN" \
        --region "$REGION" \
        --profile "$PROFILE" \
        --query '{Status:Status,InputPayload:InputPayload,Result:Result,StartTime:StartTimestamp,EndTime:EndTimestamp}' \
        --output table || echo "⚠️  Failed to get execution result: $?"
    echo
fi

echo "✅ Test completed!"
echo "💡 To view all logs: aws logs filter-log-events --log-group-name $LOG_GROUP --start-time $START_TIME --region $REGION --profile $PROFILE"
if [ -n "$EXECUTION_ARN" ]; then
    echo "💡 To view execution history: aws lambda get-durable-execution-history --durable-execution-arn $EXECUTION_ARN --region $REGION --profile $PROFILE"
    echo "💡 To view execution result: aws lambda get-durable-execution --durable-execution-arn $EXECUTION_ARN --region $REGION --profile $PROFILE"
fi

# Cleanup
rm -f "$RESPONSE_FILE"