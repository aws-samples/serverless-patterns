# Lambda Function URL (Serverless Framework)

This pattern in Serverless Framework will create a dedicated, public HTTPS endpoint for your Lambda function.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-function-url-sls](https://serverlessland.com/patterns/lambda-function-url-sls).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [NodeJS](https://nodejs.org/en/download/) (LTS version) installed
* [Serverless Framework CLI](https://www.serverless.com/framework/docs/getting-started) version 3.12 or greater installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ``` sh
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern source code folder:

    ``` sh
        cd serverless-patterns/lambda-function-url-sls
    ```

1. From the command line, use npm to install the development dependencies:

    ``` sh
    npm install
    ```

1. To deploy from the command line use the following:

    ``` sh
    serverless deploy
    ```

    The above command will deploy resources to `us-east-1` region by default. You can override the target region from the command line:

    ``` sh
    serverless deploy --region us-west-2
    ```

1. Note the `endpoint` output from the deployment process. You will use this value for testing.

## Testing

1. For local testing from the command line use the following:

    ``` sh
    npm run localGetTest
    npm run localPostTest
    npm run localDeleteTest
    ```

1. After deployment, the output shows the endpoint URL, for example: `endpoint: https://<random-endpoint-id>.lambda-url.us-east-1.on.aws/`.  
Try testing your Lambda function in a browser or API tesing tool like Postman. 

1. Or you can test using a curl command:

    ``` sh
    curl https://<random-endpoint-id>.lambda-url.us-east-1.on.aws/
    curl -d '{"greeting":"hello"}' -H 'Content-Type: application/json' https://<random-endpoint-id>.lambda-url.us-east-1.on.aws/
    curl -X "DELETE" https://<random-endpoint-id>.lambda-url.us-east-1.on.aws/
    ```

## Cleanup

1. Delete the stack

    ```sh
    serverless remove
    ```

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
