# AWS Lambda To AWS StepFunctions Express Workflow, with Amazon Cloudwatch Logs enabled - Create a Lambda function that an act as a proxy to transform data before invoking a Step Fucntions Express workflow
This pattern is a Lambda function asynchronously triggered when an object is uploaded to an S3 bucket. 

The SAM template deploys a Lambda function, an S3 bucket and the IAM resources required to ru the application. A Lambda function consumes `ObjectCreated` events from an Amazon S3 bucket. The Lambda code checks the uploaded file is an image and creates a thumbail version of the image in the same bucket.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-sfn.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS CLI already configured with Administrator permission
* [NodeJS 12.x installed](https://nodejs.org/en/download/)

## Deployment Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

1. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [install the AWS Serverless Application Model CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) on your local machine.

1. Create a new directory, navigate to that directory in a terminal and enter:
 ```
 git clone https://github.com/aws-samples/serverless-patterns

 cd lambda-sfn
 ```

4. From the command line, run:
```
sam deploy --guided
```
Choose a stack name, select the desired AWS Region, and allow SAM to create roles with the required permissions. Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

## How it works

* Use the AWS CLI upload an image to S3
* If the object is a .jpg or a .png, the code creates a thumbnail and saves it to the target bucket. 
* The code assumes that the destination bucket exists and its name is a concatenation of the source bucket name followed by the string -resized

==============================================

## Testing

Edit the sample event data in the `/events/inputFile.txt` File. Providing the sourcebucket name and a .jpg object key. Note the S3 bucket name is provided by the stack output after deployment.

### Success Testing

Run the following Lambda CLI invoke command to invoke the function. Note, you must edit the {LambdaProxyArn} placeholder with the ARN of the deployed Lambda function. This is provided in the stack outputs.

```bash
aws lambda invoke --function-name {LambdaProxyArn} --invocation-type Event --payload '{ "IsHelloWorldExample": "Hello" }' \ 
response.json --cli-binary-format raw-in-base64-out
```

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
