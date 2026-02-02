# Amazon Cognito to AWS Lambda to Amazon DynamoDB

This pattern demonstrates how to create a user in [Amazon Cognito](https://aws.amazon.com/cognito/), handle a **Post Confirmation** trigger using an [AWS Lambda](https://aws.amazon.com/lambda/) function, and store user details in [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). Specifically, when a user signs up and confirms their account in Cognito, the Lambda function automatically writes that user's information to a DynamoDB table.

Learn more about this pattern at Serverless Land Patterns: **<< Add the live URL here >>**

> **Important**: This application uses various AWS services and there are costs associated with these services after the Free Tier usage. Please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

---

## Requirements

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user/role that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
2. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured.
3. [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
4. [Node.js](https://nodejs.org/en/download/) (10.x or higher).
5. [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed (e.g., `npm install -g aws-cdk`).
6. [Docker](https://docs.docker.com/get-docker/) is recommended if you need to bundle Lambda dependencies in certain ways (though for this TypeScript example, it may not be strictly necessary).

---

## Deployment Instructions

1. **Clone the GitHub Repository**  
   Create a new directory, navigate to that directory in a terminal, and clone the **serverless-patterns** GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns.git
   ```
2. Change directory to the pattern directory:
   ```
   cd serverless-patterns/cognito-lambda-dynamodb/cdk
   ```
3. Install Dependencies:

   ```
   npm install
   ```

4. Synthesize the AWS CloudFormation Templates:

   ```
   cdk synth
   ```

5. Deploy the Stack
   ```
   cdk deploy
   ```
6. Note the Outputs

   After deployment, CDK provides outputs such as the UserPoolId and UserPoolClientId. Make sure to save these for reference. They may be required for testing or client-side integration

## How it works

### Cognito User Pool

    - A new Amazon Cognito User Pool is created. Users can sign up using their email address. An optional User Pool Client is also created to handle authentication flows.

### Post Confirmation Trigger

    - When a user signs up and confirms their email, Cognito invokes the Post Confirmation Lambda function (AddUserPostConfirmationFunc).

### AWS Lambda Handler

    - The Lambda function reads attributes from the event (such as sub [the unique user ID], email, and optional name attributes). It then inserts a new item into the DynamoDB table.

### DynamoDB Table

    - A DynamoDB table named Users is created with a primary key called UserID. The Lambda function stores user data (UserID, Email, firstName, lastName, etc.) in this table with each new sign-up.

### Result

    - Whenever a new user confirms their email in Cognito, an entry is automatically created in the DynamoDB table with that user's information.

## Testing

## Option 1: Manual Sign-Up through Cognito

1. In the Amazon Cognito Console:

- Navigate to **User Pools** and select the **USER-POOL** that was created.
- Choose the **Users** section and manually create a new user or do a user sign-up using the **Hosted UI** or any relevant client (e.g., AWS Amplify).
- After confirming the user, check the **Users** table in Amazon DynamoDB Console to see if the new record appears.

## Option 2: Automated Testing with Jest (E2E Tests)

This project includes an end-to-end test in `cdk/__tests__/e2e/confirm-user-sign-up.test.ts`. By default, the test references environment variables in `cdk/__tests__/constants.ts`. Steps:

1. Populate `REGION`, `USER_POOL_ID`, `CLIENT_USER_POOL_ID`, and `TABLE_NAME` in `cdk/__tests__/constants.ts` (or set them as environment variables before running tests if you prefer).
2. Run:

```bash
npm run test
```

This will perform a sign-up flow using AWS SDK for Cognito, confirm the new user, and then query DynamoDB to validate that the user entry exists.

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```
1. Confirm the stack has been deleted
   ```bash
   aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
   ```

---

Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
