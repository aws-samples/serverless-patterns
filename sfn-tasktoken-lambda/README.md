# Step Function Wait for a Callback with the Task Token from Lambda

This Serverless pattern is designed to start a task and then wait for a callback with a Task Token. This is useful in scenarios where a long-running task needs to be started and the system needs to wait for some external process to complete and then notify back with the result using a token. For example, include asynchrounous workflows, manual approval process etc.

This State Machine initiates a task by sending a message to an SQS queue and waits for a callback with a task token. If the callback is received within the specified timeout, the workflow proceeds to success state, otherwise it transitions to a failure state.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-tasktoken-lambda

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.cxom/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd sfn-tasktoken-lambda
    ```
1. From the command line, initialize terraform to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts
    #var.region
    - Enter a value: {enter the region for deployment}

## Testing

1. You can start the execution of the Step Function using the following CLI command
    ```
    aws stepfunctions start-execution --state-machine-arn STATE_MACHINE_ARN 
    ```

1. You will see that the State Machine successfully executes because the Lambda function returns the Task Token.

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/sfn-tasktoken-lambda
    ```
1. Delete all created resources
    ```
    terraform destroy
    ```
    
1. During the prompts:
    ```
    Enter all details as entered during creation.
    ```
1. Confirm all created resources has been deleted
    ```
    terraform show
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
