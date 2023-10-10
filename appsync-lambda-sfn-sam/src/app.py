import json
import os

import boto3
STATE_MACHINE_ARN = os.environ.get("STATE_MACHINE_ARN")
step_function_client = boto3.client("stepfunctions")
sqs = boto3.client('sqs')


def lambda_handler(event, context):
    print("Lambda function invoked")
    print(json.dumps(event))
    print(json.dumps(event["arguments"]['input']))

    step_function_client.start_execution(
        stateMachineArn=STATE_MACHINE_ARN,
        name=event["arguments"]['input']['id'],
        input="{\"details\":{\"accountId\":\"1234567\",\"bookedStatus\":\"Booked\"}}",

    )

    return True
