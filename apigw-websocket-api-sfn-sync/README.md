# Amazon API Gateway WebSocket API to AWS Step Functions Express Synchronous Execution

This pattern uses Amazon API Gateway WebSocket API and AWS Service integration type with AWS Step Functions workflow as a business logics implementation. This approach simplifies architecture by eliminating the need to use additional compute components such as AWS Lambda. 

Learn more about this pattern at Serverless Land Patterns: ["API Gateway WebSocket API to Step Functions Express (Synchronous Execution)"](https://serverlessland.com/patterns/apigw-websocket-api-sfn-sync)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-websocket-api-sfn-sync
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern uses Amazon API Gateway WebSocket API and AWS Service integration type with AWS Step Functions workflow as a business logics implementation. This approach simplifies architecture by eliminating the need to use additional compute components such as AWS Lambda. 

API Gateway uses a data transformation mapping template to pass incoming data into Step Functions input and starts a synchronous Step Functions Express workflow. Workflow in this example comprises a single "Wait" state that pauses execution for 3 seconds and returns results back to the requestor. API Gateway passes this request back to the client. 

Production implementation of this pattern would include a more complex state machine that orchestrates interactions across multiple subsystems. Keep in mind, that maximum request timeout is 29 seconds. For longer running process orchestrations, see an asynchronous execution pattern in this repository.

For extended examples of this pattern see [Serverless Samples repository](https://github.com/aws-samples/serverless-samples/tree/main/apigw-ws-integrations)

## Testing

To test this example, connect to the API Gateway WebSocket endpoint using the URL in the stack outputs and wscat (see [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-wscat.html) for more details how to set it up):

```bash
wscat -c "<API Endpoint from stack outputs>"
```

Send payload (any JSON formatted data) to the API by typing it in. Step Functions will start the workflow execution synchronously and will respond with execution details in a few seconds. For example:
```bash
> {"first_name" : "Jane", "last_name" : "Doe"}
< {
    "billingDetails": {
        "billedDurationInMilliseconds": 5100,
        "billedMemoryUsedInMB": 64
    },
    "executionArn": "arn:aws:states:us-east-1:1234567890:express:SyncSFn-C4bjpQJrzj1U:bb3bed1a-2a8e-49eb-b654-2c994dadc634:2a29abfd-a52c-4802-8ebf-df6f127e9ec2",
    "input": "{\"first_name\" : \"Jane\", \"last_name\" : \"Doe\"}",
    "inputDetails": {
        "__type": "com.amazonaws.swf.base.model#CloudWatchEventsExecutionDataDetails",
        "included": true
    },
    "name": "bb3bed1a-2a8e-49eb-b654-2c994dadc634",
    "output": "{\"first_name\" : \"Jane\", \"last_name\" : \"Doe\"}",
    "outputDetails": {
        "__type": "com.amazonaws.swf.base.model#CloudWatchEventsExecutionDataDetails",
        "included": true
    },
    "startDate": 1.652472014974E9,
    "stateMachineArn": "arn:aws:states:us-east-1:1234567890:stateMachine:SyncSFn-C4bjpQJrzj1U",
    "status": "SUCCEEDED",
    "stopDate": 1.652472019978E9,
    "traceHeader": "Root=1-627eb8ce-86a1df144b8a90fa1606afcc;Sampled=1"
}
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
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
