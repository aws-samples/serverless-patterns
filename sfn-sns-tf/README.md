# AWS Step Functions Workflow to Amazon SNS

The Step Functions Workflow can be started using the AWS CLI or from another service (e.g. API Gateway) to run an workflow and return the result.

The terraform template deploys a Step Functions workflow that sends the message to Amazon SNS and returns the response. The terraform template contains the minimum IAM resources required to run the application.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-sns-terraform

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

1. Change the working directory to this pattern's directory

   ```sh
   cd serverless-patterns/sfn-sns-tf
   ```

1. From the command line, initialize terraform to  to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts:
   -   Provide your email address to receive notification from SNS:
   -   Enter yes
   
## How it works

* Start the Workflow using the `start-execution` api command with a "InputAndMessage" string in the input payload.
* The Workflow will send the user-inputed message to the SNS Topic.

## Example event payload from Stepfunctions to SNS
```
aws stepfunctions start-execution --name "test" --state-machine-arn "{statemachineARN}" --input '{"InputAndMessage": {"Input":"You just received a message from the state machine!","Message":"hello"}}'
```

## Testing

Run the following AWS CLI command to send a 'start-execution` comand to start the Step Functions workflow. Note, you must edit the {statemachineARN} placeholder with the ARN of the deployed Step Functions workflow. This is provided in the stack outputs.

1. Click the confirmation link delivered to your email to verify the endpoint.
2. Send a 'start-execution` comand to start the Step Functions workflow:
    ```bash
    aws stepfunctions start-execution --name "test" --state-machine-arn "{statemachineARN}" --input '{"InputAndMessage": {"Input":"You just received a message from the state machine!","Message":"hello"}}'
    ```
3. The message is delivered to your email address.
    Example Message:
    ```bash         
        {"Input":"You just received a message from the state machine!","Message":"hello"}
    ```

### Example output:

```
    {
        "executionArn": "arn:aws:states:us-east-1:1234567890:execution:StateMachinetoSNS:12345",
        "startDate": "2023-11-11T16:08:54.982000+00:00"
    }
```
## Cleanup
 
## Cleanup

1. Change directory to the pattern directory:
    ```
    cd sfn-sns-tf
    ```
1. Delete all created resources by terraform
    ```bash
    terraform destroy
    ```
1. During the prompts:
    * Provide your email address to receive notification from SNS:
    * Enter yes
1. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0