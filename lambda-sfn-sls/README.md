# Invoke an AWS Step Functions workflow from AWS Lambda, with logging enabled

The Serverless Framework template deploys a Lambda function, a Step Functions Express workflow, a Log group and the IAM resources required to run the application.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-sfn.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ``` sh
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:

    ``` sh
    cd serverless-patterns/lambda-sfn-sls
    ```

1. From the command line, use npm to install the development dependencies:

    ``` sh
    npm install
    ```

1. From the command line, use Serverless Framework to deploy the AWS resources for the pattern as specified in the serverless.yml file:

    ``` sh
    serverless deploy --verbose
    ```

    The above command will deploy resources to `us-east-1` region by default. You can override the target region with `--region <region>` CLI option, e.g.

    ``` sh
    serverless deploy --verbose --region us-west-2
    ```

1. Note the `LambdaName` output from the Serverless Framework deployment process. We will need it for testing.

## How it works

A Lambda function uses the [AWS SDK for JavaScript v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/index.html) to asynchronously invoke the Express workflow, passing the event body as a string. The Express Workflow results are logged to Amazon CloudWatch Logs. The Lambda function returns the Express Workflow execution ARN and startDate.

We use the following plug-ins with the Serverless Framework template:

* [serverless-plugin-typescript](https://www.serverless.com/plugins/serverless-plugin-typescript) - enable TypeScript support for authoring Lambda functions;
* [serverless-step-functions](https://www.serverless.com/plugins/serverless-step-functions) - enable Step Functions support for Serverless Framework templates. This support adds such features as YAML support for writing [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) (ASL) definitions and pre-deployment ASL validation.

## Testing

Run the following Lambda CLI invoke command to invoke the function. Note, you must replace `<LambdaName>` placeholder with the Lambda function name from `LambdaName` from the stack output. Moreover, you must make sure that you AWS CLI default region is the same as the region, that you have deployed the demo stack to. You can use `--region <region>` parameter to select the appropriate region for running the command.

``` sh
aws lambda invoke --function-name <LambdaName> --region <region> --cli-binary-format raw-in-base64-out --payload '{ "IsHelloWorldExample": "Hello" }'  response.json
```

Once the command executes successfully, you'll have Step Function's executionARN and startDate reported to the `response.json` file and you can use AWS Console to view the Lambda and Step Function's logs in CloudWatch.

Expected console output after executing the above command:

``` json
{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}
```

Expected `response.json` file contents after executing the above command:

``` json
{
    "executionArn":"arn:aws:states:us-east-1:123456789012:express:HelloWorldStateMachine:12345678-1234-1234-1234-123456789012:12345678-1234-1234-1234-123456789012", "startDate":"2022-03-30T14:57:24.551Z"
}
```

## Cleanup

1. Delete the stack

    ```sh
    serverless remove --verbose
    ```

1. Confirm the stack has been deleted

    ```sh
    aws cloudformation list-stacks --query "StackSummaries[?StackName=='lambda-sfn-sls-prod'].StackStatus"
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
