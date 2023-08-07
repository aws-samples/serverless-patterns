# Accessing Amazon SageMaker Endpoint via API Gateway and Lambda

This pattern deploys a SageMaker Jumpstart model (Flan T5 XL) endpoint. It also adds a Lambda function and API Gateway integration to query the endpoint

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-lambda-sagemaker-jumpstartendpoint-cdk-python

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Python, pip, virtualenv](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK >= 2.2.0) Installed

## Deployment Instructions

1. Clone the project to your local working directory

   ```sh
   git clone https://github.com/aws-samples/serverless-patterns
   ```

2. Change to the pattern directory:
    ```sh
    cd serverless-patterns/apigw-lambda-sagemaker-jumpstartendpoint-cdk-python
    ```
3. Create and activate the project's virtual environment. This allows the project's dependencies to be installed locally in the project folder, instead of globally. Note that if you have multiple versions of Python installed, where the `python` command references Python 2.x, then you can reference Python 3.x by using the `python3` command. You can check which version of Python is being referenced by running the command `python --version` or `python3 --version`

   ```sh
    python3 -m venv .venv
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

6. The default instance count for inference is set to 1. The instance count can be changed by passing the instance_count_param. 

   ```sh
   cdk deploy --context instance_count_param=2
   ```


## How it works

1. This pattern deploys a SageMaker Jumpstart model (Flan T5 XL from HuggingFace) endpoint using Amazon SageMaker. The model can be changed by modifying the ```MODEL_ID``` attribute in app.py file.

2. The pattern also adds a lambda and an API Gateway query the endpoint.

3. The API Gateway is protected using an API Key. To query the Api Gateway, ```x-api-key``` header needs to be added to the HTTP request.
 

## Testing

1. Retrieve the Host URL of the API Gateway from AWS Console.

2. Retrieve the API key from AWS Console.

3. Send a sample HTTP request to the API Gateway:
   ```
   POST /prod/generateimage HTTP/1.1
   Host: <Host URL of the API Gateway>
   x-api-key: <Retreive the key from AWS Console>
   Content-Type: application/json
   Cache-Control: no-cache
   {
    "query": {
        "text_inputs": "A step by step recipe to make butter chicken:",
        "max_length": 5000
    }
   }

   ```

4.  The API Gateway should respond with a JSON formatted response from the SageMaker endpoint


## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.

```sh
cdk destroy
```

## Author bio
Kaustav Dey,
https://www.linkedin.com/in/kaustavbecs/
Solution Architect

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
