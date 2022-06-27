# AWS Step Function to Amazon S3

This CDK  pattern creates a Step Functions workflow that publishes a file to an S3 bucket.

Learn more about this pattern at Serverless Land Patterns: (https://serverlessland.com/patterns/cdk-sfn-s3)

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
     cd cdk-sfn-s3
     ```
 3. Install dependencies:
     ```
     npm install
     ```
 4. This project uses typescript as client language for AWS CDK. Run the given command to compile typescript to javascript:
     ```
     npm run build
     ```
 5. Synthesize CloudFormation template from the AWS CDK app:
     ```
     cdk synth
     ```
 6. Deploy the stack to your default AWS account and region. The output of this command should give you the StepFunctions State Machine ARN.
     ```
     cdk deploy
     ```
 8. Note the outputs from the CDK deployment process. These contain the ARN of StepFunctions State Machine.

## How it works

The AWS CDK  template deploys a Step Functions workflow that performs the specified task of putting the object onto the S3 bucket.


## Testing

Use the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) to invoke the step function. The function name is in the outputs of the AWS CDK deployment

 1. Execute the Step Functions workflow:
    ```
    aws stepfunctions start-execution --state-machine-arn ENTER_YOUR_STATE_MACHINE_ARN
    ```
 2. View S3 bucket to see files created in the previously empty bucket: You should see a file has been saved to the S3 bucket:
     ```
     aws s3 ls my-sfn-bucket-destination
     2022-06-06 14:53:12         17 filename.txt
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
