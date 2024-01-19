# API Gateway HTTP API to Step Functions Express Workflow

This pattern explains how to deploy a CDK application with a Amazon API Gateway HTTP API that invokes a Step Function Express workflow.

When an HTTP POST request is made to the Amazon API Gateway endpoint, the Step Function Express workflow is invoked and the results of the execution are returned in the HTTP response.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns](https://serverlessland.com/patterns)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [.NET 6](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Clone the project to your local working directory
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Change the working directory to this pattern's directory
    ```
    cd apigw-sfn-cdk/cdk/src
    ```

3. Install dependencies
    ```
    dotnet restore
    ```

4. Deploy the stack to your default AWS account and region. The output of this command should give you the HTTP API URL.
    ```
    cdk deploy
    ```

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

When an HTTP POST request is sent to the Amazon API Gateway endpoint a Step Function Express workflow is invoked synchronously. The output state of the Step Function is then returned in the HTTP response.

## Testing

After deployment, use the AWS Management Console (explained below) to test this pattern by sending an HTTP POST request to the Amazon API Gateway endpoint (found in the CloudFormation console Stacks Outputs tab).

## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
