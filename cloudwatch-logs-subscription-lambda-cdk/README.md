# Amazon CloudWatch Logs Subscription to AWS Lambda with CDK

This pattern demonstrates how to create the Amazon CloudWatch Log Subscription to AWS Lambda. Logs filtering is also demonstrated to filter only certain logs to be sent to AWS Lambda.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cloudwatch-logs-subscription-lambda-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd cloudwatch-logs-subscription-lambda-cdk
    ```
2. Run below command to install required dependancies:
    ```
    npm install
    ```
4. From the command line, run:
    ```
    cdk deploy --all
    ```

## Testing

1. In the stack output, you can see `logGroupName` and `logStreamName`. Copy those values.

2. Example logs are available in the `example_logs.log` file.

3. Run below command to those logs into the log group.
    ```
    aws logs put-log-events --log-group-name '[LogGroupName]' --log-stream-name '[LogStreamName]' --log-events file://example_logs.log
    ```

4. Within the Lambda function's Cloudwatch log group, you can see the logs that are received by Lambda function, but only the records that has 'WARNING' and 'ERROR' texts, because we have a filter in place.

## Cleanup
 
1. To delete the stack, run:
    ```bash
    cdk destroy --all
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
