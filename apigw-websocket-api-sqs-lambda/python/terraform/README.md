# Amazon API Gateway Websocket API to Amazon SQS to AWS Lambda

This pattern creates an Amazon API Gateway WebSocket API which sends inbound messages to an Amazon SQS FIFO queue. The queue is processed by an AWS Lambda function to return a result.

The queue acts as a buffer to alleviate traffic spikes and ensure your workload can sustain the arriving load by buffering all the requests durably. It also helps downstream consumers to process the incoming requests at a consistent pace. A FIFO (First-In-First-Out) queue is used to ensure that evens are processed in order of arrival.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-websocket-sqs-lambda-terraform.

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
    cd serverless-patterns/apigw-websocket-sqs-lambda-terraform
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

The API Gateway handles websocket message events by putting the message into a SQS FIFO (First-In-First-Out) queue. 
The SQS FIFO queue is used to ensure processing order of the websocket messages. The message payload must contain a "MessageGroupId" field which is used by SQS FIFO queue.
If message order is not required, a standard SQS queue can also be used and the message payload would not require the "MessageGroupId" field.
The API Gateway websocket request integration passes the connectionId and requestId as metadata and the message body as the payload. 
The Lambda function can now process the SQS FIFO requests in a batch manner (10 requests at a time) and send a response back to the websocket connection.

## Testing

Once the application is deployed, retrieve the `websocket_URI` value from outputs from terraform apply. To test the Websocket API, you can use [wscat](https://github.com/websockets/wscat) which is an open-source command line tool.

1. [Install NPM](https://www.npmjs.com/get-npm).

1. Install wscat:
    ```
    $ npm install -g wscat
    ```

1. Connect to your WebSocketURL by executing the following command:
    ```
    $ wscat -c <YOUR WEBSOCKET URL>
    ```

1. To test the SQS FIFO queue, send a JSON-formatted request like the following example. Note the MessageGroupId field which is required for the SQS FIFO queue. The SQS queue will be processed by the Lambda function which sends back a response:
```
$ wscat -c <YOUR WEBSOCKET URL>
connected (press CTRL+C to quit)
> {"MessageGroupId":"test", "data":"hello world"}
< {"connectionId":"<CONNECTIONID>","requestId":"<REQUESTID>","message":"{\"MessageGroupId\":\"test\",\"data\":\"hello world\"}"}
```

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigateway-rest-eventbridge-terraform
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

## Reference
- [Working with WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html)
- [Setting up a WebSocket API integration request in API Gateway ](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integration-requests.html)
- [Amazon SQS FIFO (First-In-First-Out) queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html)
- [AWS Lambda - the Basics](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/aws-lambdathe-basics.html)
- [Lambda Function Handler](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/the-handler.html)
- [Function Event Object - Overview](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/the-event-object.html)
- [Function Environment Variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html)

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
