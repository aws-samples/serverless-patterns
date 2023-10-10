# Amazon EventBridge to AWS Lambda

This template deploys a Lambda function that is triggered by an EventBridge rule. In this example, the rule filters for specific attributes in the event before invoking the function.

Provided the `events` section of the `logEvent` function definition, Serverless Framework sets up the required permissions for EventBridge to invoke this specific function.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-lambda

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [NodeJS](https://nodejs.org/en/download/) (LTS version) installed
* [Serverless Framework CLI](https://www.serverless.com/framework/docs/getting-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ``` sh
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory its source code folder:

    ``` sh
    cd serverless-patterns/eventbridge-lambda-sls
    ```

1. From the command line, use npm to install the development dependencies:

    ``` sh
    npm install
    ```

1. To deploy from the command line use the following:

    ``` sh
    serverless deploy --verbose
    ```

    The above command will deploy resources to `us-east-1` region by default. You can override the target region with `--region <region>` CLI option, e.g.

    ``` sh
    serverless deploy --verbose --region us-west-2
    ```

You can ignore stack deployment outputs, since we are using a static event bus name for testing (`demo-serverless-events`).

## Example event payload from EventBridge to Lambda

``` json
{
    "version": "0",
    "id": "12345678-39c6-07b3-c0a8-123456789012",
    "detail-type": "transaction",
    "source": "custom.myApp",
    "account": "123456789012",
    "time": "2021-02-10T14:47:48Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "location": "EUR-"
    }
}
```

## How it works

The Serverless Framework template deploys the resources and the IAM permissions required to run the application.

The EventBridge rule specified in `serverless.yml` filters the events based upon the criteria in the `pattern` section. When matching events are sent to EventBridge that trigger the rule, they are delivered as a JSON event payload (see above) to the Lambda function.

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge and observe the event delivered to the Lambda function:

1. Send an event to EventBridge. Make sure to have AWS CLI region matching the one, that you used for deploying the Serverless Framework template (`us-east-1` by default)!!!

    ``` sh
    aws events put-events --entries file://event.json --region <region>
    ```

1. Open AWS CloudWatch Console and navigate to [/aws/lambda/eventbridge-lambda-sls-prod-logEvent](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups/log-group/$252Faws$252Flambda$252Feventbridge-lambda-sls-prod-logEvent) log group.
You should be able to see a new Event Stream with the Received Event information, and Event Message, logged into the stream.

## Cleanup

1. Delete the stack

    ```sh
    serverless remove --verbose
    ```

1. Confirm the stack has been deleted

    ```sh
    aws cloudformation list-stacks --query "StackSummaries[?StackName=='eventbridge-lambda-sls-prod'].StackStatus"
    ```

    Expected output

    ```json
    [
        "DELETE_COMPLETE"
    ]
    ```

    NOTE: You might need to add `--region <region>` option to AWS CLI command if you AWS CLI default region does not match the one, that you used for the Serverless Framework deployment.

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
