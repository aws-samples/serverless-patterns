# Multi-Tenant Serverless API

This project demonstrates a pattern for building a multi-tenant serverless API using API Gateway, Lambda, and DynamoDB, with tenant based access control. Requests are authorized using API keys mapped to tenants in DynamoDB. Access to data is restricted using dynamic IAM policies based on the tenant ID. This is not a production ready implementation of a multi-tenant API and only serves as a demo to illustrate the pattern.

## Architecture

The project contains the following resources:

- API Gateway REST API
- Lambda authorizer  - Looks up the tenant ID from the API key and generates IAM policies  
- Lambda GET function - Retrieves items by ID after validating the tenant ID
- Lambda POST function - Adds new items after validating the tenant ID
- DynamoDB tables - Stores tenant data isolated by partition keys with the tenant ID

The Lambda functions assume IAM roles with temporary credentials to access the tenant's data partition.

## Setup

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/serverless-multi-tenant-api
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the workflow as specified in the template.yaml file:

    ```
    npm install
    sam build
    sam deploy --guided
    ```

This will build and deploy the Lambda functions, API Gateway API, and DynamoDB tables.
The API endpoint will be output after deployment. You can test the endpoint with valid API keys and tenant IDs stored in DynamoDB.

Steps to set up a tenant in the ConfigTable DynamoDB table with the generated API Key:

1. Get the DynamoDB table name and API key value using the stack name you created :
      aws cloudformation describe-stacks --stack-name `your-stack-name` \
          --query 'Stacks[0].Outputs[?OutputKey==`DynamoDBTableName`].OutputValue' \
          --output text

1. Get the API key name
     aws cloudformation describe-stacks --stack-name `your-stack-name` \
          --query 'Stacks[0].Outputs[?OutputKey==`TestApiKeyOutput`].OutputValue' \
          --output text

1. Use the API key output from above step to get the API key value :
    aws apigateway get-api-key --api-key `your-api-key-id` --include-value --query "value" --output text


1. Run the following command to put the sample tenant TENANT1 in DynamoDB table :
    aws dynamodb put-item \
        --table-name `your-dynamodb-table` \
        --item ' {
                "PK": {
                  "S": "`<your-api-key-value>`"
                },
                "TENANT_ID": {
                  "S": "TENANT1"
                }
              }' \
          --return-consumed-capacity TOTAL
## Testing Locally

To test locally, run:

```
sam local start-api
```

This will spin up a local API Gateway instance on port 3000. You can test routes by passing x-api-key headers mapped to tenants in your local DynamoDB tables. 

Or test using curl:

1. POST - post item (id and name)
  `curl -X POST -H "x-api-key: <the value of your api key>"  -d '{"id":"id1","name":"name1"}' <your WebEndpoint>`
   A successful POST request returns the following response:
    `{"id":"id1","name":"name1"}`
  
1. GET - get item by id  
  `curl -X GET  -H "x-api-key: <the value of your api key>" <your WebEndpoint>/id1`
  A successful GET request returns the value of `id` saved earlier by the same tenant:
    `{"id":"id1","name":"name1"}`

## Implementation Details

Key files and components:

- template.yaml - Defines the API, Lambda functions, DynamoDB tables  
- auth.js - Authorizer function to lookup tenant ID and create IAM policy
- get-by-id.js - GET function to retrieve items by ID 
- put-item.js - POST function to add new items
- DynamoDB tables - Config and items tables to store tenants and data

The authorizer function demonstrates how to implement granular access control per tenant for a multi-tenant architecture on AWS.

## Cleanup 

To delete the sample application:

```
sam delete
```
