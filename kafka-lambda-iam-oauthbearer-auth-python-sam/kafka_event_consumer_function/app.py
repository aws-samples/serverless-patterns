# Lambda Runtime delivers a batch of messages to the Lambda function.
# Each batch has an eventSource plus a "records" field: a map whose keys are a
# combination of the topic name and the partition number, and whose values are
# lists of individual Kafka messages. One batch can contain messages from
# multiple partitions.
#
# This handler flattens that structure into a list of simple message dicts,
# logs each one, and (when the DYNAMODB_TABLE_NAME environment variable is set)
# writes the Kafka metadata plus the parsed JSON payload fields to DynamoDB.
import base64
import json
import os

# boto3 is imported lazily inside _write_to_dynamodb so the module (and its unit
# tests) can be imported without the AWS SDK / credentials present.

_ddb_table = None

# `sam local invoke` sets AWS_SAM_LOCAL=true. Local runs write to DynamoDB Local
# (started by scripts/local_dynamodb.sh) so they never touch the real table.
LOCAL_DYNAMODB_ENDPOINT = "http://dynamodb-local:8000"


def _table(table_name):
    global _ddb_table
    if _ddb_table is None:
        import boto3
        endpoint = LOCAL_DYNAMODB_ENDPOINT if os.environ.get("AWS_SAM_LOCAL") == "true" else None
        _ddb_table = boto3.resource("dynamodb", endpoint_url=endpoint).Table(table_name)
    return _ddb_table


def _decode(value):
    # The key and value inside a Kafka record are base64-encoded.
    if value is None:
        return "null"
    return base64.b64decode(value).decode("utf-8")


def parse_records(event):
    """Flatten the Kafka event (records keyed by topic-partition) into a list of message dicts."""
    messages = []
    for _topic_partition, records in (event.get("records") or {}).items():
        for record in records:
            key = record.get("key")
            value = record.get("value")
            # A Kafka message can optionally carry a list of headers, each a
            # single-entry map of name -> list of byte values.
            headers = []
            for header in record.get("headers") or []:
                for header_key, header_value in header.items():
                    if isinstance(header_value, (list, tuple)):
                        header_value = bytes(header_value).decode("utf-8", "replace")
                    headers.append({"key": header_key, "value": str(header_value)})
            messages.append({
                "topic": record.get("topic"),
                "partition": record.get("partition"),
                "offset": record.get("offset"),
                "timestamp": record.get("timestamp"),
                "timestampType": record.get("timestampType"),
                "key": key,
                "value": value,
                "decodedKey": _decode(key),
                "decodedValue": _decode(value),
                "headers": headers,
            })
    return messages


def _write_to_dynamodb(message):
    """Persist one Kafka message to DynamoDB: the Kafka metadata (topic, partition,
    offset, timestamp, timestampType, key) plus every top-level primitive field of
    the decoded JSON payload (firstName, lastName, email, ...). The item is keyed by
    topicPartition (partition key) + offset (sort key). Skipped when the
    DYNAMODB_TABLE_NAME environment variable is not set."""
    table_name = os.environ.get("DYNAMODB_TABLE_NAME")
    if not table_name:
        return
    item = {
        "topicPartition": f"{message['topic']}-{message['partition']}",
        "offset": int(message["offset"]),
        "topic": message["topic"],
        "partition": int(message["partition"]),
        "timestamp": int(message["timestamp"]),
    }
    if message.get("timestampType"):
        item["timestampType"] = message["timestampType"]
    if message.get("decodedKey") is not None:
        item["key"] = message["decodedKey"]
    if message.get("decodedValue") is not None:
        item["value"] = message["decodedValue"]
    # Parse the decoded value as JSON and store each top-level primitive field.
    try:
        parsed = json.loads(message["decodedValue"])
        if isinstance(parsed, dict):
            for field_key, field_value in parsed.items():
                if isinstance(field_value, (str, int, float, bool)):
                    item[field_key] = str(field_value)
    except (ValueError, TypeError):
        # Not a JSON payload - the raw value is already stored under "value".
        pass
    _table(table_name).put_item(Item=item)
    print(f"Wrote message to DynamoDB table {table_name} "
          f"(topicPartition={item['topicPartition']}, offset={item['offset']})")


def lambda_handler(event, context):
    messages = parse_records(event)
    for message in messages:
        print(f"Received this message from Kafka - {message}")
        _write_to_dynamodb(message)
    print(f"All messages in this batch = {json.dumps(messages)}")
    return "200 OK"
