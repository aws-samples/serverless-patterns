import logging
import os
import time
from urllib.parse import urlparse

import pystache
import requests
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth
from requests import HTTPError

logger = logging.getLogger(__name__)

products_api = os.getenv('products_api')
aws_region = os.getenv('AWS_REGION')


def _load_html():
    with open('static/index.html', 'r') as file:
        html_string = file.read()
    return html_string


def _get_products():
    host = urlparse(products_api).hostname
    auth = BotoAWSRequestsAuth(aws_host=host,
                               aws_region=aws_region,
                               aws_service='execute-api')
    try:
        response = requests.get(url=products_api, timeout=(1, 3), auth=auth)
        response.raise_for_status()
        return response.json()
    except HTTPError:
        logger.exception("Exception occurred:", exc_info=True)


template = _load_html()
products = _get_products()
day_of_week = time.asctime()


def handler(event, context):

    view_args = {
        'dayOfWeek': day_of_week,
        'products': products,
    }
    html = pystache.render(template, **view_args)
    response = {
        "statusCode": 200,
        "body": html,
        "headers": {
            "Content-Type": 'text/html; charset=UTF-8'
        }
    }
    return response
