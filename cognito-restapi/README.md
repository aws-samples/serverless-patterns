# Amazon API Gateway REST API with Cognito User Pools Authorizer

The SAM template deploys an Amazon API Gateway REST API endpoint that uses a Cognito User Pools Authorizer for access control. 
It assumes that the Cognito User Pool already exists and takes the Cognito User Pool ARN as an input parameter which must be provided by the user.


Note: when deploying this pattern, *CAPABILITY_IAM* is required.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-cognito-authorizer-sam-nodejs](https://serverlessland.com/patterns/apigw-cognito-authorizer-sam-nodejs)

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
    cd cognito-restapi
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy -g
    ```
1. During the prompts:
    * Enter a stack name
    * Select the desired AWS Region
    * Enter an existing Cognito User Pools ARN.
    * Allow SAM to create roles with the required permissions if needed.

    Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

Generate an identity token from your Cognito User Pool to use in the HTTP request. Next, note the **api endpoint** in the stack outputs. Use *curl* to make an HTTP request to the API Gateway endpoint that includes a Header with the identity token.
   
```
curl -i https://{apiId}.execute-api.{region}.amazonaws.com/Prod -H "authorizationToken: {tokenProvidedByCognito}"
```

will successfully return a 200 HTTP code and the event object from the Lambda integration in the response body.

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
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0