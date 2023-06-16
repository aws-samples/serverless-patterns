from urllib import response
import boto3
import datetime
import math
import logging as logger
import botocore


def handler(event, context):
    print('Event: {}'.format(event))
    now = datetime.datetime.now()
    timestamp = math.ceil(datetime.datetime.timestamp(now))
    
    client = boto3.client('rds')
    print(event)
   
    
    
    params = {
        'DBSnapshotIdentifier'  : 'rds-snapshot-{}'.format(timestamp),
        'DBInstanceIdentifier'  : '{}'.format(event['ssm_automation_parameters']['db_instance_id'])
    }
    
    try:
       response = client.create_db_snapshot(**params,)
         #DBSnapshotIdentifier  = 'rds_snapshot_{}'.format{timestamp},
         #DBInstanceIdentifier  = event['ssm_automation_parameters']['db_instance_id'],
        #)
    
    except botocore.exceptions.ClientError as e:
        logger.error(e)
        raise
    print(response)
    return {
        'SnapshotDetails': {
            'Snapshot_Name': response['DBSnapshot']['DBSnapshotIdentifier'],
            'db_name': response['DBSnapshot']['DBInstanceIdentifier'],
            'Status': response['DBSnapshot']['Status'],
            'Arn': response['DBSnapshot']['DBSnapshotArn'],
            'MaxRetries': 3,
        }
    }