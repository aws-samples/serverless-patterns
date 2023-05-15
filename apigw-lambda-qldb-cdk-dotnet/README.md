# Amazon API Gateway REST API with AWS Lambda proxy integration to Amazon QLDB

The CDK stack creates an Amazon API Gateway REST API endpoint with AWS Lambda function proxy integration.

Proxy integration creates a proxy resource with the greedy path `{proxy+}` and the method `ANY`.
This means that the REST API endpoint accepts any method and any path by default.

The Lambda used in this pattern is an ASP.NET Core Web API application that has been configured to allow Lambda and API Gateway to act as the web server instead of Kestrel.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-lambda-qldb-cdk-dotnet

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [.NET 6](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Clone the project to your local working directory
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change the working directory to this pattern's directory
    ```
    cd apigw-lambda-qldb-cdk-dotnet/src/cdk/src
    ```
3. Build the application
    ```
    dotnet build
    ```
4. Return one level back to the path `apigw-lambda-qldb-cdk-dotnet/src/cdk`
    ```
    cd..
    ```
5. Deploy the stack to your default AWS account and region. The output of this command should give you the REST API URL.
    ```
    cdk deploy
    ```

## Testing

### Create Table and Indexes

The `cdk deploy` step will create the QLDB ledger, but not the associated table and indexes. This could be done using another AWS Lambda function as a custom resource. For now, once the application is deployed, go into the QLDB console (or use the QLDB shell), and create a new table called Person:

```code
CREATE TABLE Person
```

Then create two indexes to improve performance

```code
CREATE INDEX ON Person (email)
CREATE INDEX ON Person (name)
```
### Create Person

1. Copy this URL and append `Person`, the URL will look like this: `https://<random-id>.execute-api.ap-south-1.amazonaws.com/prod/Person`
2. Copy the curl command below
```
curl --request POST \
  --url https://<random-id>.execute-api.us-east-1.amazonaws.com/prod/person \
  --header 'Content-Type: application/json' \
  --data '{
	"Email":"test@email.com",
	"Name": "Test Name"
}'
```

### Get Person

1. Copy this URL and append `Person`, the URL will look like this: `https://<random-id>.execute-api.ap-south-1.amazonaws.com/prod/Person`
2. Copy the curl command below
```
curl --request GET \
  --url https://<random-id>.execute-api.us-east-1.amazonaws.com/prod/person/{email}
```

## Cleanup
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
