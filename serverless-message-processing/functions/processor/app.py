import json
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def validate_message_structure(message):
    """
    Validate message structure and required fields.
    Args:
        message: Dictionary containing message data
    Returns:
        bool: True if valid message structure, False otherwise
    """
    required_fields = ['messageType', 'payload', 'timestamp']
    return all(field in message for field in required_fields)

def process_message(message):
    """
    Process the message content.
    Args:
        message: Dictionary containing message data
    Returns:
        bool: True if processing successful, False otherwise
    """
    try:
        # Validate message structure
        if not validate_message_structure(message):
            logger.error("Message missing required fields")
            raise ValueError("Invalid message structure")

        message_type = message['messageType']
        payload = message['payload']
        
        # Validate message type
        valid_types = ['TYPE_A', 'TYPE_B', 'TYPE_C']
        if message_type not in valid_types:
            logger.error(f"Invalid message type: {message_type}")
            raise ValueError(f"Invalid message type: {message_type}")

        # Check for downstream system status
        if 'systemStatus' in message and message['systemStatus'].lower() == 'unavailable':
            logger.error("Target system is unavailable")
            raise ValueError("DOWNSTREAM_ERROR: Target system unavailable")

        # Process the message based on type
        logger.info(f"Processing message type: {message_type}")
        
        # Add type-specific processing logic here
        if message_type == 'TYPE_A':
            # Process TYPE_A messages
            pass
        elif message_type == 'TYPE_B':
            # Process TYPE_B messages
            pass
        elif message_type == 'TYPE_C':
            # Process TYPE_C messages
            pass

        return True

    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        raise

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
    downstream_errors = 0

    for record in event['Records']:
        try:
            # Parse the message body
            message = json.loads(record['body'])
            
            # Process the message
            if process_message(message):
                processed_count += 1
                logger.info(f"Successfully processed message: {message.get('messageId', 'unknown')}")
            else:
                failed_count += 1
                logger.warning(f"Message processing returned False: {message.get('messageId', 'unknown')}")

        except json.JSONDecodeError as e:
            failed_count += 1
            logger.error(f"Invalid JSON in message: {str(e)}")
            raise

        except ValueError as e:
            if "DOWNSTREAM_ERROR" in str(e):
                downstream_errors += 1
                logger.error("Downstream error detected")
                raise
            failed_count += 1
            logger.error(f"Validation error: {str(e)}")
            raise

        except Exception as e:
            failed_count += 1
            logger.error(f"Unexpected error processing message: {str(e)}")
            raise

    return {
        'statusCode': 200,
        'body': json.dumps({
            'processed': processed_count,
            'failed': failed_count,
            'downstream_errors': downstream_errors
        })
    }
