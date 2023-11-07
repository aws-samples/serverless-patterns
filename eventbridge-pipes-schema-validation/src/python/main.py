import os, base64, json
import boto3
from typing import List, Dict, Any
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities import parameters
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.parser import event_parser
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer

from models import MessageList


DLQ_URL = os.environ["DLQ_URL"]


sqs = boto3.client("sqs")
logger = Logger()
tracer = Tracer()


schema_registry_secret = parameters.get_secret(
    "confluent-schema-registry-secret", transform="json"
)

try:
    schema_registry_client = SchemaRegistryClient(schema_registry_secret)
    avro_deserializer = AvroDeserializer(schema_registry_client)
except Exception as e:
    logger.error({"Error creating Avro deserializer": e})
    raise e


@tracer.capture_method
def decode_key(key):
    decoded_key = base64.b64decode(key).decode()

    logger.debug({"decoded_key": decoded_key})

    return decoded_key


@tracer.capture_method
def decode_value(value, topic):
    decoded_value = base64.b64decode(value)

    deserialized_value = avro_deserializer(
        decoded_value, SerializationContext(topic, MessageField.VALUE)
    )

    logger.debug({"deserialized_value": deserialized_value})

    return deserialized_value


@tracer.capture_method
def message_handler(message):
    logger.debug({"message": message})

    topic = message.topic
    key = decode_key(message.key)
    value = decode_value(message.value, topic)

    logger.debug(
        {
            "topic": topic,
            "key": key,
            "value": value,
        }
    )

    return {"topic": topic, "key": key, "value": value}


@tracer.capture_lambda_handler
@logger.inject_lambda_context()
@event_parser(model=MessageList)
def lambda_handler(event: MessageList, context: LambdaContext) -> List[Dict[str, Any]]:
    logger.debug({"event": event})

    messages = event.__root__

    logger.info({"Number of messages to process": len(messages)})

    deserialized_messages = []
    error_messages = []
    for message in messages:
        try:
            deserialized_message = message_handler(message)
            deserialized_messages.append(deserialized_message)
        except Exception as e:
            logger.error({"Error deserializing message": e})
            error_messages.append(message)

    for message in error_messages:
        try:
            logger.debug({"Sending error message to DLQ": message})

            sqs.send_message(
                QueueUrl=DLQ_URL,
                MessageBody=json.dumps(message.dict()),
            )
        except Exception as e:
            logger.error({"Error sending message(s) to DLQ": e})
            raise e

    logger.info(
        {
            "Number of messages deserialized": len(deserialized_messages),
            "Number of messages with errors": len(error_messages),
        }
    )

    return deserialized_messages
