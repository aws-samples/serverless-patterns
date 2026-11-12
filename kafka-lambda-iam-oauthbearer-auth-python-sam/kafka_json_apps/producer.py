"""Publishes a given number of JSON "person" messages to a Kafka topic, using
SASL/OAUTHBEARER authentication (the token comes from the properties file written
by refresh_token.sh).

Usage: producer.py <properties-file> <topic> <count>
"""
import json
import sys

from faker import Faker
from kafka import KafkaProducer

from kafka_config import client_kwargs
from person import random_person


def main():
    if len(sys.argv) < 4:
        print("Usage: producer.py <properties-file> <topic> <count>", file=sys.stderr)
        sys.exit(2)
    properties_file, topic, count = sys.argv[1], sys.argv[2], int(sys.argv[3])

    producer = KafkaProducer(
        key_serializer=lambda k: k.encode("utf-8") if k is not None else None,
        value_serializer=lambda v: v.encode("utf-8"),
        # Keep the producer ACL minimal (WRITE on the topic only) by not requiring
        # the cluster-level IDEMPOTENT_WRITE permission.
        acks="all",
        **client_kwargs(properties_file),
    )

    faker = Faker()
    print(f"Producing {count} JSON message(s) to topic '{topic}'...")
    for i in range(count):
        person = random_person(faker)
        payload = json.dumps(person)
        metadata = producer.send(topic, key=person["email"], value=payload).get(timeout=30)
        print(f"Sent [{i + 1}/{count}] partition={metadata.partition} offset={metadata.offset} : {payload}")
    producer.flush()
    producer.close()
    print(f"Done. Sent {count} message(s) to '{topic}'.")


if __name__ == "__main__":
    main()
