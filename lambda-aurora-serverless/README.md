# AWS Lambda and Amazon Aurora Serverless

This pattern creates an AWS Lambda function and an [Amazon Aurora MySQL database version 2 (with MySQL 5.7 compatibility)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.20Updates.html) in an [Aurora Serverless version 1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html) DB cluster with Data API and a Secrets Manager secret.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-aurora

For AWS Lambda with Aurora Serverless v2, please use [another pattern](https://serverlessland.com/patterns/lambda-aurora-serverlessv2-postgresql)

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
    cd lambda-aurora-serverless
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

This pattern creates an AWS Lambda function and an [Amazon Aurora MySQL version 2 (with MySQL 5.7 compatibility)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.20Updates.html) in an [Aurora Serverless version 1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html) DB cluster with Data API and a Secrets Manager secret. The function creates an example table named "music", inserts a row with data from the event object, then returns the results of a select query.

## Testing

Once the application is deployed, navigate to the Lambda function and configure a test event using the sample event available in this repo. Invoke the function to execute sql statements against the database. Modify the test event before subsequent invocations to insert new data into the example "music" table. Review the Amazon CloudWatch Logs for details on the function invocation.

After a period of inactivity the DB cluster may scale down, which is expected when using Aurora Serverless. If you attempt to invoke the function during this time, you may receive a "Communications link failure" error. Simply wait a few seconds and invoke the function again. In a production environment, retry logic is recommended.

Example test event:
```
{
  "body": {
    "artist": "The Beatles",
    "album": "Abbey Road"
  }
}
```

Response:
```
{
  "statusCode": 200,
  "body": "[{\"id\":1,\"artist\":\"The Beatles\",\"album\":\"Abbey Road\"}]"
}
```

## Documentation
- [Using the Data API for Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html)
- [Data API - ExecuteStatement](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ExecuteStatement.html)
- [Data API - ExecuteStatement Response Elements](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ExecuteStatement.html#API_ExecuteStatement_ResponseElements)
- [AWS Lambda - the Basics](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/aws-lambdathe-basics.html)
- [Lambda Function Handler](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/the-handler.html)
- [Function Event Object - Overview](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/the-event-object.html)
- [Function Environment Variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html)

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
