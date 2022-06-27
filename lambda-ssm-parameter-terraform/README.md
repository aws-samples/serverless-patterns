# AWS Lambda to AWS Systems Manager Parameter Store

This pattern creates an AWS Lambda function and an AWS Systems Manager Parameter Store parameter.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-ssm-terraform.

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
    cd lambda-ssm-parameter-terraform
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
    * Enter yes
1. Note the outputs from the deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern creates an AWS Lambda function and an AWS Systems Manager Parameter Store parameter. The parameter is added as a function environment variable named "SSMParameterName". The function execution role only allows Get and Put actions on the parameter. The function supports a JSON event in the following format:

```
{
  "method": "{GET || PUT}",
  "body": "{NewParameterValue}"
}
```

The method can be either GET (retrieve current parameter value) or PUT (update parameter with new value). The body of the event is used to define the new value of the parameter.

The function code can easily be modified to support an Amazon API Gateway API event by changing the format for method:

1. API v1 event: event.httpMethod
1. API v2 event: event.requestContext.http.method

## Testing

Once the application is deployed, navigate to the Lambda function and configure GET and PUT test events. Invoke the function using each test event. Review the Amazon CloudWatch Logs for details on the function invocation. Navigate to the AWS Systems Manager Paramater Store to observe changes to the parameter value after a PUT event.

Example GET test event:
```
{
  "method": "GET",
  "body": ""
}
```

Response:
```
{
  "statusCode": 200,
  "body": "{\"Parameter\":{\"Name\":\"ExampleParameterName\",\"Type\":\"String\",\"Value\":\"{\\\"key1\\\":\\\"value1\\\"}\",\"Version\":5,\"LastModifiedDate\":\"2021-04-02T13:46:55.828Z\",\"ARN\":\"arn:aws:ssm:us-east-2:{AwsAccount}:parameter/ExampleParameterName\",\"DataType\":\"text\"}}"
}
```

Example PUT test event:
```
{
  "method": "PUT",
  "body": "{\"key1\":\"value1\", \"key2\":\"value2\"}"
}
```

Response: 
```
{
  "statusCode": 200,
  "body": "{\"Version\":6,\"Tier\":\"Standard\"}"
}
```

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd lambda-ssm-parameter-terraform
    ```
1. Delete all created resources by terraform
    ```bash
    terraform destroy
    ```
1. During the prompts:
    * Enter yes
1. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0