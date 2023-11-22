import boto3
import os
import json

client = boto3.client('stepfunctions', region_name='us-west-2')

def main():
    response = client.send_task_success(
        taskToken=os.environ['TASK_TOKEN'],
        output=json.dumps({'message': 'Hello from fargate'})
    )
    print(response)


if __name__ == "__main__":
    main()