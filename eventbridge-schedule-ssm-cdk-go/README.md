# EventBridge Scheduler to Start State Manager Association Once

This pattern will create an [Amazon EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/getting-started.html) schedule to start an [AWS Systems Manager State Manager association](https://docs.aws.amazon.com/systems-manager/latest/userguide/scheduling-automations-state-manager-associations.html) runbook every 5 minutes. The pattern is deployed using the AWS Cloud Development Kit (AWS CDK) for GO. 

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/eventbridge-schedule-ssm-cdk-go](https://serverlessland.com/patterns/eventbridge-schedule-ssm-cdk-go)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one
  and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS
  resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Go](https://go.dev/dl/) (`1.18` or above) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd eventbridge-schedule-ssm-cdk-go
    ```
3. From the command line, bootstrap the CDK if you haven't already done so. 
    ```
    cdk bootstrap 
    ```
4. Deploy the CDK stack to your default AWS account and region.
    ```
    cdk deploy
    ```

## How it works

An EventBridge Scheduler schedule is created that starts a State Manager association once in AWS Systems Manager every 5 minutes. The demo association will use an automation document `AWS-DisablePublicAccessForSecurityGroup` to revoke RDP and SSH public access in a security group.  Along with a scheduler, the CDK stack creates VPC, security group, association, IAM role, and policy for Automation and EventBridge Scheduler to assume and start association.  

## Testing

The created security group does not have inbound rule with public RDP and SSH access.  You can manually add public RDP and SSH access in the rule in the target security group.  The public RDP and SSH access rules will be revoked when the next EventBridge Scheduler schedule runs.

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
