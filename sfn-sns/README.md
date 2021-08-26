# AWS Step Functions Express Workflow to Amazon SNS

The Step Functions Express Workflow can be started using the AWS CLI or from another service (e.g. API Gateway) to run an express workflow and return the result.

The SAM template deploys a Step Functions Express workflow that sends the message to Amazon SNS and returns the response. The SAM template contains the minimum IAM resources required to run the application with logging enabled.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-lambda

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
    cd sfn-sns
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

* Start the Express Workflow using the `start-execution` api command with a "message" string in the input payload.
* The Express Workflow will send the user-inputed message to the SNS Topic.
* If the function does not fail the ID is returned in Step Function execution results within a `ticketId` object
* If the Lambda function fails, the Step Functions workflow will retry up to 5 times before exiting with a `status:FAILED` response.


## Example event payload from EventBridge to SNS
```
aws stepfunctions start-sync-execution --name "test" --state-machine-arn {statemachineARN} --input  {\"message\":\"hello\"}"
```

## Testing

Run the following AWS CLI command to send a 'start-execution` comand to start the Step Functions workflow. Note, you must edit the {statemachineARN} placeholder with the ARN of the deployed Step Functions workflow. This is provided in the stack outputs.

1. Subscribe your email address to the SNS topic:
    ```bash
    aws sns subscribe --topic-arn ENTER_YOUR_TOPIC_ARN --protocol email-json --notification-endpoint ENTER_YOUR_EMAIL_ADDRESS
    ```
2. Click the confirmation link delivered to your email to verify the endpoint.
3. send a 'start-execution` comand to start the Step Functions workflow:
    ```bash
    aws stepfunctions start-sync-execution  --name "test" --state-machine-arn "{statemachineARN}" --input "{\"message\":\"hello\"}"
    ```
4. The message is delivered to your email address.
    Example Message:
    ```bash         
        {"Input":"You just received a message from the state machine!","Message":"hello"}
    ```

### Example output:

```
    {
        "executionArn": "arn:aws:states:us-east-1:128390386658:express:StateMachineExpressSynctoSNS-zgMLgiaktsPH:StateMachineExpressSynctoSNS-zgMLgiaktsPH:55-5ea97738",
        "startDate": "2021-08-24T16:35:41.819000-05:00"
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