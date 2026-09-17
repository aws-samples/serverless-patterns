"""KQD Producer Lambda — publishes work items to Kafka topic.

PLAINTEXT, no auth. Every 7th item (taskIndex % 7 == 0) has shouldFail=True
to demonstrate the RELEASE/retry path.
"""

import json
import logging
import os
import uuid

from confluent_kafka import KafkaException, Producer
from confluent_kafka.admin import AdminClient, NewTopic

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TOPIC = os.environ.get("KAFKA_TOPIC", "kqd-task-worker")
BOOTSTRAP_SERVERS = os.environ.get("BOOTSTRAP_SERVERS", "")
DEFAULT_COUNT = 50


def _config():
    return {"bootstrap.servers": BOOTSTRAP_SERVERS}


def _ensure_topic(admin, topic):
    nt = NewTopic(topic, num_partitions=3, replication_factor=1)
    for t, future in admin.create_topics([nt]).items():
        try:
            future.result()
            logger.info("Created topic %s", t)
        except KafkaException as e:
            if "already exists" in str(e).lower():
                logger.info("Topic %s already exists", t)
            else:
                raise


def lambda_handler(event, context):
    event = event or {}
    count = int(event.get("count", DEFAULT_COUNT))
    topic = event.get("topic") or TOPIC

    _ensure_topic(AdminClient(_config()), topic)

    producer = Producer(_config())
    failures = 0

    def on_delivery(err, _):
        nonlocal failures
        if err:
            failures += 1
            logger.error("Delivery failed: %s", err)

    for i in range(count):
        item = {
            "jobId": str(uuid.uuid4()),
            "taskIndex": i,
            "payload": f"task-{i}",
            "shouldFail": i % 7 == 0,
        }
        producer.produce(
            topic,
            key=item["jobId"].encode(),
            value=json.dumps(item).encode(),
            on_delivery=on_delivery,
        )
        producer.poll(0)

    producer.flush()
    result = {"topic": topic, "produced": count, "failures": failures}
    logger.info("Producer done: %s", json.dumps(result))
    return result
