# AWS Service 1 to AWS Service 2

This pattern << explain usage >>

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd serverless-patterns/apigw-rest-api-dynamodb-lambda-proxy
   ```
1. Download the APIGWLambdaProxy.yml file within the folder
1. Navigate to the CloudFormation console and select create a stack with new resources

   - For Prerequisite, select template is ready
   - Upload the APIGWLambdaProxy.yml file as the template, click next
   - Create a name for the CloudFormation stack deployment, click next
   - On the configure stack options page, click next
   - Under the capabilities and transforms section, read/acknowledge and click all of the check boxes.
   - Submit

1. Note the outputs from the CloudFormation deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern creates a Simple Serverless REST API that is configured with Lambda Proxy Integration. Once deployed, this pattern allows a user to perform CRUD operations on a Dynamo DB table. In addition, this pattern allows users to pass input and receive responses directly to/from the back-end Lambda function; eliminating the need to configure integration request/integration response methods for the API. The pattern creates the following resources: An API GW with API endpoint, a Lambda function, a DynamoDB table, and a Lambda/DynamoDB IAM Role.

The 3 functions that this architecture revolves around are: POST, DELETE, and GET Methods. Those methods link a lambda function which maps the to the DynamoBD commands: update_item, delete_item, get_item.

## Testing

Upload the template to CloudFormation.

Post/Update_item: This method can be used to update an existing item in the dynamo table or upload a new one

Go to the Api Gateway command for POST
ID: input a new ID to upload a new item or an existing ID to update an existing item
Description: Add a body field for both Description and ProductName
NOTE: This architecture revolves around having a request body which includes the ProductName and Description fields in the body. To change this, the lambda function can be changed
Verification: Check API Gateway response and the Dynamo table for the new/updated item
Delete/delete_item: This method can be used to delete an existing item in the dynamo table

Go to the Api Gateway command for Delete
ID: Input the ID of the item you want to delete
Verification: Check the API Gateway response and Dynamo Table for the Deleted Item
Get/get_item: This method can be used to get the description an existing item in the dynamo table

Go to the Api Gateway Command for GET
ID: input the ID for an existing item you want to get the data for
Verification: Check API Gateway response for the item description

## Cleanup

1. Navigate to the CloudFormation console
   - Delete the stack.

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
