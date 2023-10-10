# EventBridge Rule invokes Lambda

This project contains a sample AWS CDK template for invoking AWS Lambda from an Amazon EventBridge Rule. It also creates a CloudWatch Log Group for the Lambda function for observation of incoming events, with a retention and removal policy.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-lambda-dotnet-cdk.

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
    cd eventbridge-lambda-dotnet-cdk
    ```

3. Install dependencies
    ```
    dotnet restore src/
    ```

4. Deploy the stack to your default AWS account and region
    ```
    cdk deploy
    ```

## How it works

The CDK stack deploys the resources and the IAM permissions required to run the application.

The EventBridge rule filters the events based upon the defined criteria. When matching events are sent to EventBridge that trigger the rule, they are delivered as a JSON event payload to the Lambda function.

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge and observe the event delivered to the Lambda function by reviewing the Amazon CloudWatch Logs associated with the function:

1. Send an event to EventBridge:

```sh
aws events put-events --entries file://event.json
```

2. Check the CloudWatch Logs for the Lambda function to see an event matching this example:
```json
{
    "Version": "0",
    "Account": "123456789012",
    "Region": "eu-west-2",
    "Detail": {
        "location": "EUR-"
    },
    "detail-type": "transaction",
    "Source": "cdk.myapp",
    "Time": "2022-04-01T23:34:25Z",
    "Id": "5832fadb-ec04-8f66-2903-1302e13e94db",
    "Resources": []
}
```

## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
