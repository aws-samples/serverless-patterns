# Preventing Amazon DynamoDB write throttling with an Amazon SQS queue-based buffer

This pattern demonstrates the ability to avoid message producer throttling when writing information into an Amazon DynamoDB table by buffering the records in an Amazon SQS queue. This approach benefits from the scaling capabilities of Amazon SQS service and allows clients to send data to AWS at maximum speed even if DynamoDB table throttles write requests.

 **Important note**: This pattern doesn't guarantee message ordering when writing information to the DynamoDB table!

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/sqs-lambda-ddb-sam-ts/](https://serverlessland.com/patterns/sqs-lambda-ddb-sam-ts/)

**Important**: This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed.
* [NodeJS](https://nodejs.org/en) 18 or later.
* [esbuild](https://esbuild.github.io/) installed globally with `npm install --location=global esbuild`.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

``` sh
git clone https://github.com/aws-samples/serverless-patterns
```

1. Change directory to the pattern directory:

    ``` sh
    cd sqs-lambda-ddb-sam-ts
    ```

1. From the command line, use AWS SAM CLI to build the application

    ``` sh
    sam build
    ```

1. From the command line, use AWS SAM CLI to deploy the AWS resources for the pattern as specified in the template.yml file:

    ``` sh
    sam deploy --guided
    ```

    or

    ```sh
    sam deploy --stack-name <STACK_NAME> --resolve-s3 --capabilities CAPABILITY_IAM --no-fail-on-empty-changeset
    ```

1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region - AWS CLI default region is recommended if you are planning to run the test (test.sh) script
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which will use for testing.

You can also use `deploy.sh` script to build SAM template and deploy it to the default AWS account and region as a new `sqs-lambda-ddb-sam-ts` CloudFormation stack.

## How it works

A new Amazon SQS queue (`IngressQueue`) will be created and configured to invoke an AWS Lambda function that will write the received messages into an Amazon DynamoDB table (`DestinationTable`). SQS queue redrive policy will be configured to send undeliverable messages to an Amazon SQS Dead-Letter Queue (`Dlq`). Undeliverable messages are the ones that couldn't be written to the DynamoDB table with a maximum of `maxReceiveCount` number of attempts.

Lambda function will stop writing messages into the DynamoDB table as soon as it catches an exception and will report the remaining messages to Amazon SQS service as failed.

Amazon DynamoDB table will have a minimal `ProvisionedThroughput` configuration for demo purposes, so that the users can observe message write retries when testing this stack. Real production throughput must be configured in accordance with the actual business requirements and message sizes.

## AWS Lambda function implementation details

This template uses AWS SAM CLI integration with the esbuild bundler and takes advantage of such feature as [ECMAScript Modules](https://tc39.es/ecma262/#sec-modules) compatible output. Producing ESM output allows esbuild bundler to perform [Tree Shaking](https://esbuild.github.io/api/#tree-shaking) optimization that automatically removes unreachable code from the output.

Additionally, output [Minification](https://esbuild.github.io/api/#minify) is enabled for the Lambda function, which reduces the output size even further.

See `Metadata` section of the `IngressProcessingFunction` resource for the Lambda function build configuration details.

## Testing

You can execute a test script to simulate the activity of sending 5 identical batches of 10 messages each to the `IngressQueue`. Batch of messages is defined in [./messages.json](./messages.json) file and each message is configured to be ~4Kb in size for demo purposes.

**Important**: The test script expects demo stack to be deployed with the `sqs-lambda-ddb-sam-ts` stack name. You'll have to change the `STACK_NAME` to match a different name, if needed.

```sh
./test.sh
```

Once you execute the test script, you cam monitor the messages being consumed by `IngressProcessingFunction` Lambda function from the `IngressQueue` SQS queue in AWS Console. Additionally, you can inspect `IngressProcessingFunction` function's CloudWatch logs to check for `The level of configured provisioned throughput for the table was exceeded` error messages.

## Cleanup

1. Delete the stack

    ```bash
    sam delete --stack-name <STACK_NAME>
    ```

1. Confirm the stack has been deleted

    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'<STACK_NAME>')].StackStatus"
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
