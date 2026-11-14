# AWS Step Functions callback integration pattern

This pattern shows how to integrate Step Functions workflows with external systems using Sqs and Lambda. Learn more about this pattern at: https://serverlessland.com/patterns/sfn-callback-cdk.

This pattern deploys a Step Function, a Lambda function and an SQS queue.

The Step Function has one task which will send a message to the SQS queue and waits for a token to be send back. The message contains the input of the task and a token.
The Lambda function is used to call to Step Functions API with the token.
Between the SQS queue and the Lambda function we imagine having an external service that consumes the message from the SQS queue and calls the Lambda function with the token.

Learn more about Step Functions callbacks https://aws.amazon.com/blogs/compute/integrating-aws-step-functions-callbacks-and-external-systems

![Architecture](img/step_function_callback.drawio.png)

The CDK application contains the minimum IAM resources required to run the application.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK >= 2.2.0) Installed

## Language

Python

## Framework

CDK

## Services From/To

AWS Step Functions to Amazon SQS / AWS Lambda to AWS Step Functions

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd sqs-lambda-cdk
    ```
1. Create a virtual environment for python:
    ```bash
    python3 -m venv .venv
    ```
1. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

    If you are in Windows platform, you would activate the virtualenv like this:

    ```
    % .venv\Scripts\activate.bat
    ```

1. Install python modules:
    ```bash
    python3 -m pip install -r requirements.txt
    ```
1. From the command line, use CDK to synthesize the CloudFormation template and check for errors:

    ```bash
    cdk synth
    ```
1. From the command line, use CDK to deploy the stack:

    ```bash
    cdk deploy
    ```

    Expected result:

    ```bash
    SqsLambdaCdkStack

    Outputs:
    SqsLambdaCdkStack.FunctionName = SqsLambdaCdkStack-MyLambdaFunction67CCA873-OsINMhWgMsXV
    SqsLambdaCdkStack.QueueArn = arn:aws:sqs:us-east-1:xxxxxxxxxxxxx:SqsLambdaCdkStack-MyQueueE6CA6235-1F31KU17V75YB
    SqsLambdaCdkStack.QueueName = SqsLambdaCdkStack-MyQueueE6CA6235-1F31KU17V75YB
    SqsLambdaCdkStack.QueueUrl = https://sqs.us-east-1.amazonaws.com/xxxxxxxxxxxxx/SqsLambdaCdkStack-MyQueueE6CA6235-1F31KU17V75YB
    ```

1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a message to the SQS queue and observe the event delivered to the Lambda function:

1. Start execution of the Step Function, using the Step Function Arn from the AWS CDK deployment outputs:

    ```bash
    aws stepfunctions start-execution --state-machine-arn ENTER_YOUR_STEP_FUNCTION_ARN --input "{\"name\" : \"serverless-pattern\"}"
    ```

    Expected result:

    ```json
    {
        "executionArn": "arn:aws:states:us-east-1:xxxxxxxxxxx:execution:StepFunction1F935F84-n8RLIkg3Z8z3:0f8e9656-4165-4060-b124-0be35488f0c0",
        "startDate": "2021-12-20T17:45:56.042000+01:00"
    }
    ```
1. Check the execution status of the Step Function using the executionArn from previous step

    ```bash
    aws stepfunctions describe-execution --execution-arn ENTER_YOUR_STEP_FUNCTION_EXECUTION_ARN
    ```

    Expected result:

    ```json
    {
        "executionArn": "arn:aws:states:us-east-1:xxxxxxxxxxx:execution:StepFunction1F935F84-n8RLIkg3Z8z3:235b67e0-9131-479f-ae1c-c75a41a0f1c0",
        "stateMachineArn": "arn:aws:states:us-east-1:xxxxxxxxxxx:stateMachine:StepFunction1F935F84-n8RLIkg3Z8z3",
        "name": "235b67e0-9131-479f-ae1c-c75a41a0f1c0",
        "status": "RUNNING",
        "startDate": "2021-12-20T18:59:33.992000+01:00",
        "input": "{\"name\" : \"serverless-pattern\"}",
        "inputDetails": {
            "included": true
        }
    }
    ```

1. Retrieve the message from the SQS queue, using the queue URL from the AWS CDK deployment outputs:

    ```bash
    aws sqs receive-message --queue-url ENTER_YOUR_QUEUE_URL
    ```

    Expected result:

    ```bash
    {
        "Messages": [
            {
                "MessageId": "af1576d9-39a8-4b43-93f0-95bf9b98d649",
                "ReceiptHandle": "AQEBGieGiswxcnQdOO+l9iF2xiqsBUJFnkAH19VPnXYyXBA6RHMXd0jx5emns2K07dDb0cwWLZOGCbCEo54pjVC9UQ7AM9zSSjyY46UTKC6MVdD9enw7Uz2vyGCbfGx1ND7usOaIGlXTavLEhE+Uk4VWuX/F+Co2FwXoPdceyacb/LkjIn7REO2lyBbds82ATz36AVrGxu7UmpKD6dZVnJruqYacnEW88GCy5+nexAx0/pq5lE5o4/3Lg5J27DTBOUnIWTyxKW1/zVoRpG63mh8rJwOCcvjYZuzrHXtoXMCJpOcm9V5icBTNit9kKMl2o3isrIkjuBZ0IqNKbSb1Y74rFGQ1T+AzeyStvSitwP8zACMtLUTUptEkCjUnSqgoFhCKEAXN4GBVdav77IDYFVXLHst+VuhF3SwNvjIkMXPI13nX8ttkm71JX3zJUO7/+OXZ",
                "MD5OfBody": "7b2bbf5552c02df61a808bbc99c8d5bb",
                "Body": "{\"input\":{\"name\":\"serverless-pattern\"},\"token\":\"AAAAKgAAAAIAAAAAAAAAATI4DHzC3fME20tXGZeGnZjfp0HtAdK8gshkk31hr5xzF32DKNyKcrSYmIlj3COSsZfhWDKXfiUt90sUyhyOqNB0CO8BiEglPahMLrCmUYxTxs9YrN4gIOMsAjN8KZZvUn5q275WZVPxl32TMQIdtG1UHUt3zkSDhuxa9qIv0PYMHWIQ08rBcMGAObPZLBW9gilXtQu123No/R8Ga5NRixknkJpoBVuTU+/kcFb0Qcf5i8ahECRcu6Lk0bvgJ+TW/omFHk2YbBzlxb7eFAsAYyj4djTwJalnTW6DYafa4Ll0k5Bp6nlEIfAKFM4BHehxWS945owiXyThvAx2MIHltRG/y3XkQIKuKQXWjgdo6IxXwU1Mog//tPG8ZI80qpnRrqnpIOrCngYb7hX2DccA3XwrsYiO/jqWRGuGMj1FeooMAP+CiQNLLHaF2dTvOIgwu6ZpR4pG7Ka0Gt81gL8q7/YzzUo3G3x7iZfSgyxX5YqvzNap2Fu7S492BYNVzngiI9Q9f0A8wt/NdrCmMfF9TV0U6qFcPqCTx/XqSbAWNQeTM3+VtgCSyMzghRR8vYEHYP3TDbr8KOdKxgd9wM4q4FQxPzsoZK1wb+gjk3+v0O9aCReTbiFJdd1ItjmaCG1jtQ==\"}"
            }
        ]
    }
    ```

    Note the value of the token field, we will use this to pass it as payload to our Lambda function.

1. Execute the Lambda function with the token as payload:

    ```bash
    aws lambda invoke --function-name ENTER_YOUR_FUNCTION_NAME \
    --cli-binary-format raw-in-base64-out \
    --invocation-type Event \
    --payload "{ \"token\": \"AAAAKgAAAAIAAAAAAAAAATI4DHzC3fME20tXGZeGnZjfp0HtAdK8gshkk31hr5xzF32DKNyKcrSYmIlj3COSsZfhWDKXfiUt90sUyhyOqNB0CO8BiEglPahMLrCmUYxTxs9YrN4gIOMsAjN8KZZvUn5q275WZVPxl32TMQIdtG1UHUt3zkSDhuxa9qIv0PYMHWIQ08rBcMGAObPZLBW9gilXtQu123No/R8Ga5NRixknkJpoBVuTU+/kcFb0Qcf5i8ahECRcu6Lk0bvgJ+TW/omFHk2YbBzlxb7eFAsAYyj4djTwJalnTW6DYafa4Ll0k5Bp6nlEIfAKFM4BHehxWS945owiXyThvAx2MIHltRG/y3XkQIKuKQXWjgdo6IxXwU1Mog//tPG8ZI80qpnRrqnpIOrCngYb7hX2DccA3XwrsYiO/jqWRGuGMj1FeooMAP+CiQNLLHaF2dTvOIgwu6ZpR4pG7Ka0Gt81gL8q7/YzzUo3G3x7iZfSgyxX5YqvzNap2Fu7S492BYNVzngiI9Q9f0A8wt/NdrCmMfF9TV0U6qFcPqCTx/XqSbAWNQeTM3+VtgCSyMzghRR8vYEHYP3TDbr8KOdKxgd9wM4q4FQxPzsoZK1wb+gjk3+v0O9aCReTbiFJdd1ItjmaCG1jtQ==\" }" \
    response.json
    ```

    Expected result:

    ```bash
    {
        "StatusCode": 202
    }
    ```

1. Retrieve the logs from the Lambda function:

    List the log streams for that log group:

    ```bash
    aws logs describe-log-streams --log-group-name '/aws/lambda/ENTER_YOUR_FUNCTION_NAME' --query logStreams[*].logStreamName
    ```

    Expected result:

    ```bash
    [
        "2021/12/20/[$LATEST]6922e90439514d8195e455360917eaa9"
    ]

    ```

    Get the log events for that stream:

    ```bash
    aws logs get-log-events --log-group-name '/aws/lambda/ENTER_YOUR_FUNCTION_NAME' --log-stream-name '2021/12/20/[$LATEST]6922e90439514d8195e455360917eaa9'
    ```

    Expected result:

    ```bash
    START RequestId: 31c1842b-5948-4f5b-a1ff-dad295bb4f1b Version: $LATEST
    Lambda function invoked
    {
        "token": "AAAAKgAAAAIAAAAAAAAAATI4DHzC3fME20tXGZeGnZjfp0HtAdK8gshkk31hr5xzF32DKNyKcrSYmIlj3COSsZfhWDKXfiUt90sUyhyOqNB0CO8BiEglPahMLrCmUYxTxs9YrN4gIOMsAjN8KZZvUn5q275WZVPxl32TMQIdtG1UHUt3zkSDhuxa9qIv0PYMHWIQ08rBcMGAObPZLBW9gilXtQu123No/R8Ga5NRixknkJpoBVuTU+/kcFb0Qcf5i8ahECRcu6Lk0bvgJ+TW/omFHk2YbBzlxb7eFAsAYyj4djTwJalnTW6DYafa4Ll0k5Bp6nlEIfAKFM4BHehxWS945owiXyThvAx2MIHltRG/y3XkQIKuKQXWjgdo6IxXwU1Mog//tPG8ZI80qpnRrqnpIOrCngYb7hX2DccA3XwrsYiO/jqWRGuGMj1FeooMAP+CiQNLLHaF2dTvOIgwu6ZpR4pG7Ka0Gt81gL8q7/YzzUo3G3x7iZfSgyxX5YqvzNap2Fu7S492BYNVzngiI9Q9f0A8wt/NdrCmMfF9TV0U6qFcPqCTx/XqSbAWNQeTM3+VtgCSyMzghRR8vYEHYP3TDbr8KOdKxgd9wM4q4FQxPzsoZK1wb+gjk3+v0O9aCReTbiFJdd1ItjmaCG1jtQ=="
    }

    Token received: AAAAKgAAAAIAAAAAAAAAATI4DHzC3fME20tXGZeGnZjfp0HtAdK8gshkk31hr5xzF32DKNyKcrSYmIlj3COSsZfhWDKXfiUt90sUyhyOqNB0CO8BiEglPahMLrCmUYxTxs9YrN4gIOMsAjN8KZZvUn5q275WZVPxl32TMQIdtG1UHUt3zkSDhuxa9qIv0PYMHWIQ08rBcMGAObPZLBW9gilXtQu123No/R8Ga5NRixknkJpoBVuTU+/kcFb0Qcf5i8ahECRcu6Lk0bvgJ+TW/omFHk2YbBzlxb7eFAsAYyj4djTwJalnTW6DYafa4Ll0k5Bp6nlEIfAKFM4BHehxWS945owiXyThvAx2MIHltRG/y3XkQIKuKQXWjgdo6IxXwU1Mog//tPG8ZI80qpnRrqnpIOrCngYb7hX2DccA3XwrsYiO/jqWRGuGMj1FeooMAP+CiQNLLHaF2dTvOIgwu6ZpR4pG7Ka0Gt81gL8q7/YzzUo3G3x7iZfSgyxX5YqvzNap2Fu7S492BYNVzngiI9Q9f0A8wt/NdrCmMfF9TV0U6qFcPqCTx/XqSbAWNQeTM3+VtgCSyMzghRR8vYEHYP3TDbr8KOdKxgd9wM4q4FQxPzsoZK1wb+gjk3+v0O9aCReTbiFJdd1ItjmaCG1jtQ==
    Token sent to the Step Function
    END RequestId: 31c1842b-5948-4f5b-a1ff-dad295bb4f1b
    REPORT RequestId: 31c1842b-5948-4f5b-a1ff-dad295bb4f1b	Duration: 191.02 ms	Billed Duration: 192 ms	Memory Size: 128 MB	Max Memory Used: 65 MB
    ```

1. Check the execution status of the Step Function

    ```bash
    aws stepfunctions describe-execution --execution-arn ENTER_YOUR_STEP_FUNCTION_EXECUTION_ARN
    ```

    Expected result:

    ```json
    {
        "executionArn": "arn:aws:states:us-east-1:xxxxxxxxxxx:execution:StepFunction1F935F84-n8RLIkg3Z8z3:235b67e0-9131-479f-ae1c-c75a41a0f1c0",
        "stateMachineArn": "arn:aws:states:us-east-1:xxxxxxxxxxx:stateMachine:StepFunction1F935F84-n8RLIkg3Z8z3",
        "name": "235b67e0-9131-479f-ae1c-c75a41a0f1c0",
        "status": "SUCCEEDED",
        "startDate": "2021-12-20T18:59:33.992000+01:00",
        "input": "{\"name\" : \"serverless-pattern\"}",
        "inputDetails": {
            "included": true
        }
    }
    ```

## Cleanup

1. Delete the stack
    ```bash
    cdk destroy
    ```

## Tutorial

See [this useful workshop](https://cdkworkshop.com/30-python.html) on working with the AWS CDK for Python projects.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


Enjoy!
