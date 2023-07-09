# AWS Step Functions callback pattern using dotnet

In workflow based application execution, few steps require a pause and wait for the confirmation/approval from external sources, after getting confirmation it resumes or terminates the execution. To accomplish this, a callback pattern can be used where an AWS Step function pause during a task, and wait for an external process or command to return the task token, that was generated when the task started. This sample provides implementation of callback pattern for approval or confirmation step from external API/service with the help of Amazon S3, and AWS Lambda functions.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-csharp.html) (AWS CDK) installed

## Deployment Instructions

1. Clone this repository to your local machine.
2. Open a terminal window and navigate to the root directory of the project.
3. In Program.cs file under cdk project, either pass you AWS account id or set enviorment variable `CDK_DEFAULT_ACCOUNT` with aws account id.
   `
                Env = new Amazon.CDK.Environment
                {
                    Account = System.Environment.GetEnvironmentVariable("CDK_DEFAULT_ACCOUNT"),
                    Region = System.Environment.GetEnvironmentVariable("CDK_DEFAULT_REGION"),
                }
   `
4. Run `dotnet restore` to restore the NuGet packages.
5. Run `dotnet publish -c Release`
5. Run `cdk bootstrap` to create an S3 bucket in your AWS account to store the CDK toolkit stack.
5. Run `cdk deploy` to deploy the application stack to your AWS account.
 
 Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This is the architecture that this sample implements for callback pattern.
![callback-pattern-sample-architecture](https://github.com/aws-samples/serverless-patterns/tree/main/sfn-callback-pattern-cdk-dotnet/src/blob/callback-pattern.png)

1. User sends process order request.
2. API Lambda function validate request.
3. API Lambda trigger the setp function workflow.
4. API Lambda sends acknowledgement response to the user.
5. Process order task execution starts.
6. Execution paused and wait for confirmation API, invoke `storeTaskToken` lambda function.
7. `storeTaskToken` lambda function stores task token into S3 bucket.
8. User sends confirmation request to API.
9. API lambda validate confirmation request.
10. API lambda fetch task token from S3 for given request and sends task success to step functions.
11. As it gets `SendTaskSuccess`, it resumes the execution.
12. API lambda sends acknowledgement response to the user.
13. Starts complete order task\
\
***Note: To store task token you can use any kind of storage as Amazon S3/ DynamoDB or Any database, based on your scenario and cost considerations. You can use ECS Task (with Fargate) if task in Step function is taking more than 15 minutes as lambda function has 15 minutes per execution time limit.***


## Testing

After deployment, you will get API Gateway endpoint URL under outputs. You can use that URL to create the requests using Postman/Swagger or any other tool for REST APIs.

1. Process Order Request:\
Method: POST\
URL: {Your API Gateway endpoint URL}/OrderRequest/ProcessOrder\
Headers: x-api-key: {Take the same value that is passed in cdkstack.cs file under Deployment project in solution}\
Body:
    `{
    "OrderId":"2d6bfae2-c279-41d5-b59e-280b22733f9d",
    "OrderDetails":"order1"
    }`
2. Check the workflow execution in AWS Console, it must be Paused and waiting for confirmation.
3. Confirm/Complete Order Request:\
Method: POST\
URL: {Your API Gateway endpoint URL}/OrderRequest/CompleteOrder\
Headers: x-api-key: {Take the same value that is passed in cdkstack.cs file under Deployment project in solution}\
Body:
    `{
    "OrderId":"2d6bfae2-c279-41d5-b59e-280b22733f9d",
    "OrderDetails":"order1",
    "IsConfirmed":true
    }`

## Cleanup

Delete the stack

`cdk destroy`

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
