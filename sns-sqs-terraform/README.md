# Amazon SNS to SQS with Terraform

The Terraform stack deploys a SNS topic and an SQS queue. The SQS queue is subscribed to the SNS topic. SNS invokes the SQS queue when new messages are available. When messages are sent to the SNS topic, they are delivered as a JSON event payload to the SQS queue.

Learn more about this pattern at Serverless Land Patterns: [serverlessland.com/patterns/sqs-lambda-terraform](https://serverlessland.com/patterns/sns-sqs-terraform)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) with version 1.x installed (this pattern has been tested with version 1.1.7)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd sns-sqs-terraform
    ```
2. From the command line, use Terraform to deploy the AWS resources for the pattern as specified in the main.tf file:
    ```
    terraform init
    terraform apply --auto-approve
    ```

3. Note the outputs from the Terraform deployment process. These contain the resource names and/or ARNs which are used for testing.

## Example event payload from SNS by SQS

```
{
    "Messages": [
        {
            "MessageId": "12345678-fef2-4639-b269-123456789012",
            "ReceiptHandle": "123456/g66F9oFe9GjqvCV123456789012qXNQWhEPjaet123456789012P1Najh0B8L4v123456789012tMhDCW8+4HemB123456789012PzU2ZccaD+TRQA6eo123456789012FEz123456789012AeJt4q123456789012xVHh7nEtwEW6/123456789012a9uXzmVl123456789012YRr/slwbLOz3H41234567890129Okiu2rM12345678901231H/5wS123456789012SJsc6juhL5RLLtlJg7GyZcfekyHR7MpVOR123456789012pqh7pJNTa1nFZwfZS2Z123456789012Y0K5d+0xyglCvxfpmg+RzH0ZKIhxN123456789012Nn9PRiTl",
            "MD5OfBody": "12345678901280dcda123456789012",
            "Body": "{\n  \"Type\" : \"Notification\",\n  \"MessageId\" : \"12345678-be92-513a-a017-1234567890\",\n  \"TopicArn\" : \"arn:aws:sns:us-east-1:123456789012:patterns-sns-to-sqs-MySnsTopic-123456789012\",\n
\"Subject\" : \"testSubject\",\n  \"Message\" : \"testMessage\",\n  \"Timestamp\" : \"2021-02-10T15:51:48.748Z\",\n  \"SignatureVersion\" : \"1\",\n  \"Signature\" : \"FMCq/123456789012+cHuU123456789012uge/123456789012/74VExy8A1234567890120LfxjMZvR123456789012pxk6YasI123456789012S7N/CM+qhHOs94lVfdu8zjauMMvRBfBL22qsU14iPB8DTHTuK766DT2IAh+eNTY123456789012u2c8D4gdzl123456789012rpqyf3j123456789012L+BIYpANf123456789012TjxeXNS+Mxh123456789012sq4cAjIqB7CA123456789012j+YpeK123456789012CMulNP282ME123456789012GjIUG6K65MKpA==\",\n  \"SigningCertURL\" : \"https://sns.us-east-1.amazonaws.com/SimpleNotificationService-12345678901236cd94b123456789012.pem\",\n  \"UnsubscribeURL\"
: \"https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:123456789012:patterns-sns-to-sqs-MySnsTopic-123456789012:123456789-1745-440a-94a2-1234567890\"\n}"
        }
    ]
}

```

## How it works

When a message is received by the SNS topic, the message is sent to the SQS queue which subscribed to the SNS topic.

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a message to the SNS topic and observe the message received by SQS (using values from Terraform output):

1. Send a message to SNS:
```bash
aws sns publish --topic-arn ENTER_YOUR_SNS_TOPIC_ARN --subject testSubject --message testMessage
```
1. Retrieve the message from SQS queue:
```bash
aws sqs receive-message --queue-url ENTER_YOUR_SQS_QUEUE_URL
```


## Cleanup

1. Delete the stack
    ```bash
    terraform destroy --auto-approve
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
