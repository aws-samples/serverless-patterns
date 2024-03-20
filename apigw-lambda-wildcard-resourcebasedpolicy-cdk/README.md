# Amazon API Gateway to AWS Lambda with wildcard resource-based policy

Create a REST API with proxy integration to a Lambda function to keep the size of resource-based policy within the allowed hard limit. Currently, in an API Gateway-Lambda setup whenever an user adds an integration, CDK adds a new policy to the Lambda function's resource-based policy. It might result in exceeding the policy size limit for Lambda function which is 20KB.",
This sample project demonstrates how to use CDK to create a customized integration that would keep the policy size within limit by using wildcards in the resource-based policy.
    

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-lambda-wildcard-resourcebasedpolicy-cdk](https://serverlessland.com/patterns/apigw-lambda-wildcard-resourcebasedpolicy-cdk)

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
   cd serverless-patterns/apigw-lambda-wildcard-resourcebasedpolicy-cdk
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

Log into the AWS Console, browse to Amazon API Gateway console to find REST API:

1. Verify the Lambda function integrated to the API resources.

2. Navigate to the function permissions option to validate its resource-based:
```JSON
    {
        "Version": "2012-10-17",
        "Id": "default",
        "Statement": [
            {
                "Sid": "CdkApigwLambdaWildCardPolicyStack-CDKFunction1BFFE2B32-wXxkAliuaQ0d",
                "Effect": "Allow",
                "Principal": {
                    "Service": "apigateway.amazonaws.com"
                },
                "Action": "lambda:InvokeFunction",
                "Resource": "arn:aws:lambda:us-east-1:01234567890:function:CdkApigwLambdaWildCardPolicySt-CDKFunction43C45D9B-pnj1nEvuxNCR",
                "Condition": {
                    "ArnLike": {
                        "AWS:SourceArn": "arn:aws:execute-api:us-east-1:01234567890:abcd1234/*/*/*"
                    }
                }
            }
        ]
    }
```

3. Invoke your API endpoint to validate that your function is getting invoked successfully. Your API should return this response which is sent by your funtion
```
Invoked Successfully
```

## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.

```sh
cdk destroy
```

----
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. 

SPDX-License-Identifier: MIT-0