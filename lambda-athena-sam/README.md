# Using Lambda function to start a query execution and fetch the results from an Athena database table.

This pattern creates a Lambda function that uses start_query_execution method to initiate query execution in an Athena table and then using get_query_results to fetch the results. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-athena

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* You must ensure that you have created a database and table in Athena either from console or using AWS Glue. Kindly refer to this document to know how to achieve it - [+] Creating tables in Athena - Creating tables using AWS Glue or the Athena console - https://docs.aws.amazon.com/athena/latest/ug/creating-tables.html#creating-tables-how-to
* Also, ensure that the S3 bucket that you are using has sufficient permissions granted in the Bucket policy.


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-athena-sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.
    
    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.
1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

1. Use the following JSON payload containing database name and queries along with S3 output location:
    ```JSON
    {
        "dbQuery":"SELECT * FROM <TABLE_NAME> limit 2;",
        "dbName": "<DB_NAME>",
        "s3OutputLocation": "s3://<BUCKET_NAME>/<PATH>/<TO>/<OUTPUT>/"
    }
    ```
2. Observe the logs of your function and verify if the expected data is returned by Athena or not.

## Cleanup

 1. For deleting the stack you can use sam delete from SAM CLI -
    ```
    sam delete
    ```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
