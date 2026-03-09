from typing import Dict, Any

def lambda_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    """Simple data validation function"""
    
    data = event['data']
    execution_id = event['execution_id']
    
    print(f"Validating data for execution: {execution_id}")
    
    # Simple validation: check if required fields exist
    required_fields = ['data_source', 'processing_type']
    missing_fields = [field for field in required_fields if not data.get(field)]
    
    is_valid = len(missing_fields) == 0
    
    return {
        'is_valid': is_valid,
        'execution_id': execution_id,
        'missing_fields': missing_fields,
        'data_source': data.get('data_source', 'unknown')
    }
