# Check S3 Object Tag Compliance Using CloudTrail, DynamoDB, and Lambda

This pattern shows how to leverage CloudTrail resource creation API calls to check for required S3 object tags and determine compliance. The resources used in this pattern include CloudTrail, S3, Lambda, and DynamoDB which are all deployed via CDK. From the CloudTrail logs stored in S3, PutObject events are populated into a DynamoDB table via Lambda. The items written into the table are then checked for the required tags to determine compliance. 

Learn more about this pattern at Serverless Land Patterns: https://github.com/aws-samples/serverless-patterns/tree/main/cloudtrail-lambda-dynamo-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
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
1. Open the lambda function object_tag_checker.py, and on line 40 replace the example keys with your required keys. These are the keys you require to be present on every S3 object created:
    ```
    required_keys = {"Key1", "Key2", "Key3", "Key4"}
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
1. Using the AWS CLI, upload the test_file.txt found in the src folder to the S3 bucket of your choosing using the following command:
    ```
    aws s3 cp test/test_file.txt s3://<bucket-name>
    ```
    If the file upload was successful, you should receive the following response:
    ```
    test/test_file.txt to s3://<bucket-name>/test_file.txt
    ```
    You can also open the AWS Management Console, navigate to S3, and confirm the uploaded file is found in the S3 bucket you specified.

    An alternative way to upload a file to a bucket is doing so via the AWS console: https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html 


1. Navigate to DynamoDB

1. Select the table created for this pattern

1. Click 'Explore table items'

1. Within a couple minutes, you should see a new item populated into the DynamoDB table specifying the ARN of the uploaded object. The ‘is_compliant’ column should be set to ‘false’ since the object was uploaded with no tags.

## Cleanup
 
1. Delete the stack
    ```
    cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0