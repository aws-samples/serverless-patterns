
# Amazon SQS to AWS Lambda

This pattern deploys a Lambda function and an SQS queue. SQS invokes the Lambda function when new messages are available. The CDK application contains the minimum IAM resources required to run the application.

Learn more about this pattern at: https://serverlessland.com/patterns/sqs-lambda-cdk

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

Amazon SQS to AWS Lambda

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

1. Send the SQS message:

```bash
aws sqs send-message --queue-url ENTER_YOUR_SQS_QUEUE_URL --message-body "Test message"
```

2. Retrieve the logs from the Lambda function:

List the log streams for that log group:

```bash
aws logs describe-log-streams --log-group-name '/aws/lambda/ENTER_YOUR_FUNCTION_NAME' --query logStreams[*].logStreamName
```

Expected result:

```bash
[
    "2021/12/17/[$LATEST]6922e90439514d8195e455360917eaa9"
]

```

Get the log events for that stream:

```bash
aws logs get-log-events --log-group-name '/aws/lambda/ENTER_YOUR_FUNCTION_NAME' --log-stream-name '2021/12/17/[$LATEST]6922e90439514d8195e455360917eaa9'
```

Expected result:

```json
{
    "events": [
        {
            "timestamp": 1639828317813,
            "message": "START RequestId: bd3f036b-3bf1-5300-8b05-595cf662119c Version: $LATEST\n",
            "ingestionTime": 1639828322765
        },
        {
            "timestamp": 1639828317815,
            "message": "Lambda function invoked\n",
            "ingestionTime": 1639828322765
        },
        {
            "timestamp": 1639828317815,
            "message": "{\"Records\": [{\"messageId\": \"e9671b5f-06d2-413d-98ef-8654e551936c\", \"receiptHandle\": \"AQEBA7X2pC+hls8kgKo9fJF5YBMmw1RIUCOWot6Qk5n3jjRmWBn1L3cMq4N4ZNgBE2qEOUTTFb9lK/p0SDrE60rKgVpO5y/5yXnM9gZN3szzDFJ5LA5y7kN8d0vcjTOZSWquX7mMRkZKkDW6VF0xNldxxKavIbjiBE7jYMLmFbipwyGdQ03qGNJSeVW9S04AnOl38VjRO2UbC3HSkFAIQifma3fDuxsifnVa+x64E5hy9OTmjAS4vkA+e9YdOaS0GUmvMFyiHRokrdGNGwilACl10Rf71vZQOKmX6FLGhLGvO2SCKqDA2WJuQLf3aDJaqSOla3ya+RiY+ZGB0giees+zp4mkR3iCMRMlAfcgNjJpTf9niv3yLzT9U6NvmXQiCRzlxQFekkWo0axrLz32K+jmzebBS6v4DbS1YkrQ3r7ELBpylKW7cqj6bWa91Y+5O40s\", \"body\": \"Test message\", \"attributes\": {\"ApproximateReceiveCount\": \"1\", \"SentTimestamp\": \"1639828317543\", \"SenderId\": \"AROAIQIEPWCCGQ4X4VMOK:azertrezza\", \"ApproximateFirstReceiveTimestamp\": \"1639828317550\"}, \"messageAttributes\": {}, \"md5OfBody\": \"82dfa5549ebc9afc168eb7931ebece5f\", \"eventSource\": \"aws:sqs\", \"eventSourceARN\": \"arn:aws:sqs:us-east-1:xxxxxxxxxxxx:SqsLambdaCdkStack-MyQueueE6CA6235-1F31KU17V75YB\", \"awsRegion\": \"us-east-1\"}]}\n",
            "ingestionTime": 1639828322765
        },
        {
            "timestamp": 1639828317815,
            "message": "END RequestId: bd3f036b-3bf1-5300-8b05-595cf662119c\n",
            "ingestionTime": 1639828322765
        },
        {
            "timestamp": 1639828317815,
            "message": "REPORT RequestId: bd3f036b-3bf1-5300-8b05-595cf662119c\tDuration: 1.35 ms\tBilled Duration: 2 ms\tMemory Size: 128 MB\tMax Memory Used: 37 MB\tInit Duration: 105.23 ms\t\n",
            "ingestionTime": 1639828322765
        }
    ],
    "nextForwardToken": "f/36569393484927409957930658349900755958289816616951021572/s",
    "nextBackwardToken": "b/36569393484882808467533597103617684521744519893939060736/s"
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
