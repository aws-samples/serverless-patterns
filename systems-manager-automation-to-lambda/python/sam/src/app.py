import boto3
import logging as logger
import botocore

def handler(event, context):

    client = boto3.client('dynamodb')

    try:
        client.put_item(
            TableName='{}'.format(event['ssm_automation_parameters']['table_name']),
            Item={
                'Album':{'S':'{}'.format(event['ssm_automation_parameters']['partition_key_input'])},
                'Artist':{'S':'{}'.format(event['ssm_automation_parameters']['sort_key_input'])}
                })

    except botocore.exceptions.ClientError as e:
        logger.error(e)
        raise

    return("Table updated")
