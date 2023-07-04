# Amazon EventBridge Scheduler to AWS Batch

This pattern will create an [EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/getting-started.html) to submit an [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/Batch_GetStarted.html) job from a job definition every 5 minutes. The pattern is deployed using Terraform to create the required VPC, Batch and EventBridge Scheduler resources. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-schedule-to-batch-terraform

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
    cd eventbridge-schedule-to-batch-terraform
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

An Amazon EventBridge Schedule is created that submits an AWS Batch job from a job definition every 5 minutes. The Terraform stack creates a VPC, Batch compute environment, jobs and job queues, and EventBridge Scheduler that invokes the submitJob API to run the AWS Batch job.

## Testing

1. After deployment, view the schedule created in the Amazon EventBridge console under Scheduler>Schedules. 
2. From the AWS Batch console, navigate to the Jobs section. The schedule will trigger a new job every 5 minutes, which will be visable in the Jobs section. You can also view the job status from the Dashboard section of the AWS Batch console in the Job queue overview. 

## Cleanup
 
1. Delete all created resources and follow prompts:
    ```
    terraform destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
