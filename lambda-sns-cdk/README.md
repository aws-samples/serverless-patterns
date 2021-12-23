
# Lambda to Amazon SNS (CDK) 

This pattern deploys an SNS Topic and a Lambda Function that will send a custom message to the topic once triggered.
The CDK application contains the minimum IAM resources required to run the application.

Learn more about this pattern at: https://serverlessland.com/patterns/lambda-sns-cdk

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
AWS Lambda to Amazon SNS

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```bash
    cd lambda-sns-cdk/src
    ```
3. Create a virtual environment for python:
    ```bash
    python3 -m venv .venv
    ```
4. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

   If you are in Windows platform, you would activate the virtualenv like this:

    ```
    % .venv\Scripts\activate.bat
    ```

5. Install python modules:
    ```bash
    python3 -m pip install -r requirements.txt
    ```
   
   If the previous command doesn't work, try this one bellow:
   ```bash
   pip3 install -r requirements.txt
   ```
6. From the command line, use CDK to synthesize the CloudFormation template and check for errors:
    ```bash
    cdk synth
    ```
7. From the command line, use CDK to deploy the stack:
    ```bash
    cdk deploy
    ```
8. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.



## How it works

The CDK stack deploys the resources and the IAM permissions required to run the application.

The SNS topic specified in the stack app.py will be the target of the Lambda Function. The function reads the event to determine which SNS topic will receive the message body.


## Testing

Tests can be done using aws-cli or directly on the console. Follow the steps below to test from the command line.


1. Invoke the lambda function with a sample message

````
aws lambda invoke --function-name <FUNCTION_NAME> --cli-binary-format raw-in-base64-out --payload '{ "topic_arn": "<TOPIC_ARN>", "message": "Hello, SNS topic!" }' response.json"
````

2. A successful publish to the topic will cause the Lambda to return a 200 status code. Go to CloudWatch and verify the related Log Group. You should see an Info level log with a success message and the Message ID of the successfully published payload.



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
