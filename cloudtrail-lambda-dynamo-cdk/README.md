# Check Resource Tag Compliance Using CloudTrail, DynamoDB, and Lambda

This pattern shows how to leverage CloudTrail resource creation API calls to check for required tags and determine compliance. The resources used in this pattern include CloudTrail, S3, Lambda, and DynamoDB which are all deployed via CDK. From the CloudTrail logs stored in S3, the relevant resource creation events are populated into a DynamoDB table via Lambda. The items written into the table are then checked for the required tags to determine compliance. 

Learn more about this pattern at Serverless Land Patterns:[Create an AWS account](https://serverlessland.com/patterns/cloudtrail-lambda-dynamodb-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS 
s.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js installed](https://nodejs.org/en/download)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK) v2 installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/cloudtrail-lambda-dynamo-cdk/src
    ```
1. Run the following command to install the required project dependencies
    ```
    npm install
    ```
1. Use the following command to generate the AWS CloudFormation template for your CDK application:
    ```
    cdk synth
    ```
1. Use the following command to deploy the AWS resources for this pattern into your AWS account:
    ```
    cdk deploy
    ```
## Testing

Once the CDK stack has deployed successfully, you can take the following steps to ensure the pattern is working appropriately:
1. Using the AWS CLI, create a bucket using the following command:
    ```
    aws s3api create-bucket --bucket {bucket-name} --region {your AWS region}
    ```
    If the S3 bucket creation was successful, you should receive the following response:
    ```
    {
        "Location": "/{bucket-name}"
    }
    ```
    You can also open the AWS Management Console, navigate to S3, and confirm the created bucket is listed there.

1. Navigate to DynamoDB

1. Select the table created for this pattern

1. Click 'Explore table items'

1. Within about 5 minutes or less, you should see a new item populated in the DynamoDB table specifying the ARN of the newly created bucket. The 'is_compliant' column should be set to 'false' since the bucket was created with no tags. 

## Cleanup
 
1. Delete the stack
    ```
    cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
