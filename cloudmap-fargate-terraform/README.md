# Enabling Service Discovery for AWS Fargate

This pattern provides sample Terraform IaC template to provision end to end Amazon Elastic Container Service (ECS) resources and deploy ECS service with integration of Cloud Map

With Cloud Map, you can define custom names for your application resources, and it maintains the updated location of these dynamically changing resources

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cloudmap-fargate-terraform

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
    cd serverless-patterns/cloudmap-fargate-terraform
    ```
1. From the command line, initialize terraform to  to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply --auto-approve
    ```

## How it works

Service discovery uses AWS Cloud Map API actions to manage HTTP and DNS namespaces for your Amazon ECS services. Amazon ECS service can is configured to use Amazon ECS service discovery.

## Testing

Application having VPC connectivity can now access the ECS tasks not only from the Taask IP but also from the Cloud Map namespace Domain name. You can do a "dig" from any EC2 instance/machine that has connectivity to the ECS tasks VPC to test access to Cloud Map Namespace. You can use either AWS Cloud Map API or DNS lookup to resolve a service's name to a current active endpoint.


## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/cloudmap-fargate-terraform
    ```
1. Delete all created resources
    ```bash
    terraform destroy --auto-approve
    ```
1. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
