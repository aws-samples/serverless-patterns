import json
import logging
from botocore.exceptions import ClientError
LOG = logging.getLogger()
LOG.setLevel(logging.INFO)
from urllib.request import Request, urlopen
from boto3 import client

def send_response(event, context, response_status, response_data):
    response_body = {'Status': response_status,
                     'Reason': 'See the details in CloudWatch Log Stream: ' + context.log_stream_name,
                     'PhysicalResourceId': context.log_stream_name,
                     'StackId': event['StackId'],
                     'RequestId': event['RequestId'],
                     'LogicalResourceId': event['LogicalResourceId'],
                     'Data': response_data}

    LOG.info(f'RESPONSE BODY: {json.dumps(response_body)}')
    LOG.info(f'EVENT BEFORE SEND: {(event)}')
    try:
        req = urlopen(Request(event['ResponseURL'], data=json.dumps(response_body).encode(),headers={'content-type': ''}, method='PUT'))
    except Exception as e:
       LOG.error(req)
       LOG.error(e)


def handler(event, context):
    LOG.info(f'REQUEST RECEIVED: {event}')
    # For Delete requests, immediately send a SUCCESS response.
    # We do this because the custom resource does not create AWS resources, only retrieves values.
    if event['RequestType'] == 'Delete':
        LOG.info('Entering Delete')
        send_response(event, context, "SUCCESS", {})
        return
    response_status = 'FAILED'
    response_data = {}
    try:
        region = event['ResourceProperties']['Region']
        acm_certificate = event['ResourceProperties']['Certificate']
        acm_region = event['ResourceProperties']['ACMRegion']
        domain_name = event['ResourceProperties']['DomainName']
        ssm_us = client('ssm', region_name=acm_region)
        route53 = client('route53', region_name=region)
        # Get the SSM parameters
        certificate_param = ssm_us.get_parameter(Name=acm_certificate)
        hosted_zone_id_param = route53.list_hosted_zones_by_name(DNSName=domain_name)
    except Exception as e:
        LOG.error(f'Exception in the lambda handler, {e}')
    if certificate_param['ResponseMetadata']['HTTPStatusCode'] == 200 and hosted_zone_id_param['ResponseMetadata']['HTTPStatusCode'] == 200:
        response_status = 'SUCCESS'
        certificate_param_val = certificate_param['Parameter']['Value']
        hosted_zone_id_param_val = hosted_zone_id_param['HostedZones'][0]['Id']
        hosted_zone_id_param_val = hosted_zone_id_param_val.split('/')[2]
        response_data["ACMCertificate"] = certificate_param_val
        response_data["HostedZoneId"] = hosted_zone_id_param_val

    send_response(event, context, response_status, response_data)
