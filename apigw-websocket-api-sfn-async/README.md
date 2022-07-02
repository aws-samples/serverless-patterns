# Amazon API Gateway WebSocket API to AWS Step Functions Standard Asynchronous Execution

This pattern uses Amazon API Gateway WebSocket API and AWS Service integration type with AWS Step Functions workflow as a business logics implementation. This approach simplifies architecture by eliminating the need to use additional compute components such as AWS Lambda. 

Learn more about this pattern at Serverless Land Patterns: ["API Gateway WebSocket API to Step Functions Express (Asynchronous Execution)"](https://serverlessland.com/patterns/apigw-websocket-api-sfn-async)

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
    cd apigw-websocket-api-sfn-async
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

API Gateway uses a data transformation mapping template to pass incoming data and WebSocket API connection ID into Step Functions input and starts an asynchronous Step Functions Standard workflow. Workflow in this example pauses execution for 5 seconds, then uses [@connections command](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html) to return results back to the requestor. Client application receives the workflow execution ID immediately after sending the request, execution results come 5 seconds later. Note that the workflow asynchronous execution can run for longer than the maximum API Gateway request timeout.

Production implementation of this pattern would include a more complex state machine that orchestrates interactions across multiple subsystems. It can also use an Express workflow if orchestration finishes faster than the maximum API Gateway request timeout of 29 seconds. 

For extended examples of this pattern see [Serverless Samples repository](https://github.com/aws-samples/serverless-samples/tree/main/apigw-ws-integrations)

## Testing

To test this example, connect to the API Gateway WebSocket endpoint using the URL in the stack outputs and wscat (see [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-wscat.html) for more details how to set it up):

```bash
wscat -c "<API Endpoint from stack outputs>"
```

Send a payload (any JSON formatted data) to the API by typing it in. Step Functions will start the workflow execution asynchronously and will respond with the execution ID immediately. Then, after a 5 seconds delay, the client will receive a message from the workflow execution. For example:
```bash
> {"first_name" : "Jane", "last_name" : "Doe"}
< {"executionArn":"arn:aws:states:us-east-1:781759781440:execution:AsyncSFn-raXy2Jv09CkK:2a95b6bd-c93e-473f-a49c-0229591ee2e1","startDate":1.652716274909E9}
< {"Message":"Hello from asynchronous workflow execution!"}
>
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
