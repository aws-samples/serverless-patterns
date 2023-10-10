# AWS Lambda Function URL to Amazon DynamoDB

This pattern shows how to use a SAM template to deploy a Serverless application comprising of AWS Lambda and Amazon DynamoDB. It makes use of the [DynamoDB package](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb) in [AWS Go SDK](https://aws.amazon.com/sdk-for-go/).

The [Lambda Function URL](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html) exposes an HTTP(s) endpoint. When an HTTP `POST` request with the right payload is sent to this endpoint, the AWS Lambda function is invoked and inserts an item into the Amazon DynamoDB table (named `users`).

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns](https://serverlessland.com/patterns)

> Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Go](https://go.dev/dl/) (`1.16` or above) installed
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-functionurl-dynamodb-sam-go
    ```
1. Use AWS SAM to build the serverless application with its dependencies
    ```
    sam build
    ```
1. Use AWS SAM to deploy the AWS resources for the pattern as specified in the `template.yml` file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    
    > Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

```
Configuring SAM deploy
======================

        Looking for config file [samconfig.toml] :  Not found

        Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [sam-app]: 
        AWS Region [us-east-1]: 
        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
        Confirm changes before deploy [y/N]: y
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]: y
        #Preserves the state of previously provisioned resources when an operation fails
        Disable rollback [y/N]: n
        DemoFunction Function Url may not have authorization defined, Is this okay? [y/N]: y
        Save arguments to configuration file [Y/n]: 
        SAM configuration file [samconfig.toml]: 
        SAM configuration environment [default]: 
```

> Note the output from the SAM deployment process. This contains the HTTP URL endpoint for your function required for testing

## How it works

The Lambda Function URL exposes an HTTP(s) endpoint. When an HTTP `POST` request with the right payload is sent to thisendpoint, the AWS Lambda function is invoked and inserts an item into the Amazon DynamoDB table (named `users`).

## Testing

Testing the integration involves sending an HTTP `POST` request to the Lambda Function URL. This example used the [curl](https://curl.se/) CLI, but you can also use other options.

Export the Lambda Function URL endpoint as an environment variable.

```
export LAMBDA_FUNCTION_URL_ENDPOINT=<SAM deployment output>

e.g. export LAMBDA_FUNCTION_URL_ENDPOINT=https://vj6lck76h422e6i3yl5ooniexm0iisqv.lambda-url.us-east-1.on.aws/
```

Invoke the endpoint:

```
curl -i -X POST -H "Content-Type: application/json" -d '{"email":"user1@foo.com", "username":"user-1"}' $LAMBDA_FUNCTION_URL_ENDPOINT

curl -i -X POST -H "Content-Type: application/json" -d '{"email":"user2@foo.com", "username":"user-2"}' $LAMBDA_FUNCTION_URL_ENDPOINT
```

You should get an HTTP `201 Created` response in both the cases. This indicates that the items have been added to the `users` table in DynamoDB.

In this example, we will use the AWS CLI to check DynamoDB records:

```
aws dynamodb scan --table-name users
```

You should get a response:

```
{
    "Items": [
        {
            "email": {
                "S": "user1@foo.com"
            },
            "user_name": {
                "S": "user-1"
            }
        },
        {
            "email": {
                "S": "user2@foo.com"
            },
            "user_name": {
                "S": "user-2"
            }
        }
    ],
    "Count": 2,
    "ScannedCount": 2,
    "ConsumedCapacity": null
}
```

Try to insert the same record again:

```
curl -i -X POST -d '{"email":"user2@foo.com", "username":"user-2"}' $LAMBDA_FUNCTION_URL_ENDPOINT
```

The Lambda function returns an HTTP `409 Conflict` to API Gateway in this case since a [Condition Expression](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html) (`attribute_not_exists(email)`) prevents an existing item (with the same `email`) from being overwritten by the `PutItem` call.

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
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0