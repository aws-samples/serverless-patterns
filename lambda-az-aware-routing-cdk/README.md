# AWS Lambda AZ-aware routing with metadata endpoint

This pattern deploys a Lambda function that uses the new Lambda metadata endpoint to discover its Availability Zone ID and demonstrates same-AZ routing to reduce cross-AZ latency and data transfer costs.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-az-aware-routing-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed

## How it works

![Architecture](architecture.png)

1. A client invokes the Lambda function.
2. The function calls the Lambda metadata endpoint (`http://${AWS_LAMBDA_METADATA_API}/2026-01-15/metadata/execution-environment`) using the `AWS_LAMBDA_METADATA_TOKEN` for authentication.
3. The endpoint returns the AZ ID (e.g., `use1-az1`) — a consistent identifier across all AWS accounts.
4. The function uses the AZ ID to make routing decisions, such as selecting same-AZ endpoints for ElastiCache, RDS, or DynamoDB DAX.
5. Same-AZ routing eliminates cross-AZ data transfer costs (~$0.01/GB) and reduces latency by ~1ms per hop.

## Deployment

1. Clone the repository and navigate to the pattern directory:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/lambda-az-aware-routing-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy the stack:
    ```bash
    cdk deploy
    ```

## Testing

Invoke the function multiple times to see different AZ assignments:

```bash
FUNCTION_NAME=$(aws cloudformation describe-stacks \
  --stack-name LambdaAzAwareRoutingStack \
  --query 'Stacks[0].Outputs[?OutputKey==`FunctionName`].OutputValue' \
  --output text)

# Invoke 5 times to see AZ distribution
for i in {1..5}; do
  aws lambda invoke --function-name $FUNCTION_NAME --payload '{}' /dev/stdout 2>/dev/null | python3 -m json.tool
  echo "---"
done
```

Expected output: Each invocation returns the AZ ID where the function is running (e.g., `use1-az1`, `use1-az2`).

## Cleanup

```bash
cdk destroy
```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
