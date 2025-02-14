import logging

logger = logging.getLogger()
logger.setLevel("INFO")
logger = logging.getLogger(__name__)

def handler(event, context):
    logger.info(f"Event received: {event}")
