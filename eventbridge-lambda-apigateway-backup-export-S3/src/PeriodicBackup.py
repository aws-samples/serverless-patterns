import json
import boto3
import os
from datetime import datetime
from datetime import date
import botocore


# Create AWS clients
apigw_client = boto3.client('apigateway')
s3_client = boto3.client('s3')
sns_client = boto3.client('sns')

# Get from environment Variables
region = os.environ.get('AWS_REGION')
your_s3_bucket_name = os.environ.get('YOUR_S3_BUCKET_NAME')
parameter_extension = os.environ.get('PARAMETER_EXTENSION')

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

def lambda_handler(event, context):
    
    #Inspect incoming event and capture the option
    print('Incoming Event:' + json.dumps(event))

    # Get all REST APIs
    rest_apis = apigw_client.get_rest_apis()['items']
    
    # Initialize lists to store success and error messages
    success_messages = []
    error_messages = []

    # Iterate over each REST API
    api_resources = []
    for api in rest_apis:
        api_id = api['id']
        api_name = api['name']
        print('API ID = ' + api_id)
        print('API Name = ' + api_name)

        # List all stages for the REST API
        stages = apigw_client.get_stages(restApiId=api_id)

        # Iterate over the stages and print their names for reference
        for stage in stages['item']:
            stage_name = stage['stageName']
            print('Stage Name = '+ stage_name)
            
            export_response = apigw_client.get_export(
                        restApiId=api_id,
                        stageName=stage_name,
                        exportType='swagger',
                        parameters={
                            'extensions': parameter_extension,
                        },
            )
                           
            exported_api = export_response['body'].read().decode('utf-8')
            api_resources = json.loads(exported_api)
            today = datetime.now().strftime('%Y-%m-%d_%H-%M')

        # Save the API resources as a JSON file in S3
        try:
            s3_bucket_name = your_s3_bucket_name
            s3_key = f'{today}-{parameter_extension}/{api_id}.json'
            put_response = s3_client.put_object(
                Bucket=s3_bucket_name,
                Key=s3_key,
                Body=json.dumps(api_resources, cls=DatetimeEncoder, indent=2).encode('utf-8')
            )
            success_messages.append(f"API Gateway with '{s3_key}' and {parameter_extension} uploaded successfully to S3 bucket '{s3_bucket_name}'.")
        except Exception as e:
            error_messages.append(f"Error exporting file API Gateway with '{s3_key}' and {parameter_extension} to S3 bucket '{s3_bucket_name}': {str(e)}")

    # Check if any errors occurred
    if error_messages:
        # Join the error messages into a single string
        error_message = "\n".join(error_messages)
    
        # Send an error notification via SNS
        sns_client.publish(
            TopicArn=os.environ.get("SNS_TOPIC_ARN"),
            Message=error_message,
            Subject='API Gateway export notification: Failed'
        )
        return {
            'statusCode': 500,
            'body': f"Failure notification sent via SNS: {error_message}"
        }
    else:
        # Join the success messages into a single string
        success_message = "\n".join(success_messages)
        
        # Send a success notification via SNS
        sns_client.publish(
            TopicArn=os.environ.get("SNS_TOPIC_ARN"),
            Message=success_message,
            Subject='API Gateway export notification: Success'
        )
        return {
            'statusCode': 200,
            'body': f"Success notification sent via SNS: {success_message}"
        }