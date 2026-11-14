# Amazon Dynamodb Streams to AWS Lambda

This version is a Java port of the [original pattern](https://serverlessland.com/patterns/dynamodb-lambda-filters-terraform).

The Terraform template deploys a Lambda function, a DynamoDB table, and the minimum IAM resources required to run the application.

When items are written or updated in the DynamoDB table, the changes are sent to a stream. This pattern configures a Lambda function to poll this stream. The function is invoked with a payload containing the contents of the table item that changed.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd dynamodb-streams-lambda-terraform-java
    ```
1. Buid the Java Lambda function jar file using Maven. 
   ```
   mvn package
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
    * Enter your AWS region
    * Enter yes
1. Note the outputs from the deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

When items are written or updated in a DynamoDB table, the changes are sent to a stream. This pattern configures a Lambda function to poll this stream. The function is invoked with a payload containing the contents of the table item that changed.

## Testing

After deployment, add an item to the DynamoDB table. Go to the CloudWatch Logs for the deployed Lambda function. You will see the event is logged out containing the item data.

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd dynamodb-streams-lambda-terraform-java
    ```
1. Delete all created resources
    ```bash
    terraform destroy
    ```
1. During the prompts:
    * Enter yes
1. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
