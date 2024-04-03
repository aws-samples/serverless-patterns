# Create S3 Presigned URL with API Gateway and Lambda Authorizer to allow URL access only once.

This pattern demonstrates how to create an S3 Presigned URL with API Gateway and Lambda Authorizer to allow URL access only once for security reasons. Implemented in CDK.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-s3presigned-nonce-api

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Python 3.x Installed](https://www.python.org/) Python 3.x installed with pip.
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-s3presigned-nonce-api
    ```
3. Manually create a Python virtualenv on MacOS and Linux:

   ```bash
   $ python3 -m venv .venv
   $ source .venv/bin/activate
   ```

   Windows:

   ```powershell
   python3 -m venv .venv
   .venv\Scripts\activate.bat
   ```

4. Once virtualenv is activated, install dependencies:

   ```bash
   $ pip install -r requirements.txt
   ```

5. Bootstrap AWS account (if not already done):

   ```bash
   cdk bootstrap aws://ACCOUNT-NUMBER/REGION
   # e.g.
   cdk bootstrap aws://1111111111/us-west-2
   cdk bootstrap --profile test 1111111111/us-west-2
   ```

6. Deploy the stack to your default AWS account and region. The output of this command contains the WebSocket API URL.

   ```bash
   cdk deploy
   ```
      Enter y when prompted:
      Do you wish to deploy these changes (y/n)? y
   
## How it works

This pattern deploys an API that can be used for generation of a presigned URL that is only accessible once. The presigned url is saved to a dynamo db table along with the nonce value. Upon access, the nonce is deleted and the url is no longer accessible via API that is sent to the customer.


## Testing

1. In the stack output, you get an `PreSignedURLStack.ApiGatewayEndpoint` and an S3 bucket name `PreSignedURLStack.BucketUrl`. 

2. Create a POST request to the following url as an IAM authenticated user, you get the access-object endpoint along with the nonce:

      API URL : https://<APIendpoint>/generate-url 
      Payload : {"bucket_name":"<bucketname>", "object_name":"S3.png"}

      You get response in the form of a URL that can be used once to access the object : https://<APIendpoint>/access-object?nonce=<the-unique-object-nonce>

3. Access the object once using the access-object URL - it is available only once while the nonce is active.
   Access it again - it is not available.

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to delete.

```bash
cdk destroy
```
---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
