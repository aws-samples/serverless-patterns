# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# 2026

"""
Lambda handler for Amazon Macie sensitive data quarantine operations.
Supports two modes:
  - quarantine: Copy object to quarantine bucket, delete from source, tag
  - tag_only: Tag the source object with finding metadata without moving it
"""

import os
import json
import boto3
from datetime import datetime, timezone


s3 = boto3.client('s3')
QUARANTINE_BUCKET = os.environ['QUARANTINE_BUCKET']


def handler(event, context):
    """Handle quarantine or tag-only operations for sensitive data objects."""
    bucket_name = event['bucketName']
    object_key = event['objectKey']
    finding_id = event['findingId']
    severity = event['severity']
    tag_only = event.get('tagOnly', False)

    timestamp = datetime.now(timezone.utc).isoformat()

    tags = [
        {'Key': 'MacieFinding', 'Value': finding_id},
        {'Key': 'MacieSeverity', 'Value': severity},
        {'Key': 'QuarantineDate', 'Value': timestamp},
    ]

    if tag_only:
        return tag_object(bucket_name, object_key, tags)
    else:
        return quarantine_object(bucket_name, object_key, tags, finding_id)


def tag_object(bucket_name, object_key, tags):
    """Tag the source object with Macie finding metadata."""
    try:
        s3.put_object_tagging(
            Bucket=bucket_name,
            Key=object_key,
            Tagging={'TagSet': tags}
        )
        return {
            'status': 'TAGGED',
            'bucket': bucket_name,
            'key': object_key,
            'tags': tags,
        }
    except Exception as e:
        print(f'Error tagging object: {e}')
        raise


def quarantine_object(bucket_name, object_key, tags, finding_id):
    """Move object to quarantine bucket with metadata preservation."""
    quarantine_key = f'quarantined/{finding_id}/{object_key}'

    try:
        # Copy to quarantine bucket with finding metadata
        s3.copy_object(
            Bucket=QUARANTINE_BUCKET,
            Key=quarantine_key,
            CopySource={'Bucket': bucket_name, 'Key': object_key},
            MetadataDirective='COPY',
            TaggingDirective='REPLACE',
            Tagging='&'.join([f"{t['Key']}={t['Value']}" for t in tags]),
        )

        # Tag source object to indicate it was quarantined
        quarantine_tags = tags + [{'Key': 'QuarantineStatus', 'Value': 'MOVED'}]
        s3.put_object_tagging(
            Bucket=bucket_name,
            Key=object_key,
            Tagging={'TagSet': quarantine_tags}
        )

        # Delete from source bucket
        s3.delete_object(
            Bucket=bucket_name,
            Key=object_key
        )

        return {
            'status': 'QUARANTINED',
            'sourceBucket': bucket_name,
            'sourceKey': object_key,
            'quarantineBucket': QUARANTINE_BUCKET,
            'quarantineKey': quarantine_key,
        }
    except Exception as e:
        print(f'Error quarantining object: {e}')
        raise
