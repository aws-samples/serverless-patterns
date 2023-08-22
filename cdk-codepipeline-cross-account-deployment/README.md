# CDK CodePipline Cross-Account Deployment

This pattern deploys a CodePipline using CodeCommit and CodeBuild. From this pipeline it deploys a CloudFront distribution in front of an S3 Bucket to serve as a static website, across 2 accounts. This is an example of how you can use one pipline to deploy the same stack across multiple environments.

Note that CloudFront and S3 are used in this pattern for demonstration purposes, you can use this pattern with any stack you wish to deploy.

![Pattern architecture](img/serverless-pattern.png)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create AWS account(s)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK >= 2.2.0) Installed

## Language

Python

## Framework

CDK

## How It Works

After cloning this pattern, you will bootstrap 2 AWS environments with CDK. An environment is an Account-Region pair. This example uses 2 different accounts as a way to demonstrate deploying the same CDK stack(s) across accounts i.e. Development and Production. The pipeline will only deploy in the account you designate in the app.py file.

While bootstrapping the, you include a ```--trust``` flag that creates a trust relationship from the primary (pipeline) account to the accounts you wish to deploy to.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```bash
    cd cdk-crossaccount-deployment
    ```
3. Use CDK to bootstrap environments (note that the trust flag will need to be included on all environments you wish to deploy to):
    ```bash
    cdk bootstrap aws://ACCOUNT-NUMBER-1/REGION-1
    ```

    ```bash
    cdk bootstrap aws://ACCOUNT-NUMBER-2/REGION-2 --trust <PRIMARY-ACCOUNT-NUMBER>
    ```

4. Create a virtual environment for python:
    ```bash
    python3 -m venv .venv
    ```
5. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

    If you are in Windows platform, you would activate the virtualenv like this:

    ```
    % .venv\Scripts\activate.bat
    ```

6. Install python modules:

    ```bash
    python3 -m pip install -r requirements.txt
    ```

7. From the command line, use CDK to synthesize the CloudFormation template and check for errors:

    ```bash
    cdk synth
    ```

8. From the command line, use CDK to deploy the stack:

    ```bash
    cdk deploy
    ```
## Testing

1. After deploying, you can make changes in the repo, and push those changes to main. After these changes are pushed, navigate to the CodePipline dashboard and select the pipline to watch the CI/CD process.

2. After the pipline is complete, you can navigate to CloudFront in both accounts and see the distribution that has been created. The CloudFront dashboard will provide you with a URL you can use to navigate to the exmaple website that has been created.

## Cleanup

1. Delete the stack in both accounts

    ```bash
    cdk destroy
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0