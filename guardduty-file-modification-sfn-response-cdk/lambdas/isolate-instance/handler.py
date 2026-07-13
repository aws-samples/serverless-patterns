# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0 (2026)
"""Instance Isolation: Triggered by AWS Step Functions when Amazon GuardDuty
detects HIGH severity sensitive file modification. Isolates the compromised
Amazon EC2 instance by replacing its security group, creating forensic
snapshots, and tagging for investigation."""

import json
from datetime import datetime, timezone

import boto3

EC2_CLIENT = boto3.client('ec2')


def lambda_handler(event, context):
    """Isolate a compromised Amazon EC2 instance."""
    detail = event.get('detail', {})
    resource = detail.get('resource', {})
    instance_details = resource.get('instanceDetails', {})
    instance_id = instance_details.get('instanceId', '')
    finding_type = detail.get('type', 'Unknown')
    severity = detail.get('severity', 0)

    if not instance_id:
        print(f'No instanceId in finding: {finding_type}')
        return {'status': 'SKIPPED', 'reason': 'No instance ID in finding'}

    print(f'Isolating instance {instance_id} | Finding: {finding_type} | Severity: {severity}')

    try:
        # Step 1: Get instance details
        instance_info = get_instance_info(instance_id)
        vpc_id = instance_info['VpcId']
        original_sgs = [sg['GroupId'] for sg in instance_info.get('SecurityGroups', [])]

        # Step 2: Create isolation security group (no ingress, no egress)
        isolation_sg = create_isolation_sg(vpc_id, instance_id)

        # Step 3: Replace security groups with isolation SG
        EC2_CLIENT.modify_instance_attribute(
            InstanceId=instance_id,
            Groups=[isolation_sg],
        )
        print(f'Replaced security groups on {instance_id} with isolation SG {isolation_sg}')

        # Step 4: Create forensic snapshots of all volumes
        snapshot_ids = create_forensic_snapshots(instance_id, instance_info, finding_type)

        # Step 5: Tag instance as isolated
        tag_instance(instance_id, finding_type, original_sgs)

        return {
            'status': 'ISOLATED',
            'instanceId': instance_id,
            'findingType': finding_type,
            'severity': severity,
            'isolationSecurityGroup': isolation_sg,
            'originalSecurityGroups': original_sgs,
            'forensicSnapshots': snapshot_ids,
            'isolatedAt': datetime.now(timezone.utc).isoformat(),
        }

    except Exception as e:
        print(f'Isolation failed for {instance_id}: {e}')
        return {
            'status': 'FAILED',
            'instanceId': instance_id,
            'error': str(e),
        }


def get_instance_info(instance_id: str) -> dict:
    """Get Amazon EC2 instance details."""
    try:
        response = EC2_CLIENT.describe_instances(InstanceIds=[instance_id])
        return response['Reservations'][0]['Instances'][0]
    except Exception as e:
        raise Exception(f'Failed to describe instance {instance_id}: {e}')


def create_isolation_sg(vpc_id: str, instance_id: str) -> str:
    """Create a security group with no ingress and no egress rules."""
    sg_name = f'guardduty-isolation-{instance_id}'

    try:
        response = EC2_CLIENT.create_security_group(
            GroupName=sg_name,
            Description=f'Isolation SG for compromised instance {instance_id}',
            VpcId=vpc_id,
        )
        sg_id = response['GroupId']

        # Remove the default egress rule (allow all outbound)
        EC2_CLIENT.revoke_security_group_egress(
            GroupId=sg_id,
            IpPermissions=[{
                'IpProtocol': '-1',
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}],
            }],
        )

        EC2_CLIENT.create_tags(
            Resources=[sg_id],
            Tags=[
                {'Key': 'Purpose', 'Value': 'GuardDuty-Isolation'},
                {'Key': 'CreatedBy', 'Value': 'guardduty-incident-response'},
            ],
        )

        print(f'Created isolation SG: {sg_id} (no ingress, no egress)')
        return sg_id

    except EC2_CLIENT.exceptions.ClientError as e:
        if 'InvalidGroup.Duplicate' in str(e):
            # SG already exists from a prior isolation
            sgs = EC2_CLIENT.describe_security_groups(
                Filters=[
                    {'Name': 'group-name', 'Values': [sg_name]},
                    {'Name': 'vpc-id', 'Values': [vpc_id]},
                ]
            )
            return sgs['SecurityGroups'][0]['GroupId']
        raise


def create_forensic_snapshots(instance_id: str, instance_info: dict, finding_type: str) -> list:
    """Create snapshots of all attached volumes for forensic analysis."""
    snapshot_ids = []
    block_devices = instance_info.get('BlockDeviceMappings', [])

    for device in block_devices:
        volume_id = device.get('Ebs', {}).get('VolumeId', '')
        if not volume_id:
            continue

        try:
            response = EC2_CLIENT.create_snapshot(
                VolumeId=volume_id,
                Description=f'Forensic snapshot - {instance_id} - {finding_type}',
                TagSpecifications=[{
                    'ResourceType': 'snapshot',
                    'Tags': [
                        {'Key': 'Purpose', 'Value': 'GuardDuty-Forensics'},
                        {'Key': 'SourceInstance', 'Value': instance_id},
                        {'Key': 'FindingType', 'Value': finding_type},
                        {'Key': 'CreatedAt', 'Value': datetime.now(timezone.utc).isoformat()},
                    ],
                }],
            )
            snapshot_ids.append(response['SnapshotId'])
            print(f'Created forensic snapshot {response["SnapshotId"]} for volume {volume_id}')
        except Exception as e:
            print(f'Failed to snapshot volume {volume_id}: {e}')

    return snapshot_ids


def tag_instance(instance_id: str, finding_type: str, original_sgs: list) -> None:
    """Tag the isolated instance for investigation tracking."""
    try:
        EC2_CLIENT.create_tags(
            Resources=[instance_id],
            Tags=[
                {'Key': 'GuardDuty:Status', 'Value': 'ISOLATED'},
                {'Key': 'GuardDuty:FindingType', 'Value': finding_type},
                {'Key': 'GuardDuty:IsolatedAt', 'Value': datetime.now(timezone.utc).isoformat()},
                {'Key': 'GuardDuty:OriginalSecurityGroups', 'Value': ','.join(original_sgs)},
            ],
        )
    except Exception as e:
        print(f'Failed to tag instance {instance_id}: {e}')
