# AppSync Lambda Bedrock Streaming Pattern for Long-running Invocations

This pattern demonstrates how to implement [long-running invocations](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-bedrock-js.html#long-running-invocations)  with Amazon Bedrock using AWS AppSync subscriptions and AWS Lambda, following the official AWS AppSync documentation pattern.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/appsync-lambda-bedrock-async-stream-subscription-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) (AWS CDK) installed
* Make sure to enable the **Anthropic - Claude V2** model on the [Bedrock console](https://console.aws.amazon.com/bedrock/home#/modelaccess).

## How it works

The pattern implements an asynchronous [streaming architecture](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-bedrock-js.html#long-running-invocations) where:

1. Client initiates a WebSocket subscription and makes a request to AppSync
2. AppSync invokes Lambda function in Event mode
3. Lambda function streams responses from Bedrock using ConverseStream
4. Lambda sends updates via mutations to AppSync
5. Updates are delivered to client through WebSocket subscription

![alt text](image.png)

This pattern is ideal for:
- Long-running AI model invocations
- Real-time streaming responses
- Asynchronous processing patterns
- Progressive UI updates

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
```sh
git clone https://github.com/aws-samples/serverless-patterns
```
2. Change directory to the pattern directory:
```sh
cd appsync-lambda-bedrock-async-stream-subscription-cdk
```

3. Install the required dependencies:
```sh
npm install
```

4. Deploy the stack to your default AWS account and region:
```sh
npm run deploy
```

## Testing

After deployment, you can test the Bedrock streaming integration using the provided test script. The script demonstrates:
- WebSocket subscription initialization
- Conversation start with Bedrock
- Real-time streaming chunks display
- Graceful cleanup on exit

Run the test script using:
```sh
npx tsx test/test.ts  
```

You should see output similar to:
```sh
Starting subscription...
Starting conversation...
StartConversation response: {
data: {
startConversation: {
conversationId: '123e4567-e89b-12d3-a456-426614174000',
status: 'STARTED'
}
}
}
Received chunk: {
conversationId: '123e4567-e89b-12d3-a456-426614174000',
chunk: "Here's a joke for you: Why don't scientists trust atoms? Because they make"
}
Received chunk: {
conversationId: '123e4567-e89b-12d3-a456-426614174000',
chunk: 'up everything!'
}
```
## Cleanup
 
1. Delete the stack
```sh
cdk destroy --all
```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
