"""
Webhook Processor - Lambda durable function
Processes incoming webhook events with automatic checkpointing
"""
import json
import os
import time
import logging
from datetime import datetime
from typing import Dict, Any
from aws_durable_execution_sdk_python import DurableContext, durable_execution
from aws_durable_execution_sdk_python.config import StepConfig
from aws_durable_execution_sdk_python.retries import RetryPresets
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['EVENTS_TABLE_NAME'])


def store_event(execution_token: str, event_data: Dict[str, Any], status: str, 
                current_step: str = None, error: str = None) -> None:
    """Store webhook event and processing state in DynamoDB"""
    timestamp = int(time.time())
    item = {
        'executionToken': execution_token,
        'timestamp': timestamp,
        'status': status,
        'webhookPayload': event_data,
        'createdAt': datetime.utcnow().isoformat(),
        'lastUpdated': datetime.utcnow().isoformat(),
        'ttl': timestamp + (7 * 24 * 60 * 60)
    }
    
    if current_step:
        item['currentStep'] = current_step
    if error:
        item['error'] = error
    
    table.put_item(Item=item)
    logger.info("Stored event", extra={"executionToken": execution_token, "status": status})


@durable_execution
def lambda_handler(event: Dict[str, Any], context: DurableContext) -> Dict[str, Any]:
    """
    Main webhook processor with durable execution
    
    Processes webhooks through 3 checkpointed steps:
    1. Validate payload
    2. Process business logic
    3. Finalize
    """
    execution_token = context.execution_id if hasattr(context, 'execution_id') else str(int(time.time() * 1000))
    
    logger.info("Processing webhook", extra={"executionToken": execution_token})
    webhook_data = event if isinstance(event, dict) else {}
    
    # Step 1: Validate
    def validate_webhook(_) -> Dict[str, Any]:
        logger.info("Step 1: Validating", extra={"executionToken": execution_token})
        
        if not webhook_data:
            error_msg = "Empty webhook payload"
            store_event(execution_token, webhook_data, 'failed', 'validate', error_msg)
            raise ValueError(error_msg)
        
        store_event(execution_token, webhook_data, 'validated', 'validate')
        return {'validated': True, 'timestamp': datetime.utcnow().isoformat()}
    
    validation_result = context.step(
        validate_webhook,
        name='validate-webhook',
        config=StepConfig(retry_strategy=RetryPresets.none())
    )
    
    # Step 2: Process
    def process_business_logic(_) -> Dict[str, Any]:
        logger.info("Step 2: Processing", extra={"executionToken": execution_token})
        
        event_type = webhook_data.get('type', 'unknown')
        source = webhook_data.get('source', 'unknown')
        
        result = {
            'eventType': event_type,
            'source': source,
            'processedAt': datetime.utcnow().isoformat(),
            'recordsProcessed': len(webhook_data.keys())
        }
        
        store_event(execution_token, webhook_data, 'processing', 'business-logic')
        return result
    
    processing_result = context.step(process_business_logic, name='process-business-logic')
    
    # Step 3: Finalize
    def finalize_processing(_) -> Dict[str, Any]:
        logger.info("Step 3: Finalizing", extra={"executionToken": execution_token})
        
        store_event(execution_token, webhook_data, 'completed', 'finalize')
        
        return {
            'executionToken': execution_token,
            'status': 'completed',
            'validation': validation_result,
            'processing': processing_result,
            'completedAt': datetime.utcnow().isoformat()
        }
    
    return context.step(finalize_processing, name='finalize-processing')
