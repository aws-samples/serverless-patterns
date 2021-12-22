import json
import boto3

step_function_client = boto3.client("stepfunctions")

def handler(event, context):
    print("Lambda function invoked")
    print(json.dumps(event))

    #get the toke from the event
    token = event['token']
    print(f"Token received: {token}")

    #this is the output of the Step Function step
    output = {
        "name": "serverless-pattern"
    }
    output = json.dumps(output)

    #send the token to the Step Function
    step_function_client.send_task_success(
                taskToken=token,
                output=output,
    )
    print("Token sent to Step Function")

    return