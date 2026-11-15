import csv
import boto3
import json

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table_name = 'employeeInfoNew'

def lambda_handler(event, context):
    table = dynamodb.Table(table_name)
    # Iterate through the records in the event
    for record in event['Records']:
        body = json.loads(record['body'])
        bucket = body['Records'][0]['s3']['bucket']['name']
        key = body['Records'][0]['s3']['object']['key']
        # Fetch the CSV file from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        csv_data = response['Body'].read().decode('utf-8').splitlines()

        # Parse the CSV file
        csv_reader = csv.DictReader(csv_data)
        for row in csv_reader:
            
            name = row['name']
            email = row['email']
            
            item = {
                
                'name': row['name'],
                'email': row['email']
            }

            print(f"Received record: name={name}, email={email}")
                        # Insert the item into DynamoDB table
            table.put_item(Item=item)

    print('CSV processing completed.')
