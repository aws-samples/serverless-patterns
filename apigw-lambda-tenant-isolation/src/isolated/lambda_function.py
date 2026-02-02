import json
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# In-memory counter that persists across invocations within the same execution environment
# With tenant isolation, each tenant gets their own separate instance of this counter
counter = 0

def lambda_handler(event, context):
    """
    Tenant-isolated Lambda function handler with tenant isolation enabled.
    Maintains separate counters for each tenant using context.tenant_id.
    
    Args:
        event: API Gateway event containing request information
        context: Lambda context object with tenant_id attribute
        
    Returns:
        dict: API Gateway response with tenant-specific counter value and tenant ID
    """
    global counter
    
    try:
        # Validate event structure first
        if not isinstance(event, dict):
            logger.error("Invalid event structure: event is not a dictionary")
            return create_error_response(400, 'Bad Request', 'Invalid request format')
        
        # Log the incoming request (sanitized for security)
        logger.info(f"Processing isolated request - Method: {event.get('httpMethod', 'UNKNOWN')}, Path: {event.get('path', 'UNKNOWN')}")
        
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
        if path and not path.endswith('/isolated'):
            logger.warning(f"Unexpected path: {path}")
        
        # Get tenant ID from Lambda context
        # AWS Lambda provides tenant_id in the context when tenant isolation is enabled
        tenant_id = getattr(context, 'tenant_id', None)
        
        # Enhanced tenant ID validation
        if not tenant_id:
            logger.error("Missing tenant ID in Lambda context")
            return create_error_response(400, 'Missing Tenant ID', 'Tenant ID is required for isolated function calls. Ensure x-tenant-id header is provided.')
        
        # Validate tenant ID format (basic validation)
        if not isinstance(tenant_id, str) or len(tenant_id.strip()) == 0:
            logger.error(f"Invalid tenant ID format: {tenant_id}")
            return create_error_response(400, 'Invalid Tenant ID', 'Tenant ID must be a non-empty string')
        
        # Sanitize tenant ID for logging
        tenant_id = tenant_id.strip()
        
        # Validate tenant ID length (reasonable limit)
        if len(tenant_id) > 100:
            logger.error(f"Tenant ID too long: {len(tenant_id)} characters")
            return create_error_response(400, 'Invalid Tenant ID', 'Tenant ID must be 100 characters or less')
        
        # With tenant isolation, each tenant gets their own execution environment
        # So this simple counter is automatically isolated per tenant by AWS Lambda
        counter += 1
        
        # Log the isolated behavior
        logger.info(f"Tenant '{tenant_id}' using isolated counter value: {counter}")
        
        # Prepare response body
        response_body = {
            'counter': counter,
            'tenant_id': tenant_id,
            'isolation_enabled': True,
            'message': f'Counter incremented successfully for tenant {tenant_id}'
        }
        
        # Log the response
        logger.info(f"Returning isolated counter value {counter} for tenant {tenant_id}")
        
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
    except AttributeError as e:
        logger.error(f"Context attribute error: {str(e)}")
        return create_error_response(500, 'Configuration Error', 'Lambda function configuration error')
    except Exception as e:
        # Log the error with more context
        logger.error(f"Unexpected error processing isolated request: {str(e)}", exc_info=True)
        
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