import json
import logging
import re

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def validate_email(email):
    """
    Validate email format
    Args:
        email: Email string to validate
    Returns:
        bool: True if valid email format, False otherwise
    """
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    if not bool(re.match(email_pattern, email)):
        logger.error(f"Invalid email format: {email}")
        return False
    return True

def validate_message_structure(message):
    """
    Validate message structure and required fields.
    Args:
        message: Dictionary containing message data
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    required_fields = ['messageType', 'payload', 'timestamp']
    
    # Check required fields
    if not all(field in message for field in required_fields):
        return False, "Missing required fields"
    
    # Validate message type
    valid_types = ['TYPE_A', 'TYPE_B', 'TYPE_C']
    if message['messageType'] not in valid_types:
        return False, f"Invalid message type: {message['messageType']}"
    
    # Validate payload structure
    if 'email' not in message['payload']:
        return False, "Missing email in payload"
        
    # Validate email format
    if not validate_email(message['payload']['email']):
        return False, f"Invalid email format: {message['payload']['email']}"
    
    # Check system status if present
    if 'systemStatus' in message and message['systemStatus'].lower() == 'unavailable':
        return False, "DOWNSTREAM_ERROR: Target system unavailable"
        
    return True, ""

def lambda_handler(event, context):
    """
    Main Lambda handler function.
    Args:
        event: Lambda event object
        context: Lambda context object
    Returns:
        dict: Response object
    """
    logger.info(f"Processing {len(event['Records'])} messages")
    
    processed_count = 0
    failed_count = 0
    validation_errors = []

    for record in event['Records']:
        try:
            # Parse the message body
            message = json.loads(record['body'])
            message_id = message.get('messageId', 'unknown')
            
            # Validate message
            is_valid, error_message = validate_message_structure(message)
            
            if is_valid:
                # Process valid message
                logger.info(f"Successfully validated message: {message_id}")
                processed_count += 1
                
                # Add your processing logic here
                # process_valid_message(message)
                
            else:
                # Track validation failure
                failed_count += 1
                validation_errors.append({
                    'messageId': message_id,
                    'error': error_message
                })
                logger.warning(f"Validation failed for message {message_id}: {error_message}")
                # Message will automatically go to DLQ due to raised exception
                raise ValueError(error_message)

        except json.JSONDecodeError as e:
            failed_count += 1
            logger.error(f"Invalid JSON in message: {str(e)}")
            raise

        except Exception as e:
            failed_count += 1
            logger.error(f"Error processing message: {str(e)}")
            raise

    return {
        'statusCode': 200,
        'body': json.dumps({
            'processed': processed_count,
            'failed': failed_count,
            'validation_errors': validation_errors
        })
    }
