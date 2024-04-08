# Amazon API Gateway REST API to AWS Lambda in VPC to SQS

This pattern creates an Amazon API Gateway REST API and an AWS Lambda function in a VPC that sends the received message to SQS

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/apigw-rest-api-lambda-vpc-sqs).

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
    cd apigw-rest-api-lambda-vpc-sqs
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Enter Subnets
    * Enter LambdaSecurityGroupId

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern deploys an Amazon API Gateway REST API with Dev stage, API key required for the authentication and a Lambda proxy integration. The API will send a message to the Lambda function that is in a VPC, and this function will send the message to SQS queue.

## Testing

Once the application is deployed, retrieve the RestApiEndpoint value from CloudFormation Outputs. Either run curl command or call the endpoint from Postman.

Example: POST https://{RestApiId}.execute-api.eu-west-1.amazonaws.com/Dev/sendmessage
- Request Body: {"message":"hello world"}
- Request Headers: Content-Type:application/json
                   x-api-key:api_key

Curl command: curl -d '{"message":"hello"}' -H "Content-Type:application/json" -H "x-api-key:api_key" -X POST https://{RestApiId}.execute-api.eu-west-1.amazonaws.com/Dev/sendmessage

Response:
```
"Message has been sent to SQS Queue"
```
## Documentation
- [Working with REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html)
- [Working with AWS Lambda proxy integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html)
- [API key](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-setup-api-key-with-console.html)
- [Lambda in a VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html)
- [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html)

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
This pattern was contributed by Sana FATHALLAH.
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
