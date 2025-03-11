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

def fix_email(email):
    """
    Attempt to fix common email format issues
    Args:
        email: String containing malformed email
    Returns:
        str: Fixed email or original if unfixable
    """
    try:
        logger.info(f"Starting email fix attempt for: {email}")
        
        # Remove whitespace
        email = email.strip()
        
        # Handle multiple @ symbols
        if email.count('@') > 1:
            parts = email.split('@')
            email = f"{parts[0]}@{parts[-1]}"
            logger.info(f"Fixed multiple @ symbols. Result: {email}")
        
        # Common domain typo fixes
        domain_fixes = {
            '.con': '.com',
            '.vom': '.com',
            '.comm': '.com',
            '.orgg': '.org',
            '.nett': '.net',
            '.ckm': '.com',
            '.cm': '.com'
        }
        
        original_email = email
        for wrong, right in domain_fixes.items():
            if email.endswith(wrong):
                email = email[:-len(wrong)] + right
                logger.info(f"Fixed domain from {wrong} to {right}. Before: {original_email}, After: {email}")
                break
                
        return email
    except Exception as e:
        logger.error(f"Error fixing email: {str(e)}")
        return None

def validate_fixed_email(email):
    """
    Validate fixed email format.
    Args:
        email: String containing fixed email
    Returns:
        bool: True if valid email format, False otherwise
    """
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\$'
    return bool(re.match(email_pattern, email))

def lambda_handler(event, context):
    """
    Processes messages from a DLQ that have failed validation, 
    attempting to fix common email format issues.
    If fixed successfully, messages are sent back to the main queue.
    If unfixable, messages are sent to a fatal DLQ.
    
    Flow:
    1. Extract email from failed message
    2. Attempt to fix common issues
    3. If fixed → Main Queue
    4. If unfixable → Fatal DLQ
    
    Extension points:
    1. Add more sophisticated routing logic- including a delay queue 
    2. Implement custom error handling
    3. Add message transformation
    4. Implement retry mechanisms
    5. Add monitoring and metrics

    Args:
        event: Lambda event object containing SQS messages
        context: Lambda context object
    Returns:
        dict: Processing summary with counts and batchItemFailures
    """
    processed_count = 0
    fixed_count = 0
    fatal_count = 0
    failed_message_ids = []

    logger.info(f"Starting to process batch of {len(event['Records'])} messages")
    
    for record in event['Records']:
        original_message_id = "unknown"
        try:
            # Parse the failed message
            message = json.loads(record['body'])
            original_message_id = message.get('messageId', 'unknown')
            
            # Detailed message content logging
            logger.info(f"Processing message content: {json.dumps(message, indent=2)}")
            
            # Check if message has already been remediated
            if 'remediation' in message:
                logger.info("Message already remediated, skipping processing")
                continue

            # Extract email from payload
            if 'payload' in message and 'email' in message['payload']:
                original_email = message['payload']['email']
                
                # Attempt to fix email
                fixed_email = fix_email(original_email)
                
                if fixed_email and validate_fixed_email(fixed_email):
                    # Update message with fixed email
                    message['payload']['email'] = fixed_email
                    message['remediation'] = {
                        'original_email': original_email,
                        'fixed_email': fixed_email,
                        'timestamp': context.invoked_function_arn
                    }
                    
                    # Send back to main queue
                    sqs.send_message(
                        QueueUrl=MAIN_QUEUE_URL,
                        MessageBody=json.dumps(message)
                    )
                    fixed_count += 1
                else:
                    # Send to fatal DLQ if unfixable
                    message['failureReason'] = 'Email could not be remediated'
                    sqs.send_message(
                        QueueUrl=FATAL_DLQ_URL,
                        MessageBody=json.dumps(message)
                    )
                    fatal_count += 1
            else:
                # Send to fatal DLQ if message structure is invalid
                message['failureReason'] = 'Invalid message structure - missing email in payload'
                sqs.send_message(
                    QueueUrl=FATAL_DLQ_URL,
                    MessageBody=json.dumps(message)
                )
                fatal_count += 1
            
            processed_count += 1
            
        except Exception as e:
            logger.error(f"Error processing message {original_message_id}: {str(e)}")
            # Add message ID to failed messages list
            failed_message_ids.append(record['messageId'])
            try:
                error_message = {
                    'originalMessage': record['body'],
                    'failureReason': f"Remediation error: {str(e)}",
                    'timestamp': context.invoked_function_arn
                }
                sqs.send_message(
                    QueueUrl=FATAL_DLQ_URL,
                    MessageBody=json.dumps(error_message)
                )
                fatal_count += 1
            except Exception as fatal_e:
                logger.critical(f"Could not send to fatal DLQ: {str(fatal_e)}")

    # Execution summary
    logger.info(f"""
    === Execution Summary ===
    Messages Processed: {processed_count}
    Messages Fixed: {fixed_count}
    Messages Fatal: {fatal_count}
    Messages Failed: {len(failed_message_ids)}
    ========================
    """)

    # Return both the processing info and the batch failures for SQS
    result = {
        'batchItemFailures': [{"itemIdentifier": message_id} for message_id in failed_message_ids],
        'processingInfo': {
            'processed': processed_count,
            'fixed': fixed_count,
            'fatal': fatal_count
        }
    }
    
    return result
