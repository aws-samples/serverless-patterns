# AWS pattern for S3 to SQS to Lambda and DynamoDB

This CDK pattern creates a serverless data processing workflow using Amazon S3, Amazon SQS, AWS Lambda and Amazon DynamoDB.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

## Deployment Instructions

 1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
 2. Change directory to the pattern directory:
     ```
     cd cdk-s3-sqs-lambda-dynamodb
     ```
 3. Install dependencies:
     ```
     npm install
     ```

 4. Synthesize CloudFormation template from the AWS CDK app:
     ```
     cdk synth
     ```
 5. Deploy the stack to your default AWS account and region. This command should deploy the serverless workflow to your AWS account.
     ```
     cdk deploy
     ```
 6. Browse to the AWS cloudformation console to verify successful deployment of the stack

## How it works

1. The AWS CDK  template deploys S3 bucket, SQS queue, lambda and DynamoDB table 
2. SQS queue is configured to listen to s3 create object events
3. Lambda function is configured to read messages from the SQS queue, process messages and insert records into the DynamoDB table named EmployeeInfo.

## Testing

Use the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) to invoke the step function. The function name is in the outputs of the AWS CDK deployment

 1. Upload the sample csv file from data folder to the s3 bucket name from the output of cloudformation stack
    ```
    s3 cp ./data/test.csv s3://BUCKET_NAME/test.csv
    ```
 2. View S3 bucket to see files created in the previously empty bucket: You should see a file has been saved to the S3 bucket:
    ```
    Verify the Lambda function CloudWatch logs for successfull processing of csv file
    Verify the DynamoDB table that the expected record was inserted
    ```

## Cleanup

 1. Delete the stack
    ```
    cdk destroy
    ```
 2. Confirm the stack has been deleted
    ```
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'ENTER_STACK_NAME')].StackStatus"
    ```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
