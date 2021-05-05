# AWS Step Functions Standard Workflow to Amazon SQS, with no callback 

The SAM template deploys a Step Functions workflow, that takes in a payload and sends part of it to an Amazon SQS. In this pattern, the state machine 
DOES NOT WAIT for a callback from the queue. The SAM template contains the minimum IAM resources required to run the application.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-sqs

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
2. Change directory to the pattern directory:
    ```
    cd sfn-sqs
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

* Start the Step Function execution with the sample event payload 
* As part of the execution, part of the payload (the `message` attribute of the payload) gets pushed to the queue
* Run the cli command to pull messages from the queue to verify if the message got delivered.

## Testing

Run the following AWS CLI command to send a 'start-execution` command to start the Step Functions workflow. Note, you must edit the {StateMachineExpressSynctoLambda} placeholder with the ARN of the deployed Step Functions workflow. This is provided in the stack outputs.

```bash
aws stepfunctions start-execution  --name "test" --state-machine-arn "{StateMachinetoSQS}" --input "{\"message\": {\"hello\" : \"world\" } }"
```

### output:

```bash
{
    "executionArn": "arn:aws:states:us-east-1:123456789012:execution:MyStateMachine-LIXV3ls6HtnY:test",
    "startDate": 1620244153.977
}
```

Note the `executionArn` from the above output and run the below  cli command to get the status of the execution

```bash
aws stepfunctions describe-execution --execution-arn  "{executionArn}"
```

### Get execution status output:

```bash
{
    "executionArn": "arn:aws:states:us-east-1:123456789012:execution:MyStateMachine-LIXV3ls6HtnY:test",
    "stateMachineArn": "arn:aws:states:us-east-1:123456789012:stateMachine:MyStateMachine-LIXV3lsV8tnY",
    "name": "60805db6-ca0a-44ee-b280-c6a44c5578a1",
    "status": "SUCCEEDED",
    "startDate": 1620244175.722,
    "stopDate": 1620244175.849,
    "input": "{\"message\": {\"hello\" : \"world\" } }",
    "inputDetails": {
        "included": true
    },
    "output": "{\"MD5OfMessageBody\":\"fbc24bcc7a1794758fc1327fcfebdaf6\",\"MessageId\":\"faec3da7-cb2c-4b72-9cc8-98fdc4e72773\",\"SdkHttpMetadata\":{\"AllHttpHeaders\":{\"x-amzn-RequestId\":[\"522cc894-5c35-493d-a1ce-f95e71162dfd\"],\"Content-Length\":[\"378\"],\"Date\":[\"Wed, 05 May 2021 19:49:35 GMT\"],\"Content-Type\":[\"text/xml\"]},\"HttpHeaders\":{\"Content-Length\":\"378\",\"Content-Type\":\"text/xml\",\"Date\":\"Wed, 05 May 2021 19:49:35 GMT\",\"x-amzn-RequestId\":\"522cc894-5c35-493d-a1ce-f95e71162dfd\"},\"HttpStatusCode\":200},\"SdkResponseMetadata\":{\"RequestId\":\"522cc894-5c35-493d-a1ce-f95e71162dfd\"}}",
    "outputDetails": {
        "included": true
    }
}
```
Once the `status` is `SUCCEEDED`, we can verify if the message got delivered to the SQS or not by running the below command

```bash
aws sqs receive-message --queue-url  "{MyQueueURL}"
```

### Queue Message output:

```bash
{
    "Messages": [
        {
            "MessageId": "3f7fb159-df5f-4acd-a127-f535064a73fd",
            "ReceiptHandle": "AQEBi9nc1QjBPdjVNfoIBz0F7momTMA0EdMCv4UkQAQEBi9nc1QjBPdjVNfoIBz0F7momTMA0EdMCv4UkQ",
            "MD5OfBody": "fbc24bcc7a1794758fc1327fcfebdaf6",
            "Body": "{\"hello\":\"world\"}"
        }
    ]
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
