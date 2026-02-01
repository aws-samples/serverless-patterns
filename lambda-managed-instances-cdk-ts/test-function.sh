#!/bin/bash

# Test script for Lambda Managed Instances function
# This script tests the deployed Lambda function

set -e

FUNCTION_NAME="my-managed-instance-function"
PAYLOAD='{"test": "Hello from test script", "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}'

echo "Testing Lambda Managed Instances function..."
echo "Function Name: $FUNCTION_NAME"
echo "Payload: $PAYLOAD"
echo ""

# Invoke the function
echo "Invoking function..."
aws lambda invoke \
  --function-name "$FUNCTION_NAME" \
  --payload "$PAYLOAD" \
  --cli-binary-format raw-in-base64-out \
  response.json

echo ""
echo "Response:"
cat response.json
echo ""

# Check if response file exists and contains expected content
if [ -f "response.json" ]; then
    if grep -q "Hello from Lambda Managed Instances!" response.json; then
        echo "✅ Test PASSED: Function returned expected message"
    else
        echo "❌ Test FAILED: Function did not return expected message"
        exit 1
    fi
else
    echo "❌ Test FAILED: No response file generated"
    exit 1
fi

# Clean up
rm -f response.json

echo "✅ Test completed successfully!"