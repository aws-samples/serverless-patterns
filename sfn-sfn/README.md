# AWS Step Functions Express Workflow to call another State Machine

The Step Functions Express Workflow can be started using the AWS CLI or from another service (e.g. API Gateway) to run an express workflow.

The SAM template deploys two Step Functions Express workflows: "Parent" and "Child". The SAM template contains the minimum IAM resources required to run the application with logging enabled.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-sfn

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

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
    cd sfn-sfn
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

* Start the Express Workflow using the `start-execution` api command.
* The Parent Express Workflow will execute the Child Express Workflow.


## Testing

Run the following AWS CLI command to send a 'start-execution` comand to start the Step Functions workflow. Note, you must edit the {parentStatemachineARN} placeholder with the ARN of the deployed "Parent" Step Functions workflow. This is provided in the stack outputs.

1. send a 'start-execution` comand to start the "Parent" Step Functions workflow:
    ```bash
    aws stepfunctions start-execution  --name "test" --state-machine-arn "{parentStatemachineARN}"
    ```
2. The "Parent" Express Workflow will execute the "Child" Express Workflow
3. Check the CloudWatch Logs Groups for each State Machine Workflow to see details. The CloudWatch Log Group names are provided in the stack outputs.


### Example output:

```
    {
        "executionArn": "arn:aws:states:us-west-2:123456789012:express:ParentStateMachine-AbGSUE23kS22:test:1a1b1111-030c-12d0-4e0f-1g56h780ij12",
        "startDate": "2021-09-09T23:20:51.743000-05:00"
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