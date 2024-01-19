# Amazon EventBridge Scheduler to Amazon CloudWatch

This pattern will create an [EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/getting-started.html) to publish [custom metrics to Amazon Cloudwatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html). The pattern is deployed using Terraform to create the EventBridge Scheduler and IAM resources required for Scheduler to interact with CloudWatch. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-schedule-to-cloudwatch-terraform.

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
    cd eventbridge-schedule-to-cloudwatch-terraform
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

An Amazon EventBridge Schedule is used to publish custom metrics to Amazon CloudWatch every minute. The Terraform stack creates an EventBridge Schedule and the required IAM resource for Scheduler to interact with CloudWatch.

## Testing

1. After deployment, view the schedule created in the Amazon EventBridge console under Scheduler>Schedules. 
2. From the Amazon CloudWatch console, navigate to the Metrics dashboard and view the CustomMetrics namespace which contains the metrics published by the schedule. You can view additional metrics published each minute in the same CustomMetrics namespace.  

## Cleanup
 
1. Delete all created resources and follow prompts:
    ```
    terraform destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0