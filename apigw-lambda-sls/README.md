# Amazon API Gateway REST API with AWS Lambda proxy integration

This pattern in Serverless Framework offers a boilerlate to generate an Amazon API Gateway REST API endpoint with a greedy proxy ("{proxy+}") and "ANY" method from the specified path, meaning it will accept by default any method and any path. The Lambda function, provided in TypeScript, only returns the path.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-lambda-sls](https://serverlessland.com/patterns/apigw-lambda-sls).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [NodeJS](https://nodejs.org/en/download/) (LTS version) installed
* [Serverless Framework CLI](https://www.serverless.com/framework/docs/getting-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ``` sh
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory its source code folder:

    ``` sh
        cd serverless-patterns/apigw-lambda-sls
    ```

1. From the command line, use npm to install the development dependencies:

    ``` sh
    npm install
    ```

1. To deploy from the command line use the following:

    ``` sh
    serverless deploy --verbose
    ```

    The above command will deploy resources to `us-east-1` region by default. You can override the target region with `--region <region>` CLI option, e.g.

    ``` sh
    serverless deploy --verbose --region us-west-2
    ```

1. Note the `ServiceEndpoint` output from the deployment process. You will use this value for testing.

## Testing

1. After deployment, the output shows the API Gateway URL with the Lambda integration, for example: `ServiceEndpoint: https://<random-id>.execute-api.us-east-1.amazonaws.com/prod/`.
1. Accessing the URL in a browser, you see: `Hello Serverless Citizen, your happy path is: "/"`.
1. This page logs any path you type after "/". You can use this as a starting point as a general purpose endpoint for various types of applications. That said, you can try adding extra path to the `ServiceEndpoint` URL and confirm it being reported back to the user, e.g. navigating to `<ServiceEndpoint>/aaa/bbb/ccc` URL results in `Hello Serverless Citizen, your happy path is: "/aaa/bbb/ccc"` returned to the user.

## Cleanup

1. Delete the stack

    ```sh
    serverless remove --verbose
    ```

1. Confirm the stack has been deleted

    ```sh
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'apigw-lambda-sls-prod')].StackStatus"
    ```

    Expected output

    ```json
    [
        "DELETE_COMPLETE"
    ]
    ```

    NOTE: You might need to add `--region <region>` option to AWS CLI command if you AWS CLI default region does not match the one, that you used for the Serverless Framework deployment.

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
