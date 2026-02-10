# Lambda Managed Instances with AWS CDK TypeScript

This pattern demonstrates how to create and deploy AWS Lambda Managed Instances using AWS CDK in TypeScript. Lambda Managed Instances allow you to run Lambda functions on dedicated EC2 instances for workloads that require more control over the underlying infrastructure.

Learn more about this pattern at Serverless Land Patterns: [Lambda Managed Instances](https://serverlessland.com/patterns/lambda-managed-instances)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node.js](https://nodejs.org/) (version 18.x or later)
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) installed (`npm install -g aws-cdk`)
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Architecture

This CDK stack creates:

1. **IAM Roles**: 
   - Lambda execution role with basic execution permissions
   - Capacity provider operator role for managing EC2 instances

2. **VPC Resources**:
   - New VPC with CIDR 10.0.0.0/16
   - Private subnet with NAT Gateway for outbound internet access
   - Security group for Lambda Managed Instances

3. **Lambda Capacity Provider**:
   - Manages EC2 instances (x86_64 architecture)
   - Maximum 30 vCPUs scaling configuration

4. **Lambda Function**:
   - Node.js 20.x runtime
   - 2048 MB memory allocation
   - 512 MB ephemeral storage
   - Configured to use the managed instances capacity provider

## Deployment Instructions

1. Clone this repository and navigate to the pattern directory:
    ```bash
    cd lambda-managed-instances-cdk-ts
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Build the TypeScript code:
    ```bash
    npm run build
    ```

4. Bootstrap CDK (if you haven't done this before in your account/region):
    ```bash
    cdk bootstrap
    ```

5. Deploy the stack:
    ```bash
    cdk deploy
    ```

6. Note the outputs from the CDK deployment process. These contain the resource names and ARNs which are used for testing.

## How it works

1. **Infrastructure Setup**: The CDK creates all necessary infrastructure including VPC, subnets, security groups, and IAM roles.

2. **Capacity Provider**: A Lambda capacity provider is created that manages EC2 instances in your VPC. This provider can scale up to 30 vCPUs based on demand.

3. **Lambda Function**: The Lambda function is configured to use the managed instances capacity provider instead of the standard serverless execution environment.

4. **Function Execution**: When invoked, the Lambda function runs on dedicated EC2 instances managed by the capacity provider, providing more control over the execution environment.

## Testing

1. Test the Lambda function using the AWS CLI:
    ```bash
    aws lambda invoke \
      --function-name my-managed-instance-function \
      --payload '{"test": "data"}' \
      response.json
    ```

2. Check the response:
    ```bash
    cat response.json
    ```

3. You should see a response like:
    ```json
    {
      "statusCode": 200,
      "body": "{\"message\":\"Hello from Lambda Managed Instances!\",\"event\":{\"test\":\"data\"}}"
    }
    ```

4. Monitor the function execution in CloudWatch Logs to see the detailed execution logs.

## Useful CDK Commands

* `npm run build`   - compile typescript to js
* `npm run watch`   - watch for changes and compile
* `cdk deploy`      - deploy this stack to your default AWS account/region
* `cdk diff`        - compare deployed stack with current state
* `cdk synth`       - emits the synthesized CloudFormation template
* `cdk destroy`     - delete the stack

## Cleanup
 
1. Delete the stack:
    ```bash
    cdk destroy
    ```

2. Confirm when prompted to delete the stack and all its resources.

## Notes

- Lambda Managed Instances require VPC configuration and have different networking requirements compared to standard Lambda functions.
- The capacity provider manages EC2 instances automatically, scaling based on function invocation demand.
- This pattern is suitable for workloads that need more control over the execution environment or have specific networking requirements.

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
