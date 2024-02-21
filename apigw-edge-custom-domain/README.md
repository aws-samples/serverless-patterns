# Edge-optimized AWS API Gateway with custom domain name
This pattern provides a simple stack (API Gateway /hello) to deploy an EDGE-Optimized API Gateway in your preferred region with ACM certificate in us-east-1(mandatory with EDGE API).

## Requirements
* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* Having your Route53 zone in the same AWS account.

## Deployment Instructions
1. Create the certificate in us-east-1
    ```
    $ sam deploy -t certificate.yaml --stack-name cert-sample-api --parameter-overrides "Domain=sample.com" --region us-east-1 --resolve-s3 --capabilities CAPABILITY_IAM --no-fail-on-empty-changeset --no-progressbar
    ```
1. Create the main stack in your preferred region
    ```
    $ sam deploy -t template.yaml --stack-name sample-api --parameter-overrides "Env=Dev Domain=sample.com" --region eu-west-1 --resolve-s3 --capabilities CAPABILITY_NAMED_IAM --no-fail-on-empty-changeset --no-progressbar
    ```
## How it works
<img width="1273" alt="image" src="assets/architecture.png">

## Testing
    $ wget sample-api.<your-domain-name>/hello

## Cleanup

1. Delete the stack
    ```
    $ sam delete --stack-name sample-api --region eu-west-1
    $ sam delete --stack-name cert-sample-api --region us-east-1
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
