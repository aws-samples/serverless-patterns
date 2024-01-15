import json
import os
from http import HTTPStatus

from boto3 import Session
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from requests import request

private_api = os.getenv('private_api')
aws_region = os.getenv('AWS_REGION')


def sigv4_signing_request(
        url,
        method='GET',
        body=None,
        params=None,
        headers=None,
        service='execute-api',
        region=aws_region,
        credentials=Session().get_credentials().get_frozen_credentials()):
    req = AWSRequest(
        method=method,
        url=url,
        data=body,
        params=params,
        headers=headers
    )
    SigV4Auth(credentials, service, region).add_auth(req)
    req = req.prepare()
    return request(
        method=req.method,
        url=req.url,
        headers=req.headers,
        data=req.body
    )


def handler(event, context):
    response = sigv4_signing_request(
        url=private_api,
        method='GET'
    )
    return {
        "statusCode": int(HTTPStatus.OK),
        "body": json.dumps(response.json())
    }
