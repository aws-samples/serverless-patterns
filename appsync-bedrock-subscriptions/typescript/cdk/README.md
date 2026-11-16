# Stream Amazon Bedrock completions via AWS AppSync Subscriptions

This pattern shows how to stream Amazon Bedrock completions via AWS AppSync Subscriptions.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/appsync-bedrock-subscriptions-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.


## Requirements
* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) (AWS CDK) installed
* Access to **Anthropic Claude Haiku 5.5** in Amazon Bedrock. The first time you use an Anthropic model in an account, submit the Anthropic use case form from the model catalog in the [Bedrock console](https://console.aws.amazon.com/bedrock/home#/model-catalog).
* Deploy in a Region that supports the `global.anthropic.claude-haiku-5-5` [global cross-Region inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/global-cross-region-inference.html), for example us-east-1. Bedrock can route requests from this profile to any supported Region. To keep requests in one geography, change `MODEL_ID` and the IAM policy in [lib/backend-stack.ts](lib/backend-stack.ts) to a geographic profile such as `us.anthropic.claude-haiku-5-5` or `eu.anthropic.claude-haiku-5-5`.


## How it works
![diagram](assets/diagram.png)
1. The Client subscribes to `chat` and performs the `ask` mutation passing the prompt as an argument via its API KEY;
2. The [Lambda Resolver](src/ask.ts) takes the input prompt and calls the Bedrock [ConverseStream API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) with the AWS SDK for JavaScript v3;
3. The prompt is sent to Claude Haiku 5.5 through its global inference profile;
4. The Lambda receives multiple completion chunks in a stream;
5. The Lambda performs the `send` mutation every time it receives a new completion chunk from Bedrock;
6. The `send` mutation is attached to a Local Resolver;
7. The [Local Resolver](src/send.js) simply returns the input data;
8. The client receives the completion data in chunks via the `chat` subscription.


### Permissions and Security
* Every GraphQL operation requires a `chatId` argument that is used to uniquely identify the chat session;
* The GraphQL [schema](src/schema.gql) uses [multiple authorization types](https://aws.amazon.com/blogs/mobile/using-multiple-authorization-types-with-aws-appsync-graphql-apis/) to ensure that:
  * The Client is only able to perfom the `ask` mutation and the `chat` subscription via its API_KEY;
  * The Lambda is only able to perform the `send` mutation via IAM.
* The Lambda role can stream only from the Claude Haiku 5.5 inference profile, and from the model only when the request comes through that profile.



## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
```sh
git clone https://github.com/aws-samples/serverless-patterns
```
2. Change directory to the pattern directory:
```sh
cd appsync-bedrock-subscriptions/typescript/cdk
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
Open the AWS Management console and use the API KEY authentication method to subscribe to the `chat` subscription by providing the `chatId` parameter:
![Subscription-before](assets/subscription-before.png)

Run tests with jest. `test/backend.test.ts` calls the deployed API using `cdk-outputs.json`, and `test/backend-stack.test.ts` checks the synthesized template:
```sh
npm run test
```

The completion chunks will appear one by one in the console:
![Subsription-after](assets/subscription-after.png)

## Cleanup
 
Delete the stack:
```sh
cdk destroy --all
```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
