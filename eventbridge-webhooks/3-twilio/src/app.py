"""Webhook implementation for Twilio"""

import os
import json
import urllib.parse
import base64
import hmac
import hashlib
from functools import reduce
import boto3
import botocore
import botocore.session
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig


client = botocore.session.get_session().create_client('secretsmanager')
cache_config = SecretCacheConfig()
cache = SecretCache(config=cache_config, client=client)

twilio_webhook_secret_arn = os.environ.get('TWILIO_WEBHOOK_SECRET_ARN')
event_bus_name = os.environ.get('EVENT_BUS_NAME', 'default')

event_bridge_client = boto3.client('events')

def _add_header(request, **kwargs):
    userAgentHeader = request.headers['User-Agent'] + ' fURLWebhook/1.0 (Twilio)'
    del request.headers['User-Agent']
    request.headers['User-Agent'] = userAgentHeader

event_system = event_bridge_client.meta.events
event_system.register_first('before-sign.events.PutEvents', _add_header)

class PutEventError(Exception):
    """Raised when Put Events Failed"""
    pass

def lambda_handler(event, _context):
    """Webhook function"""

    headers = event.get('headers')

    try:
        payload = normalize_payload(
            raw_payload=event.get('body'),
            is_base64_encoded=event['isBase64Encoded'])
        content_type = get_content_type(headers)
        payload_object = parse_payload(
            payload=payload,
            content_type=content_type)
    except ValueError as err:
        print_error(f'400 Bad Request - {err}', headers)
        return {'statusCode': 400, 'body': str(err)}
    except BaseException as err:  # Unexpected Error
        print_error('500 Internal Server Error\n' +
                    f'Unexpected error: {err}, {type(err)}', headers)
        return {'statusCode': 500, 'body': 'Internal Server Error'}

    try:
        url = 'https://' + headers['host'] + event['rawPath']

        if not contains_valid_signature(
                payload_object=payload_object,
                url=url,
                event_signature=headers.get('x-twilio-signature', '')):
            print_error('401 Unauthorized - Invalid Signature', headers)
            return {'statusCode': 401, 'body': 'Invalid Signature'}

        response = forward_event(get_json_payload(payload_object))

        if response['FailedEntryCount'] > 0:
            print_error('500 FailedEntry Error - The event was not successfully forwarded to Amazon EventBridge\n' +
                        str(response['Entries'][0]), headers)
            return {'statusCode': 500, 'body': 'FailedEntry Error - The entry could not be succesfully forwarded to Amazon EventBridge'}

        return {'statusCode': 202, 'body': 'Message forwarded to Amazon EventBridge'}

    except PutEventError as err:
        print_error(f'500 Put Events Error - {err}', headers)
        return {'statusCode': 500, 'body': 'Internal Server Error - The request was rejected by Amazon EventBridge API'}

    except BaseException as err:  # Unexpected Error
        print_error('500 Client Error\n' +
                    f'Unexpected error: {err}, {type(err)}', headers)
        return {'statusCode': 500, 'body': 'Internal Server Error'}


def normalize_payload(raw_payload, is_base64_encoded):
    """Decode payload if needed"""
    if raw_payload is None:
        raise ValueError('Missing event body')
    if is_base64_encoded:
        return base64.b64decode(raw_payload).decode('utf-8')
    return raw_payload


def parse_payload(payload, content_type):
    """Parse payload based on the content-type"""
    if content_type == 'application/x-www-form-urlencoded':
        return urllib.parse.parse_qs(payload, keep_blank_values=True)
    if content_type == 'application/json':
        return json.loads(payload)
    raise ValueError('Invalid content-type')


def get_payload_bytes(url, payload_object):
    """Get payload bytes to feed hash function"""
    return reduce(lambda acc, key: acc + key + payload_object[key][0],
                  sorted(list(payload_object)),
                  url).encode('utf-8')


def contains_valid_signature(payload_object, url, event_signature):
    """Check for the payload signature
       Twilio documentation: https://www.twilio.com/docs/usage/webhooks/webhooks-security#validating-signatures-from-twilio
    """
    secret = cache.get_secret_string(twilio_webhook_secret_arn)
    payload_bytes = get_payload_bytes(
        url=url,
        payload_object=payload_object
    )
    computed_signature = compute_signature(
        payload_bytes=payload_bytes, secret=secret)
    return hmac.compare_digest(event_signature, computed_signature)


def compute_signature(payload_bytes, secret):
    """Compute HMAC-SHA1"""
    m = hmac.new(key=secret.encode(), msg=payload_bytes,
                 digestmod=hashlib.sha1)
    return base64.b64encode(m.digest()).decode('utf-8')


def get_json_payload(payload_object):
    """Get JSON string from payload"""
    output = {}
    for key in payload_object:
        if isinstance(payload_object[key], list):
            output[key] = payload_object[key][0]
        else:
            output[key] = payload_object[key]
    if output.get('PayloadType') == 'application/json' and output.get('Payload') is not None:
        output['Payload'] = json.loads(output['Payload'])
    return json.dumps(output)


def forward_event(payload):
    """Forward event to EventBridge"""
    try:
        return event_bridge_client.put_events(
            Entries=[
                {
                    'Source': 'twilio.com',
                    'DetailType': 'twilio-webhook-lambda',
                    'Detail': payload,
                    'EventBusName': event_bus_name
                },
            ]
        )
    except BaseException as err:
        raise PutEventError('Put Events Failed')

def get_content_type(headers):
    """Helper function to parse content-type from the header"""
    raw_content_type = headers.get('content-type')

    if raw_content_type is None:
        return None
    content_type = raw_content_type.split(';')[0].strip()
    return content_type


def print_error(message, headers):
    """Helper function to print errors"""
    print(f'ERROR: {message}\nHeaders: {str(headers)}')
