import json
from typing import Dict, Any

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    try:
        # Extract user context from authorizer (JWT already verified)
        request_context = event.get('requestContext', {})
        authorizer = request_context.get('authorizer', {})
        
        # Get basic user info from JWT
        user_id = authorizer.get('userId', 'unknown')
        scope = authorizer.get('scope', '')
        
        # Simple success response
        response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'success': True,
                'message': 'JWT verification successful - Connection established',
                'user': user_id,
                'scope': scope,
                'timestamp': context.get_remaining_time_in_millis()
            })
        }
        
        # Print successful connection
        print(f" JWT verification successful - User {user_id} connected successfully")
        return response
        
    except Exception as e:
        print(f" Error: {str(e)}")
        
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'success': False,
                'message': 'JWT verification failed - Connection error',
                'error': str(e)
            })
        }
