# Amazon Kinesis Data Streams to AWS Lambda with event filtering

This pattern demonstrates the ability configure Amazon Kinesis as an event source for AWS Lambda to use event filtering to control which records are sent to your function for processing. The pattern deploys a Kinesis data stream and Lambda functions that are subscribed to the stream with different event filter configurations.

Review [Filter rule syntax](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-syntax) for more details on the event filtering configuration.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/kinesis-data-stream-lambda-esm-cdk-python/

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd kinesis-data-stream-lambda-esm-cdk-python/cdk
    ```
1. Create a Python virtual environment
    ```
    python -m venv .venv
    ```
1. Activate the virtualenv
    ```
    source .venv/bin/activate
    ```

    If you are using a Windows platform, you would activate the virtualenv like this:
    ```
    .venv\Scripts\activate.bat
    ```
2. After the virtualenv is activated, you can install the required dependencies.
    ```
    pip install -r requirements.txt
    ```
3. Bootstrap your AWS account and Region (if you have not already done so)
    ```
    cdk bootstrap
    ```
4. Deploy the stack to your AWS account and region.
    ```
    cdk deploy
    ```

## How it works

Multiple Lambda functions and a Kinesis data stream are created with Kinesis configured as the event source. Event source mappings are created with different event filter settings to demonstrate how filtering settings affect which events are sent to the Lambda functions for processing.



## Testing

You can execute a test Python script to write sample records to the stream.

```bash
python scripts/producer.py
```

### Example Records


```json
{
    'EVENT_TIME': '2023-12-21T16:43:09.730234',
    'SENSOR_ID': '4d894af2-aea5-4a38-bcc0-336b8741f476',
    'VALUE': 65.9,
    'STATUS': 'WARN'
}
```

```json
{
    'EVENT_TIME': '2023-12-21T16:43:09.889185',
    'SENSOR_ID': '8be06d7d-9278-4ba0-93d2-567bebbde784',
    'VALUE': 49.62,
    'STATUS': 'OK'
}
```

```json
{
    'EVENT_TIME': '2023-12-21T16:43:10.005793',
    'SENSOR_ID': 'eb560fc8-bb0b-4032-8229-69d864d2e7d5',
    'VALUE': 31.81,
    'STATUS': 'FAIL'
}
```

### Viewing test results

Navigate to the CloudWatch console and inspect messages logged to the log groups named similar to those listed below:

| Log Group | Event filter pattern(s) | Comment |
| --- | --- | --- |
| /aws/lambda/KinesisLambdaStack-LambdaConsumerNoFilter | N/A | logs all records |
| /aws/lambda/KinesisLambdaStack-LambdaConsumerFailStatus | `{"data":{"STATUS":["FAIL"]}}` |  logs records where STATUS equals FAIL |
| /aws/lambda/KinesisLambdaStack-LambdaConsumerNotOkStatus | `{"data":{"STATUS":[{"anything-but":["OK"]}]}}`| logs records where STATUS is not "OK" |
| /aws/lambda/KinesisLambdaStack-LambdaConsumerWarnValue | `{"data":{"STATUS":["WARN"], "VALUE":[{"numeric":[">",0,"<=",80]}]}}`| logs records where STATUS is "WARN" **and** VALUE is between 0 and 80 (inclusive) |
| /aws/lambda/KinesisLambdaStack-LambdaConsumerWarnLessValue | `{"data":{"STATUS":["WARN"]}}` and `{"data":{"VALUE":[{"numeric":["<",80]}]}}` | logs records where STATUS is "WARN" **or** VALUE is greater than 80 |


## Cleanup

1. Run the following command to delete the resources

```bash
cdk destroy
```


----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0