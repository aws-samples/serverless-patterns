# Serverless ETL Pattern with AWS Glue and DynamoDB 

This AWS serverless pattern utilizes the Serverless Applicton Model (SAM) to deploy Glue scripts seamlessly, offering an efficient solution for managing multiple transformations. Users can focus on crafting their Glue scripts without worrying about the underlying infrastructure. This pattern will automatically configure and deploy the correct resources and permissions tailored to the user-specified data, such as the DynamoDB table where transformations will be performed and the associated script name. This approach provides users with a streamlined process to deploy their Glue scripts. 

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Python](https://www.python.org/downloads/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/sam-dynamodb-glue-transform/src
    ```
1. From the terminal, set your AWS account ID and default region environment variables:
    ```
    export ACCOUNT=<your-aws-account-id>
    export AWS_DEFAULT_REGION=<aws-region> (i.e us-east-1)
    ```

1. From the terminal, run the following commands to give `batch-orchestration-script.sh` and `run-job.sh` execution rights:
    ```
    chmod +x scripts/batch-orchestration-script.sh
    chmod +x scripts/run-job.sh
    ```

1. Install the toml library, if not already installed:
    ```
    pip3 install toml
    ```

1. Put the glue script you would like to deploy in the `glue_jobs` folder

1. Specify the data for the transformation in the method `class TransformationType` found in the `data/etl_data.py`, following the same format as the sample. 

1. Add an entry for your transformation in the method `def getTransformationByName` found in `data/etl_data.py`, following the same format as the sample. 

1. Deploy the stack using the following command:
    ```
    python3 main.py <script_name>
    ```

## Testing

1. From the terminal, create a sample DynamoDB table using the following command (this table will be used for testing): 
    ```
    aws dynamodb create-table \
        --table-name TestTable \
        --attribute-definitions \
            AttributeName=id,AttributeType=S \
        --key-schema \
            AttributeName=id,KeyType=HASH \
        --provisioned-throughput \
            ReadCapacityUnits=5,WriteCapacityUnits=5 \
        --table-class STANDARD
    ```

    If successful, you should see a similar response:
    ```
    {
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "id",
                "AttributeType": "S"
            }
        ],
        "TableName": "TestTable",
        "KeySchema": [
            {
                "AttributeName": "id",
                "KeyType": "HASH"
            }
        ],
        "TableStatus": "CREATING",
        "CreationDateTime": "2024-01-04T18:40:06.837000-05:00",
        "ProvisionedThroughput": {
            "NumberOfDecreasesToday": 0,
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        },
        "TableSizeBytes": 0,
        "ItemCount": 0,
        "TableArn": "arn:aws:dynamodb:<aws-region>:<account-id>:table/TestTable",
    :
    ```
    You can also navigate to DynamoDB in the AWS console to confirm TestTable is there.

1. From the terminal, enable point-in-time-recovery for the TestTable using the following command:
    ```
    aws dynamodb update-continuous-backups \
        --table-name TestTable \
        --point-in-time-recovery-specification PointInTimeRecoveryEnabled=true
    ```
    **NOTE: Point-in-time-recovery needs to be enabled on the DynamoDB table for this pattern to work**


1. From the terminal, we will populate TestTable with sample data with the following command:
    ```
    aws dynamodb put-item \
        --table-name TestTable  \
        --item \
            '{"id": {"S": "1"}, "firstName": {"S": "John"}, "lastName": {"S": "Doe"}, "birthday": {"S": "January 1, 1999"}}'

    aws dynamodb put-item \
        --table-name TestTable  \
        --item \
            '{"id": {"S": "2"}, "firstName": {"S": "Jane"}, "lastName": {"S": "Doe"}, "birthday": {"S": "April 1, 1990"}}'
    ```

    Take note of the data being added: id, firstName, lastName, and birthday

1. A sample glue script has been created for this test, `glue_jobs/transform_testtable.py`. And the necessary information has already been added to `data/etl_data.py`. 
    
    Under `def getTransformationByName`:
    ```
    if name == 'transform_testtable':
        return TransformationType['transform_testtable'].value
    ```
    Under `class TransformationType`:
    ```
    transform_testtable = Transformations(
        f"arn:aws:dynamodb:{os.getenv('AWS_DEFAULT_REGION')}:{os.getenv('ACCOUNT')}:table/TestTable",
        "transform_testtable",
        f"testtable-aws-glue-assets-{os.getenv('ACCOUNT')}-{os.getenv('AWS_DEFAULT_REGION')}"
    )
    ```

1. Time to deploy! In the terminal, run the following command:
    ```
    python3 main.py transform_testtable
    ```

    Once successfully deployed, the glue job will start running automatically. You should see a similar output:
    ```
    Successfully created/updated stack - TestTableStack in <aws-region>

    Running the Glue Job...
    {
        "JobRunId": "jr_1ddbec18fb4a0ccd58223d141751bad8491710c15a8c067b91a29a374c8e3434"
    }
    ```

1. Navigate to AWS Glue on the AWS console. Click on 'ETL jobs', and click on the transformation deployed by this stack 'TransformTestTable'

1. It may take a few minutes for the job to successfully run. But once successful, navigate to DynamoDB on the console, and view the items in the TestTable. You should see that 'birthday' has been renamed to 'dateOfBirth', and a new column 'fullName' was added.


You're all set to continue using this pattern for other Glue scripts! 

## Cleanup
 
1. Delete the TestTable
    ```
    aws dynamodb delete-table \
        --table-name TestTable
    ```
1. Delete the stack
    ```
    sam delete --stack-name TestTableStack
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0