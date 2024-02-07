# REST API as an Amazon S3 proxy in API Gateway

This pattern utilizes Serverless framework to deploy a REST API via API Gateway, acting as an S3 proxy for write operations. 
It includes API-Key Setup, Request Body Validator, Lambda invocation on S3 events, and enables CloudWatch logs and X-Ray tracing for API Gateway and Lambda using AWS Powertool for Lambda framework.

Learn more about this pattern
at [Serverless Land Patterns](https://serverlessland.com/patterns/apigw-s3-lambda-sls-py).

**Important**: this application uses various AWS services and there are costs associated with these services after the Free
Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any
AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already
  have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls
  and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [Python 3](https://www.python.org/downloads/) installed
* [Serverless Framework](https://www.serverless.com/framework/docs/getting-started) installed
* [Powertools for AWS Lambda (Python)](https://docs.powertools.aws.dev/lambda/python/latest/)

## Setup and Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```commandline
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```commandline
    cd apigw-s3-lambda-sls-py
    ```
3. Install dependencies:
    ```commandline
    pipenv install
    ```
4. Install following Serverless (sls) Framework plugins:
    ```commandline
    sls plugin install -n serverless-python-requirements
    sls plugin install -n serverless-plugin-log-retention
    sls plugin install -n serverless-iam-roles-per-function
    ```
   - `serverless-python-requirements` plugin will automatically detect `Pipfile` and pipenv installed and generate a `requirements.txt` file
   - `serverless-plugin-log-retention` plugin will control the retention of serverless function's cloudwatch logs
   - `serverless-iam-roles-per-function` plugin to easily define IAM roles per function via the use of iamRoleStatements at the function definition block

5. Deploy the services specified in [serverless.yml](./serverless-compose.yml) by running:
   ```commandline
      sls deploy --stage dev --verbose
   ```
6. The outputs from the Serverless deployment process containing the resource names, IDs and/or ARNs which are used for
   testing.


## How it works

The high-level diagram below serves to visually represent this pattern.

![storage-first-pattern.png](./docs/storage-first-pattern.png)

This setup involves creating and launching a REST API using API Gateway, allowing direct S3 writing without additional services. 
It utilizes an open-source Serverless framework for deployment. The pattern includes setting up API keys with Usage Plan, Request Body Validator, and triggering Lambda functions on S3 events.
Additionally, this setup establishes Cloudwatch logs and X-Ray tracing for both API Gateway and Lambda, harnessing the capabilities of AWS Powertool specifically for Lambda functions.

## Testing

#### I.

This setup can be tested using the [curl command](https://github.com/curl/curl/blob/master/docs/MANUAL.md) or  [xh utility](https://github.com/ducaale/xh)  by accessing the `PUT /dev/api/{order_object_path+}
` endpoint. 

In this context, the inclusion of 'suffix' alongside 'order_object_path' suggests that we have the flexibility to substitute multiple folders in place of 'order_object_path'.

```commandline
xh https://${ApiGatewayRestApi}.execute-api.${AWS::Region}.amazonaws.com/${sls:stage}/api/orders_recevied/order001.json X-Api-Key:ttLMU7hv2S4qEpBVaCYXt4OWoy38jRmF7txgEBXy orderDate=2024-02-06 orderPaymentAmount:=23.99 orderPaymentCurrency=USD customerId:=10002
```
_Or_
```commandline

curl --request PUT \
  --url https://${ApiGatewayRestApi}.execute-api.${AWS::Region}.amazonaws.com/${sls:stage}/api/orders_recevied/order001.json \
  --header 'x-api-key: ttLMU7hv2S4qEpBVaCYXt4OWoy38jRmF7txgEBXy' \
  --data '{
		"orderId": 10023,
		"orderDate": "2024-02-03",
		"orderPaymentAmount": 23.99,
		"orderPaymentCurrency": "USD",
		"customerId": 100023
}'
```
Response:

```commandline
HTTP/2.0 200 OK
content-length: 0
content-type: application/json
date: Wed, 07 Feb 2024 01:54:37 GMT
x-amz-apigw-id: SvhitG7XoAMEifg=
x-amzn-requestid: 1dd4f2f1-f5ac-46d6-8f65-0d60d4370f0b
x-amzn-trace-id: Root=1-65c2e2dd-737319bc469770c954e78a1c

```
S3 Event Triggered Lambda logs:

```commandline
{
    "level": "INFO",
    "location": "lambda_handler:23",
    "message": {
        "orderId": 10023,
        "orderDate": "2024-02-03",
        "orderPaymentAmount": 23.99,
        "orderPaymentCurrency": "USD",
        "customerId": 100023,
        "processed": true
    },
    "timestamp": "2024-02-07 03:10:49,719+0000",
    "service": "processS3Order",
    "cold_start": true,
    "function_name": "sls-bb245-sfp-dev-ProcessS3Data",
    "function_memory_size": "256",
    "function_arn": "arn:aws:lambda:us-east-1:000440860992:function:sls-bb245-sfp-dev-ProcessS3Data",
    "function_request_id": "2262edad-50f3-4216-8c97-d74721ddbe6a",
    "xray_trace_id": "1-65c2f4b7-584ae2cf70a37f700d109c26"
}
```
#### II. Testing Request Validator:
In this scenario, a value of "ZZZ" is passed for `orderPaymentCurrency` in the request body, which is not among the permitted values.
```commandline
xh https://${ApiGatewayRestApi}.execute-api.${AWS::Region}.amazonaws.com/${sls:stage}/api/orders_recevied/order001.json X-Api-Key:ttLMU7hv2S4qEpBVaCYXt4OWoy38jRmF7txgEBXy orderDate=2024-02-06 orderPaymentAmount:=23.99 orderPaymentCurrency=ZZZ customerId:=10002
```
_Or_
```commandline

curl --request PUT \
  --url https://${ApiGatewayRestApi}.execute-api.${AWS::Region}.amazonaws.com/${sls:stage}/api/orders_recevied/order001.json \
  --header 'x-api-key: ttLMU7hv2S4qEpBVaCYXt4OWoy38jRmF7txgEBXy' \
  --data '{
		"orderId": 10023,
		"orderDate": "2024-02-03",
		"orderPaymentAmount": 23.99,
		"orderPaymentCurrency": "ZZZ",
		"customerId": 100023
}'
```
Response:

```commandline
HTTP/2.0 400 Bad Request
content-length: 35
content-type: application/json
date: Wed, 07 Feb 2024 03:20:21 GMT
x-amz-apigw-id: SvuGdFUPIAMERkg=
x-amzn-errortype: BadRequestException
x-amzn-requestid: 08b9ba47-24f1-430c-8568-cf7c52f39b1f
x-amzn-trace-id: Root=1-65c2f6f5-79d73edc65b20ee1272f2fb0

{
    "message": "Invalid request body"
}
```

#### III. Testing without API Key:
```commandline
xh https://${ApiGatewayRestApi}.execute-api.${AWS::Region}.amazonaws.com/${sls:stage}/api/orders_recevied/order001.json orderDate=2024-02-06 orderPaymentAmount:=23.99 orderPaymentCurrency=USD customerId:=10002
```
_Or_
```commandline

curl --request PUT \
  --url https://${ApiGatewayRestApi}.execute-api.${AWS::Region}.amazonaws.com/${sls:stage}/api/orders_recevied/order001.json \
  --data '{
		"orderId": 10023,
		"orderDate": "2024-02-03",
		"orderPaymentAmount": 23.99,
		"orderPaymentCurrency": "USD",
		"customerId": 100023
}'
```
Response:

```commandline
HTTP/2.0 403 Forbidden
content-length: 23
content-type: application/json
date: Wed, 07 Feb 2024 03:32:23 GMT
x-amz-apigw-id: Svv3PHS_oAMEP6Q=
x-amzn-errortype: ForbiddenException
x-amzn-requestid: a3e5283d-827b-4e32-b1cc-9e4b28154bce
x-amzn-trace-id: Root=1-65c2f9c7-6fa15f204c6b011527ee7c54

{
    "message": "Forbidden"
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
