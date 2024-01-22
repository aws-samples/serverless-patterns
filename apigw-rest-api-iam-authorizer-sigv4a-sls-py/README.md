# AWS API Gateway, IAM authorization and AWS v4 request signing

This pattern involves employing an AWS_IAM authorizer to secure an API endpoint through Python 3 and the Serverless framework. 
It illustrates the process of signing the HTTP request using IAM credentials and adhering to the AWS v4 signing method. 
This ensures access to the protected endpoint from a public API. 
The interaction with APIs is facilitated by AWS API Gateway.

**Note**: The pattern employs Lambda behind an APIGW as a Public API. 
However, even if Lambda is not used in the system, the core considerations remain consistent. 
The scenario involves a public API making calls to a private API, secured by AWS_IAM. 
Consequently, the signing process with AWS v4 is essential, irrespective of specific implementation details.

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
3. Install dependencies by navigating to `/private` and `/public` folders and running:
    ```commandline
    pipenv install
    ```
4. From the project root, install following Serverless (sls) Framework plugins:
    ```commandline
    sls plugin install -n serverless-python-requirements
    sls plugin install -n serverless-plugin-log-retention
    ```
   - `serverless-python-requirements` plugin will automatically detect `Pipfile` and pipenv installed and generate a `requirements.txt` file
   - `serverless-plugin-log-retention` plugin will control the retention of serverless function's cloudwatch logs

5. From the project root, deploy the services specified in [serverless-compose.yml](./serverless-compose.yml) for the pattern using:
   ```commandline
      sls deploy --stage dev --verbose
   ```
6. The outputs from the Serverless deployment process containing the resource names and/or ARNs which are used for
   testing can be obtained any time using:
   ```commandline
      sls outputs
   ```

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
date: Sat, 27 Jan 2024 22:25:36 GMT
via: 1.1 f762d56afc88f7f52f51da3b63ad4658.cloudfront.net (CloudFront)
x-amz-apigw-id: SOFjIFt9oAMEW5Q=
x-amz-cf-id: plGeuXjziKSzYMtMx5laDkMVzrJJWPstajMWT-rCiyw2FY6sDkT7Aw==
x-amz-cf-pop: IAD50-C2
x-amzn-requestid: 767b548d-c1d2-404c-913a-0a730553019d
x-amzn-trace-id: Root=1-65b582e0-3d9b1e793369a0f811c5ca7c;Sampled=0;lineage=0cf5a4d5:0
x-cache: Miss from cloudfront

{
    "message": "Hi from AWS_IAM auth enabled API"
}
```

When `GET /private` is directly called as:

```commandline
xh https://${PrivateApiGatewayRestApi}.execute-api.${AWS::Region}.amazonaws.com/${sls:stage}/private
```
_Or_

```commandline
curl -i --request GET --url https://${PrivateApiGatewayRestApi}.execute-api.${AWS::Region}.amazonaws.com/${sls:stage}/private
```

Response:

```commandline
HTTP/2.0 403 Forbidden
content-length: 42
content-type: application/json
date: Sat, 27 Jan 2024 22:25:17 GMT
via: 1.1 64287378cade03feddd2042bfe0ee6a4.cloudfront.net (CloudFront)
x-amz-apigw-id: SOFgFFoEoAMERDw=
x-amz-cf-id: rl2Okhix_AnRpaZH9hp3xvAIF0RrA-a3bJJwfRyFj4Ii17c-HewH3Q==
x-amz-cf-pop: IAD79-C3
x-amzn-errortype: MissingAuthenticationTokenException
x-amzn-requestid: 6feb0801-eb82-455d-ad49-dae1516a6b7e
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
