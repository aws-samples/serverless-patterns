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
    describe_response = {}
    try:
        region = event['ResourceProperties']['Region']
        domain_name = event['ResourceProperties']['DomainName']
        route53 = client('route53', region_name=region)
        # Get the GetHostedZoneId
        describe_response = route53.list_hosted_zones_by_name(DNSName=domain_name)
    except ClientError as e:
        LOG.error(e.response['Error']['Code'])
    except Exception as e:
        LOG.error(f'Exception in the lamda handler, {e}')
    if describe_response['ResponseMetadata']['HTTPStatusCode'] == 200:
        response_status = 'SUCCESS'
        hosted_zone_field = describe_response['HostedZones'][0]['Id']
        hosted_zone_id = hosted_zone_field.split('/')[2]
        response_data["HostedZoneId"] = hosted_zone_id
        
    send_response(event, context, response_status, response_data)