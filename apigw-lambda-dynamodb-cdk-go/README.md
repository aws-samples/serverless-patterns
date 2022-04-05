# API Gateway REST API to Lambda to DynamoDB

This pattern demonstrates how to deploy a CDK application consisting of Amazon API Gateway, AWS Lambda, and Amazon DynamoDB. It makes use of the [DynamoDB package](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb) in [AWS Go SDK](https://aws.amazon.com/sdk-for-go/) and the [Go bindings](https://pkg.go.dev/github.com/aws/aws-cdk-go/awscdk/v2) for [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html).

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns](https://serverlessland.com/patterns)

> Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Go](https://go.dev/dl/) (`1.16` or above) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed

## Deployment Instructions

1. Clone the project to your local working directory
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Start by packaging the Lambda function in a zip file
    ```
    cd apigw-lambda-dynamodb-cdk-go/function
    GOOS=linux go build -o my-func main.go && zip function.zip my-func
    ```

4. Deploy the stack to your default AWS account and region
    ```
    cd ../cdk
    cdk deploy
    ```

> Enter `y` when prompted *Do you wish to deploy these changes (y/n)?*

Note the output from the CDK deployment process - it contains the API Gateway endpoint which will be used to test the integration.

## How does the integration work?

When an HTTP `POST` request is sent to the Amazon API Gateway endpoint, the AWS Lambda function is invoked and inserts an item into the Amazon DynamoDB table (named `users-table`).

## Testing

Testing the integration involves sending an HTTP `POST` request to the Amazon API Gateway endpoint. This example used the [curl](https://curl.se/) CLI, but you can also use other options.

Export the Amazon API Gateway endpoint as an environment variable.

```
export APIGW_REST_ENDPOINT=<CDK deployment output>

e.g. export APIGW_REST_ENDPOINT=https://abc12345ff.execute-api.us-east-1.amazonaws.com/prod/
```

Invoke the endpoint:

```
curl -i -X POST -d '{"email":"user1@foo.com", "username":"user-1"}' $APIGW_REST_ENDPOINT

curl -i -X POST -d '{"email":"user2@foo.com", "username":"user-2"}' $APIGW_REST_ENDPOINT
```

You should get an HTTP `201 Created` response in both the cases. This indicates that the items have been added to the `users` table in DynamoDB.

In this example, we will use the AWS CLI to check DynamoDB records:

```
aws dynamodb scan --table-name users-table
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
curl -i -X POST -d '{"email":"user2@foo.com", "username":"user-2"}' $APIGW_REST_ENDPOINT
```

The Lambda function returns an HTTP `409 Conflict` to API Gateway in this case since a [Condition Expression](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html) (`attribute_not_exists(email)`) prevents an existing item (with the same `email`) from being overwritten by the `PutItem` call.

## Cleanup
 
To delete the resources that were created:

```
cdk destroy
```

> It might take some time for the CloudFormation stack to get deleted.

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0