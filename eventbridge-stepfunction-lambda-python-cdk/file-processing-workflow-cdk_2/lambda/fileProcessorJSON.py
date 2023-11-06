import json
import boto3
import os



def lambda_handler(event, context):
    destination_bucket_name = os.getenv("destination_bucket_name", default=None)
    print(destination_bucket_name)

    # Extracting information from the event payload
    try:
        bucket_name = event['body']['bucket_name']
        object_key = event['body']['object_key']
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': f'Invalid event payload. Missing key: {str(e)}'
        }

    # Initializing S3 client
    s3 = boto3.client('s3')

    try:
        # Read the JSON file from S3 bucket
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        json_data = json.loads(response['Body'].read().decode('utf-8'))

        # Transform the "jobTitleName" from "Developer" to "Engineer"
        for employee in json_data['Employees']:
            if employee['jobTitleName'] == 'Developer':
                employee['jobTitleName'] = 'Engineer'

        # Convert the modified JSON data back to a string
        updated_json = json.dumps(json_data)

        # Save the updated JSON back to the S3 bucket (optional)
        s3.put_object(Bucket=destination_bucket_name, Key=object_key, Body=updated_json)

        return {
            'statusCode': 200,
            'body': updated_json
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
