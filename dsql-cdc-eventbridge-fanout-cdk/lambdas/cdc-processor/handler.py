# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0 (2026)
"""CDC Processor: Parse Amazon Aurora DSQL CDC events from Amazon Kinesis
and fan out to Amazon EventBridge with typed detail-type routing."""

import base64
import json
import os
from datetime import datetime, timezone

import boto3

EVENTS_CLIENT = boto3.client('events')
EVENT_BUS_NAME = os.environ['EVENT_BUS_NAME']
SOURCE = 'dsql.cdc'


def lambda_handler(event, context):
    """Process Amazon Kinesis records containing Amazon Aurora DSQL CDC events."""
    records = event.get('Records', [])
    if not records:
        return {'statusCode': 200, 'processed': 0}

    # DSQL CDC JSON format:
    # {"type":"full","op":"c|u|d","before":null|{...},"after":{...}|null,"source":{...}}
    OP_MAP = {'c': 'INSERT', 'u': 'UPDATE', 'd': 'DELETE'}

    entries = []
    for record in records:
        try:
            payload = base64.b64decode(record['kinesis']['data'])
            cdc_event = json.loads(payload)

            # Map DSQL CDC op codes to human-readable operation types
            raw_op = cdc_event.get('op', '').lower()
            operation = OP_MAP.get(raw_op, 'UNKNOWN')
            table_name = cdc_event.get('source', {}).get('table', 'unknown')

            # Use operation as EventBridge detail-type for content-based routing
            detail_type = operation

            entry = {
                'Source': SOURCE,
                'DetailType': detail_type,
                'Detail': json.dumps({
                    'tableName': table_name,
                    'operation': operation,
                    'newImage': cdc_event.get('after'),
                    'oldImage': cdc_event.get('before'),
                    'timestamp': cdc_event.get('source', {}).get('ts_ms',
                                               datetime.now(timezone.utc).isoformat()),
                    'sequenceNumber': record['kinesis'].get('sequenceNumber'),
                }),
                'EventBusName': EVENT_BUS_NAME,
            }
            entries.append(entry)

        except (json.JSONDecodeError, KeyError) as e:
            print(f'Failed to parse CDC record: {e}')
            continue

    # Publish in batches of 10 (EventBridge PutEvents limit)
    failed_count = 0
    for i in range(0, len(entries), 10):
        batch = entries[i:i + 10]
        try:
            response = EVENTS_CLIENT.put_events(Entries=batch)
            failed_count += response.get('FailedEntryCount', 0)
        except Exception as e:
            print(f'EventBridge PutEvents error: {e}')
            failed_count += len(batch)

    print(f'Processed {len(records)} records, published {len(entries)} events, '
          f'{failed_count} failures')

    if failed_count > 0:
        raise Exception(f'{failed_count} events failed to publish to Amazon EventBridge')

    return {
        'statusCode': 200,
        'processed': len(records),
        'published': len(entries),
    }
