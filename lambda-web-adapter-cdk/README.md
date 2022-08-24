# Lambda Web Adapter with Function URL

This pattern creates a Lambda function that is triggered by a Function URL.
The function contains a NodeJS application - lift and shift - that is wrapped using the Lambda Web Adapter.
Lambda Web Adapter is an open source project that allows you to wrap any HTTP web application with a Lambda function

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-web-adapter-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Node and NPM](https://nodejs.org/en/download/) installed
- [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:

   ```
   cd lambda-web-adapter-cdk
   ```

3. Install the node dependencies for the NodeJS application

   ```
   cd app/
   npm install
   ```

4. From the command line, use AWS CDK to deploy the AWS resources for the pattern:
   ```
   cdk deploy
   ```
5. During the prompts:

   - Allow CDK to create IAM roles with the required permissions.

6. Note the outputs from the CDK deployment process, as it contains the URL used for testing

## How it works

This pattern creates a Lambda function that is triggered by a Function URL.
The function code is a NodeJS application, you can see it in the `app` folder.
The function is wrapped using the Lambda Web Adapter.
Lambda Web Adapter is an open source project that allows you to wrap any HTTP web application with a Lambda function, learn more about is component in the [GitHub repository](https://github.com/awslabs/aws-lambda-web-adapter).

## Testing

After deploying the stack, put the URL that CDK returns into a browser: "Hi there!"
You should see a message back from the NodeJS app.

## Cleanup

Delete the stack

```
cdk destroy
```

---

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
