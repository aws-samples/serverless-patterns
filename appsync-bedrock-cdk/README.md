# AWS AppSync to Amazon Bedrock

This pattern shows how to invoke Amazon Bedrock models from AppSync via HTTP resolvers.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/appsync-bedrock-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) (AWS CDK) installed
* Make sure to enable the **Anthropic - Claude V2** model on the [Bedrock console](https://console.aws.amazon.com/bedrock/home#/modelaccess).

## How it works
In this pattern the end user is able to provide a prompt that will be used to invoke an Amazon Bedrock model from the JS resolver.
It is possible to augment the integration by adding functions in the pipeline resolver and change the invoked model by inserting the relative inference parameters in the JS resolver.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
```sh
git clone https://github.com/aws-samples/serverless-patterns
```
2. Change directory to the pattern directory:
```sh
cd appsync-bedrock-cdk
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

Run tests
```sh
npm run test
```

## Cleanup
 
1. Delete the stack
```sh
cdk destroy --all
```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0