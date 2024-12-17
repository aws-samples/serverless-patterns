import json
import boto3
import os
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
sqs = boto3.client('sqs')

# Environment variables
MAIN_QUEUE_URL = os.environ['MAIN_QUEUE_URL']
FATAL_DLQ_URL = os.environ['FATAL_DLQ_URL']

def can_fix_message(message):
    """
    Determine if a message can be fixed automatically.
    
    Extension points:
    1. Add validation for specific message formats
    2. Implement business-specific fix rules
    3. Add data transformation logic
    4. Implement retry strategies
    5. Add validation against external systems
    """
    try:
        # Basic message validation
        # Add your validation logic here
        return True
    except Exception as e:
        logger.error(f"Validation error: {str(e)}")
        return False

def fix_message(message):
    """
    Apply fixes to the message.
    
    Extension points:
    1. Add data normalization
    2. Implement field-specific fixes
    3. Add data enrichment
    4. Implement format conversion
    5. Add validation rules
    """
    try:
        fixed_message = message.copy()
        # Add your fix logic here
        fixed_message['wasFixed'] = True
        return fixed_message
    except Exception as e:
        logger.error(f"Fix error: {str(e)}")
        return None

def lambda_handler(event, context):
    """
    Process messages and route them based on fixability.
    
    Flow:
    1. Attempt to fix message
    2. If fixable -> Main Queue
    3. If unfixable -> Fatal DLQ
    
    Extension points:
    1. Add more sophisticated routing logic
    2. Implement custom error handling
    3. Add message transformation
    4. Implement retry mechanisms
    5. Add monitoring and metrics
    """
    processed_count = 0
    
    for record in event['Records']:
        message_id = 'unknown'  # Initialize message_id with default value
        
        try:
            message = json.loads(record['body'])
            message_id = record.get('messageId', 'unknown')
            
            logger.info(f"Processing message: {message_id}")
            
            if can_fix_message(message):
                fixed_message = fix_message(message)
                if fixed_message:
                    # Send to main queue
                    sqs.send_message(
                        QueueUrl=MAIN_QUEUE_URL,
                        MessageBody=json.dumps(fixed_message)
                    )
                    logger.info(f"Fixed message sent to main queue: {message_id}")
                else:
                    raise ValueError("Message fix failed")
            else:
                # Send to fatal DLQ
                message['failureReason'] = 'Message cannot be automatically fixed'
                sqs.send_message(
                    QueueUrl=FATAL_DLQ_URL,
                    MessageBody=json.dumps(message)
                )
                logger.warning(f"Message sent to fatal DLQ: {message_id}")
            
            processed_count += 1
            
        except Exception as e:
            logger.error(f"Error processing message {message_id}: {str(e)}")
            try:
                error_message = {
                    'originalMessage': record['body'],
                    'failureReason': str(e),
                    'timestamp': context.invoked_function_arn
                }
                sqs.send_message(
                    QueueUrl=FATAL_DLQ_URL,
                    MessageBody=json.dumps(error_message)
                )
                logger.error(f"Error message sent to fatal DLQ: {message_id}")
            except Exception as fatal_e:
                logger.critical(f"Fatal DLQ error: {str(fatal_e)}")
                raise

    return {
        'statusCode': 200,
        'body': json.dumps({
            'processedMessages': processed_count
        })
    }
