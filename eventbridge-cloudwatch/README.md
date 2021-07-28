# Amazon EventBridge to Amazon CloudWatch Logs

This template creates an EventBridge event bus and rule that publishes matched events to CloudWatch Logs. In this example, the rule filters for specific attributes in the event before sending to the CloudWatch Logs target.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-cloudwatch

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd eventbridge-cloudwatch
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

## How it works

The AWS SAM template deploys the resources and the IAM permissions required to run the application.

The EventBridge rule specified in `template.yaml` filters the events based upon the criteria in the `EventPattern` section. When matching events are sent to EventBridge that trigger the rule, they are delivered as a JSON event payload to CloudWatch Logs.

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge and observe the event delivered to the Lambda function:

1. Send an event to EventBridge:

```bash
aws events put-events --entries file://event.json
```

2. The event appears in the CloudWatch Logs stream called `/aws/events/resource-policy-test`:

```
{
    "version": "0",
    "id": "c81888ee-1234-1234-1234-1dd5eaccc8d2",
    "detail-type": "message",
    "source": "my-application",
    "account": "123456789012",
    "time": "2021-07-27T15:22:48Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "message": "Hello world!"
    }
}
```

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
