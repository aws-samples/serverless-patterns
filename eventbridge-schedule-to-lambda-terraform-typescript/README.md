# Amazon EventBridge Schedule to Amazon Lambda


This pattern will create an EventBridge schedule to invoke a TypeScript based AWS Lambda function every 5 minutes. The pattern is deployed using Terraform.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one
  and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS
  resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd eventbridge-schedule-to-lambda-terraform-typescript
    ```
1. From the command line, install the required dependencies:
    ```
    npm install 
    ```
1. From the command line, run the following command to build the TypeScript function and create the zip file for deployment:
    ```
    npm run build
    ```
1. From the command line, initialize terraform:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file and follow the prompts:
    ```
    terraform apply
    ```

## How it works

An EventBridge Schedule is created to invoke an AWS Lambda function every 5 minutes. Along with the schedule and Lambda function, an IAM role is created to allow EventBridge Scheduler to invoke the Lambda function.  

## Testing

After deployment, you can verify the schedule is invoking the Lambda function by viewing the functions execution logs in CloudWatch or viewing the functions "Invocations" metric in CloudWatch for positive data points.

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd eventbridge-schedule-to-lambda-terraform-typescript
    ```
1. Delete all created resources and follow prompts
    ```bash
    terraform destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
