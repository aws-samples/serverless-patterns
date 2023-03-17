# AWS AppSync to MongoDB

This project demonstrates how to connect directly to a MongoDB Atlas cluster using AWS Appsync. Connecting directly to MongoDB requires the use of their Data API and AppSync's HTTP resolver. In doing so, there is no need for a proxying Lambda function.

Learn more about this pattern at Serverless Land Patterns: https://github.com/aws-samples/serverless-patterns/appsync-mongodb

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:

   ```
   cd ./serverless-patterns/appsync-mongodb/cdk
   ```

3. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `./appsync-mongodblib/cognito-auth-cdk-stack.ts` file:

   ```bash
   npx aws-cdk deploy
   ```

## How it works

Using AWS AppSync's pipeline resolvers (written in JavaScript), a request is made to AWS Secrets Manager. This request grabs the API Key needed for MongoDB. Once successful, an API request is made to MongoDB.

For detailed steps on setting up a MongoDB Atlas Cluster, testing and configuring it with AppSync so that a frontend application can make use of it, it's highly recommended to follow the blog post titled, [The fullstack guide to using AWS AppSync and MongoDB Atlas](https://aws.amazon.com/blogs/mobile/the-fullstack-guide-to-using-aws-appsync-and-mongodb-atlas/)

## Cleanup

```bash
npx aws-cdk destroy
```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
