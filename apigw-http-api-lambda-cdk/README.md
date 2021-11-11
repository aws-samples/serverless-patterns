# Amazon API Gateway HTTP API to AWS Lambda

This pattern creates an Amazon API Gateway HTTP API and an AWS Lambda function using AWS Cloud Development Kit (AWS CDK) in
Python. This template also has a sample CORS configuration. The sample application was developed in Python and it shows some
context, event and environment variables properties.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-http-lambda-cdk.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier
usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs
incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one
  and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS
  resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Python 3.9+](https://www.python.org/downloads/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-http-api-lambda-cdk
    ```
1. Create a virtual environment for Python:
    ```
    python3 -m venv .venv
    ```
1. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

    For a Windows platform, activate the virtualenv like this:
    ```
    .venv\Scripts\activate.bat
    ```
1. Install the Python required dependencies:
    ```
    pip install -r requirements.txt
    ```
1. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the app.py file:
    ```
    cdk deploy
    ```
1. Note the outputs from the CDK deployment process. These contain the API endpoint which is used for testing.

## How it works

The API Gateway handles the incoming API requests and it selects the route with the most-specific match from those declared in
each `add_routes` statement. The response is routed back to the requester. 

## Testing

Run the following command to send an HTTP `GET` request to the HTTP APIs endpoint. Note that you must edit the {api_endpoint}
placeholder with the URL of the deployed HTTP APIs endpoint. This is provided in the deployment outputs.

```
curl -H "Origin: https://www.example.com" "{api_endpoint}?path=parameter" --verbose
```

The `--verbose` argument is to show the http handshake, the status code, and headers. The `-H "Origin: https://www.example.com"`
is the third party domain making the request, which you can substitute for other domains.

The output will show a JSON object created by the sample application.

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
