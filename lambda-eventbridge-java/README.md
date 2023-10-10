# AWS Lambda to Amazon EventBridge

This pattern creates a Lambda function that publishes an event to EventBridge. 

This version is a Java port of the [original pattern](https://serverlessland.com/patterns/lambda-eventbridge).

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

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
    cd lambda-eventbridge-java
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

The AWS SAM template deploys the following resources:

| Type | Logical ID |
| --- | --- |
| AWS::Lambda::Function | PublisherFunction |
| AWS::IAM::Role | PublisherFunctionRole |

When the Lambda function is invoked, it publishes an event to the default event bus in EventBridge.


## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge and observe the Lambda function logs:

1. Send an event to EventBridge:

```bash
aws lambda invoke \
    --cli-binary-format raw-in-base64-out \
    --function-name ENTER_YOUR_PUBLISHER_FUNCTION_NAME \
    --payload file://input.json \
     response.json
```

2. View the logs from the Lambda function:

You should see a response showing the event delivered to the default event bus:
```bash
2022-04-04T20:24:07.738+10:00   Event: {message=Hello from publisher, state=new}
2022-04-04T20:24:08.173+10:00   PutEventsResponse(FailedEntryCount=0, Entries=[PutEventsResultEntry(EventId=92b5bee4-cc3b-34db-fd2d-a38c1ac5b600)])
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
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
