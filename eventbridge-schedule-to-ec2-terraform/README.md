# EventBridge Scheduler to start and stop EC2 instances
This pattern will create two EventBridge schedules that will start and stop a given array of instance-ids. You can control the start/stop time and timezone of you chosing. This example will start instances at 08:00 and stop them at 17:00 in the US/Eastern timezone.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-schedule-to-ec2-terraform.

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
    cd eventbridge-schedule-to-ec2-terraform
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

An Amazon EventBridge Schedule is used to start and stop an EC2 instance. The Terraform stack creates a VPC, EC2 instance and EventBridge Scheduler that invokes the startInstance and stopInstance API on a schedule.

## Testing

1. After deployment, view the schedule created in the Amazon EventBridge console under Scheduler>Schedules. 
2. View the `ec2-start-schedule`. Navigate to the *Target* tab and note the `Payload` value which is in the format: `{"InstanceIds":["i-006c2e9f4e706bf48"]}`
3. Navigate to the EC2 console and find the EC2 instance from the `Payload` value. Check the instance is powered on during 08:00 and 17:00 in the US/Eastern timezone.

## Cleanup
 
1. Delete all created resources and follow prompts:
    ```
    terraform destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
