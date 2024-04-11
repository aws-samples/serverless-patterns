# Amazon SNS to Amazon SQS fanout with filtering

This pattern demonstrates fanning out SNS messages to SQS with the CDK in Java.

In this example, we create an SNS Topic named `my-topic`. We also create three SQS Queues named `queue1`, `queue2`, and `queue3`.

Then, we subscribe each queue to the SNS topic using `topic.addSubscription()`. For `queue1`, we simply subscribe it to the topic without any filters, so it will receive all messages published to the topic.

For `queue2`, we use a subscription filter to only receive messages with the attribute `event` set to `order_placed`. Similarly, for `queue3`, we use a subscription filter to only receive messages with the attribute `event` set to `order_shipped`.

This demonstrates the fanout pattern, where a single message published to the SNS topic can be delivered to multiple SQS queues based on the subscription filters. For example, if you publish a message with the attribute `{ "event": "order_placed" }`, it will be delivered to `queue1` and `queue2`. If you publish a message with the attribute `{ "event": "order_shipped" }`, it will be delivered to `queue1` and `queue3`.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```bash
   cd serverless-patterns/sns-sqs-fanout-cdk-java
   ```

3. From the command line, configure AWS CDK:

The cdk bootstrap command only needs to be run if the account and region hasn't been bootstrapped before. This sets up the necessary resources for deploying CDK apps in the specified AWS account and region.
   ```bash
   cdk bootstrap ACCOUNT-NUMBER/REGION # e.g.
   cdk bootstrap 1111111111/us-east-1
   cdk bootstrap --profile test 1111111111/us-east-1
   ```
4. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/cdk-stack.ts` file:
   ```bash
   cdk deploy
   ```

## How it works

After deploying the stack, you can publish messages to the SNS topic using the AWS CLI or any other tool of your choice. The messages will be delivered to the appropriate SQS queues based on the subscription filters.

### Example 1

```
aws sns publish --topic-arn <YOUR_SNS_TOPIC_ARN> --message '{"event": "order_placed", "order_id": 123}'
```

This message will be delivered to `queue1` and `queue2`.

You can verify that the messages were successfully received by the queues using the AWS Management Console or AWS CLI.

```
aws sqs receive-message --queue-url <QUEUE_1_URL> --max-number-of-messages=2
aws sqs receive-message --queue-url <QUEUE_2_URL> --max-number-of-messages=2
```

### Example 2:

```
aws sns publish --topic-arn <YOUR_SNS_TOPIC_ARN> --message '{"event": "order_shipped", "order_id": 456}'
```

This message will be delivered to `queue1` and `queue3`.

You can verify that the messages were successfully received by the queues using the AWS Management Console or AWS CLI.

```
aws sqs receive-message --queue-url <QUEUE_1_URL> --max-number-of-messages=2
aws sqs receive-message --queue-url <QUEUE_3_URL> --max-number-of-messages=2
```

## Delete stack

```bash
cdk destroy
```

---

Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
