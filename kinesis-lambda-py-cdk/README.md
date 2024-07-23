# Amazon Kinesis Data Stream trigger AWS Lambda function with CDK

This pattern creates a Kinesis Data Stream that is added as an event source to AWS Lambda function.

Learn more about this pattern at Serverless Land Patterns: <live url to be added>

Important: This application uses various AWS services and there are costs associated with these services after the Free Tier usage. Please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK >= 2.1.0) installed


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```
   cd serverless-patterns/kinesis-lambda-py-cdk
   ```
3. Create a virtual environment for Python:
   ```
   python3 -m venv .venv
   ```
4. Activate the virtual environment :
   ```
   Linux : source .venv/bin/activate
   Windows : .venv\Scripts\activate.bat
   ```
5. Install the Python required dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Review the CloudFormation template the cdk generates for you stack using the following AWS CDK CLI command:
   ```
   cdk synth
   ```
7. From the command line, use AWS CDK to deploy the AWS resources for the serverless application as specified in the app.py file:
   ```
   cdk deploy
   ```
8. Note the outputs from the CDK deployment process. These contain the API Gateway ID which is used for testing.

## How it works

This pattern creates a Kinsesis Data stream and a Lambda function. The data stream is then added as an event source which can trigger the Lambda function.

## Testing

From the command line, run the following command to send a single data record to the Kinesis data stream. Note that you must edit the <stream_arn> with the Kinesis data stream ARN that is deployed which will be provided in the stack deployment outputs.

```
aws kinesis put-record --stream-arn <stream_arn> --partition-key 123 --data testdata
```

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.

```
cdk destroy
```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
