# Lambda in a VPC with access to Secrets Manager (Serverless Framework)

This pattern using the Serverless Framework will create a Lambda function in a VPC with strict access to Secrets Manager using the AWS private network.
It also creates a second Lambda function not in a vpc using the same code so you can compare the differences.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-vpc-secrets-sls](https://serverlessland.com/patterns/lambda-vpc-secrets-sls).

Important: this application uses AWS services that always have a small cost and there are costs associated with other services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.
[AWS Secrets Manager Pricing](https://aws.amazon.com/secrets-manager/pricing/)
[AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/)

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [NodeJS](https://nodejs.org/en/download/) (LTS version) installed
* [Serverless Framework CLI](https://www.serverless.com/framework/docs/getting-started) version 3 or greater installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ``` sh
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern source code folder:

    ``` sh
        cd serverless-patterns/lambda-vpc-secrets-sls
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



## Testing

1. After the secret is deployed, you can test the code locally using these commands:
    

    ``` sh
    npm run localVpcTest
    npm run localOpenTest
    ```
    

1. After deployment, use the function names in the output to execute a test in the cloud from the command line.

    ``` sh
    aws lambda invoke \
    --function-name lambda-vpc-secrets-sls-dev-VpcLambdaFunction \
    --invocation-type RequestResponse \
    response.json
    ```
    [Invoke Lambda CLI docs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/invoke.html)
    
1. Retrieve the CloudWatch logs 

    ``` sh
    sls logs -f VpcLambdaFunction
    ```
    [Serverless Framework logs CLI docs](https://www.serverless.com/framework/docs/providers/aws/cli-reference/logs/)


## Cleanup

1. Delete the stack

    ```sh
    serverless remove
    ```

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0