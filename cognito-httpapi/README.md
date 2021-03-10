# Amazon Cognito to Amazon API Gateway HTTP APIs (JWT)

The SAM template deploys a nested stack with authentication configured using Cognito. It also deploys an HTTP API configured with a JWT authorizer based on the Cognito configuration and a Lambda function on a secure route.
Note: when deploying this pattern, both *CAPABILITY_AUTO_EXPAND* and *CAPABILITY_IAM* are required.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/cognito-to-httpapi](https://serverlessland.com/patterns/cognito-to-httpapi)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS CLI already configured with Administrator permission
* [NodeJS 14.x installed](https://nodejs.org/en/download/)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

1. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [install the AWS Serverless Application Model CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) on your local machine.

1. Create a new directory, navigate to that directory in a terminal and enter ```git clone https://github.com/aws-samples/serverless-patterns```.

1. Change directory to this pattern.

1. From the command line, run:
```
sam deploy -g --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM
```
* Choose a stack name
* Select the desired AWS Region
* Enter a ckient domain
* Enter an AppName
* For **TestWithPostman**, set this to true for local development and testing only. Do not enable for production as it allows implicit grant OAuth flow that is less secure.
* Allow SAM to create roles with the required permissions.

Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

* Note the outputs from the SAM deployment process. These contain the resource names and ARNs.

## Testing

The stack will output the **authorization domain** and **client id** required for using authorization via postman. Configure postman authorization as follows:

![Postman authentication](https://serverlessland.s3.amazonaws.com/assets/patterns/patterns-cognito-httpapi1.png)

1. The first time you get a new token, click **Sign Up** on the bottom of the hosted URL

    ![Postman authentication](https://serverlessland.s3.amazonaws.com/assets/patterns/patterns-cognito-httpapi2.png)
2. Retrieve code from your email
3. After verifying the code you can login and then be returned to postman with the proper access token.

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0