#!/bin/bash

set -e

REGION=${AWS_DEFAULT_REGION:-us-west-2}

echo "Fetching CloudFront distribution..."
DISTRIBUTION_ID=$(aws cloudfront list-distributions --query "DistributionList.Items[*].[Id, Origins.Items[0].DomainName] | [?contains([1], 'bedrock-agentcore')] | [0][0]" --output text --no-cli-pager | grep -v "^None$" | head -1)
if [ -z "$DISTRIBUTION_ID" ]; then
  echo "Error: Could not find CloudFront distribution for AgentCore"
  exit 1
fi
CF_DOMAIN=$(aws cloudfront get-distribution --id $DISTRIBUTION_ID --query "Distribution.DomainName" --output text --no-cli-pager)
CF_URL="https://${CF_DOMAIN}"

echo "Fetching A2A agent runtime..."
RUNTIME_ID=$(aws bedrock-agentcore-control list-agent-runtimes --region $REGION --query "agentRuntimes[?contains(agentRuntimeName, 'A2a_Agent')].agentRuntimeId" --output text --no-cli-pager | grep -v "^None$" | head -1)
if [ -z "$RUNTIME_ID" ]; then
  echo "Error: Could not find A2A agent runtime"
  exit 1
fi

echo "Found runtime: $RUNTIME_ID"

RUNTIME_INFO=$(aws bedrock-agentcore-control get-agent-runtime --agent-runtime-id $RUNTIME_ID --region $REGION --no-cli-pager)
CONTAINER_URI=$(echo $RUNTIME_INFO | jq -r '.agentRuntimeArtifact.containerConfiguration.containerUri')
ROLE_ARN=$(echo $RUNTIME_INFO | jq -r '.roleArn')
DISCOVERY_URL=$(echo $RUNTIME_INFO | jq -r '.authorizerConfiguration.customJWTAuthorizer.discoveryUrl')
CLIENT_ID=$(echo $RUNTIME_INFO | jq -r '.authorizerConfiguration.customJWTAuthorizer.allowedClients[0]')

echo "Updating A2A agent with CloudFront URL: ${CF_URL}/a2a/"

aws bedrock-agentcore-control update-agent-runtime \
  --agent-runtime-id $RUNTIME_ID \
  --agent-runtime-artifact containerConfiguration={containerUri=$CONTAINER_URI} \
  --role-arn $ROLE_ARN \
  --network-configuration networkMode=PUBLIC \
  --protocol-configuration serverProtocol=A2A \
  --authorizer-configuration "customJWTAuthorizer={discoveryUrl=$DISCOVERY_URL,allowedClients=$CLIENT_ID}" \
  --environment-variables "AWS_DEFAULT_REGION=$REGION,CLOUDFRONT_URL=${CF_URL}/a2a/" \
  --region $REGION \
  --no-cli-pager

echo "Waiting for runtime to be ready..."
while true; do
  STATUS=$(aws bedrock-agentcore-control get-agent-runtime --agent-runtime-id $RUNTIME_ID --region $REGION --query "status" --output text --no-cli-pager)
  if [ "$STATUS" == "READY" ]; then
    echo "Runtime is ready."
    break
  fi
  echo "Status: $STATUS. Waiting..."
  sleep 5
done

echo "Done."
