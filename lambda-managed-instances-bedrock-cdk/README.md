# Lambda Managed Instances with Amazon Bedrock

This pattern deploys a Lambda function on [Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html) (EC2-backed compute) that invokes Amazon Bedrock (Claude) for text generation.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-managed-instances-bedrock-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed

## How it works

Lambda Managed Instances combine EC2 flexibility with serverless simplicity:

- **EC2-backed compute**: Your function runs on dedicated EC2 instances in your VPC
- **Serverless management**: AWS handles provisioning, scaling, OS patching, and load balancing
- **Cost optimization**: Use Compute Savings Plans and Reserved Instances for Lambda workloads
- **Specialized hardware**: Access Graviton, GPU, and network-optimized instance types

This pattern adds Bedrock integration to demonstrate a real-world use case beyond hello-world.

## Architecture

```
User → Lambda Function (on Managed Instances / EC2)
         ├── VPC with private subnets
         ├── CapacityProvider (ARM64)
         └── Bedrock InvokeModel → Claude response
```

## Deployment Instructions

1. Clone the repository and navigate to the pattern directory:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/lambda-managed-instances-bedrock-cdk
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

Invoke the function:

```bash
aws lambda invoke \
  --function-name managed-instances-bedrock-cdk \
  --payload '{"prompt":"Explain Lambda Managed Instances in 3 sentences"}' \
  --cli-binary-format raw-in-base64-out \
  output.json && cat output.json | python3 -m json.tool
```

## Cleanup

```bash
cdk destroy
```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
