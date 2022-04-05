# Amazon API Gateway HTTP API to AWS Lambda

This pattern creates an Amazon API Gateway HTTP API and an AWS Lambda function.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/apigw-lambda-terraform).

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
    cd serverless-patterns/apigw-http-api-lambda-terraform
    ```
1. From the command line, initialize terraform to download and install the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts:
    * Enter yes
1. Note the outputs from the deployment process, these contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern deploys an Amazon API Gateway HTTP API with a default route and basic CORS configuration. The default route is integrated with an AWS Lambda function written in Python. The function logs the incoming API event (v2) and context object to an Amazon CloudWatch Logs log group and returns basic information about the event to the caller.

## Testing

Once the stack is deployed, retrieve the apigwy_url value from the outputs of the terraform apply, then call the endpoint using curl or Postman.

```
curl '<your http api endpoint>'

#sample output
{
  "message ": {
    "functionName": "test_apigw_integration",
    "xForwardedFor": "{YourIpAddress}",
    "method": "GET",
    "rawPath": "/",
    "queryString": null,
    "timestamp": "04/Apr/2022:22:50:34 +0000"
  }
}
```

```
curl '<your http api endpoint>'/pets/dog/1?foo=bar -X POST \
--header 'Content-Type: application/json' \
-d '{"key1":"hello", "key2":"World!"}'

#sample output
{
  "message ": {
    "functionName": "test_apigw_integration",
    "xForwardedFor": "{YourIpAddress}",
    "method": "POST",
    "rawPath": "/pets/dog/1",
    "queryString": {
      "foo": "bar"
    },
    "timestamp": "04/Apr/2022:22:49:14 +0000",
    "body": "{\"key1\":\"hello\", \"key2\":\"World!\"}"
  }
}
```

Then check the logs for the Lambda function from the Lambda console.

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-http-api-lambda-terraform
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
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
