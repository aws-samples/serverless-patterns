# Amazon API Gateway Websocket API to Amazon ECS Fargate

This pattern deploys an API Gateway WebSocket API integrated with an Application Load Balancer(ALB) and Amazon ECS Fargate.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
- [Python 3.x Installed](https://www.python.org/) Python 3.x installed with pip.

## Deployment Instructions

1. Clone the project to your local working directory

   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```

2. Change the working directory to this pattern's directory

   ```bash
   cd apigw-websocket-api-fargate-cdk
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

## How it works

This pattern deploys API Gateway WebSocket API, Fargate Cluster, Networking, and an Application Load Balancer. The webSocket client connects using the API endpoint url, and communicates using the default route. Using http integration, API gateway communicates with the ALB and invokes the Fargate task. The Fargate task, running the FASTAPI framework, receives the POST request and communicates back to the client through API Gateway using the connectionId in the request context.

## Testing

### Testing with `wscat` CLI

1. The stack will output the **websocketsapiendpoint**. Use wscat to test the API (see [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-wscat.html) for more details on how to set it up):

   ```bash
   wscat -c wss://hxxraj3sh.execute-api.us-west-2.amazonaws.com/dev
   ```

2. Send a payload to the API in the below format and the api will echo back:

   ```bash
   > {"data": "this is the way!"}
   < {"data": "this is the way!"}
   ```

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to delete.

```bash
cdk destroy
```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
