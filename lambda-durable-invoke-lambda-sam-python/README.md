# Lambda Durable Function Invoking Lambda Function (Python)

This pattern demonstrates how an AWS Lambda durable function can invoke a standard Lambda function using `context.invoke()` from the AWS Durable Execution SDK. The invocation is automatically checkpointed, so if the durable function is interrupted after the invoked function completes, it resumes with the stored result without re-invoking the target function.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-durable-invoke-lambda-sam-python

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* Python 3.14

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-durable-invoke-lambda-sam-python
    ```
1. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region (durable functions are available in supported regions)
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern deploys two Lambda functions:

1. **DurableLambdaFunction** - A durable Lambda function that orchestrates the workflow. It uses the `@durable_execution` decorator and performs two checkpointed operations:
   - A `@durable_step` that prepares and validates input values.
   - A `context.invoke()` call that invokes the ProcessorFunction and waits for its result.

2. **ProcessorFunction** - A standard Lambda function that receives a list of numeric values and returns computed statistics (sum, average, max, min).

The durable function uses automatic checkpointing. Each step and invoke operation creates a checkpoint. If the function is interrupted (e.g., due to a transient failure), it replays from the beginning but skips completed checkpoints, resuming execution from where it left off.


## Testing

1. After deployment, invoke the durable function using the alias ARN from the stack outputs:

    ```bash
    aws lambda invoke \
      --function-name <DurableLambdaFunctionAliasArn> \
      --payload '{"values": [10, 20, 30, 40, 50]}' \
      --cli-binary-format raw-in-base64-out \
      output.json
    ```

2. Check the response:

    ```bash
    cat output.json
    ```

    Expected output:
    ```json
    {"statusCode": 200, "body": "{\"message\": \"Durable orchestration completed successfully\", \"input_values\": [10, 20, 30, 40, 50], \"processing_result\": {\"operation\": \"sum_and_average\", \"count\": 5, \"sum\": 150, \"average\": 30.0, \"max\": 50, \"min\": 10}}"}
    ```

3. Monitor the durable execution steps in the Lambda console under the **Durable executions** tab of the DurableLambdaFunction.

## Cleanup

1. Delete the stack
    ```bash
    sam delete
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
