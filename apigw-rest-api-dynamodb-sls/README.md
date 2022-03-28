# Amazon API Gateway REST API to Amazon DynamoDB

This pattern creates an Amazon API Gateway REST API that integrates with an Amazon DynamoDB table.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-rest-api-dynamodb-sls](https://serverlessland.com/patterns/apigw-rest-api-dynamodb-sls).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [NodeJS](https://nodejs.org/en/download/) (LTS version) installed
* [Serverless Framework CLI](https://www.serverless.com/framework/docs/getting-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ``` sh
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:

    ``` sh
    cd serverless-patterns/apigw-rest-api-dynamodb-sls
    ```

1. From the command line, use Serverless Framework to deploy the AWS resources for the pattern as specified in the serverless.yml file:

    ``` sh
    serverless deploy --verbose
    ```

    The above command will deploy resources to `us-east-1` region by default. You can override the target region with `--region <region>` CLI option, e.g.

    ``` sh
    serverless deploy --verbose --region us-west-2
    ```

1. Note the `ApiRootUrl` output from the Serverless Framework deployment process. You will use this value for testing.

## How it works

This pattern creates an Amazon API Gateway REST API that integrates with an Amazon DynamoDB table named "Music". The API includes an API key and usage plan. The DynamoDB table includes a Global Secondary Index named "Artist-Index". The API integrates directly with the DynamoDB API and supports [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html) and [Query](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html) actions.

## Testing

### API key value

Retrieve API Gateway API key value, so that you can provide the appropriate security context for the test messages:

``` sh
aws apigateway get-api-keys --region <region> --include-values --query "items[?name=='api-music-apikey'].value" --output text
```

### Sending a new test message to API Gateway endpoint

To test the endpoint first send data using the following command. Be sure to update the endpoint with endpoint of your stack.

``` sh
curl --location --request POST '<ApiRootUrl>/music' \
--header 'Content-Type: application/json' \
--header 'x-api-key: <api key from the previous step>' \
--data-raw '{
    "artist": "The Beatles",
    "album": "Abbey Road"
}'
```

Expected output:

```json
{}
```

``` sh
curl --location --request GET '<ApiRootUrl>/music/The+Beatles' \
--header 'x-api-key: <api key from the previous step>'
```

Expected output:

``` json
{
    "music": [
        {
            "id": "00000000-0000-0000-0000-000000000000",
            "artist": "The Beatles",
            "album": "Abbey Road"
        }
    ]
}
```

### DynamoDB data

You can validate test records being saved into the `Music` DynamoDB table with the following command (you can omit `--region` option if AWS CLI default region is `us-east-1` and you didn't override Serverless Framework default region by providing a custom `--region` option for `serverless deploy`):

``` sh
aws dynamodb scan --table-name Music --region <region>
```

## Cleanup

1. Delete the stack

    ```sh
    serverless remove --verbose
    ```

1. Confirm the stack has been deleted

    ```sh
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'apigw-rest-api-dynamodb-sls-v1')].StackStatus"
    ```

    Expected output

    ```json
    [
        "DELETE_COMPLETE"
    ]
    ```

    NOTE: You might need to add `--region <region>` option to AWS CLI command if you AWS CLI default region does not match the one, that you used for the Serverless Framework deployment.

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
