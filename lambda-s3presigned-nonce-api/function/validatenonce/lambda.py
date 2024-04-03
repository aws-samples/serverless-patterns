import json
import logging
import os

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['NONCE_TABLE']
nonce_table = dynamodb.Table(table_name) 

def lambda_handler(event, context):
    logger.info('Received event validate nonce: ' + json.dumps(event))

    nonce = event['queryStringParameters']['nonce']
    logger.info('Received nonce: ' + nonce)

    # Validate nonce
    if validate_nonce(nonce):
        logger.info('Valid nonce:'+ nonce)
        return generate_policy('*', 'Allow', event['methodArn'])
    else:
        logger.info('Invalid nonce: '+ nonce)
        return generate_policy('*', 'Deny', event['methodArn'])

def validate_nonce(nonce):
    try:
        response = nonce_table.get_item(Key={'nonce_id': nonce}) 
        print('The ddb key response is {}'.format(response))
   
    except ClientError as e:
        logger.error(e)
        return False
        
    if 'Item' in response:
        # Nonce found
            return True
    else:
        # Nonce not found    
        return False
        
def generate_policy(principal_id, effect, resource):
    return {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': resource
                }
            ]
        }
    }


