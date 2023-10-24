# AWS Secrets Manager to CloudWatch Events to SNS

This pattern contains a terraform template to detect and notify on Amazon Secrets Manager Secret Key Creation, Updation and Deletion using Amazon CloudWatch event and Amazon SNS.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sm-cw-lambda-sns-terraform

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed


## Deployment Instructions

1. Clone the project to your local working directory

   ```sh
   git clone https://github.com/aws-samples/serverless-patterns/ 
   ```

2. Change the working directory to this pattern's directory

   ```sh
   cd serverless-patterns/sm-cw-lambda-sns-terraform
   ```

1. From the command line, initialize terraform to  to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts:
   -   Provide your email address to receive notification from SNS:
   -   Enter yes
## How it works

This template is used to monitor AWS Secrets Manager secret keys. This helps in reporting when something is wrong, and take automatic actions when appropriate. Once the template is deployed, you will receive an email notification on the email address you defined. Make sure to confirm email subscription in order to receive updates related to your Secret Keys present in AWS Secret manager.

## Testing

Once the template deployed successfully, first thing to do is to confirm the Email subscription. You will receive an email to confirm it.  Then, head to AWS Secrets Manager console and Create a Secret Key by following these steps - https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html . That's it. You will soon receive a notification about the key you created. Now any event (Like Update or Delete) happens related to that Secret Key, you will receive the notification.
Log into the AWS Console, browse to AWS IoT Core:


## Cleanup

1. Change directory to the pattern directory:
    ```
    cd sm-cw-lambda-sns-terraform
    ```
1. Delete all created resources by terraform
    ```bash
    terraform destroy
    ```
1. During the prompts:
    * Provide your email address to receive notification from SNS:
    * Enter yes
1. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```

----
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. 

SPDX-License-Identifier: MIT-0
