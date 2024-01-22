import json
import os
from http import HTTPStatus

from boto3.session import Session
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from requests import request


class AWSSigV4Requester:
    apigw_component_service = 'execute-api'

    def __init__(self):
        self.service = self.apigw_component_service
        self.region = os.getenv('AWS_REGION')
        self.credentials = Session().get_credentials().get_frozen_credentials()

    def sigv4_request(self, url, method, body, params, headers):
        req = AWSRequest(method=method, url=url, data=body, params=params, headers=headers)
        SigV4Auth(self.credentials, self.service, self.region).add_auth(req)
        req = req.prepare()
        return request(method=req.method, url=req.url, headers=req.headers, data=req.body)

    def call_aws_iam_secured_api(self, url, method, body, params, headers):
        response = self.sigv4_request(url=url, method=method, body=body, params=params,
                                      headers=headers)
        return response.json()


def handler(event, context):
    aws_requester = AWSSigV4Requester()
    result = aws_requester.call_aws_iam_secured_api(url=os.getenv('aws_iam_secured_service_url'), method='GET',
                                                    body=None, params=None,
                                                    headers={'content-type': 'application/json'})
    response = {
        "statusCode": int(HTTPStatus.OK),
        "body": json.dumps(result)
    }
    return response
