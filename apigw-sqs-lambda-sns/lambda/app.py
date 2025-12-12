import json
import boto3
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def publish_to_sns(event_body):
    """Helper function to publish message to SNS"""
    sns = boto3.client('sns')
    
    try:
        # Extract phone number and message from the event body
        phone_number = event_body.get('phoneNumber')
        message = event_body.get('message')
        
        if not phone_number or not message:
            logger.error("Missing phoneNumber or message in event body")
            return
            
        logger.info(f"Publishing message to phone number: {phone_number}")
        logger.info(f"Message: {message}")
        
        # Publish directly to phone number (no topic needed for PoC)
        response = sns.publish(
            PhoneNumber=phone_number,
            Message=message
        )
        
        logger.info(f"SNS publish response: {response}")
        
    except Exception as e:
        logger.error(f"Error publishing to SNS: {str(e)}")
        raise

def lambda_handler(event, context):
    """Main lambda handler function"""
    logger.info(f"Received event: {json.dumps(event)}")
    
    try:
        # Process each SQS record
        for record in event['Records']:
            event_body = json.loads(record['body'])
            publish_to_sns(event_body)
            
        return {
            'statusCode': 200,
            'body': json.dumps('Messages processed successfully')
        }
        
    except Exception as e:
        logger.error(f"Error processing event: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error processing messages: {str(e)}')
        }
