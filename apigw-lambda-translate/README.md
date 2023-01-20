# Amazon API Gateway REST API to AWS Lambda and AWS Translate service

This pattern creates an Amazon API Gateway REST API and an AWS Lambda function that calls AWS Translate service.

Learn more about this pattern at: https://serverlessland.com/patterns/apigw-lambda-translate.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [AWS Translate](https://aws.amazon.com/translate/)
* [AWS Translate Languages](https://docs.aws.amazon.com/translate/latest/dg/pairs.html)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd apigw-lambda-translate
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs that were created.

## How it works

This pattern deploys an Amazon API Gateway REST API and a default route integrated with an AWS LAMBDA function written in Python. The lambda function calls AWS Translate service using the text and language given in the request body and returns the translated text or error response if the language code is not supported.

## Testing

Once the application is deployed, either use a curl or call the endpoint from Postman.

Example POST Request to translate text to Spanish:
```
    curl -X POST "https://{api-gateway-endpoint}/prod"  -H 'Content-Type: application/json' -d '{"OriginalText":"Hello, my name is AWS","TranslateToLanguage":"es"}'
```

Response:
```
  "Hola, mi nombre es AWS"
```

Example POST Request to translate text to Afrikaans:
```
    curl -X POST "https://{api-gateway-endpoint}/prod"  -H 'Content-Type: application/json' -d '{"OriginalText":"Hello, my name is AWS","TranslateToLanguage":"af"}'
```

Response:
```
  "Hallo, my naam is AWS"
```

Example POST Request with unsupported language:
```
    curl -X POST "https://{api-gateway-endpoint}/prod"  -H 'Content-Type: application/json' -d '{"OriginalText":"Hello, my name is AWS","TranslateToLanguage":"ef"}'
```

Response:
```
  "An error occurred (UnsupportedLanguagePairException) when calling the TranslateText operation: Unsupported language pair: en to ef. Target language 'ef' is not supported"
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
    sam delete
    ```

This pattern was contributed by Sudheer Yalamanchili.

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
