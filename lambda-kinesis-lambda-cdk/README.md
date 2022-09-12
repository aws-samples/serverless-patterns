# Serverless producer-consumer use case using AWS Lambda and AWS Kinesis Data Stream

This pattern creates two Lambda functions, one that puts data into the Kinesis Data Stream and another one that gets trigger when there is data in the stream.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-kinesis-lambda-cdk](https://serverlessland.com/patterns/lambda-kinesis-lambda-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [Python, pip, virtuenv](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Clone the project to your local working directory

   ```sh
   git clone https://github.com/aws-samples/serverless-patterns/ 
   ```

2. Change the working directory to this pattern's directory

   ```sh
   cd serverless-patterns/lambda-kinesis-lambda-cdk
   ```

3. Create and activate the project's virtual environment. This allows the project's dependencies to be installed locally in the project folder, instead of globally. Note that if you have multiple versions of Python installed, where the `python` command references Python 2.x, then you can reference Python 3.x by using the `python3` command. You can check which version of Python is being referenced by running the command `python --version` or `python3 --version`

   ```sh
    python -m venv .venv
    source .venv/bin/activate
   ```

4. Install the project dependencies

   ```sh
   python -m pip install -r requirements.txt
   ```

5. Deploy the stack to your default AWS account and region. 

   ```sh
   cdk deploy
   ```

## How it works

The CDK app deploys the resources and the IAM permissions required to run the application. 

## Testing

Log into the AWS Console, browse to AWS Lambda page to find your producer Lambda function:

1. Use the following dummy JSON payload to trigger your producer Lambda function:
    ```JSON
    {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    }
    ```
2. Observe the logs of the consumer Lambda function to verify if the data pushed by the producer is received or not.

## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.

```sh
cdk destroy
```

----
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. 

SPDX-License-Identifier: MIT-0