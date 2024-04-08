from urllib import response
import boto3
import datetime
import math
import logging as logger
import botocore


def handler(event, context):
    print('Event: {}'.format(event))
    client = boto3.client('rds')
    
    param_DBSnapshotIdentifier = event['SnapshotDetails']['Snapshot_Name']
    param_DBInstanceIdentifier = event['SnapshotDetails']['db_name']
    try:
        response = client.describe_db_snapshots(
         DBSnapshotIdentifier = param_DBSnapshotIdentifier,
         DBInstanceIdentifier = param_DBInstanceIdentifier,
        )
    
    except botocore.exceptions.ClientError as e:
        logger.error(e)
        raise

    print(response)
    return {
        'Snapshot': {
            'Snapshot_Name': response['DBSnapshots'][0]['DBSnapshotIdentifier'],
            'DB_Name': response['DBSnapshots'][0]['DBInstanceIdentifier'],
            'Snapshot_Status': response['DBSnapshots'][0]['Status'],
            'http_Status': response['ResponseMetadata']['HTTPStatusCode']
        }
    }