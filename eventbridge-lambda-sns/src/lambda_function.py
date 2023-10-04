import logging
import json
import boto3
import os
from botocore.exceptions import ClientError

# Initialize Boto3 clients
ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')

# Initialize IP limit
ip_limit = os.environ['IP_limit']

def lambda_handler(event, context):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    # Initialize a list to store the results
    results = []
    
    # Get all available regions
    regions = ec2_client.describe_regions()['Regions']
    
   # Get all available regions
    regions = ec2_client.describe_regions()['Regions']
    
    sns_topic_arn = os.environ.get('SNStopic')
    
    for region in regions:
        # Create EC2 client for each region
        ec2_client_region = boto3.client('ec2', region_name=region['RegionName'])
        
        # Get all subnets in the region
        subnets = ec2_client_region.describe_subnets()['Subnets']
        
        for subnet in subnets:
            subnet_id = subnet['SubnetId']
            
            # Get the available IP address count for the subnet
            available_ip_addresses = subnet['AvailableIpAddressCount']
            if available_ip_addresses < int(ip_limit):
                results.append(f"Region: {region['RegionName']}, Subnet ID: {subnet_id}, Available IP Count: {available_ip_addresses}")
                
    print(results)           
    # Publish results to an SNS topic
    subject = 'Amazon VPC Subnets that are below IP address threshold alert'
    message = '\n'.join(results)
    
    try:
        sent_message = sns_client.publish(TopicArn=sns_topic_arn, Subject=subject, Message=message)
        
        if sent_message is not None:
            logger.info(f"Success - SNS Message ID: {sent_message['MessageId']}")
        return {
            "statusCode": 200,
            "body": json.dumps("Message published successfully")
        }

    except ClientError as e:
        logger.error(e)
        return None
