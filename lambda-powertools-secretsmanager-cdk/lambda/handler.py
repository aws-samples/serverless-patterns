import os
import urllib3
from aws_lambda_powertools.utilities import parameters
from aws_lambda_powertools import (
    Tracer,
    Logger
)

API_KEY_SECRET = "API_KEY_SECRET"
API_URL        = "API_URL"

tracer = Tracer()
logger = Logger()


@tracer.capture_method(capture_response=False, capture_error=False)
def get_secret(secret_name):
    try:
        return parameters.get_secret(secret_name) # Plaintext API key

    except parameters.exceptions.GetParameterError as e:
        logger.exception("Error getting paramaeter \"" + secret_name + "\ from secrets manager")
        raise RuntimeError("Error getting parameter from secrets manager") from e


@tracer.capture_method
def call_api(api_url, api_key):
    try:
        http = urllib3.PoolManager()
        headers = { 
            "x-api-key": api_key 
        }

        response = http.request(
            "POST", 
            url = api_url,
            headers = headers
        )

        return response

    except urllib3.HTTPError as e:
        logger.exception("Received HTTP error")
        raise RuntimeError("Received HTTP error while calling API") from e


@tracer.capture_lambda_handler
@logger.inject_lambda_context(log_event=False)
def handler(event, context):
    api_url = os.getenv(API_URL)
    api_key = get_secret(os.getenv(API_KEY_SECRET))
    
    response = call_api(api_url, api_key)

    return {
        'statusCode': 200,
        'body': response.data
    }