# Amazon API Gateway HTTP API to AWS Lambda

This pattern creates an AWS Lambda function and an Aurora Serverless cluster with Data API and a Secrets Manager secret.

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
    cd apigw-http-api-lambda
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern creates an AWS Lambda function and an Aurora Serverless cluster with Data API and a Secrets Manager secret. The function queries a database on the Aurora cluster and returns the results.

!!! Explain how the function queries a system database by default, but you can use the RDS Query Editor to connect to the database using the Secret Arn to create a table and insert records. Then update the lambda function sqlParams to execute statements against the new table. !!!

## Testing

Once the application is deployed, navigate to the Lambda function and configure test events. Invoke the function with each test event to query a database on the Aurora cluster. Review the Amazon CloudWatch Logs for details on the function invocation.

When first connecting to the Aurora Serverless cluster after a period of inactivity, you may receive the following error: 

```
BadRequestException: Communications link failure
The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.
code: 'BadRequestException'
statusCode: 400
retryable: true
```


Example POST Request: https://{HttpApiId}.execute-api.us-east-2.amazonaws.com/path1/path2?foo=bar
- Request Header: "Content-Type: application/json"
- Request Body: {"key1":"value1", "key2":"value2"}

Response: 
```
{
  "functionName": "http-api-lambda-proxy-function",
  "xForwardedFor": "{YourIpAddress}",
  "contentType": "application/json",
  "method": "POST",
  "rawPath": "/path1/path2",
  "queryString": {
    "foo": "bar"
  },
  "body": "{\"key1\":\"value1\", \"key2\":\"value2\"}"
}
```

## Documentation
- [Using the Data API for Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html)
- [Data API - ExecuteStatement](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ExecuteStatement.html)
- [Data API - ExecuteStatement Response Elements](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ExecuteStatement.html#API_ExecuteStatement_ResponseElements)
- [AWS Lambda - the Basics](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/aws-lambdathe-basics.html)
- [Lambda Function Handler](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/the-handler.html)
- [Function Event Object - Overview](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/the-event-object.html)
- [Function Environment Variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html)

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
