# AWS API Gateway (REST API) to SQS

This pattern creates an Amazon API Gateway REST API with a send route that send message to a SQS queue. 

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
    cd apigw-sqs-rest
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The API Gateway handles the incoming API requests and send the $request.body.MessageBody as a message to SQS queue. 

## Testing

1. Copy the API Endpoint from SAM Deploy output
ex: https://********.<region>.amazonaws.com/Prod 

2. Send a post request to the API Endpoint with sample JSON body
ex:
{
  "type": "API Request",
  "message": "sample message from API Gateway"
}

3. Copy the SQS Queue URL from the deploy output and check the message received in the SQS queue using below command by replacing {Queue URL } to the actual URL value you copied from output
aws sqs receive-message --queue-url {Queue URL} --attribute-names All --message-attribute-names All --max-number-of-messages 10

## Cleanup
 
1. Delete the stack
    sam delete
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0