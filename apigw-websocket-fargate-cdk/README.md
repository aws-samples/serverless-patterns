# Amazon API Gateway Websocket API to AWS ECS Fargate

This pattern deploys an API Gateway WebSocket API integrated with Application Load Balancer to AWS ECS Fargate.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Clone the project to your local working directory

   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```

2. Change the working directory to this pattern's directory

   ```bash
   cd apigw-websocket-fargate-cdk
   ```

3. Create manually create a Python virtualenv on MacOS and Linux:

   ```bash
   $ python3 -m venv .venv
   $ source .venv/bin/activate
   ```

4. Once virtualenv is activated then install dependencies

   ```bash
   $ pip install -r requirements.txt
   ```

5. Deploy the stack to your default AWS account and region. The output of this command should give you the WebSocket API URL.
   ```bash
   cdk deploy
   ```

## How it works

The CDK deploys, API Gateway WebSocket API, Fargate Cluster, Networking, and Application Load Balancer. WebSocket client connects using API endpoint url, and communicates using default route. Using http integration API gateway communicated to ALB which in turns invokes Fargate Tasks. Fargate task running FASTAPI framework receives the POST request and communicates back using connectionId in the request context from API Gateway.

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.

```bash
cdk destroy
```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
