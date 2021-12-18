
# Amazon SQS to AWS Lambda

This pattern deploys deploys a Lambda function, an SQS queue. SQS invokes the Lambda function when new messages are available. The CDK application contains the minimum IAM resources required to run the application.

Learn more about this pattern at: https://serverlessland.com/patterns/sqs-lambda-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) (AWS CDK >= 1.124.0) Installed

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
1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

1. Run unit tests:

    ````bash
    python3 -m pytest
    ````


## Example event payload from SQS to Lambda

```
{
    "Records": [
        {
            "messageId": "fa2012777678e969-0a33-4681-ba8f-1234567870",
            "receiptHandle": "1234567890NmjC1234567890qODTr1234561478/XPPk/f0qU4tJtQ1234567890ihWDp8YHKhDr3V1234567890e9amjZhgg1234567890RodR1234567890lwDGpf6oLa8/B/1234567890/Pq+xP/1234567890/1234567890fIV6nFUGs71234567890zsj616CBx912M12345678908rxtUEj1234567890J8d1234567890yDcI9E12345678905mTyYZ41S2cP01NCA1234567890jcalHD1234567890Kio+HFQp1234567890OI7bTs5I7pZJ4pu+BnM8Bcki1234567890aNML5B7S12345678904eYKKcrunp1234567890Qhz7BUWPG41",
            "body": "Test message",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1612966720445",
                "SenderId": "AIDA3DTKMG1234567890",
                "ApproximateFirstReceiveTimestamp": "1612966720455"
            },
            "messageAttributes": {},
            "md5OfBody": "82dfa5549ebc91234567890ece5f",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:patterns-sqs-to-lambda-MySqsQueue-1234567890",
            "awsRegion": "us-east-1"
        }
    ]
}

```
### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a message to the SQS queue and observe the event delivered to the Lambda function:

1. Send the SQS message:
```bash
aws sqs send-message --queue-url ENTER_YOUR_SQS_QUEUE_URL --message-body "Test message"
```
2. Retrieve the logs from the Lambda function:

List the log streams for that log group:
```bash
aws logs describe-log-streams --log-group-name '/aws/lambda/MyFunction' --query logStreams[*].logStreamName
```

Expected result:

```bash
[
    "2021/12/17/[$LATEST]6922e90439514d8195e455360917eaa9"
]

```

Get the log events for that stream:

```bash
aws logs get-log-events --log-group-name '/aws/lambda/MyFunction' --log-stream-name '2021/12/17/[$LATEST]6922e90439514d8195e455360917eaa9'
```

Expected result:

```json
{
    "events": [
        {
            "timestamp": 1639766691013,
            "message": "START RequestId: 3329cdeb-47f5-4269-82af-e7038be754c1 Version: $LATEST\n",
            "ingestionTime": 1639766691392
        },
        {
            "timestamp": 1639766691014,
            "message": "Lambda function invoked\n",
            "ingestionTime": 1639766691392
        },
        {
            "timestamp": 1639766691014,
            "message": "{\"key1\": \"value1\", \"key2\": \"value2\", \"key3\": \"value3\"}\n",
            "ingestionTime": 1639766691392
        },
        {
            "timestamp": 1639766691017,
            "message": "END RequestId: 3329cdeb-47f5-4269-82af-e7038be754c1\n",
            "ingestionTime": 1639766691392
        },
        {
            "timestamp": 1639766691017,
            "message": "REPORT RequestId: 3329cdeb-47f5-4269-82af-e7038be754c1\tDuration: 1.18 ms\tBilled Duration: 2 ms\tMemory Size: 128 MB\tMax Memory Used: 37 MB\tInit Duration: 102.31 ms\t\n",
            "ingestionTime": 1639766691392
        }
    ],
    "nextForwardToken": "f/36568019161407810641321426295023073810994699050339663876/s",
    "nextBackwardToken": "b/36568019161318607660527303802456930937904105604315742208/s"
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
