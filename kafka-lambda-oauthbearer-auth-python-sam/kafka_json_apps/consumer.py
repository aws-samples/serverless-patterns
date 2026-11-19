"""Consumes JSON messages from a Kafka topic and prints each one parsed and
pretty-printed, using SASL/OAUTHBEARER authentication (the token comes from the
properties file written by refresh_token.sh).

Usage: consumer.py <properties-file> <topic> [group-id]
"""
import json
import sys

from kafka import KafkaConsumer

from kafka_config import client_kwargs


def main():
    if len(sys.argv) < 3:
        print("Usage: consumer.py <properties-file> <topic> [group-id]", file=sys.stderr)
        sys.exit(2)
    properties_file, topic = sys.argv[1], sys.argv[2]
    group_id = sys.argv[3] if len(sys.argv) >= 4 else "kafka-oauth-consumer-group"

    consumer = KafkaConsumer(
        topic,
        group_id=group_id,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        key_deserializer=lambda b: b.decode("utf-8") if b is not None else None,
        value_deserializer=lambda b: b.decode("utf-8") if b is not None else None,
        **client_kwargs(properties_file),
    )

    print(f"Consuming from topic '{topic}' (group '{group_id}'). Press Ctrl-C to stop.")
    try:
        for record in consumer:
            try:
                pretty = json.dumps(json.loads(record.value), indent=2)
            except (ValueError, TypeError):
                pretty = record.value
            print(f"\n--- message partition={record.partition} offset={record.offset} "
                  f"key={record.key} ---\n{pretty}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        print("Consumer closed.")


if __name__ == "__main__":
    main()
