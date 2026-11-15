import logging
import json
import ast

def handler(event, context):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.info("request: " + json.dumps(event))

    logger.info("AWS Glue Job timeout successfully caught")
    
    return
