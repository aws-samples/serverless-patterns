# AWS Step Functions (SFN) integration with AWS Lambda with VPC access.

This pattern in CDK offers a example to generate an AWS Step Functions state machine which consumes an AWS Lambda function with AWS VPC access.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-lambda-vpc-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node and NPM](https://nodejs.org/en/download/) installed
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd cdk-vpc-lambda-sfn
    ```
3. To deploy from the command line use the following:
    ```bash
      npm install
      npx cdk bootstrap aws://accountnumber/region
      npm run lambda
      npx cdk synth
      npx cdk deploy --all
    ```

## How it works

AWS Lambda Function is created which is part of VPC's Private Subnet. Network interface created from VPC to access state functions. All traffic will route through this interface.

## Testing

1. Deploy the stack. On successful creation under VPCs one can find the list of Private, Public, Isolated Subnets.
2. Under Endpoints, Endpoint Interface for `STEP_FUNCTIONS` which will have private DNS.
3. Under Lambda Service, one can find the lambda function named `test-lambdaFunction`. By navigating to Configurations one can find the VPCs, Subnets attached to it.
4. Under State Function Service, one can find the state machine named `test-testMachineFlow`, with lambda invoke step. After exection of state machine, it should run successfully.

## Cleanup

1. From the command line, use the following in the source folder
    ```bash
    npx cdk destroy
    ```
2. Confirm the removal and wait for the resource deletion to complete.
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
