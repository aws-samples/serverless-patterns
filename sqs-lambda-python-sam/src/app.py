import json
import random
import time
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def process_sqs_message(record):
    """
    Process individual SQS record
    
    Args:
        record (dict): The SQS record to process
        
    Returns:
        dict: Processing result with success status
    """
    try:
        # Randomly fail some messages for demonstration
        if random.random() < 0.2:
            logger.info(f"Randomly failing message: {record['body']}")
            raise Exception('Random processing failure')

        # Extract message body
        message_body = record['body']
        
        logger.info(f"Processing message: {record['messageId']}")
        # Simulate some processing, add your business logic here
        time.sleep(0.1)

        logger.info(f"Successfully processed message: {record['body']}")
        return {"success": True}
    except Exception as error:
        logger.error(f"Failed to process record {record['messageId']}: {str(error)}")
        return {"success": False}

def lambda_handler(event, context):
    """
    AWS Lambda handler for processing SQS messages
    
    Args:
        event (dict): Lambda event containing SQS records
        context (LambdaContext): Lambda context
        
    Returns:
        dict: Response containing batch item failures
    """
    logger.info(f"Received event: {json.dumps(event, indent=2)}")
    batch_item_failures = []

    # Process each record individually
    for record in event['Records']:
        result = process_sqs_message(record)
        if not result['success']:
            batch_item_failures.append({
                "itemIdentifier": record['messageId']
            })

    # Return the failed items to be returned to the queue
    return {
        "batchItemFailures": batch_item_failures
    } 