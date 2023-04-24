# AWS EventBridge Pipes from DynamoDB Stream To API Gateway with AWS Integration to Iot Core

This project contains a sample AWS Cloud Development Kit (AWS CDK) template for deploying a DynamoDb Table with a Stream configured to an EventBridge. The Pipe will detect the Stream payload and target an API Gateway endpoint that uses AWS direct integration to publish the stream change to a pre-configured Iot Core Topic

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-pipes-ddb-stream-apigateway-iot-core-cdk.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```bash
   cd serverless-patterns/eventbridge-pipes-ddb-stream-apigateway-iot-core-cdk/cdk
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. From the command line, configure AWS CDK:
   ```bash
   cdk bootstrap ACCOUNT-NUMBER/REGION # e.g.
   cdk bootstrap 9999999999/us-east-1
   cdk bootstrap --profile test 9999999999/us-east-1
   ```
5. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/cdk-stack.ts` file:
   ```bash
   cdk deploy
   ```
6. Note: The AWS CDK deployment process will output the DynamoDB table name, the API endpoint and the Iot Core Topic name used for testing this project

## How it works

This pattern follows a _functionless_ approach to achieve a full-circle event propagation, and report the change back to the client.

- A DynamoDB Table that stores data and configured with a DDB Stream
- An EventBridge Pipe configured as a target for the DDB Stream
- A REST Api configured as a target for the EventBridge Pipe
- The REST Api configures a path `iot` with a POST request and an AWS Direct Service Integration to Iot Data
- An Iot Core Topic & Iot Core Endpoint to publish data to

Iot Core is an AWS service that covers a wide verity of use cases. One important feature that can be leveraged in serverless event driven architectures, is the scalable pub/sub topic based api.

NOTICE: the pattern doesn't use AWS Lambda at any stage to propagate the data change

**_Disclaimer:_** This pattern doesn't favor one architectural pattern over another. It is merely an example of using _functionless_ development with Iot Core

## Testing

Go to the AWS Iot Core Console -> `MQTT test client` -> Under `Subscribe to a topic` enter the {topicName} into the topic filter -> hit `Subscribe`
Run the following DynamoDB CLI put command to put an item in the DynamoDB table. Note, you must edit the {TableName} placeholder with the Name of the deployed DynamoDB table. This is provided in the stack outputs. Note that this requires AWS CLI v2.

```bash
aws dynamodb put-item \
--table-name "DYNAMODB_TABLE_NAME" \
--item file://inputFilePath.json \
--return-consumed-capacity TOTAL \
--return-item-collection-metrics SIZE \
response.json

# Example 1
aws dynamodb put-item \
    --table-name MusicCollection \
    --item file://item.json \
    --return-consumed-capacity TOTAL \
    --return-item-collection-metrics SIZE \
response.json

# Example 2
aws dynamodb put-item \
    --table-name MessagesTable \
    --item PK={S="MESSAGE#1234"},SK={S="CHANNEL#1231"},messageId={S="1234"}
response.json
```

Wait for the change propagate through the various AWS services and a message on iot topic will be published with the item detail

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```

---

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
