# AWS SNS integration with slack/teams channels

This pattern demonstrates how you can setup a fully serverless setup to integrate your SNS topic with Slack/Teams channel. This provisions AWS resources for you and you just need to integrate your Slack/Teams webhooks to get it running.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform CLI Installed](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) 

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd sns-slack-teams-terraform-python
    ```
3. Open the main.tf file and provide your AWS credentials and set the correct region where you would like to deploy the resources:
    
    * [refer to this article to understand various types of available methods to provide credentials](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
    
4. From the command line, use terraform to deploy the AWS resources for the pattern as specified in the main.tf file:
    ```
    terraform init && terraform apply --auto-approve
    ```

1. Note the outputs from the Terraform deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Terraform checks the resources defined in the main.tf and creates a deployment plan for it and deploys the resources in your AWS account using the credentials provided and in the region mentioned in the main.tf file.
It will created a SNS topic which you can use to publish notifications to your Slack/Teams channel. A Lambda function which will process the SNS message and pass it to the Slack/Teams webhook. You can customise the code to apply additional formatting as per your usecase.

## Testing

Publish a message from AWS Console or by CLI.

Example using CLI:

aws sns publish --topic-arn ENTER_YOUR_SNS_TOPIC_ARN --subject testSubject --message testMessage

## Cleanup
 
1. Delete the stack
    ```
    terraform destroy --auto-approve
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0