# AWS CodePipeline with Parallel E2E Tests

This pattern in CDK provides scaffolding for a CI/CD pipeline with parallelized End-to-End (E2E) tests.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Create an AWS CodeCommit repository and add it as a remote:
    ```
    git remote add << repository name >> << repository url >>
    ```
2. Change directory to the pattern directory:
    ```bash
    cd parallel-e2e-pipeline-cdk
    ```
3. Change directory to the pipeline directory:
    ```bash
    cd src/pipeline
    ```
4. From the command line, use npm to install the development dependencies:
    ```bash
    npm install
    ```
5. Configure the pipeline based on your environment. Navigate to pipeline-stack.ts and make changes based on the TODO comments.
5. From the command line, configure environment variables for the AWS account you desire to deploy the pipeline to (the pipeline should be deployed in the same region as the AWS CodeCommit repo). For example:
    ```bash
    export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
    export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    export AWS_DEFAULT_REGION=us-west-2
    ```
6. Navigate back to the pipeline directory and from the command line, use CDK to deploy the AWS resources for the pattern:
    ```bash
    cdk synth ParallelE2EPipelineCDK
    cdk deploy ParallelE2EPipelineCDK
    ```

## How it works

The provided pipeline consists of two stages: `Source` and `End_to_End_Tests`. The `Source` stage is linked to the AWS CodeCommit repository, so whenever any commit(s) is pushed to that repository, the pipeline will be triggered. Once the `Source` stage passes, the `End_to_End_Tests` stage will run. In this stage, two AWS CodeBuild servers are provisioned and each is assigned a group of test(s). The tests are then ran in parallel.

The described pattern can be modified to meet your needs. For example:
* Introduce a deployment stage before `End_to_End_Tests`
* Provision N AWS CodeBuild servers
* Run tests that use the framework you desire (e.g. Cypress, Puppeteer, Jest)

## Testing

Whenever a commit(s) is pushed to the AWS CodeCommit repository, it will automatically trigger the deployed pipeline. To manually trigger the pipeline follow the below steps:
1. Log into your AWS account and navigate to the AWS CodePipeline console.
2. Select ParallelE2EPipelineCDK and release a change.
3. The pipeline execution should succeed. 
4. To view build logs, click on `Details` under each action.

## Cleanup
 
1. From the command line, configure environment variables for the AWS account the pipeline is deployed in:
    ```bash
    export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
    export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    export AWS_DEFAULT_REGION=us-west-2
    ```
2. Navigate to to the pipeline directory and delete the deployed pipeline by running:
    ```bash
    cdk destroy ParallelE2EPipelineCDK
    ```
3. Delete the AWS CodeCommit repository.
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
