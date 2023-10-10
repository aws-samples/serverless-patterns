import json
import os

import boto3

step_function_client = boto3.client("stepfunctions")

step_functions_arn = os.environ['STEP_FNS_ARN']


def handler(event, context):

    print("Lambda function invoked")
    print(json.dumps(event))
    print('step functions arn is ',step_functions_arn);

    response = step_function_client.start_execution(
        stateMachineArn=step_functions_arn,
        name=event["arguments"]['input']['id'],
        input="{\"details\":{\"accountId\":\"1234567\",\"bookedStatus\":\"Booked\"}}",

    )

    return {"id": event["arguments"]['input']['id'], "arn": step_functions_arn}
