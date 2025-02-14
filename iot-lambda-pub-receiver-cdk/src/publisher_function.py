import boto3
import logging
import os
import json

logger = logging.getLogger()
logger.setLevel("INFO")
logger = logging.getLogger(__name__)

def handler(event, context):
    mqtt_topic_region = os.environ['MQTT_TOPIC_REGION']
    mqtt_topic_name = os.environ['MQTT_TOPIC_NAME']
    logger.info(f"""Started with env variables: 
                    MQTT_TOPIC_REGION= + {mqtt_topic_region}
                    MQTT_TOPIC_NAME=" + {mqtt_topic_name}""")
    iot_client = boto3.client('iot-data', region_name=mqtt_topic_region)
    response = iot_client.publish(
        topic=mqtt_topic_name,
        qos=1, # The MQTT message is delivered at least once.
        payload=json.dumps(event)
    )
    logger.info("Msg published.")