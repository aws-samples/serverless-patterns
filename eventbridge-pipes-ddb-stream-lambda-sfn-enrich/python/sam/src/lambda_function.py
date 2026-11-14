import json
import logging

#Set Logging

logging.getLogger().setLevel(logging.INFO)

def lambda_handler(event, context):
    logging.info(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
