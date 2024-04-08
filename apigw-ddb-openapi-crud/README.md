# Amazon API Gateway to Amazon DynamoDB CRUD aplication using OpenAPI

This pattern creates a basic create, read, update, and delete (CRUD) REST API. The backend is purely API Gateway and DynamoDB and uses OpenAPI to create the API and connections.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-ddb-openapi-crud

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
1. Change directory to the pattern directory:
    ```
    cd apigw-ddb-openapi-crud
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Amazon API Gateway has the ability to transform incoming requests using [Apach Velocity Templating Language (VTL)](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-data-transformations.html) templates. Using vtl, this application builds a CRUD app to save a simple data object to a DynamoDB database.

## Testing

* After the application is deployed, grab the CrudApiUrl endpoint from the outputs. If you missed it, simple use the SAM list command to retrieve.
```
sam list outputs
```
* using Postman or another API tool send a POST to the endpoint with the following payload:
```
{
  "message": "Whatever you want to say"
}
```
* Using the returned ID, you can do a GET request to the endpoint `<endpoint>/<returned ID>` to fetch the record.
* Available emdpoints are:
  * < endpoint >:GET - lists all items
  * < endpoint >:POST - creates an item
  * < endpoint >/< id >:GET - retrieves one item
  * < endpoint >/< id >:PUT - updates one item
  * < endpoint >/< id >:DELETE - delete one item

Optionally, you can use [Artillery](https://www.artillery.io/) to load test the application. First ensure Artillery is installed then run:
```
artillery run load.yaml
```

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete --stack-name STACK_NAME
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
