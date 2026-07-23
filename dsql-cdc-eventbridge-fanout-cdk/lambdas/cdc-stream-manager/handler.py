# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0 (2026)
"""Custom Resource: Create and delete Amazon Aurora DSQL CDC streams."""

import json
import os
import time

import boto3

DSQL_CLIENT = boto3.client('dsql')


def on_event(event, context):
    """Handle CloudFormation Custom Resource lifecycle events."""
    request_type = event['RequestType']
    properties = event['ResourceProperties']

    cluster_id = properties.get('ClusterId', os.environ.get('CLUSTER_ID', ''))
    kinesis_arn = properties.get('KinesisStreamArn', os.environ.get('KINESIS_STREAM_ARN', ''))
    role_arn = properties.get('RoleArn', os.environ.get('CDC_ROLE_ARN', ''))

    if request_type == 'Create':
        return create_stream(cluster_id, kinesis_arn, role_arn)
    elif request_type == 'Update':
        # CDC streams are immutable — delete old, create new
        old_stream_id = event.get('PhysicalResourceId', '')
        if old_stream_id:
            delete_stream(cluster_id, old_stream_id)
        return create_stream(cluster_id, kinesis_arn, role_arn)
    elif request_type == 'Delete':
        stream_id = event.get('PhysicalResourceId', '')
        if stream_id and stream_id != 'NONE':
            delete_stream(cluster_id, stream_id)
        return {'PhysicalResourceId': stream_id or 'NONE'}


def create_stream(cluster_id: str, kinesis_arn: str, role_arn: str) -> dict:
    """Create a DSQL CDC stream targeting Amazon Kinesis."""
    try:
        response = DSQL_CLIENT.create_stream(
            clusterIdentifier=cluster_id,
            targetDefinition={
                'kinesis': {
                    'streamArn': kinesis_arn,
                    'roleArn': role_arn,
                }
            },
            ordering='UNORDERED',
            format='JSON',
        )

        stream_id = response['streamIdentifier']
        print(f'Created CDC stream: {stream_id} (status: {response["status"]})')

        # Wait for stream to become ACTIVE (max 60s)
        wait_for_active(cluster_id, stream_id)

        return {
            'PhysicalResourceId': stream_id,
            'Data': {
                'StreamId': stream_id,
                'StreamArn': response.get('arn', ''),
                'Status': 'ACTIVE',
            },
        }

    except Exception as e:
        print(f'Failed to create CDC stream: {e}')
        raise


def delete_stream(cluster_id: str, stream_id: str) -> None:
    """Delete a DSQL CDC stream."""
    try:
        DSQL_CLIENT.delete_stream(
            clusterIdentifier=cluster_id,
            streamIdentifier=stream_id,
        )
        print(f'Deleted CDC stream: {stream_id}')
    except DSQL_CLIENT.exceptions.ResourceNotFoundException:
        print(f'Stream {stream_id} already deleted')
    except Exception as e:
        print(f'Failed to delete CDC stream {stream_id}: {e}')
        raise


def wait_for_active(cluster_id: str, stream_id: str, max_wait: int = 60) -> None:
    """Poll until stream status is ACTIVE."""
    waited = 0
    while waited < max_wait:
        try:
            response = DSQL_CLIENT.get_stream(
                clusterIdentifier=cluster_id,
                streamIdentifier=stream_id,
            )
            status = response.get('status', '')
            if status == 'ACTIVE':
                return
            if status == 'FAILED':
                raise Exception(f'CDC stream {stream_id} entered FAILED state')
        except Exception as e:
            if 'ResourceNotFound' not in str(e):
                raise
        time.sleep(5)
        waited += 5

    print(f'Warning: stream {stream_id} not ACTIVE after {max_wait}s, proceeding')
