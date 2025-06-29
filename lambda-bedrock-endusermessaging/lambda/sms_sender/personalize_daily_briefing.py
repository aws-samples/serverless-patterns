import json
import os
import boto3
from datetime import datetime

def invoke_weather_agent(location: str) -> str:
    """Invoke weather agent to get intelligent summary"""
    
    lambda_client = boto3.client('lambda')
    
    try:
        # Invoke weather agent Lambda
        response = lambda_client.invoke(
            FunctionName=os.environ['WEATHER_AGENT_FUNCTION_NAME'],
            InvocationType='RequestResponse',
            Payload=json.dumps({
                'location': location
            })
        )
        
        # Parse response
        payload = json.loads(response['Payload'].read())
        
        if payload['statusCode'] == 200:
            body = json.loads(payload['body'])
            return body['briefing']
        else:
            # Use fallback from error response
            error_body = json.loads(payload['body'])
            return error_body.get('fallback_message', f"Good morning! Have a great day in {location}!")
            
    except Exception as e:
        print(f"Error invoking weather agent: {str(e)}")
        return f"Good morning! Weather service temporarily unavailable. Have a wonderful day in {location}!"

def get_secret_value(secret_arn):
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
    """Main Lambda handler for daily briefing SMS"""
    
    # Get configuration from environment variables
    location = os.environ['LOCATION']
    phone_number = get_secret_value(os.environ['DESTINATION_PHONE_SECRET_ARN'])
    originating_number = get_secret_value(os.environ['ORIGINATION_PHONE_SECRET_ARN'])

    
    try:
        # Get intelligent briefing from weather agent + Bedrock
        briefing = invoke_weather_agent(location)
        
        # Send SMS
        sms_response = send_sms(phone_number, originating_number, briefing)
        
        print(f"SMS sent successfully: {briefing}")
        print(f"SMS Message ID: {sms_response.get('MessageId')}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Daily briefing sent successfully!',
                'briefing': briefing,
                'sms_message_id': sms_response.get('MessageId'),
                'timestamp': datetime.now().isoformat()
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Failed to send daily briefing',
                'details': str(e),
                'timestamp': datetime.now().isoformat()
            })
        }