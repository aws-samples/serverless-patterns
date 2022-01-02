import json
import os
import boto3
import urllib3
import time

# This function creates a custom security group with the IP addresses from a NLB.

# Implements own cfn-response

def send_response(event, context, response_status, response_data, reason, physical_resource_id=None, no_echo=False):
    http = urllib3.PoolManager()
    response_body = {
        'Status': response_status,
        'Reason': reason,
        'PhysicalResourceId': physical_resource_id,
        'StackId': event['StackId'],
        'RequestId': event['RequestId'],
        'LogicalResourceId': event['LogicalResourceId'],
        'NoEcho': no_echo, 'Data': response_data
    }
    json_response_body = json.dumps(response_body)
    r = http.request('PUT', event['ResponseURL'], body=json_response_body)

def on_create(event, context):
    try:
        sec_group_ips = os.environ['WhiteList']
        ports_allowed = list(event['ResourceProperties']['Ports'].split(','))
        ports_allowed = [int(port.strip()) for port in ports_allowed]
        sec_group_list = list(sec_group_ips.split(","))
        sec_group_list = [ip.strip() for ip in sec_group_list]
        vpc_id = os.environ['VpcId']
        client = boto3.client('ec2')
        response = client.create_security_group(
            GroupName=os.environ['StackName'] + ' - Access to CloudHSM API instance from NLB',
            Description='Allows connections to port 8080 from NLB private IP addresses',
            VpcId=vpc_id
        )
        security_group_id = response['GroupId']
        ingress_list = []
        for port in ports_allowed:
            for ip in sec_group_list:
                ingress_list.append({
                    'IpProtocol': 'tcp',
                    'FromPort': port,
                    'ToPort': port,
                    'IpRanges': [{'CidrIp': ip + '/32'}]
                })
        client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=ingress_list
        )
        data = {"SecGroupId": security_group_id}
        send_response(event, context, 'SUCCESS', data, 'SecGroup Created', security_group_id, False)
    except Exception as e:
        send_response(event, context, 'FAILED', {}, str(e), 'None', False)

def on_delete(event, context):
    try:
        client = boto3.client('ec2')
        response = client.delete_security_group(
            GroupId=event['PhysicalResourceId']
        )
        send_response(event, context, 'SUCCESS', {}, 'SecGroup deleted', 'None', False)
    except Exception as e:
        send_response(event, context, 'FAILED', {}, str(e), 'None', False)

def lambda_handler(event, context):
    if event['RequestType'] == 'Delete':
        on_delete(event, context)
    if event['RequestType'] == 'Create':
        on_create(event, context)
