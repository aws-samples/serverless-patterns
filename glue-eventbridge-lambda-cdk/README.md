
# Lambda to Amazon SQS (CDK) 

This pattern deploys a Spark Streaming AWS Glue Job, an EventBridge Rule and a Lambda Function that is triggered 
whenever the Glue Job times out.

The CDK application contains the minimum IAM resources required to run the application.

Learn more about this pattern at: https://serverlessland.com/patterns/glue-eventbridge-lambda-cdk

Important: this application uses various AWS services and there are costs associated with these services after the 
Free Tier usage - please see the AWS Pricing page for details. 
You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) (AWS CDK >= 2.42.1) Installed

## Language
Python

## Framework
CDK

## Services From/To
AWS Glue to AWS Lambda over Amazon EventBridge

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd glue-eventbridge-lambda-cdk
    ```
1. Create a virtual environment for python:
    ```bash
    python3 -m venv .venv
    ```
1. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

   If you are in Windows platform, you would activate the virtualenv like this:

    ```
    % .venv\Scripts\activate.bat
    ```

1. Install python modules:
    ```bash
    python3 -m pip install -r requirements.txt
    ```
   
   If the previous command doesn't work, try this one bellow:
   ```bash
   pip3 install -r requirements.txt
   ```
1. From the command line, use CDK to synthesize the CloudFormation template and check for errors:
    ```bash
    cdk synth
    ```
1. From the command line, use CDK to deploy the stack:
    ```bash
    cdk deploy
    ```
1. Note the output from the CDK deployment process. It contain the resources names and/or ARNs which are used for testing.

1. Run unit tests:

    ````bash
    python3 -m pytest
    ````


## How it works

The CDK stack deploys the resources and the IAM permissions required to run the application.

The AWS Lambda Function specified in the stack glue_eventbridge_lambda_cdk_stack.py will be triggered by the EventBridge Rule
whenever the AWS Glue Job times out.
To save time, the Timeout property of AWS Glue Job is set to 1 minute, so it is the time that need to be waited until the
Lambda Function been triggered after start the Glue Job.

The Glue Job script used is a simple Structured Spark Streaming example that will be running until it reaches the Glue Job timeout setting.

To learn more about AWS Glue in practical mode, search for Glue workshops here: https://www.workshops.aws


## Testing

Tests can be done using aws-cli or directly on the console. Follow the steps below to test from the command line.

1. After sucessfully deploying the stack, get the AWS Glue Job Name:

````
aws glue get-jobs --query 'Jobs[].Name'
````

2. Run AWS Glue Job

````
aws glue start-job-run --job-name '<replace by job name>'
````

3. After 1 minute, check the status of the last Glue Job run status. It must be: "JobRunState": "TIMEOUT" 
````
aws glue get-job-runs --job-name '<replace by job name>'
````

4. Go to CloudWatch Console and verify the lambda Log Group. You must see a Info log with the message "AWS Glue Job timeout successfully caught". It means that the Lambda Function was executed by the Event, after the Glue Job State has been changed to TIMEOUT.


## Cleanup

1. Delete the stack. You will see the message "GlueEventBridgeLambda: destroyed" at the end
    ```bash
    cdk destroy
    ```
1. You can confirm that the stack has been deleted by executing the command bellow
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```



## Tutorial
See [this useful workshop](https://cdkworkshop.com/30-python.html) on working with the AWS CDK for Python projects.

## Useful commands

* `cdk ls`          list all stacks in the app
* `cdk synth`       emits the synthesized CloudFormation template
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk docs`        open CDK documentation


Enjoy!
