import boto3
import argparse
import json
import cfnresponse
import logging

# This function gets the IP addresses from a NLB, as they aren't returned by CloudFormation.

def handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # initialize our responses, assume failure by default

    response_data = {}
    response_status = cfnresponse.FAILED

    logger.info('Received event: {}'.format(json.dumps(event)))

    if event['RequestType'] == 'Delete':
        response_status = cfnresponse.SUCCESS
        cfnresponse.send(event, context, response_status, response_data)

    name_filter = event['ResourceProperties']['NameFilter']
    name_filter_parts = name_filter.split('/')
    resource_type = name_filter_parts[0]

    if resource_type == "net":
    
        response = {}
        
        try:
            ec2 = boto3.client('ec2')
            response = ec2.describe_network_interfaces(
                Filters=[
                    {
                        'Name': 'description',
                        'Values': ['ELB ' + name_filter]
                    },
                ],
            )
        except Exception as e:
            logger.info('ec2.describe_network_interfaces failure: {}'.format(e))
            cfnresponse.send(event, context, response_status, response_data)

        number_of_enis = len(response['NetworkInterfaces'])
        logger.info('number of network interfaces returned: {}'.format(number_of_enis))

        if number_of_enis >= 1:
            ip_addresses = [ sub['PrivateIpAddress'] for sub in response['NetworkInterfaces'] ]
            separator = ', '
            ip_addresses_string = separator.join(ip_addresses)
            response_data['IpAddresses'] = ip_addresses_string
            logger.info('NLB IP Addresses {}'.format(ip_addresses_string))
            
            response_status = cfnresponse.SUCCESS
            cfnresponse.send(event, context, response_status, response_data)

        else:
            logger.info('no matching network interfaces for filter {}'.format(name_filter))
            cfnresponse.send(event, context, response_status, response_data)

    else:
        logger.info('invalid resource type {}'.format(resource_type))
        cfnresponse.send(event, context, response_status, response_data)
