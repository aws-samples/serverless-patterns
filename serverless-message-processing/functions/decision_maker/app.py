import json
import re
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

# Email validation pattern
EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def fix_email(email):
    """
    Attempt to fix common email format issues
    Can be amended to other scenarios e.g. Downstream issues
    """
    # Remove multiple @ symbols, keep the last one
    if email.count('@') > 1:
        parts = email.split('@')
        email = f"{parts[0]}@{parts[-1]}"
    
    # Remove spaces
    email = email.strip().replace(' ', '')
    
    # Fix common typos in domain extensions
    common_fixes = {
        '.con': '.com',
        '.vom': '.com',
        '.comm': '.com',
        '.orgg': '.org',
        '.nett': '.net'
    }
    
    for wrong, right in common_fixes.items():
        if email.endswith(wrong):
            email = email[:-len(wrong)] + right
    
    return email

def can_fix_email(message):
    """
    Check if the email in the message can be fixed
    """
    if 'email' not in message:
        return False
        
    email = message['email']
    fixed_email = fix_email(email)
    
    return bool(re.match(EMAIL_PATTERN, fixed_email))


def lambda_handler(event, context):
    """
    Processes messages from a DLQ that have already failed to be automatically processed, 
    and attempts automated remediation and redelivery of the messages back to the main queue. 
    If no suitable fixes can be applied, messages end up in a fatal DLQ where the typical 
    approach of human intervention is required. 

    Flow:
    1. Attempt to fix message
    2. If fixable -> Main Queue
    3. If unfixable -> Fatal DLQ
    
    Extension points:
    1. Add more sophisticated routing logic- including a delay queue 
    2. Implement custom error handling
    3. Add message transformation
    4. Implement retry mechanisms
    5. Add monitoring and metrics

   """
    processed_count = 0
    
    for record in event['Records']:
        try:
            # Parse the message body
            message = json.loads(record['body'])
            original_message_id = record.get('messageId', 'unknown')
            
            logger.info(f"Processing failed message: {original_message_id}")
            
           
                

            # Option A: Try to fix malformed email

            if can_fix_email(message) and not re.match(EMAIL_PATTERN, message['email']):
                fixed_email = fix_email(message['email'])
                logger.info(f"Fixed email from '{message['email']}' to '{fixed_email}'")
                
                # Update the message with fixed email
                message['email'] = fixed_email
                message['emailWasFixed'] = True
                
                # Send back to main queue
                sqs.send_message(
                    QueueUrl=MAIN_QUEUE_URL,
                    MessageBody=json.dumps(message)
                )
              
                logger.info(f"Sent fixed message back to main queue: {original_message_id}")   

            # Option B: Cannot fix - send to fatal DLQ
            else:
                logger.warning(f"Message cannot be fixed, sending to fatal DLQ: {original_message_id}")
                
                # Add failure reason if not present
                if 'failureReason' not in message:
                    message['failureReason'] = 'Unrecoverable error - could not fix message'
                
                # Send to fatal DLQ
                sqs.send_message(
                    QueueUrl=FATAL_DLQ_URL,
                    MessageBody=json.dumps(message)
                )
             
            processed_count += 1
            
        except Exception as e:
            logger.error(f"Error processing message {original_message_id}: {str(e)}")
            # If we can't process the decision, send to fatal DLQ
            try:
                error_message = {
                    'originalMessage': record['body'],
                    'failureReason': f"Decision maker error: {str(e)}",
                    'timestamp': context.invoked_function_arn
                }
                sqs.send_message(
                    QueueUrl=FATAL_DLQ_URL,
                    MessageBody=json.dumps(error_message)
                )
               
            except Exception as fatal_e:
                logger.critical(f"Could not send to fatal DLQ: {str(fatal_e)}")
                raise

    return {
        'statusCode': 200,
        'body': json.dumps({
            'processedMessages': processed_count
        })
    }
