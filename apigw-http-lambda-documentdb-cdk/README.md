# Amazon API Gateway to AWS Lambda to Amazon DocumentDB 

This AWS CDK stack deploys an API Gateway HTTP API that integrates with a Lambda function and a DocumentDB cluster. The Lambda function is connected to the DocumentDB cluster through a VPC. The Lambda implements the CRUD operations function for this REST API.

You should use this pattern if you want to migrate your application to DocumentDB using a serverless REST API application layer


Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
* [Node and NPM](https://nodejs.org/en/download/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
```bash
git clone https://github.com/aws-samples/serverless-patterns
```
1. Change directory to the pattern directory:
```bash
cd apigw-http-lambda-documentdb-cdk
```
1. run npm install to install npm packages:
```bash
npm install
```    
1. From the command line, configure AWS CDK with
```bash
cdk bootstrap
```  
6. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/cdk-stack.ts` file:
```bash
cdk deploy
```
## How it works

This will create an API Gateway HTTP API, a Lambda function, and a DocumentDB cluster. The output of the command will include the URL of the API Gateway HTTP API.

### Usage
To use the API Gateway HTTP API, send a GET request to the root path (/). The Lambda function will be invoked and will return the contents of the DocumentDB cluster.

### Example
1. **GET** - Retrieve data from the MongoDB collection.:
```bash
curl -X GET "YOUR_API_ENDPOINT" -H "CONTENT-TYPE: application/json"
```
2. **POST**  - Insert data into the MongoDB collection.:
```bash
curl -X POST "YOUR_API_ENDPOINT" -H "CONTENT-TYPE: application/json" -d '{"key": "value"}'
```
3. **PUT** - Update data in the MongoDB collection.:
```bash
curl -X PUT "YOUR_API_ENDPOINT" -H "CONTENT-TYPE: application/json" -d '{"_id": "id", "key": "newvalue"}'
```
4. **DELETE** - Delete data from the MongoDB collection.:
```bash
curl -X DELETE "YOUR_API_ENDPOINT"?id=id
```

### Security
The Lambda function is granted access to the DocumentDB cluster through a VPC security group. The security group only allows traffic from the Lambda function to the DocumentDB cluster.

The Lambda function is also granted access to the AWS Secrets Manager secret for the DocumentDB cluster. The secret contains the credentials for accessing the DocumentDB cluster.

### Troubleshooting
If you are having trouble deploying or using the stack, please refer to the following resources:

AWS CDK documentation: https://docs.aws.amazon.com/cdk/latest/guide/
DocumentDB documentation: https://docs.aws.amazon.com/documentdb/latest/developerguide/
Lambda documentation: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html

## Testing

Provide steps to trigger the integration and show what should be observed if successful.

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0