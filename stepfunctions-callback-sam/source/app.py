import json
import random
import boto3

sqs = boto3.client('sqs')
sfn = boto3.client('stepfunctions')

def lambda_handler(event, context):
  
  for record in event['Records']:
    body = json.loads(record['body'])
    taskToken = body['myTaskToken']
    
    params = {
      'output': '"Payment processed successfully."',
      'taskToken': taskToken
    }

    try:
        # Randomly call StepFunctions API
        if random.random() < 0.5:
          print(f"Calling SendTaskSuccess for {taskToken}")
          sfn.send_task_success(output=params['output'], taskToken=taskToken)
        else:
          print(f"Calling SendTaskFailure for {taskToken}")  
          sfn.send_task_failure(taskToken=taskToken, error='Failed to process payment', cause='Invalid Credit Card')
    except Exception as e:
        print(e)
        raise e
        
  return {
    'statusCode': 200,
    'body': json.dumps('Processed SQS messages')
  }