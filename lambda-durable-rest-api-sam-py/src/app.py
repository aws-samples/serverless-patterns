"""
AWS Lambda durable function - Calls REST API using AWS durable execution SDK
"""
import json
import os
import requests
from aws_durable_execution_sdk_python.config import Duration, StepConfig
from aws_durable_execution_sdk_python.context import StepContext, durable_step
from aws_durable_execution_sdk_python.execution import durable_execution
from aws_durable_execution_sdk_python.retries import (
    RetryStrategyConfig,
    create_retry_strategy,
)

DEFAULT_API_URL = os.environ.get('API_URL', 'https://jsonplaceholder.typicode.com/posts/1')

# Retry strategy: 3 attempts, exponential backoff starting at 2s, max 30s, with jitter
retry_config = RetryStrategyConfig(
    max_attempts=3,
    initial_delay=Duration.from_seconds(2),
    max_delay=Duration.from_seconds(30),
    backoff_rate=2.0,
    retryable_error_types=[
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
        requests.exceptions.HTTPError,
    ],
)
step_config = StepConfig(retry_strategy=create_retry_strategy(retry_config))


@durable_step
def call_rest_api(step_context: StepContext, url: str) -> dict:
    """
    Durable step that calls an external REST API.
    Transient failures (timeouts, connection errors) are raised so the
    durable execution SDK can automatically retry the step.
    Only non-retryable errors (oversized response, invalid JSON) are
    returned as error dicts.
    """
    step_context.logger.info(f"Calling REST API: {url}")

    max_response_size = 1_000_000  # 1 MB limit

    response = requests.get(url, timeout=30, stream=True)
    response.raise_for_status()

    # Validate response size before reading body
    content_length = response.headers.get('Content-Length')
    if content_length and int(content_length) > max_response_size:
        step_context.logger.error(f"Response too large: {content_length} bytes")
        return {
            'status': 'error',
            'error': f'Response size {content_length} bytes exceeds limit of {max_response_size} bytes'
        }

    # Read body with size limit
    body = response.content[:max_response_size]
    if len(response.content) > max_response_size:
        step_context.logger.error("Response body exceeded size limit")
        return {
            'status': 'error',
            'error': f'Response body exceeds limit of {max_response_size} bytes'
        }

    data = json.loads(body)

    step_context.logger.info(f"API call successful: {response.status_code}")
    return {
        'status': 'success',
        'status_code': response.status_code,
        'data': data
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
    # Transient failures (timeouts, connection errors) will raise exceptions,
    # allowing the durable execution SDK to automatically retry the step.
    try:
        result = context.step(call_rest_api(api_url), config=step_config)
    except Exception as e:
        context.logger.error(f"Step failed after retries: {str(e)}")
        return {
            'statusCode': 502,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'error': 'API call failed after retries',
                'url': api_url,
                'details': str(e)
            })
        }
    
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
