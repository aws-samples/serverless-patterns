# Amazon API Gateway REST API to AWS Lambda with Request Validator

This pattern creates an Amazon API Gateway REST API with Request Validator and an AWS Lambda function.

Learn more about this pattern at: https://serverlessland.com/patterns/apigw-lambda-validator.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [API Request Validation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-lambda-request-validator
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the REST API Name

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs that were created.

## How it works

This pattern deploys an Amazon API Gateway REST API with a request validator and a default route integrated with an AWS Lambda function written in Node.js. The request validator is used to validate query string, header and request body passed on each REST API call. The lambda function returns a basic response when all validations are passed and when any validation fails API will return a response.

## Testing

Once the application is deployed, either use a curl or call the endpoint from Postman.

Example POST Request: curl -X POST "https://{api-gateway-endpoint}/prod?myQueryString=mystring123" --header "myHeader:myhead123" -H 'Content-Type: application/json' -d '{"firstName":"John","lastName":"Bean"}'

Response:
```
{
  "queryString": "mystring123",
  "header": "myhead123",
  "message": "Hello John Bean, from AWS Lambda!"
}
```

Example POST Request without queryString: curl -X POST "https://{api-gateway-endpoint}/prod" --header "myHeader:myhead123" -H 'Content-Type: application/json' -d '{"firstName":"John","lastName":"Bean"}'

Response:
```
{
  "message": "Missing required request parameters: [myQueryString]"
}
```

Example POST Request without header: curl -X POST "https://{api-gateway-endpoint}/prod?myQueryString=mystring123" -H 'Content-Type: application/json' -d '{"firstName":"John","lastName":"Bean"}'

Response:
```
{
  "message": "Missing required request parameters: [myHeader]"
}
```

Example POST Request without queryString and header: curl -X POST "https://{api-gateway-endpoint}/prod"  -H 'Content-Type: application/json' -d '{"firstName":"John","lastName":"Bean"}'

Response:
```
{
  "message": "Missing required request parameters: [myHeader, myQueryString]
}
```

Example POST Request with invalid request body: curl -X POST "https://{api-gateway-endpoint}/prod?myQueryString=mystring123" --header "myHeader:myhead123" -H 'Content-Type: application/json' -d '{"firstName":"John"}'

Response:
```
{
  "message": "Invalid request body"
}
```

## Documentation
- [Working with HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html)
- [Working with AWS Lambda proxy integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html)
- [AWS Lambda - the Basics](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/aws-lambdathe-basics.html)
- [Lambda Function Handler](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/the-handler.html)
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

This pattern was contributed by Sudheer Yalamanchili.

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
