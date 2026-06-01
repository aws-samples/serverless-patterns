import boto3
import os
from typing import Dict, Any
from datetime import datetime

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    """Simple data storage function that saves to DynamoDB"""
    
    transformed_data = event['transformed_data']
    execution_id = event['execution_id']
    original_data = event['original_data']
    
    table_name = os.environ['PROCESSED_DATA_TABLE']
    
    print(f"Storing processed data for execution: {execution_id}")
    
    try:
        table = dynamodb.Table(table_name)
        
        # Store processed data in DynamoDB
        item = {
            'execution_id': execution_id,
            'original_data': original_data,
            'transformed_data': transformed_data,
            'stored_at': datetime.utcnow().isoformat(),
            'data_source': original_data.get('data_source', 'unknown'),
            'processing_type': original_data.get('processing_type', 'standard')
        }
        
        table.put_item(Item=item)
        
        return {
            'success': True,
            'execution_id': execution_id,
            'table_name': table_name,
            'stored_at': datetime.utcnow().isoformat()
        }
        
    except Exception as e:
        print(f"Error storing data: {str(e)}")
        return {
            'success': False,
            'execution_id': execution_id,
            'error': str(e)
        }
