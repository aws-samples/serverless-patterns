# DynamoDB Stream to AWS Lambda with Filters 

This pattern demonstrates how to Lambda functions that be trigger by DynamoDB streams based on filters. The IaC has been definied in Terraform. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/dynamodb-streams-lambda-filters-tf

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform Installed](https://developer.hashicorp.com/terraform/downloads)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory and the terraform directory:
    ```
    cd dynamodb-streams-lambda-filters-tf/tf
    ```
1. From the command line, run the following command to initializes terraform:
    ```
    terraform init
    ```
1. From the command line, run the following command to cerate terraform execution plan:
    ```
    terraform plan
    ```
1. From the command line, run the following command to excute the deployment:
    ```
    terraform apply
    ```

    > ** if choose skip the confirmation prompt, use -auto-approve

## How it works

A DynamoDB stream triggers different Lambda functions based on a filter. The stack has one DynamoDB table with 4 functions with selective filters:

1. Bachelors Lambda (process-bachelors-request) - Triggers for every insert of Bachelors Record
2. Masters Lambda (process-masters-requests) - Triggers for every insert of Masters Record
3. Modify Lambda (process-modify-request) - Triggers for any updates
4. Delete Lambda (process-delete-request) - Triggeres for any remove

## Testing

1. Test Bachelors Lambda delivery by inserting new record using the following command,
    
    ```
    aws dynamodb put-item --table-name students_table --item '{"request_id": {"S": "stu_101"},"degree": {"S": "Bachelors"},"verified": {"N": "1"}}'
    ```
2. Test Masters Lambda delivery by inserting new record using the following command,
    ```
    aws dynamodb put-item --table-name students_table --item '{"request_id": {"S": "stu_201"},"degree": {"S": "Masters"},"verified": {"N": "0"}}'
    ```
3. Test Modify Data deliver by updaing the record in DynamoDB using the following command,
    ```
    aws dynamodb update-item --table-name students_table --key '{"request_id": {"S": "stu_101"}}' --update-expression "set #attribute_name = :attribute_value" --expression-attribute-names '{"#attribute_name":"verified"}' --expression-attribute-values '{":attribute_value":{"N":"0"}}' --return-values ALL_NEW
    ```
4. Test Delete Data deliver by delete the record in DynamoDB using the following command,
    ```
    aws dynamodb delete-item --table-name students_table --key '{"request_id": {"S": "stu_201"}}'
    ```

## Cleanup
 
1. From the command line, run the following command to delete the stack:
    ```
    terraform destroy
    ```
    > ** if choose skip the confirmation prompt, use -auto-approve

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
