# Amazon API Gateway, AWS Step Functions, to Amazon DynamoDB CRUD API

This stack creates a fully functioning CRUD API powered by Amazon API Gateway direct integration to AWS Step Functions and backed by Amazon DynamoDB.

*CRUD = Create, Read, Update, Delete*

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-sfn-crud-terraform

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
2. Change directory to the pattern directory:
    ```
    cd apigw-sfn-crud-terraform
    ```
3. From the command line, initialize terraform to download and install the providers defined in the configuration:
    ```
    terraform init
    ```
4. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
5. During the prompts:
    * Enter yes
6. Note the outputs from the deployment process. These contain the resource names and/or URLs which are used for testing.

## How it works

Amazon API Gateway creates a direct integration with AWS Step Functions utilizing a synchronous call. The Step Functions state machine evaluates the path and method to choose the proper action. The action steps can be modified to meet your needs.

## Testing

Once your application is up and running, you can verify the CRUD operations in two ways:
- Make a curl request directly to the endpoint shown in the Terraform output
- Use Postman by importing the provided collection file (make sure to update the endpoint URLs to match your deployed environment)

Both methods will allow you to test and interact with your API endpoints.

## Cleanup
1. Change directory to the pattern directory:
    ```
    cd apigw-sfn-crud-terraform
    ```
2. Delete all created resources by terraform
    ```bash
    terraform destroy
    ```
3. During the prompts:
    * Enter yes
4. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

