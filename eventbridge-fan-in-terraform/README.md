# Amazon Eventbridge Eventbus fan-in to Central Eventbus to different region

This pattern demonstrates how to aggregate all your events from multiple Eventbus (in the same region) to a central Eventbus in a different region. This pattern is deployed using Terraform to create a central EventBridge bus, Eventbridge rules on fan-in buses and all IAM resources required. The Eventbuses to aggregate can be defined in terraform.tfvars file (Sample ARNs is provided, replace with Eventbus ARNs as needed). The provider.tf file also lists the AWS regions of the fan-in Eventbus and central Eventbus (replace these based on where your Eventbuses exist and where you want your central bus to be created).

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-fan-in-terraform

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
    cd eventbridge-fan-in-terraform
    ```
1. From the command line, initialize Terraform:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file and follow the prompts:
     ```
    terraform apply
    ```

## How it works

This application picks the configurations from terraform.tfvars files to create Eventbridge rules on all entered Eventbus for fan-in to a central Eventbus. The terraform creates the rules, along with the required IAM roles and policies and configures the target as the central Eventbus which it also creates. The central Eventbus has a rule that routes all events to a Cloudwatch log group for testing.

## Testing

Login to the AWS account where the terraform is deployed. Publish an event on any of the fan-in Eventbuses. Switch to the region where the central Eventbus is created and navigate to Cloudwatch logs. You should see the event you published in the log group of the Central Eventbus.


## Cleanup
 
1. Delete all created resources and follow the prompts:
     ```
    terraform destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0