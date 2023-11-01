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
API_URL=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`RAGApi`].OutputValue' --output text)

WARMUP_URL="$API_URL?warmup=true"
PROMPT_URL="$API_URL?question=amazon+bedrock+pricing+model"

WARMUP_FILE=warmup.txt
BODY_FILE=response_body.json

echo "Starting warmup at $(date +"%Y-%m-%d %T.%3N")"
curl -s $WARMUP_URL -o $WARMUP_FILE
echo "Warmup ended at $(date +"%Y-%m-%d %T.%3N")"
echo "Time to Lambda timeout: $(cat $WARMUP_FILE | jq .toTimeout) ms"

echo "Testing prediction endpoint at $(date +"%Y-%m-%d %T.%3N")"
curl -s $PROMPT_URL -o $BODY_FILE
echo "Prediction ended at $(date +"%Y-%m-%d %T.%3N")"

cat $BODY_FILE

rm $BODY_FILE
rm $WARMUP_FILE
