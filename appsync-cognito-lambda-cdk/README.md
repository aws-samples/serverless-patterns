# Authenticating an AppSync API using Amazon Cognito

This CDK template deploys an AWS AppSync API and a Cognito userpool.
You'll need to create a user in Cognito before being able to have authorized access to the API.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cognito-appsync-lambda-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/api/v2/) (AWS CDK) installed

## Deployment Instructions

1. Clone the ServerlessLand repository
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:

   ```
   cd ./serverless-patterns/cognito-appsync-lambda-cdk/
   ```

3. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `./cognito-appsync-lambda-cdk/lib/cognito-auth-cdk-stack.ts` file:

   ```bash
   npx aws-cdk deploy
   ```

## Testing

When our application was deployed, the `UserpoolId` was output to our terminal. We'll use that value to create a user in our Userpool by running the following command:

```bash
aws cognito-idp sign-up \
  --client-id <client-id> \
  --username <username> \
  --password <password> \
  --user-attributes Name=<attribute-name>,Value=<attribute-value>
```

Where:

- `client-id`: the app client ID of your user pool.
- `username`: the desired username for the new user.
- `password`: the password for the new user.
- `attribute-name`: the name of the user attribute to set, such as email or phone_number.
- `attribute-value`: the value to set for the user attribute.

Sign in to your AWS console and search for appsync. Open up appsync and click on your newly deployed project.

- Click on `Queries` on the left hand side menu to create and run the `getUserAccount` query with an API Key as the authorization mode.

- You should get an `unauthorized access` error.

This occurs because we applied the appsync directive `@aws_cognito_user_pools` to the Query endpoint in `schema.graphql`.
That appsync directive ensures that, that query can only be accessed by authenticated cognito users.

Sign in with the credentials you used when creating the user in cognito.
![alt text](./assets/cognito_5.png)

You'll be prompted to create a new password for the user
![alt text](./assets/cognito_6.png)

Once you've successfully logged in, run your query again, and you should successfully get a response.

Congratulations, you've successfully created and tested an authenticated appsync api.

## Cleanup

run the command `npx aws-cdk destory` from your local terminal.

---

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
