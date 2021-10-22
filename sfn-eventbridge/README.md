# AWS Step Functions to Amazon EventBridge

This pattern creates a Step Functions workflow that publishes events to EventBridge.

Learn more about this pattern at the Serverless Land Patterns Collection: https://serverlessland.com/patterns/sfn-eventbridge

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

You are responsible for any AWS costs incurred. No warranty is implied in this example.

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
    cd sfn-eventbridge
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

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The AWS SAM template deploys a Step Functions workflow that publishes an event to an EventBridge event bus. An IAM Role allows the workflow execution to publish events onto the event bus. An EventBridge rule forwards all events to a CloudWatch Logs log group for easy inspection.

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to execute the Step Functions workflow and observe events published to the EventBridge event bus:

1. Execute the Step Functions workflow:

```bash
aws stepfunctions start-execution --state-machine-arn ENTER_YOUR_STATE_MACHINE_ARN
```

2. View CloudWatch Logs to see events that Step Functions published to EventBridge:
```bash
aws logs tail ENTER_YOUR_CLOUDWATCH_LOG_GROUP
```
You should see an event that was delivered to the event bus:
```bash
2021-06-03T00:55:46+00:00 551720c6-1832-3700-8172-b6c584ac6d6c
{
  "version":"0",
  "id":"99c02ee9-53b9-ae01-87cb-18c59081ce73",
  "detail-type":"MyTestMessage",
  "source":"MyTestApp",
  "account":"123456789012",
  "time":"2021-06-03T00:55:46Z",
  "region":"ap-southeast-2",
  "resources": [
    "arn:aws:states:ap-southeast-2:123456789012:stateMachine:MyStateMachine-BS6NgNCly8Ju",
    "arn:aws:states:ap-southeast-2:123456789012:execution:MyStateMachine-BS6NgNCly8Ju:be1b8b85-24ab-40de-a293-a47f4cc677cb"
  ],
  "detail": {
    "Message":"Hello from Step Functions!"
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
