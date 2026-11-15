import json
import boto3
import os

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

# DynamoDB table name
table_name = os.environ['DYNAMODB_TABLE_NAME']

def lambda_handler(event, context):
    try:
        # Get the S3 bucket and key (file path) from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        # Download the JSON file from S3
        response = s3.get_object(Bucket=bucket_name, Key=key)
        data = json.load(response['Body'])

        # Write the data to the DynamoDB table
        table = dynamodb.Table(table_name)
        table.put_item(Item=data)

        return {
            'statusCode': 200,
            'body': json.dumps('Data successfully written to DynamoDB table!')
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }