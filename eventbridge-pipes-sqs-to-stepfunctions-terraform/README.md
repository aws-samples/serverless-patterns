# Invoke AWS Step Functions state machine with Amazon with EventBridge Pipes

This pattern shows how to use [Amazon EventBridge Pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html) to launch an AWS Step Functions state machine with a message coming from an Amazon SQS Queue. The pattern is deployed using Terraform.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-pipes-sqs-to-stepfunctions-terraform.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd eventbridge-pipes-sqs-to-stepfunctions-terraform
    ```
1. From the command line, initialize Terraform:
    ```
    terraform init
    ```
1. From the commend line, apply the configuration in the main.tf file and follow the prompts:
    ```
    terraform apply
    ```

## How it works

Amazon EventBridge Pipes connects sources to targets. This Terraform stack creates an EventBridge Pipe which receives message from the source SQS queue and sends it to the target AWS Step Functions state machine. 

## Testing

1. Starts a Live Tail streaming session for StepFunction LogGroup 

```
aws logs start-live-tail --log-group-identifiers <StepFunction LogGroup ARN>
```

2. Put a message into the queue

```
aws sqs send-message --queue-url <SQS Queue URL> --message-body "Test"
```

3. Observe the logs for the new execution.

## Cleanup
 
1. Delete all created resources and follow prompts:
    ```
    terraform destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
