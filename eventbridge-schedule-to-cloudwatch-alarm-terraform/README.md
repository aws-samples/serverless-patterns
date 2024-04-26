# Amazon EventBridge Scheduler for Amazon CloudWatch Alarm

This pattern will create two Amazon EventBridge Scheduler schedules to enable and disable the action of a Amazon CloudWatch alarm in a specific period. This example will enable the alarm at 08:00 and disable it at 17:00 in the US/Eastern timezone.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-schedule-to-cloudwatch-alarm-terraform.

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
    cd eventbridge-schedule-to-cloudwatch-alarm-terraform
    ```
1. From the command line, initialize terraform to download and install the providers defined in the configuration: 
    ```
    terraform init
    ```
1. From the commend line, apply the configuration in the main.tf file and follow the prompts: 
    ```
    terraform apply
    ```


## How it works

Two Amazon EventBridge Scheduler schedules will be used to enable and disable the action of a CloudWatch alarm. The Terraform template creates a VPC, an EC2 instance and two schedules that invokes the enableAlarmActions and disableAlarmActions API regularly.

## Testing

1. After the deployment, review the schedule created in the Amazon EventBridge console under Scheduler > Schedules. 
2. Navigate to the CloudWatch console to verify the alarm graph, a period with blue color under the graph is representing the action has been disabled.
3. Navigate to the CloudTrail console to verify the enableAlarmActions and disableAlarmActions API calls.

## Cleanup
 
1. Delete all created resources and follow prompts:
    ```
    terraform destroy
    ```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
