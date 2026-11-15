import requests
from aws_lambda_powertools import Metrics, Logger
from aws_lambda_powertools.event_handler import (APIGatewayRestResolver,
                                                 Response)
from aws_lambda_powertools.metrics import MetricUnit

logger = Logger()
metrics = Metrics(namespace="CWMApp", service="CWMApp-Lambda")
app = APIGatewayRestResolver()

URL_500 = "https://httpbin.org/status/500"
URL_200 = "https://httpbin.org/status/200"

REQUEST_TIMEOUT = "Request Timeout"
RESPONSE_408 = "response_408"
RESPONSE_500 = "response_500"
RESPONSE_200 = "response_200"

def response_500():
    metrics.add_metric(name="Response_500", unit=MetricUnit.Count, value=1)
    
    try:
        requests.request("GET", URL_500, timeout=5)
    except Exception as e:
        logger.exception(f'{REQUEST_TIMEOUT} - {e}')


def response_200():
    metrics.add_metric(name="Response_200", unit=MetricUnit.Count, value=1)
    
    try:
        requests.request("GET", URL_200, timeout=5)
    except Exception as e:
        logger.exception(f'{REQUEST_TIMEOUT} - {e}')

@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event, context):
    try:
        response_200()
        response_500()
    except Exception as e:
        logger.exception(f'{REQUEST_TIMEOUT} - {e}')
        
