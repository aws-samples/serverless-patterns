# AWS AppSync: Ecommerce Starter

This pattern creates creates various stacks that can be used to create a sample ecommerce application. The core of this application is the AWS AppSync API that allows products to be created, and listed, and fetched individually.

**Stack Overview:**

- `AuthStack.ts`: Creates a Cognito userpool that allows email signups
- `FileStorageStack.ts`: Creates an S3 bucket and various IAM policies along with a Cloudfront Distribution. This houses product images.
- `IdentityStack.ts`: Creates a Cognito identity pool that authorizes both our API and our S3 bucket
- `APIStack.ts`: Creates an AppSync API to allow product creation.
- `DatabaseStack.ts`: Creates a single product table that will contain data about our products such a price, title, and description.

## How it works

When a request to create a `Product` is sent, it is first authorized with a JWT token from our Cognito userpool. If authorized, the product image is sent either directly to an S3 bucket or first to Cloudfront (depending on if the product is public, or private). The product data is sent to DynamoDB via our AppSync API.

**Important:** this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

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
   cd serverless-patterns/appsync-data-with-images
   ```
1. Install dependencies
   ```
   npm install
   ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```
   npx aws-cdk deploy
   ```

## Testing

The easiest way to test the AppSync API is with the AppSync console at https://us-west-2.console.aws.amazon.com/appsync/home (change to your appropriate region)

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted

```
npx aws-cdk destroy
```

---

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
