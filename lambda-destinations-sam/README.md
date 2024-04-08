# Lambda Destinations to Lambda and SQS

This pattern demonstrates how to create a Lambda function that on success sends message to another function and on failure to SQS using Lambda destinations. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-destinations-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd lambda-destinations-sam
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The Main Lambda function has configured Lambda destinations. For asynchronous invocations, if the function succeeds it will send a message to the onSuccess destination configured (Lambda OnSuccess). If the Main function fails it sends a message to the onFailure destination configured (SQS Queue OnFailure).


## Testing

1. Run command below to invoke the Main Lambda Function which depending on the execution result (success or failure) will send the response to the destination. Make sure to replace --function-name parameter with the SAM output value of the key "MainLambdaFunction".
    ```
    aws lambda invoke --function-name <function-name> --invocation-type Event --cli-binary-format raw-in-base64-out --payload '{}' response.json
    ```
2. Get logs from Lambda Function "MainLambdaFunction" and "OnSuccessLambdaFunction" to make sure that both of them were executed as expected. Make sure to replace --stack-name parameter with the name of the Stack used for the sam project
    ```
    sam logs --name MainLambdaFunction --stack-name <stack-name> -s '30min ago'
    ```
    ```
    sam logs --name OnSuccessLambdaFunction --stack-name <stack-name> -s '30min ago'
    ```

3. Run command below to invoke the Main Lambda Function and simulate an error. It will send the response to the on failure destination. Make sure to replace --function-name parameter with the SAM output value of the key "MainLambdaFunction".
    ```
    aws lambda invoke --function-name <function-name> --invocation-type Event --cli-binary-format raw-in-base64-out --payload '{"type":"failure"}' response.json
    ```

4. Get messages from the SQS Queue to make sure the message was received by the Queue. Make sure to replace --queue-url parameter with the SAM output value of the key "OnFailureSqsQueue".
    ```
    aws sqs receive-message --queue-url <queue-url> --max-number-of-messages 10 --wait-time-seconds 20
    ```

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
