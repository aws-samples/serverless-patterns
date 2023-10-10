# Amazon EventBridge Scheduler to AWS Step Functions

This pattern will trigger the execution of a Step Function every hour using an EventBridge schedule and the CDK in Go.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-schedule-to-step-function-cdk-go

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Go](https://go.dev/dl/) (`1.18` or above) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```bash
    cd serverless-patterns/eventbridge-schedule-to-step-function-cdk-go/cdk/
    ```
3. (Optional) It might be necessary to download the Golang modules directly from the source:
    ```bash
    go env -w GOPROXY=direct
    ```
4. From the command line, use AWS CDK to deploy the AWS resources for the pattern:
    ```bash
    cdk deploy
    ```
> Enter `y` when prompted *Do you wish to deploy these changes (y/n)?*

## How it works

The template will create an EventBridge schedule and a Step Function. Every hour, EventBridge schedule will trigger a Step Function execution.

## Testing

Check the execution log of the Step Function state machine. There should be a successful execution at the start of every hour.

## Cleanup

To delete the resources that were created:

```
cdk destroy
```

> It might take some time for the CloudFormation stack to get deleted.


----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
