# Amazon API Gateway to AWS Lambda to Amazon DocumentDB 

This AWS CDK stack deploys an API Gateway HTTP API that integrates with a Lambda function and a DocumentDB cluster. The Lambda function is connected to the DocumentDB cluster through a VPC. The Lambda implements the CRUD operations function for this REST API.

You should use this pattern if you want to migrate your application to DocumentDB using a serverless REST API application layer.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-http-lambda-documentdb-cdk

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
2. Change directory to the pattern directory:
```bash
cd apigw-http-lambda-documentdb-cdk
```
3. run npm install to install npm packages:
```bash
npm install
```    
4. From the command line, configure AWS CDK with:
```bash
cdk bootstrap
```  
5. From the command line, use AWS CDK to deploy the AWS resources for the pattern:
```bash
cdk deploy
```
## How it works

This will create an API Gateway HTTP API, a Lambda function, and a DocumentDB cluster. The output of the command will include the URL of the API Gateway HTTP API.

### Security
The Lambda function is granted access to the DocumentDB cluster through a VPC security group. The security group only allows traffic from the Lambda function to the DocumentDB cluster.

The Lambda function is also granted access to the AWS Secrets Manager secret for the DocumentDB cluster. The secret contains the credentials for accessing the DocumentDB cluster.

### Troubleshooting
If you are having trouble deploying or using the stack, please refer to the following resources:

AWS CDK documentation: https://docs.aws.amazon.com/cdk/latest/guide/

DocumentDB documentation: https://docs.aws.amazon.com/documentdb/latest/developerguide/

Lambda documentation: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html

Amazon API Gateway HTTP documentation: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html

## Testing

To use the API Gateway HTTP API, send a GET request to the root path (/). The Lambda function will be invoked and will return the contents of the DocumentDB cluster.

In the stack output, you can see `ApiGatewayUrl`. This URL can be used with the curl commands below to interact with the DocumentDB.

### Example
1. **GET** - Retrieve data from the DocumentDB collection:
```bash
curl -X GET "YOUR_API_ENDPOINT" -H "CONTENT-TYPE: application/json"
```
2. **POST**  - Insert data into the DocumentDB collection:
```bash
curl -X POST "YOUR_API_ENDPOINT" -H "CONTENT-TYPE: application/json" -d '{"key": "value"}'
```
3. **PUT** - Update data in the DocumentDB collection:
```bash
curl -X PUT "YOUR_API_ENDPOINT" -H "CONTENT-TYPE: application/json" -d '{"_id": "A_VALID_ID_FROM_THE_DATABASE", "key": "newvalue"}'
```
4. **DELETE** - Delete data from the DocumentDB collection:
```bash
curl -X DELETE "YOUR_API_ENDPOINT?id=A_VALID_ID_FROM_THE_DATABASE"
```

## Cleanup
 
Delete the stack

```bash
cdk destroy
```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
