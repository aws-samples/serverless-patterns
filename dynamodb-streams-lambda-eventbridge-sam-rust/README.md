# Amazon Dynamodb Streams to AWS Lambda to Amazon EventBridge

The AWS SAM template deploys a Lambda function, a DynamoDB table and an Amazon EventBridge bus, and the minimum IAM resources required to run the application.

When items are written in the DynamoDB table, the changes are sent to a stream. This pattern configures a Lambda function to poll this stream. The function is invoked with a payload containing the contents of the table item that changed.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/dynamodb-lambda.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Rust](https://www.rust-lang.org/) 1.67.0 or higher
* [cargo-zigbuild](https://github.com/messense/cargo-zigbuild) and [Zig](https://ziglang.org/) for cross-compilation
* [AWS AppConfig integration with Lambda extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd dynamodb-streams-lambda-eventbridge-sam-rust
    ```
3. From the command line, initialize terraform to  to downloads and installs the providers defined in the configuration:
    ```
    make build
    ```
4. From the command line, apply the configuration in the main.tf file:
    ```
    make deploy
    ```
5. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The changes are sent to a stream when items are written in a DynamoDB table. This pattern configures a Lambda function to poll this stream. The function is invoked with a payload containing the table item that has been inserted. The Lambda will then emit an event to Amazon EventBridge.

## Testing

After deployment, add an item to the DynamoDB table. Next, go to the CloudWatch Logs for the deployed Lambda function. Finally, the event is logged out, containing the item data and response from the Amazon EventBridge operation.

```
PutEventsOutput { failed_entry_count: 0, entries: Some([PutEventsResultEntry { event_id: Some("cb189d14-8799-80b4-66d1-e512d637889a"), error_code: None, error_message: None }]) }
```

Alternatively, you can use the events.json payload in Lambda to simulate over 100 inserted records.

## Cleanup
 
1. Delete the stack
    ```bash
    make delete
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
