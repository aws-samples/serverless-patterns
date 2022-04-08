# VPC and RDS Proxy for Aurora MySQL

This module deploys a VPC with private and public subnets along with all the dependencies necessary to implement the API-Gateway-HTTP-API-to-AWS-Lambda-to-RDS-Proxy pattern including an RDS Aurora cluster and RDS Proxy instance. 
This module will also spin up and EC2 instance that connects to the MySQL database to create a new database user. Reference deployment instructions section for additional details.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions (Review input variables at variables.tf)

1. Change directory to the module directory:
    ```
    cd serverless-patterns/apigw-http-api-lambda-rds-proxy-terraform/vpc-rds-setup
    ```
1. From the command line, initialize terraform to download and install the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts:
    * Enter yes
1. Note the outputs from the deployment process, these contain the resource names and/or ARNs which are used by the apigw-http-api-lambda-rds-proxy module.
    * lambda_log 
    * lambda_secret 
    * lambda_sg 
    * lambda_subnet_1 
    * lambda_subnet_2 
    * rds_proxy_arn 
    * rds_proxy_endpoint 
    * rds_proxy_log 
    * vpc_id 




## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-http-api-lambda-rds-proxy-terraform/vpc-rds-setup
    ```
1. Delete all created resources
    ```
    terraform destroy
    ```
1. During the prompts:
    * Enter yes
1. Confirm all created resources has been deleted
    ```
    terraform show
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
