# AWS API Gateway IAM authorization and AWS v4 request signing

This pattern uses an AWS_IAM authorizer to secure an API endpoint using Python 3 and the Serverless framework. 
It demonstrates how to sign the HTTP request using IAM credentials and follow the
[AWS v4 signing process](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) in order to grant access to the secured endpoint from a public API. AWS ApiGateway facilitates all communication with the APIs.

Learn more about this pattern
at [Serverless Land Patterns](https://serverlessland.com/patterns/apigw-lambdas-ddb-authorizer-sigv4a-sls-py).

**Important**: this application uses various AWS services and there are costs associated with these services after the Free
Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any
AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already
  have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls
  and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Serverless Framework](https://www.serverless.com/framework/docs/getting-started) installed
* [Python 3 installed](https://www.python.org/downloads/)

## Setup and Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```commandline
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```commandline
    cd apigw-rest-api-iam-authorizer-sigv4a-sls-py
    ```
3. Install dependencies:
    ```commandline
    pipenv install
    ```
4. From the command line, install following Serverless (sls) Framework plugins:
    ```commandline
    sls plugin install -n serverless-python-requirements
    sls plugin install -n serverless-plugin-log-retention
    ```
   - `serverless-python-requirements` plugin will automatically detect `Pipfile` and pipenv installed and generate a `requirements.txt` file
   - `serverless-plugin-log-retention` plugin will control the retention of serverless function's cloudwatch logs

5. Deploy the AWS resources specified in [serverless.yml](./serverless.yml) for the pattern using:
   ```commandline
      sls deploy --stage dev --verbose
   ```
6. Note the outputs from the Serverless deployment process. These contain the resource names and/or ARNs which are used for
   testing.

## How it works

The high-level diagram below serves to visually represent this pattern.

![arch.png](docs%2Farch.png)

In this setup, the `get-private` endpoint is secured with AWS_IAM. 
Requests to the `GET /private` endpoint require signing the HTTP request using IAM credentials, following the [AWS v4 signing process](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html). 
The requester must also have the required IAM permission to execute this endpoint, granted to the `GET /public` function. Notably, the `get-public` function has a method for signing HTTP requests.

## Testing

This example can be tested using the [curl command](https://github.com/curl/curl/blob/master/docs/MANUAL.md) or  [xh utility](https://github.com/ducaale/xh)  by accessing the `GET /public` endpoint.

```commandline
xh https://${ApiGatewayRestApi}.execute-api.${AWS::Region}.amazonaws.com/${sls:stage}/public

curl -i --request GET --url https://${ApiGatewayRestApi}.execute-api.${AWS::Region}.amazonaws.com/${sls:stage}/public
```
Response:

```commandline
HTTP/2.0 200 OK
content-length: 47
content-type: application/json
date: Thu, 18 Jan 2024 02:52:59 GMT
via: 1.1 a770e75e0ebdb44f23f7a7ef20bbbffa.cloudfront.net (CloudFront)
x-amz-apigw-id: RtvV4HlsoAMEASw=
x-amz-cf-id: 7XFrsfopdXijC-PgWWDUOTRUcSVRqWCTanaomRTphlzgXJHUEQ-TIQ==
x-amz-cf-pop: IAD55-P1
x-amzn-requestid: 64422709-d4f1-43a5-8613-5215d0e30617
x-amzn-trace-id: Root=1-65a8928b-0b4c78e27eb050ee2d760ad3;Sampled=0;lineage=c10ff951:0
x-cache: Miss from cloudfront

{
    "message": "Hi from AWS_IAM auth enabled API"
}
```

When `GET /private` is directly called as:

```commandline
xh https://${ApiGatewayRestApi}.execute-api.${AWS::Region}.amazonaws.com/${sls:stage}/private
```
_Or_

```commandline
curl -i --request GET --url https://${ApiGatewayRestApi}.execute-api.${AWS::Region}.amazonaws.com/${sls:stage}/private
```

Response:

```commandline
HTTP/2.0 403 Forbidden
content-length: 42
content-type: application/json
date: Thu, 18 Jan 2024 02:56:18 GMT
via: 1.1 6e44ac4753bea102fe3aae286f68acfe.cloudfront.net (CloudFront)
x-amz-apigw-id: Rtv0-HmFoAMEm8g=
x-amz-cf-id: MiZeGJuX9zPl9o8gIhWx0OgmBSLDASwapI2PFLNX1kSpWiRWaYdvMg==
x-amz-cf-pop: IAD55-P1
x-amzn-errortype: MissingAuthenticationTokenException
x-amzn-requestid: 3aa6efbe-6824-436d-8433-a0af57435fcf
x-cache: Error from cloudfront

{
    "message": "Missing Authentication Token"
}
```

## Cleanup

1. Delete the stack
    ```commandline
    sls remove --verbose
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
