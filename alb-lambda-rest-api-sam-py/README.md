# AWS Lambda REST API with Amazon ALB and Listener Rules

This configuration employs Python 3.9 and the Serverless Application Model (SAM) CLI to establish an Application Load
Balancer with route-based listener rules, paired with an AWS Lambda RESTful API function as the target.

Learn more about this pattern
at [Serverless Land Patterns](https://serverlessland.com/patterns/alb-lambda-rest-api-sam-py).

Important: this application uses various AWS services and there are costs associated with these services after the Free
Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any
AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already
  have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls
  and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (
  AWS SAM) installed
* [Python 3 installed](https://www.python.org/downloads/)
* [Docker](https://www.docker.com/products/docker-desktop/)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd alb-lambda-rest-api-sam-py
    ```
3. Install dependencies and build:
    ```
    pipenv install
    ```
4. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam validate && sam build && sam deploy
    ```
5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for
   testing.

## How it works

This setup orchestrates the deployment of an Application Load Balancer, configures path-based routes directing traffic
to a Python-based AWS Lambda function, and leverages
the [AWS Lambda Powertools for Python](https://docs.powertools.aws.dev/lambda/python/latest/core/event_handler/api_gateway/)
library. The Lambda function, serving as the target, records details of the incoming ALB event, along with the API and
context objects, logging them to an Amazon CloudWatch Logs log group and Amazon X-Ray.

## Testing

### SAM CLI for Local API Testing

The SAM CLI is an extension of the AWS CLI that ass functionality for building and test Lambda applications.
It uses Docker to run the function in an Amazon Linux environment that matches Lambda runtime
from [sam/build-python3.9](https://gallery.ecr.aws/sam/build-python3.9). It emulates application's build environment and
API.
To build and execute your function, run the following:

[event.json](./events/event.json) corresponds to ALB event. Generated using SAM
command: `sam local generate-event alb request`

```commandline
pipenv requirements > requirements.txt
sam build
sam local invoke -e events/event.json
```

### Deploy and Test API in AWS

Once the application is deployed, retrieve the Application Load Balancer endpoint value from CloudFormation Outputs.

```commandline
curl --request GET --header "Client-Correlation-Id:bb245" --url http://{ALB_ID}.{REGION}.elb.amazonaws.com/hello'
```

Alternatively, you use [xh utility](https://github.com/ducaale/xh), a lightweight, nicely formatted CLI too as:

```commandline
xh http://{ALB_ID}.{REGION}.elb.amazonaws.com/hello Client-Correlation-Id:bb245
```

Response:

```commandline
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 37
Content-Type: application/json
Server: awselb/2.0

{
    "message": "Hi from API behind ALB"
}

```

When an invalid resource is used as:

```commandline
xh http://{ALB_ID}.{REGION}.elb.amazonaws.com/nf-test Client-Correlation-Id:'not-found-test-1'
```

Response:

```commandline
HTTP/1.1 400 Bad Request
Connection: keep-alive
Content-Length: 27
Content-Type: text/plain; charset=utf-8
Date: Wed, 27 Dec 2023 23:13:43 GMT
Server: awselb/2.0

404 Error!!! Page Not Found

```

## Cleanup

1. Delete the stack
    ```bash
    sam delete
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0