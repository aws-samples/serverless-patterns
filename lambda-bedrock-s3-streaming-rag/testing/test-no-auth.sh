#!/bin/bash

# Function to display help message
usage() {
  echo "Usage: $0 <stack-name>"
  echo "Please provide your stack name. You can find it in your samconfig.toml"
  echo "Example: $0 my-stack-name"
}

# Check if at least one argument is provided
if [ "$#" -ne 1 ]; then
  usage
  exit 1
fi

STACK_NAME=$1
LAMBDA_ENDPOINT_URL=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`StreamingRAGFunctionURL`].OutputValue' --output text)


curl -s -XPOST ${LAMBDA_ENDPOINT_URL} \
    -d @./event.json \
    --no-buffer