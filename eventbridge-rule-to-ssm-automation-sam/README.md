# Amazon EventBridge Rule to AWS Systems Manager Automation

This pattern demonstrates how to create an Amazon EventBridge Rule to trigger based on a specific event, and then run an AWS Systems Manager Automation Runbook using information from the event.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-rule-to-ssm-automation-sam

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
    cd eventbridge-rule-to-ssm-automation-sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter a value for the MetadataHttpPutResponseHopLimit parameter (or use the default)
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern will create an EventBridge rule that is configured to trigger when an EC2 instance goes into the "running" state. The rule will then execute the [AWSSupport-ConfigureEC2Metadata](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-configureec2metadata.html) Automation Runbook against that instance to disable IMDSv1.

## Testing

Once the stack is deployed, launch a new EC2 Instance, and then navigate to https://console.aws.amazon.com/systems-manager/automation/executions. There will be a new Execution of the `AWSSupport-ConfigureEC2Metadata` Document against the new instance.

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
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0