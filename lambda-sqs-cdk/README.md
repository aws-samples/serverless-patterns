
# Lambda to Amazon SQS (CDK) 

This pattern deploys a SQS Queue and a Lambda Function that once triggered will send a message to the Sqs Queue.
The CDK application contains the minimum IAM resources required to run the application.

Learn more about this pattern at: https://serverlessland.com/patterns/lambda-sqs-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) (AWS CDK >= 1.124.0) Installed

## Language
Python

## Framework
CDK

## Services From/To
AWS Lambda to Amazon SQS

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd lambda-sqs-cdk
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
1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

1. Run unit tests:

    ````bash
    python3 -m pytest
    ````


## How it works

The CDK stack deploys the resources and the IAM permissions required to run the application.

The SQS Queue specified in the stack lambda_sqs_cdk_stack.py will be the target of the Lambda Function. The function extracts the event and send it as message payload and log it if success or not. Just for demonstration, the body can be a simple string message like "test message".


## Testing

Tests can be done using aws-cli or directly on the console. Follow the steps below to test from the command line.

1. After sucessfully deploying the stack, get the Lambda Function Name:

````
aws lambda list-functions --query "Functions[].FunctionName" --output text
````

2. Invoke lambda function with a sample message

````
aws lambda invoke --function-name <Replace by function name> --cli-binary-format raw-in-base64-out --payload '{ "msg": "test" }' response.json"
````

3. Go to CloudWatch and verify the related Log Group. You must see a Info log with the message payload.

4. Alternatively you can retrieve the message from SQS using aws cli. First get SQS Queue URL:
````
aws sqs get-queue-url --queue-name LambdaToSqsQueue
````

5. Receive the message
````
aws sqs receive-message --queue-url ENTER_YOUR_QUEUE_URL
````


## Cleanup

1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
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
