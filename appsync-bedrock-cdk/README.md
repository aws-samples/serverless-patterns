# AWS AppSync to Amazon Bedrock

This pattern shows how to invoke Amazon Bedrock models from AppSync via HTTP resolvers.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/appsync-bedrock

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) (AWS CDK) installed
* Make sure to enable the **Anthropic - Claude V2** model on the [Bedrock console](https://console.aws.amazon.com/bedrock/home#/modelaccess).


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd appsync-bedrock-cdk
    ```

3. Install the required dependencies:
    ```
    npm install
    ```

4. Deploy the stack to your default AWS account and region:
    ```
    cdk deploy
    ```

## How it works

In this pattern the end user is able to provide a prompt that will be used to invoke an Amazon Bedrock model from within the JS resolver.
It is possible to augment the integration by adding functions in the pipeline resolver.

## Testing

Provide steps to trigger the integration and show what should be observed if successful.

1. Generate code for invoking the API (only if you changed the definition):
    ```
    npx @aws-amplify/cli codegen add --apiId <GraphQLApiID> --region <Region>
    ```

2. Input the API parameters in [backend.test.ts](test/backend.test.ts)
    ```ts
        Amplify.configure({
            aws_appsync_graphqlEndpoint:
            '<GraphQLApiURL>',
            aws_appsync_region: '<Region>',
            aws_appsync_authenticationType: 'API_KEY',
            aws_appsync_apiKey: '<GraphQLApiKey>'
        })
    ```

3. Run tests
    ```
    nom run test
    ```

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy --all
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0