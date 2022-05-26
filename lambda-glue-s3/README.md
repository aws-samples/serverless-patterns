# AWS Lambda workflow to integrate with AWS Glue Job using CDK

This CDK application deploys a Lambda function, that takes in a payload and trigger a AWS Glue job synchronously. The glue job then performs the assigned task to convert a CSV file to Parquet and uploads the output file in S3. The application contains the minimum IAM resources required to run the workflow and Glue job.

Learn more about this pattern at Serverless Land Patterns: (https://serverlessland.com/patterns/lambda-glue-s3)

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
     cd lambda-glue-s3
     ```
 3. Create a virtual environment for python: 
     ```
     python3 -m venv .venv
     ```
 4. Activate the virtual environment: 
     ```
     source .venv/bin/activate
     ```
 5. Install python modules:
     ```
     python3 -m pip install -r requirements.txt
     ```
 6. From the command line, use CDK to synthesize the CloudFormation template and check for errors:
     ```
     cdk synth
     ```
 7. From the command line, use CDK to deploy the stack: 
     ```
     cdk deploy
     ```
 8. Note the outputs from the CDK deployment process. These contain the lambda ARN , Glue Job Name and S3 Bucket Name which are used for testing.

## How it works

The CDK stack deploys the resources and the IAM permissions required to run the application. This stack will deploy S3 bucket to store glue job scripts, csv file which will be used as input for file conversion in Glue job.

Lambda supports AWS Glue through the service integration pattern. Lambda task defined in the app.py triggers the glue job in handler function and wait for job completion before transitioning to next step.

Task the glue job needs to perform is documented in script.py where we are converting a csv file to parquet file and storing the output file in s3 bucket.

## Testing

Use the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) to invoke the Lambda function. The function name is in the outputs of the AWS CDK deployment

 1. Invoke the Lambda function to start the AWS Glue job:
    ```
    aws lambda invoke --function-name ENTER_YOUR_FUNCTION_NAME --payload '{}' /tmp/response.json
    ```
 2. Check the status of the AWS Glue job and wait for the status to be SUCCEEDED
     ```
     aws glue get-job-runs --job-name "ENTER_YOUR_GLUE_JOB_NAME"
     ```
 3. List down the files present in S3 bucket for find the csv converted file with .parquet format
     ```
     aws s3 ls s3://ENTER_YOUR_S3_BUCKET_NAME --recursive --human-readable --summarize
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