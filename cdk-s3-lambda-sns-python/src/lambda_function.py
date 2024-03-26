import os
import boto3

def lambda_handler(event, context):

  print("S3 Put Event Detected")

  # Get the object from the event
  bucket = event['Records'][0]['s3']['bucket']['name'] 
  key = event['Records'][0]['s3']['object']['key']

  # Print a message
  print(f"File uploaded to bucket {bucket} with key {key}")

  # read sns topic arn from environment variable
  topic_arn = os.environ['TOPIC_ARN']

  # Uncomment to read csv or json files from s3 bucket and apply business logic before sending SNS notifications #
  #read_csv_file(bucket, key)
  #read_json_file(bucket, key)

  # Publish message to sns topic
  sns_client = boto3.client('sns')
  response = sns_client.publish(
      TopicArn=topic_arn,
      Message=f"File uploaded to bucket {bucket} with key {key}",
      Subject="S3 Put Event"    
  )


  return

# function to read csv file from s3 bucket
def read_csv_file(bucket, key):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket, Key=key)
    data = obj['Body'].read().decode('utf-8')
    return data.split(',')

# function to read json file from s3 bucket
def read_json_file(bucket, key):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket, Key=key)
    data = obj['Body'].read().decode('utf-8')
    return data
