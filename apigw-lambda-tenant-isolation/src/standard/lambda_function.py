import json
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# In-memory counter that persists across invocations within the same execution environment
counter = 0

def lambda_handler(event, context):
    """
    Standard Lambda function handler without tenant isolation.
    Maintains a shared counter across all invocations within the same execution environment.
    This function receives tenant headers but CANNOT isolate tenants - demonstrating the problem.
    
    Args:
        event: API Gateway event containing request information
        context: Lambda context object
        
    Returns:
        dict: API Gateway response with counter value and isolation status
    """
    global counter
    
    try:
        # Validate event structure first
        if not isinstance(event, dict):
            logger.error("Invalid event structure: event is not a dictionary")
            return create_error_response(400, 'Bad Request', 'Invalid request format')
        
        # Extract tenant ID from headers (for demonstration purposes)
        headers = event.get('headers', {}) or {}
        # API Gateway may pass headers in different cases, so check both
        tenant_id_from_header = (
            headers.get('x-tenant-id') or 
            headers.get('X-Tenant-Id') or 
            headers.get('X-TENANT-ID')
        )
        
        # Log the incoming request with tenant information
        logger.info(f"Processing standard request - Method: {event.get('httpMethod', 'UNKNOWN')}, Path: {event.get('path', 'UNKNOWN')}, Tenant Header: {tenant_id_from_header}")
        
        # Check if this is a GET request
        http_method = event.get('httpMethod', '')
        if not http_method:
            logger.error("Missing httpMethod in event")
            return create_error_response(400, 'Bad Request', 'Missing HTTP method in request')
        
        if http_method != 'GET':
            logger.warning(f"Unsupported HTTP method: {http_method}")
            return create_error_response(405, 'Method Not Allowed', f'HTTP method {http_method} is not supported. Only GET requests are allowed.')
        
        # Validate path (optional but good practice)
        path = event.get('path', '')
        if path and not path.endswith('/standard'):
            logger.warning(f"Unexpected path: {path}")
        
        # CRITICAL DEMONSTRATION: Without tenant isolation, all tenants share the same counter!
        # This is the problem that tenant isolation solves
        counter += 1
        
        # Log the problematic behavior
        if tenant_id_from_header:
            logger.warning(f"PROBLEM: Tenant '{tenant_id_from_header}' is using shared counter value {counter}! This demonstrates data leakage between tenants.")
        else:
            logger.info(f"Request without tenant header using shared counter value: {counter}")
        
        # Prepare response body - showing the received tenant header but no isolation
        response_body = {
            'counter': counter,
            'tenant_id_received': tenant_id_from_header,  # Show what tenant was requested
            'tenant_id': None,  # But no actual tenant isolation
            'isolation_enabled': False,
            'message': f'Counter incremented successfully - SHARED across all tenants! (Received tenant: {tenant_id_from_header or "none"})',
            'warning': 'This function does NOT provide tenant isolation - all tenants share the same counter!'
        }
        
        # Log the response with warning
        logger.info(f"Returning SHARED counter value {counter} for requested tenant '{tenant_id_from_header}' - NO ISOLATION!")
        
        # Return successful response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Cache-Control': 'no-cache'
            },
            'body': json.dumps(response_body)
        }
        
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {str(e)}")
        return create_error_response(400, 'Bad Request', 'Invalid JSON in request')
    except KeyError as e:
        logger.error(f"Missing required field: {str(e)}")
        return create_error_response(400, 'Bad Request', f'Missing required field: {str(e)}')
    except ValueError as e:
        logger.error(f"Value error: {str(e)}")
        return create_error_response(400, 'Bad Request', f'Invalid value: {str(e)}')
    except Exception as e:
        # Log the error with more context
        logger.error(f"Unexpected error processing request: {str(e)}", exc_info=True)
        
        # Return generic error response for security
        return create_error_response(500, 'Internal Server Error', 'An unexpected error occurred while processing the request')


def create_error_response(status_code, error_type, message):
    """
    Create a standardized error response.
    
    Args:
        status_code (int): HTTP status code
        error_type (str): Type of error
        message (str): Error message
        
    Returns:
        dict: Standardized error response
    """
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache'
        },
        'body': json.dumps({
            'error': error_type,
            'message': message,
            'statusCode': status_code
        })
    }