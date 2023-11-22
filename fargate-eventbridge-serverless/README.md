# Leveraging Fargate for Scheduled Jobs

This pattern contains a sample serverless framework template to deploy a scheduled AWS Fargate task using EventBridge running on an Amazon Elastic Container Service (ECS) cluster. The docker image is pushed to Amazon Elastic Container Registry (ECR) using serverless framework template without having to pre-push the image to ECR or another container library. The serverless framework plugin for fargate, `serverless-fargate` is used to deploy tasks on ECS Cluster. This task runs every 10th minute of the hour using Eventbridge Rule and a simple file containing JSON is put in S3 bucket. 

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [NodeJS](https://nodejs.org/en/download/) (LTS version) installed
* [Serverless Framework CLI](https://www.serverless.com/framework/docs/getting-started) installed
* [Docker Desktop](https://docs.docker.com/desktop/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ``` sh
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:

    ``` sh
    cd fargate-eventbridge-serverless
    ```

1. Open Docker Desktop and keep it running in the background.

1. Install serverless-fargate plugin in dev dependencies:
    ```
        // using yarn
        yarn add serverless-fargate --dev
        // using npm
        npm install serverless-fargate --save-dev
    ```
1. From the command line, use Serverless Framework to deploy the AWS resources for the pattern as specified in the serverless.yml file:

    ``` sh
    serverless deploy --verbose
    ```

    The above command will deploy resources to `ap-south-1` region by default. You can override the target region with `--region <region>` CLI option, e.g.

    ``` sh
    serverless deploy --verbose --region eu-west-1
    ```

## How it works

- Make sure you have all the things configured mentioned in Requirements section.
- The image is constructed directly from the Dockerfile that is provided using Docker Desktop.
- The image is pushed to Amazon Elastic Container Repository (ECR).
- Fargate Task role is created.
- Fargate Execution role is created.
- The S3 bucket for output is created.
- The ECS cluster is created.
- The Task Definition is created. This also passes the environment variable to the scheduled task.
- Networking resources are created.
- Finally EventBridge Rule is created for running task every 10th minute of the hour.

## Testing

To test the deployment, you can verify by going to the output S3 bucket and find the output JSON file which contains a message and timestamp as below:
    ```
    {
    "message": "Task executed from Fargate Cluster.",
    "timestamp": 1692648300534
    }
    ```

## Cleanup

1. Empty the output S3 bucket.

1. Delete the stack:

    ```sh
    serverless remove --verbose
    ```

    NOTE: You might need to add `--region <region>` option to AWS CLI command if you AWS CLI default region does not match the one, that you used for the Serverless Framework deployment.

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0