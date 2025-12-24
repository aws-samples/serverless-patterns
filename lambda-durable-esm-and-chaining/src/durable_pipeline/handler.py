import json
import os
import boto3
from datetime import datetime
from typing import Dict, Any, List
from aws_durable_execution_sdk_python import DurableContext, durable_execution

# Initialize AWS clients
dynamodb = boto3.resource('dynamodb')
lambda_client = boto3.client('lambda')

@durable_execution
def lambda_handler(event: Dict[str, Any], context: DurableContext) -> Dict[str, Any]:
    """
    Main durable pipeline function that processes SQS events directly via ESM.
    Demonstrates lambda invoke chaining with checkpointing and recovery.
    Limited to 15 minutes total execution time due to ESM constraints.
    """
    
    # Extract configuration from environment
    validation_function_arn = os.environ['VALIDATION_FUNCTION_ARN']
    transformation_function_arn = os.environ['TRANSFORMATION_FUNCTION_ARN']
    storage_function_arn = os.environ['STORAGE_FUNCTION_ARN']
    processed_data_table = os.environ['PROCESSED_DATA_TABLE']
    environment = os.environ.get('ENVIRONMENT', 'dev')
    
    print(f"Processing SQS batch with {len(event.get('Records', []))} records")
    
    # Process each SQS record in the batch
    batch_results = []
    
    for record in event.get('Records', []):
        try:
            # Extract data from SQS record
            message_id = record['messageId']
            data = json.loads(record['body'])
            execution_name = f"{environment}-esm-{message_id}"
            
            print(f"Processing record: {message_id}")
            
            # Step 1: Validate data by invoking validation function
            validation_result = context.invoke(
                validation_function_arn,
                {'data': data, 'execution_id': execution_name},
                name=f'validate-data-{message_id}'
            )
            
            if not validation_result.get('is_valid', False):
                batch_results.append({
                    'message_id': message_id,
                    'status': 'failed',
                    'reason': 'validation_failed'
                })
                continue
            
            # Step 2: Transform data by invoking transformation function
            transformation_result = context.invoke(
                transformation_function_arn,
                {'data': data, 'execution_id': execution_name},
                name=f'transform-data-{message_id}'
            )
            
            # Step 3: Store processed data by invoking storage function
            storage_result = context.invoke(
                storage_function_arn,
                {
                    'transformed_data': transformation_result,
                    'execution_id': execution_name,
                    'original_data': data
                },
                name=f'store-data-{message_id}'
            )
            
            batch_results.append({
                'message_id': message_id,
                'status': 'completed',
                'execution_id': execution_name
            })
            
        except Exception as e:
            print(f"Error processing record {record.get('messageId', 'unknown')}: {str(e)}")
            batch_results.append({
                'message_id': record.get('messageId', 'unknown'),
                'status': 'error',
                'error': str(e)
            })
    
    # Return batch processing summary
    successful_records = len([r for r in batch_results if r['status'] == 'completed'])
    failed_records = len([r for r in batch_results if r['status'] in ['failed', 'error']])
    
    return {
        'batch_summary': {
            'total_records': len(batch_results),
            'successful_records': successful_records,
            'failed_records': failed_records
        },
        'record_results': batch_results,
        'processed_at': datetime.utcnow().isoformat()
    }
