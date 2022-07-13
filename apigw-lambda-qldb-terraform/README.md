# Amazon API Gateway to AWS Lambda to Amazon QLDB

This pattern shows how to deploy a SAM template with Amazon API Gateway, AWS Lambda and Amazon Quantum Ledger Database (QLDB). The API Gateway exposes a REST API with a number of methods. Each API method uses a Lambda proxy integration to invoke a separate AWS Lambda function that interacts with a ledger in Amazon QLDB. This allows you to create a new Person record, update the record, delete the record, view the current state of the record, and view the entire revision history.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

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
    cd apigw-lambda-qldb
    ```
1. From the command line, use AWS SAM to build the serverless application with its dependencies
    ```
    sam build
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

1. Note the outputs from the SAM deployment process. This contains the API Gateway endpoint URL required for testing

## How it works

The `sam template` creates the QLDB ledger, API Gateway REST API with the relevant API methods, and the AWS Lambda functions.

* The API Gateway endpoint is publically accessible
* You call the relevant API method passing in the appropriate data
* The API method defined in the API Gateway will pass the request on to an AWS Lambda function set up for proxy integration
* The AWS Lamba function has the least privilege permissions configured
* The AWS Lambda function uses the `QLDB Driver` to interact with the ledger in QLDB 

## Testing

### Create Table and Indexes

The `sam deploy` step will create the QLDB ledger, but not the associated table and indexes. This could be done using another AWS Lambda function as a custom resource. For now, once the application is deployed, go into the QLDB console (or use the QLDB shell), and create a new table called Person:

```code
CREATE TABLE Person
```

Then create two indexes to improve performance

```code
CREATE INDEX ON Person (personId)
CREATE INDEX ON Person (email)
```

### Create Person record

Create a new Person record using the `curl` command or a tool such as `Postman`. This requires an HTTP POST to the endpoint which ends `/Prod/person` passing in the body in JSON format:

```json
{
    "firstName":"Matt", 
    "lastName":"Lewis", 
    "email":"matt@example.com",
    "address":"1 Test Address"
}
```

The `curl` command for this is shown below:

```code
curl --location --request POST <your API endpoint> \
--header 'Content-Type: application/json' \
--data-raw '{
    "firstName":"Matt", 
    "lastName":"Lewis", 
    "email":"matt@example.com",
    "address":"1 Test Address"
}'
```

The response includes a `personId` which is the unique ID for the document created in QLDB. Make a note of this identifier.

### Update Person record

Update the address attribute for the Person record just created. This requires an HTTP POST to the endpoint which ends `/Prod/person/<personId>` passing in the new address in the body in JSON format:

```json
{
    "address":"2 Test Address"
}
```

The `curl` command for this is shown below:

```code
curl --location --request POST <your API endpoint> \
--header 'Content-Type: application/json' \
--data-raw '{
    "address":"1 Test Address"
}'
```

### View Current State

Retrieve the current status of the Person record by making an HTTP GET call to the endpoint which ends `/Prod/person/<personId>`. The `curl` command for this is shown below:

```code
curl --location --request GET <your API endpoint> \
--header 'Content-Type: application/json'
```

### View History

Retrieve the full history of all changes made to the Person record by making an HTTP GET call to the endpoint which ends `/Prod/person/history/<personId>`. The `curl` command for this is shown below:

```code
curl --location --request GET <your API endpoint> \
--header 'Content-Type: application/json'
```

This will return all document revisions. Each document consists of four parts. The `blockAddress` tells you the location of the block in the ledger's journal. The `hash` is the SHA-256 generated hash covering the `data` and `metadata` sections. The `data` section contains the user data. The `metadata` section contains the system-generated metadata

```json
[
    {
        "blockAddress": {
            "strandId": "5kelavToIcrB1Tv53EEZXg",
            "sequenceNo": 19
        },
        "hash": "0j0rPn5Bp3jGnv+EPmSDHteQivmZE2Jx4l8LJ+IPiVk=",
        "data": {
            "firstName": "Matt",
            "lastName": "Lewis",
            "email": "matt@example.com",
            "address": "1 Test Address",
            "personId": "Dzd7ggQD4qEJLp2ht4luw4"
        },
        "metadata": {
            "id": "Dzd7ggQD4qEJLp2ht4luw4",
            "version": 0,
            "txTime": "2022-01-01T23:06:50.051Z",
            "txId": "30Iytfs7xx6A81lnOHse6S"
        }
    },
    ...
]
```

### Delete Person record

Delete the Person record by making an HTTP DELETE call to the endpoint which ends `/Prod/person/<personId>`. The `curl` command for this is shown below:

```code
curl --location --request DELETE <your API endpoint> \
--header 'Content-Type: application/json'
```

This will delete the record from the current state view, but you will still be able to view the full revision history.

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
