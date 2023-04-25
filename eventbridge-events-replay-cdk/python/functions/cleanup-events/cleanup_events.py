import json
import logging
import json
import base64

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()


def handler(event, context):
    # TODO: Add logic to filter events OR scrub sensitive data or any other complex transformation/translation needed
    logger.setLevel(logging.INFO)
    logger.info(f"Event: {event}")
    response = None
    for e in event:
        payload_b = base64.b64decode(e["data"])
        payload = payload_b.decode("utf-8")
        payload_j = json.loads(payload)
        response = payload_j["detail"]
    logger.info(f"Decoded payload: {response}")
    return response
