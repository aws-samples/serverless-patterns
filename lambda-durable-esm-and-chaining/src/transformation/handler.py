from typing import Dict, Any
from datetime import datetime

def lambda_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    """Simple data transformation function"""
    
    data = event['data']
    execution_id = event['execution_id']
    
    print(f"Transforming data for execution: {execution_id}")
    
    # Simple transformation: add processing metadata and uppercase data_source
    transformed_data = {
        'original_data': data,
        'data_source': data.get('data_source', '').upper(),
        'processing_type': data.get('processing_type', 'standard'),
        'processed_at': datetime.utcnow().isoformat(),
        'execution_id': execution_id,
        'transformation_applied': 'uppercase_data_source'
    }
    
    return transformed_data
