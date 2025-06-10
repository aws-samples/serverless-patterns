# Amazon API Gateway, AWS Lambda and Amazon Aurora DSQL

 Amazon Aurora DSQL is the fastest serverless, distributed SQL database with active-active high availability and multi-Region strong consistency. Aurora DSQL enables you to build always available applications with virtually unlimited scalability, the highest availability, and zero infrastructure management. It is designed to make scaling and resilience effortless for your applications and offers the fastest distributed SQL reads and writes.

This pattern deploys a API Gateway REST API, Lambda function and an Aurora DSQL PostgreSQL cluster.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/apigw-lambda-dsql)

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
    cd apigw-lambda-dsql
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region (verify which [regions Aurora DSQL is available in](https://aws.amazon.com/rds/aurora/dsql/faqs/))
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This sample project demonstrates how to use a Lambda function (invoked by API Gateway), that stores and retrieves data from an Amazon Aurora DSQL PostgreSQL cluster.

## Testing

Use the `Value` from `UsersApi` URL output from the above `sam deploy` command to invoke the API Gateway API, e.g:
`curl https://abc123.execute-api.eu-west-1.amazonaws.com/Prod/users/`
which should return with
`{"id": "e3ce23b5-c6a1-4289-bb02-2f34a2f7b956", "name": "John", "city": "LA", "telephone": "555-555-0150"}`

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
