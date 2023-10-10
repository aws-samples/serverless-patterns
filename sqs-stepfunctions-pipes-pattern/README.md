# Exponential Backoff in SQS Processing with Step Functions and EventBridge Pipes

This pattern demonstrates a seamless integration between an SQS queue and AWS Step Functions using Amazon EventBridge Pipes. It enables direct routing of messages from an SQS queue into a Step Functions state machine, which orchestrates the processing flow and manages AWS Lambda invocation errors. When Lambda encounters an error, the erroneous message is directed to an SQS Dead Letter Queue (DLQ) for further inspection or reprocessing.

Learn more about this pattern at Serverless Land Patterns: [Add the live URL here](#).

**Important**: This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Change directory to the pattern directory:
    ```bash
    cd serverless-patterns/sqs-stepfunctions-pipes-pattern
    ```

3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```bash
    sam deploy --guided
    ```

4. During the prompts:
    * Enter a stack name.
    * Enter the desired AWS Region.
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Messages sent to the SQS queue are routed through EventBridge Pipes to a Step Functions state machine. The state machine manages message processing and invokes a Lambda function, which is intentionally set with a reserved concurrency of 0 to simulate throttling. When errors, such as throttling, occur in the Lambda function, the state machine employs an exponential backoff retry strategy that starts with a 5-second delay, doubling this delay after each subsequent retry, for up to 6 maximum retry attempts. If all retry attempts are exhausted, the message is directed to a Dead Letter Queue (DLQ) for further analysis.

## Testing

1. Retrieve the Queue URL from the outputs of the SAM deployment:
    ```bash
    aws cloudformation describe-stacks --stack-name YOUR_STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='MyQueueUrl'].OutputValue" --output text
    ```
    Replace `YOUR_STACK_NAME` with the name you provided for your stack during deployment.

2. Send a test message to the SQS queue using the AWS CLI:
    ```bash
    aws sqs send-message --queue-url [RETRIEVED_QUEUE_URL] --message-body "Your test message content here"
    ```
    Replace `[RETRIEVED_QUEUE_URL]` with the URL you obtained in the previous step.

3. Monitor the Step Functions state machine to observe the execution.
4. If the Lambda function is simulated to fail, check the DLQ for the erroneous message.

## Cleanup

1. To delete the deployed resources, use:
    ```bash
    sam delete --stack-name YOUR_STACK_NAME
    ```
    Replace `YOUR_STACK_NAME` with the name you provided for your stack during deployment.

---
Copyright 2023 [Amazon.com, Inc. or its affiliates](http://Amazon.com). All Rights Reserved.

SPDX-License-Identifier: MIT-0