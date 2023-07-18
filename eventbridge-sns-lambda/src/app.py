import json
import logging
# import requests


def lambda_handler(event, context):
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    logger.info("Recieved the SNS event")
    logger.info(json.dumps(event))
    

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
