# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0 (2026)
"""Auto-remediation handler: Triggered by Amazon CloudWatch Log Alarm via
Amazon SNS. Restarts application service on tagged Amazon EC2 instances
using AWS Systems Manager RunCommand."""

import json
import os

import boto3

SSM_CLIENT = boto3.client('ssm')
LOGS_CLIENT = boto3.client('logs')


def lambda_handler(event, context):
    """Process Amazon SNS notification from Amazon CloudWatch Log Alarm."""
    for record in event.get('Records', []):
        try:
            sns_message = json.loads(record['Sns']['Message'])
            alarm_name = sns_message.get('AlarmName', 'unknown')
            new_state = sns_message.get('NewStateValue', 'UNKNOWN')
            reason = sns_message.get('NewStateReason', '')

            print(f'Alarm: {alarm_name} | State: {new_state} | Reason: {reason}')

            if new_state == 'ALARM':
                remediate(alarm_name, reason)
            elif new_state == 'OK':
                print(f'Alarm {alarm_name} recovered to OK — no action needed')

        except (json.JSONDecodeError, KeyError) as e:
            print(f'Failed to parse SNS message: {e}')
            continue

    return {'statusCode': 200, 'message': 'Processed'}


def remediate(alarm_name: str, reason: str) -> None:
    """Execute remediation via AWS Systems Manager RunCommand."""
    print(f'Executing remediation for alarm: {alarm_name}')

    # Send command to instances tagged with AutoRemediate=true
    try:
        response = SSM_CLIENT.send_command(
            Targets=[
                {
                    'Key': 'tag:AutoRemediate',
                    'Values': ['true'],
                }
            ],
            DocumentName='AWS-RunShellScript',
            Parameters={
                'commands': [
                    '#!/bin/bash',
                    'echo "Auto-remediation triggered by CloudWatch Log Alarm"',
                    f'echo "Alarm: {alarm_name}"',
                    f'echo "Reason: {reason[:200]}"',
                    'systemctl restart application.service || echo "Service restart failed"',
                    'echo "Remediation complete at $(date)"',
                ],
                'executionTimeout': ['60'],
            },
            TimeoutSeconds=120,
            Comment=f'Auto-remediation: {alarm_name}',
        )

        command_id = response['Command']['CommandId']
        instance_count = response['Command']['TargetCount']
        print(f'SSM command sent: {command_id} | Targets: {instance_count} instance(s)')

    except SSM_CLIENT.exceptions.InvalidInstanceId:
        print('No instances found with tag AutoRemediate=true')
    except Exception as e:
        print(f'SSM SendCommand failed: {e}')
        raise
