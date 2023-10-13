# AWS AppSync to Amazon Bedrock

This pattern shows how to invoke Amazon Bedrock models from AppSync through HTTP resolvers.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/appsync-bedrock

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
2. Change directory to the pattern directory:
    ```
    cd appsync-bedrock
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region (choose a region where [Amazon Bedrock](https://aws.amazon.com/bedrock/) is currently available)
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

## How it works

In this pattern the end user is able to provide a query and a role. Based on the role provided (philosopher, schoolteacher or politician), a specific context will be added to the prompt used to invoke an Amazon Bedrock model from within the JS resolver.

## Testing

1. Visit the [AppSync on the AWS Console](https://console.aws.amazon.com/appsync/home#/apis) in the region you deployed this sample in.
2. Select the AppSync API called AppSyncToBedrockApi
3. From the left pane, click on **Queries**
4. Fill in the following query and run it:
   ```graphql
    mutation MyMutation {
        invokeModel(query: "How is bread baked?", role: "schoolteacher") {
            output
        }
    }
   ```
   In this query we are providing the schoolteacher role. The expected output should take this role into consideration.

5. Now let's run the same query with a **philosopher** role.
    ```graphql
    mutation MyMutation {
        invokeModel(query: "How is bread baked?", role: "philosopher") {
            output
        }
    }
   ```
   The result is noticably different and matches the response a philosopher might give to the given question.

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0