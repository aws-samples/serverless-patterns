# Amazon Bedrock AgentCore with Amazon OpenSearch Serverless NextGen

This pattern deploys an Amazon Bedrock AgentCore Runtime running a containerized Python Strands agent that searches an Amazon OpenSearch Serverless NextGen collection using opensearch-py.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/agentcore-opensearch-serverless-nextgen-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
- [Node.js 20+](https://nodejs.org/en/download/) installed
- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed (`npm install -g aws-cdk`)
- [Docker](https://docs.docker.com/get-docker/) installed and running
- CDK bootstrapped in your target account and region: `cdk bootstrap aws://ACCOUNT-NUMBER/REGION`

## Supported Regions

Amazon Bedrock AgentCore is available in: **us-east-1**, **us-west-2**, **eu-central-1**, **ap-southeast-2**.

## Deployment Instructions

1. Clone the repository and navigate to the pattern directory:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/agentcore-opensearch-serverless-nextgen-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Build and push the agent Docker image to ECR:
    ```bash
    export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    export AWS_REGION=us-east-1

    # Create ECR repo (CDK will also create it, but we need it for the initial push)
    aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

    # Build and push
    cd src/agent
    docker build -t agentcore-opensearch-agent .
    docker tag agentcore-opensearch-agent:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/agentcore-opensearch-agent:latest
    docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/agentcore-opensearch-agent:latest
    cd ../..
    ```

4. Deploy the stack:
    ```bash
    export CDK_DEFAULT_ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
    export CDK_DEFAULT_REGION=us-east-1
    cdk deploy
    ```

## How it works

- **Amazon OpenSearch Serverless NextGen** collection group with scale-to-zero provides a SEARCH-type collection for document storage and retrieval.
- **Amazon Bedrock AgentCore Runtime** hosts a containerized Python agent built with the Strands Agents framework.
- The agent uses the `search_documents` tool backed by opensearch-py to query the OpenSearch Serverless collection.
- IAM roles grant the runtime permissions to invoke Amazon Bedrock models (Claude Sonnet) and access the OpenSearch Serverless collection via `aoss:APIAccessAll`.

## Testing

After deployment, index a sample document into the OpenSearch collection:

```bash
COLLECTION_ENDPOINT=$(aws cloudformation describe-stacks --stack-name AgentcoreOpensearchServerlessNextgenStack --query 'Stacks[0].Outputs[?OutputKey==`CollectionEndpoint`].OutputValue' --output text)

curl -X PUT "$COLLECTION_ENDPOINT/documents" -H "Content-Type: application/json" --aws-sigv4 "aws:amz:us-east-1:aoss" --user "" -d '{}'

curl -X POST "$COLLECTION_ENDPOINT/documents/_doc" -H "Content-Type: application/json" --aws-sigv4 "aws:amz:us-east-1:aoss" --user "" -d '{"title": "Hello World", "content": "This is a test document for the AgentCore search agent."}'
```

Then invoke the AgentCore Runtime endpoint to test the search agent.

## Cleanup

⚠️ **Warning**: Deleting the stack will permanently remove the OpenSearch Serverless collection and all indexed data. The ECR repository and all pushed images will also be deleted.

```bash
cdk destroy
```

## Architecture

```
User → AgentCore Runtime → Strands Agent → opensearch-py → OpenSearch Serverless NextGen Collection
                              ↓
                     Bedrock (Claude Sonnet) for reasoning
```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
