# Amazon API Gateway WebSocket API connection tracking using AWS Service integration type and Amazon DynamoDB

This pattern uses Amazon API Gateway WebSocket API and AWS Service integration type with Amazon DynamoDB for the connection tracking. This approach simplifies architecture by eliminating the need to use additional compute components such as AWS Lambda. 

Learn more about this pattern at Serverless Land Patterns: ["API Gateway WebSocket API connection ID tracking"](https://serverlessland.com/patterns/apigw-websocket-api-connection-dynamodb)

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
    cd apigw-websocket-api-connection-dynamodb
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

API Gateway forwards initial connection request to the \$connect route, along with headers and query string information. This pattern uses AWS Service integration and data transformation mapping templates to store WebSocket connection IDs in a DynamoDB table instead of a traditional approach that uses AWS Lambda functions to do that. Along with the connection ID in the DynamoDB, it stores headers and query string that are available at the connection time only. It also specifies Time to Live for the object (24 hours) to clean up failed connections if needed. 

In a similar way, $disconnect route uses AWS Service integration along with data transformation mapping templates to delete connection data from the DynamoDB when the client or the server disconnects from the API.

To implement sample business logic, this pattern uses AWS Lambda function as an integration target of the \$default route. It responds with the event data, performing no further actions.

Production implementation of this pattern would include a more complex business logics implementation. It would also read session data (headers, query string parameters) from the DynamoDB table to provide request context to the downstream resources. You can also use connection ID stored in the DynamoDB table in the [@connections command](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html) to send messages to the connected clients from the backend.

For extended examples of this pattern see [Serverless Samples repository](https://github.com/aws-samples/serverless-samples/tree/main/apigw-ws-integrations)

## Testing

To test this example, connect to the API Gateway WebSocket endpoint using the URL in the stack outputs and wscat (see [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-wscat.html) for more details how to set it up):

```bash
wscat -c "<API Endpoint from stack outputs>?foo=bar"
```

Send a payload to the API by typing it in. Lambda function will respond with the request details. For example:
```bash
> {"first_name" : "Jane", "last_name" : "Doe"}
< {
    "requestContext": {
        "routeKey": "$default",
        "messageId": "SOqIDdzSoAMCEeg=",
        "eventType": "MESSAGE",
        "extendedRequestId": "SOqIDEacoAMFaHQ=",
        "requestTime": "16/May/2022:17:30:27 +0000",
        "messageDirection": "IN",
        "stage": "api",
        "connectedAt": 1652722217711,
        "requestTimeEpoch": 1652722227357,
        "identity": {
            "sourceIp": "123.456.789.123"
        },
        "requestId": "SOqIDEacoAMFaHQ=",
        "domainName": "u9jlm1pv1h.execute-api.us-east-1.amazonaws.com",
        "connectionId": "SOqGjdZioAMCEeg=",
        "apiId": "u9jlm1pv1h"
    },
    "body": "{\"first_name\" : \"Jane\", \"last_name\" : \"Doe\"}",
    "isBase64Encoded": false
}
```

Note the connectionId field value. Open a new terminal window and check the DynamoDB item corresponding to this connection (use the DynamoDB table name in the stack outputs):

```bash
aws dynamodb get-item --table-name <DynamoDB table name from stack outputs> \
  --key '{"connectionid" : {"S":"<connection ID field value from the Lambda function response>"}}'

{
    "Item": {
        "connectionid": {
            "S": "SOqGjdZioAMCEeg="
        },
        "ttl": {
            "N": "1652722304111"
        },
        "querystring": {
            "S": "{foo=bar}"
        },
        "headers": {
            "S": "{Host=u9jlm1pv1h.execute-api.us-east-1.amazonaws.com, Sec-WebSocket-Extensions=permessage-deflate; client_max_window_bits, Sec-WebSocket-Key=oWaeekvolZlFevfyQ7SRRw==, Sec-WebSocket-Version=13, X-Amzn-Trace-Id=Root=1-62828a29-3824232936b70e2306c11218, X-Forwarded-For=123.456.789.123, X-Forwarded-Port=443, X-Forwarded-Proto=https}"
        }
    }
}

```

Disconnect from the WebSocket API and try to get the same DynamoDB item again. It should be deleted automatically and the command should not return any result.

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
