# AWS Service 1 to AWS Service 2

This pattern explains how to deploy a Data piepline with Amazon API Gateway (HTTP API), AWS Lambda and Amazon Redshift Serverless

This pattern is useful to accept and respond to requests quickly but offloading the processing as asynchronous process. Once the data ingestion / DDL / query request is made to the API Gateway HTTP API the query will be presented to Redshift Serverless workgroup through Redshift DataAPI. 

When an HTTP POST request (Synchronous / Asychronous) is made to the Amazon API Gateway endpoint, request payload is sent to AWS Lamdba function as event and the Lambda function connects to the Redshift Serverless workgropu via Data API to send the request to Redshift workgroup. Lambda function then responds back to API Gateway as query submitted during asynchronous invocation. Where as Lambda responds back with the result set during a synchronous invocation. 

Choose Asynchronous mode for ETL, Data ingestion operations like Copy command and use Synchronous mode to quickly get response for a query.

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
    cd apigw-lambda-redshift-serverless-dataapi
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Provide the DBName, Adminuser name, Admin Password, vpc, subnet CIDR details or accept the default values
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Allow No API authorization

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The API Gateway handles the incoming API requests and send the $request.body.MessageBody as an event to Lambda function. The Lambda fucntion extracts the Redshift serverless workgroup name, dbname and SQL Query  from the event request. Post a SQL Query request to the Redshift serverless workgroup as an API request using Redshift DataAPI. If invoked asynchronous responds back with the success status. In case of synchronous waits for the max_wait_cycle time given in request as seconds to get the result set to send as a response to the API Gateway request.

## Testing

1. Get the API URL from the output of SAM deploy (URL of your API endpoint)

2. Send a create table post request to the API URL copied in step 1 as provided below,
{
  "redshift_workgroup_name": "demowg",
  "redshift_database": "demo",
  "run_type": "synchronous",
  "sql_query": "CREATE TABLE IF NOT EXISTS public.region (R_REGIONKEY bigint NOT NULL,R_NAME varchar(25),R_COMMENT varchar(152)) diststyle all;",
  "max_wait_cycle": 30
}

3. Insert data to the table using below post request
{
  "redshift_workgroup_name": "demowg",
  "redshift_database": "demo",
  "run_type": "synchronous",
  "sql_query": "INSERT INTO public.region values(1,'India','APAC Region')",
  "max_wait_cycle": 30
}

4. Select the data from the table using below request
{
  "redshift_workgroup_name": "demowg",
  "redshift_database": "demo",
  "run_type": "synchronous",
  "sql_query": "select * from public.region",
  "max_wait_cycle": 30
}

5. You can change the run_type in the request to says "asynchronous" and submit queries for asynchronous invocation

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0