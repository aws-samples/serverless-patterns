# S3 Triggered Lambda Function that starts an Amazon Translate Job and stores result into another S3 bucket
This repo contains serverless patterns showing how to setup a Lambda with an S3 *object created* trigger that starts a basic, Amazon Translate Job. The result is placed into another S3 bucket.

![Demo Project Solution Architecture Diagram](architecture.png)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS Account
* AWS CLI already configured with Administrator permission
* [NodeJS 14.x installed](https://nodejs.org/en/download/)
* CDK v2 installed: See Getting Started With the AWS CDK
* Python CDK required libraries: (install with pip install -r requirements.txt)
* Clone this repo!

## Deployment Instructions

1. Within your CDK Python module directory(where all your cdk stacks are located) create a constructs folder and within the constructs folder, create an assets folder.
2. Place the `lambda_s3_translate_cdk.py` file in the constructs folder you created and then place the lambda_function.py file in the assets folder you created.
3. In your terminal run `CDK Deploy` for the specified stack that uses this construct

### Removing the resources

1. run `cdk destroy <stack id>` for the specified stack that used this construct

```
git clone https://github.com/aws-samples/serverless-patterns/lambda-s3-translate-cdk
```

Each subdirectory contains additional installation and usage instructions. 

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.
----

