# Amazon API Gateway data validation models

This pattern creates an Amazon API Gateway that handles simple data validation at the endpoint without invoking the Lambda function when the data validation fails.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-custom-resource-policy](https://serverlessland.com/patterns/apigw-custom-resource-policy)

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
    apigw-data-validation
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The data model is declared in the API Gateway resource. The Lambda function then requires the request body to be validated against this model.

## Testing

After the application is deployed try the following scenarios.

### Create a new vehicle entering valid data:
```
curl --location --request POST 'https://qap9jh21xk.execute-api.us-west-2.amazonaws.com/Prod/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "make":"MINI",
    "model":"Countryman",
    "year": 2010
}'
```
Expected response: `{"message": "Data vbalidation succeded", "data": {"make": "MINI", "model": "Countryman", "year": 2010}}`
### Now enter a year less than 2010
```
curl --location --request POST 'https://qap9jh21xk.execute-api.us-west-2.amazonaws.com/Prod/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "make":"MINI",
    "model":"Countryman",
    "year": 2002
}'
```
Expected response: `{"message": "Invalid request body"}`

Try some other combinations and see what you get!

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
