import json
import os
import boto3
from datetime import datetime

def get_secret_value(secret_arn):
    """Retrieve a secret value from AWS Secrets Manager"""
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_arn)
    return response['SecretString']

def send_sms(phone_number: str, originating_number: str, message: str):
    """Send SMS using AWS End User Messaging"""
    sms_client = boto3.client('pinpoint-sms-voice-v2')
    
    response = sms_client.send_text_message(
        DestinationPhoneNumber=phone_number,
        OriginationIdentity=originating_number,
        MessageBody=message
    )
    
    return response

def lambda_handler(event, context):
    """Main Lambda handler for sending SMS messages"""
    
    # Get configuration from environment variables
    message = os.environ['MESSAGE']
    phone_number = get_secret_value(os.environ['DESTINATION_PHONE_SECRET_ARN'])
    originating_number = get_secret_value(os.environ['ORIGINATION_PHONE_SECRET_ARN'])
    
    try:
        # Send SMS
        sms_response = send_sms(phone_number, originating_number, message)
        
        print(f"SMS sent successfully: {message}")
        print(f"SMS Message ID: {sms_response.get('MessageId')}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'SMS message sent successfully!',
                'sms_message_id': sms_response.get('MessageId'),
                'timestamp': datetime.now().isoformat()
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Failed to send SMS message',
                'details': str(e),
                'timestamp': datetime.now().isoformat()
            })
        }