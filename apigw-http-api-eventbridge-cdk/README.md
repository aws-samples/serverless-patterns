# Amazon API Gateway HTTP API to Amazon EventBridge

This pattern creates an HTTP API endpoint that directly integrates with Amazon EventBridge

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigateway-http-eventbridge-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Clone the project to your local working directory
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change the working directory to this pattern's directory
    ```
    cd apigw-http-api-eventbridge-cdk/cdk
    ```

1. Install dependencies
    ```
    npm install
    ```

1. Deploy the stack to your default AWS account and region. The output of this command should give you the HTTP API URL.
    ```
    cdk deploy
    ```

## How it works

This pattern creates an Amazon API gateway HTTP API endpoint. The endpoint uses service integrations to directly connect to Amazon EventBridge. An EventBridge rule sends all events to Cloudwatch Logs.

## Testing

To test the endpoint first send data using the following command. Be sure to update the endpoint with endpoint of your stack.

```
curl --location --request POST '<your api endpoint>' --header 'Content-Type: application/json' \
--data-raw '{
    "Detail":{
        "message": "This is my test"
    }
}'
```

Then check the logs in Cloudwatch logs

## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
