"""
Lambda Durable Function - Calls REST API using AWS Durable Execution SDK
"""
import json
import os
import requests
from aws_durable_execution_sdk_python.config import Duration
from aws_durable_execution_sdk_python.context import StepContext, durable_step
from aws_durable_execution_sdk_python.execution import durable_execution

DEFAULT_API_URL = os.environ.get('API_URL', 'https://jsonplaceholder.typicode.com/posts/1')


@durable_step
def call_rest_api(step_context: StepContext, url: str) -> dict:
    """
    Durable step that calls an external REST API
    """
    step_context.logger.info(f"Calling REST API: {url}")
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        result = {
            'status': 'success',
            'status_code': response.status_code,
            'data': response.json()
        }
        
        step_context.logger.info(f"API call successful: {response.status_code}")
        return result
        
    except requests.exceptions.RequestException as e:
        step_context.logger.error(f"API call failed: {str(e)}")
        return {
            'status': 'error',
            'error': str(e)
        }


@durable_execution
def lambda_handler(event, context) -> dict:
    """
    Lambda handler using AWS Durable Execution
    """
    context.logger.info("Starting durable REST API call")
    
    # Get API URL from event or use default
    api_url = event.get('url', DEFAULT_API_URL)
    
    context.logger.info(f"Using API URL: {api_url}")
    
    # Execute the REST API call as a durable step
    result = context.step(call_rest_api(api_url))
    
    # Optional: Add a wait period (demonstrates durable wait without consuming CPU)
    context.logger.info("Waiting 2 seconds before returning response")
    context.wait(Duration.from_seconds(2))
    
    context.logger.info("Durable execution completed")
    
    # Return response based on result
    if result['status'] == 'success':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'message': 'API call successful',
                'url': api_url,
                'data': result['data']
            })
        }
    else:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'error': 'API call failed',
                'url': api_url,
                'details': result.get('error')
            })
        }
