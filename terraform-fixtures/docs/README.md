# Getting Started with Terraform Serverless Patterns

*Important:* the Terraform configurations use various AWS services and there can be costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

More information about using Terraform to manage serverless resources on AWS is available on [serverless.tf](https://serverless.tf).

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory. For e.g., run this to go to the `terraform-apigw-api-lambda` pattern:
    ```bash
    cd serverless-patterns/terraform-apigw-api-lambda
    ```
1. From the command line, initialize terraform to download and install the providers and required modules defined in the configuration:
    ```bash
    terraform init
    ```
1. From the command line, apply the Terraform configurations:
    ```bash
    terraform apply
    ```
1. During the prompts:
    * Enter yes
1. Note the outputs from the deployment process, these contain the resource names and/or ARNs which are used for testing.

## Testing

Once terraform finishes execution, resources will be deployed.

See `Testing` section in the documentation for the pattern for further steps.

Please note, by default, resources will be created in AWS region `Ireland (eu-west-1)`.

## Cleanup

1. Change directory to the pattern directory. For e.g., run this to go to the `terraform-apigw-api-lambda` pattern:
    ```bash
    cd serverless-patterns/terraform-apigw-api-lambda
    ```
1. Delete all created resources:
    ```bash
    terraform destroy
    ```
1. During the prompts:
    * Enter yes

1. Confirm all created resources has been deleted:
    ```bash
    terraform show
    ```
