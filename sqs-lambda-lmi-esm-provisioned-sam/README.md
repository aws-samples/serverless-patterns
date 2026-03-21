# Amazon SQS + Lambda Managed Instances (LMI) with Provisioned Mode ESM

This pattern deploys an Amazon SQS Standard Queue connected to an AWS Lambda function via an Event Source Mapping (ESM) configured with **Provisioned Mode** — an ESM feature that pre-allocates dedicated polling resources for predictable, high-throughput message processing.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/sqs-lambda-lmi-esm-provisioned-sam](https://serverlessland.com/patterns/sqs-lambda-lmi-esm-provisioned-sam)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Build Instructions

1. From the command line, use AWS SAM to build the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    ```

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd sqs-lambda-lmi-esm-provisioned-sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Accept the default parameter values or tune them for your workload
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

1. A producer (any AWS service, SDK client, or CLI) sends messages to the SQS Standard Queue.
2. The ESM's provisioned event pollers continuously long-poll the queue using up to 10 SQS API calls per second per poller.
3. When messages are available, pollers assemble batches (up to `BatchSize` messages, waiting up to `MaxBatchingWindowInSeconds`) and invoke the Lambda function concurrently.
4. Lambda scales the number of active pollers between `MinimumPollers` and `MaximumPollers` based on queue depth, adding up to **1,000 concurrent executions per minute**.
5. If a message fails processing after 3 attempts (`maxReceiveCount`), it is moved to the Dead Letter Queue.
6. A CloudWatch Alarm fires as soon as any message lands in the DLQ.

## Testing

1. Get the queue URL from the stack outputs:

```bash
aws cloudformation describe-stacks \
  --stack-name <your-stack-name> \
  --query "Stacks[0].Outputs"
```

2. Send test messages:

```bash
QUEUE_URL=<QueueUrl from outputs>

# Send a single message
aws sqs send-message \
  --queue-url $QUEUE_URL \
  --message-body '{"orderId": "123", "amount": 99.99}'

# Send a batch of 10
for i in $(seq 1 10); do
  aws sqs send-message \
    --queue-url $QUEUE_URL \
    --message-body "{\"orderId\": \"$i\", \"amount\": $((RANDOM % 100))}"
done
```

3. Check Lambda logs:

```bash
sam logs --stack-name <your-stack-name> --tail
```

4. Inspect the ESM status and poller count:

```bash
ESM_ID=<EventSourceMappingId from outputs>

aws lambda get-event-source-mapping --uuid $ESM_ID
```

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
