# AWS AppSync to Amazon DynamoDB - Single table design

This pattern creates an AppSync API with a schema and a resolver to a DynamoDB table following the single table design model.

Learn more about this pattern at ServerlessLand Patterns: https://serverlessland.com/patterns/appsync-dynamodb-singletable

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd serverless-patterns/appsync-dynamodb-singletable-cdk/cdk
   ```
1. Install dependencies
   ```
   npm install
   ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```
   npx aws-cdk deploy
   ```

## How it works

This template creates an AppSync api that uses a DynamoDB resolver. The `getParentAndChildren` resolver demonstrates using a custom resolver to format results from a single table design for AppSync.

## Testing

The easiest way to test the AppSync API is with the AppSync console at https://us-west-2.console.aws.amazon.com/appsync/home (change to your appropriate region)
![AppSync Console](./console.png)

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted

```
cdk destroy
```

---

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
