import json
import logging
from typing import Dict, Any

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, str]:
    """
    Lambda function handler that returns a greeting message.
    
    Args:
        event: Lambda event containing optional 'name' field
        context: Lambda context object
        
    Returns:
        Dictionary with greeting response
    """
    logger.info(f"Processing event: {json.dumps(event)}")
    
    name = event.get('name', 'World')
    
    response = {
        'response': f'Hello {name}'
    }
    
    logger.info(f"Returning response: {json.dumps(response)}")
    
    return response