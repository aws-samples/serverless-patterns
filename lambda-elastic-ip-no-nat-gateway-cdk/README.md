# AWS Lambda Elastic IP without NAT Gateway

This sample project a sample AWS Cloud Development Kit (AWS CDK) template for deploying an AWS Lambda function with a public Elastic IP without provisioning a NAT Gateway. This approach saves costs in a non-production environment.

## Architecture 
![Architecture](assets/Lambda-elastic-ip-no-nat-gateway.svg)
## Production Architecture 
![Production Architecture](assets/Lambda-elastic-ip-with-nat.svg)
## Non-prod cost effective Architecture
![Non-prod cost effective Architecture](assets/Lambda-elastic-ip-with-x-nat-gateway.svg)


Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-elastic-ip-no-nat-gateway-cdk.

Important: This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal, and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change the directory to the pattern directory:
   ```bash
   cd serverless-patterns/lambda-elastic-ip-no-nat-gateway-cdk/cdk
   ```
3. Install dependencies for both the infrastructure project and the typescript project:
   ```bash
   npm install
   cd src
   npm install
   cd ..
   ```

4. From the command line, configure AWS CDK:
   ```bash
   cdk bootstrap ACCOUNT-NUMBER/REGION # e.g.
   cdk bootstrap 9999999999/us-east-1
   cdk bootstrap --profile test 9999999999/us-east-1
   ```
5. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/cdk-stack.ts` file:
   ```bash
   cdk deploy
   ```

## Use Case
You have a Lambda function that requires internet access to make API calls to 3rd party service but you need a dedicated IP to be whitelisted by the 3rd party vendors. 

## How it works

This pattern allows you to assign your Lambda function a static public IP address that you can use to interact with APIs that require whitelisted IPs without the need to provision a NAT Gateway. Therefore, this pattern will save almost **$33/month** in NAT Gateway costs.

##### **NOTE:** This pattern is best suited for non-production environments since it is not multi-AZ nor highly scalable.

The following resources will be provisioned:

- A Lambda function to test the pattern
- An Elastic IP to associate with the Lambda function
- A custom resource with Lambda function to associate the Elastic IP with the test lambda's ENI

Since AWS manages the provisioning of any Lambda ENI, we cannot access that ENI in CDK code. Therefore, to automate the process, we have to associate the Elastic IP with the ENI in a custom resource after the deployment occurs and the ENI is provisioned.

## Testing

To test this pattern, use the AWS Console or the AWS CLI.

### AWS Console Part

1. Open the AWS Lambda Console
2. Navigate to `vin-api-lambda`
3. Test the lambda with any payload
4. The Lambda function shouldn't time out and a random vin should be returned and logged.

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```

## Resources

1. [Lambda in a VPC](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html)

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
