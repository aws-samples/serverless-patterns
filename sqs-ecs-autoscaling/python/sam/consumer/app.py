# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

# SPDX-License-Identifier: MIT-0

import os
import boto3
import json
import logging
import time
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize AWS SQS client
sqs = boto3.client('sqs')
queue_url = os.environ.get('QUEUE_URL')

if not queue_url:
    raise ValueError("QUEUE_URL environment variable is required")

def process_message(message_body):
    """
    Process the message from the queue.
    Replace this with your actual message processing logic.
    """
    try:
        data = json.loads(message_body)
        logger.info(f"Processing message: {data}")
        # Add your processing logic here
        
        # Simulate some work
        time.sleep(1)
        
        return True
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        return False

def main():
    logger.info(f"Starting SQS consumer for queue: {queue_url}")
    
    while True:
        try:
            # Receive messages from SQS queue
            response = sqs.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=10,  # Fetch up to 10 messages at once
                WaitTimeSeconds=20,      # Long polling
                VisibilityTimeout=30      # 30 seconds to process each message
            )

            messages = response.get('Messages', [])
            
            if not messages:
                logger.debug("No messages received")
                continue

            logger.info(f"Received {len(messages)} messages")

            for message in messages:
                message_body = message['Body']
                receipt_handle = message['ReceiptHandle']

                if process_message(message_body):
                    # Delete message after successful processing
                    try:
                        sqs.delete_message(
                            QueueUrl=queue_url,
                            ReceiptHandle=receipt_handle
                        )
                        logger.info("Message processed and deleted successfully")
                    except ClientError as e:
                        logger.error(f"Error deleting message: {e}")
                else:
                    logger.error("Failed to process message")

        except ClientError as e:
            logger.error(f"Error receiving messages: {e}")
            time.sleep(5)  # Wait before retrying
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            time.sleep(5)  # Wait before retrying

if __name__ == "__main__":
    main()