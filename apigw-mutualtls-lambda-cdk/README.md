# Amazon REST API Gateway with MutualTLS authentication

This pattern creates an Amazon [API Gateway RESTful API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html), an AWS [Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), and API is authenticated by certificate based MutualTLS(https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mutual-tls.html) using the AWS Cloud Development Kit (AWS CDK) in Python.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-mutualtls-lambda-cdk](https://serverlessland.com/patterns/apigw-mutualtls-lambda-cdk).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Python 3.9+](https://www.python.org/downloads/) installed
* [Custom domain name certificate](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains-prerequisites.html) before setting up a custom domain name for an API, you must have an SSL/TLS certificate ready in AWS Certificate Manager.
* [Configure truststore](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-mutual-tls.html) Create a truststore of X.509 certificates that you trust to access your API and upload the truststore to an Amazon S3 bucket in a single file.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-mutualtls-lambda-cdk
    ```
3. Create a virtual environment for Python
    ```
    python3 -m venv .venv
    ```
4. Activate the virtual environment
    ```
    source .venv/bin/activate
    ```
    For a Windows platform, activate the virtualenv like this:
    ```
    .venv\Scripts\activate.bat
    ```
5. Install the Python required dependencies:
    ```
    pip install -r requirements.txt
    ```
6. From the command line, use AWS CDK to deploy the AWS resources for the serverless application as specified in the app.py file. We need to pass the custom domain name, certificate arn, s3 bucket name, public hosted zone id and name as parameters:
    ```
    cdk deploy --parameters customdomainname={custom-domain-name} --parameters certificatearn={certificate-arn} --parameters truststorebucket={bucket-name} --parameters publiczoneid={public-zone-hosted-id} --parameters publiczonename={public-hosted-zone-name}
    ```
7. Note the outputs from the CDK deployment process, it contains the custom domain name hosted zone and alias.

## How it works

This pattern deploys an Amazon API Gateway REST API with a default route which is integrated with an AWS Lambda function written in Python. The REST API is authenticated by certificate based mutual TLS. The Lambda function returns a basic response to the caller.

## Testing

From the command line, run the following command to send an HTTP `GET` request to your custom domain name value. As a best practice the default endpoint for the REST API will be disabled when mutual TLS is enabled. Either use a curl or call the endpoint from Postman using your client side public and private keys.

```
curl --key my_client.key --cert my_client.pem https://{your-custom-domain-name}
```

## Cleanup

1. Delete the MutualTLSAPIGatewayStack Deployment stack
    ```
    cdk destroy
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
