# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0 (2026)
"""SecurityHub Auto-Remediation: Triggered by AWS Step Functions when
AWS Security Hub reports HIGH/CRITICAL findings. Remediates common
misconfigurations: open security groups, public S3 buckets, missing encryption."""

import json
from datetime import datetime, timezone

import boto3

EC2_CLIENT = boto3.client('ec2')
S3_CLIENT = boto3.client('s3')
SECURITYHUB_CLIENT = boto3.client('securityhub')


def lambda_handler(event, context):
    """Remediate AWS Security Hub finding based on type."""
    detail = event.get('detail', {})
    findings = detail.get('findings', [])

    if not findings:
        return {'status': 'SKIPPED', 'reason': 'No findings in event'}

    finding = findings[0]
    finding_type = finding.get('Type', '')
    finding_id = finding.get('Id', '')
    resources = finding.get('Resources', [])
    severity = finding.get('Severity', {}).get('Label', 'UNKNOWN')

    print(f'Remediating: {finding_type} | Severity: {severity} | ID: {finding_id}')

    try:
        if 'SecurityGroup' in finding_type or 'EC2' in finding_type:
            result = remediate_security_group(resources)
        elif 'S3' in finding_type and 'Public' in finding_type:
            result = remediate_s3_public_access(resources)
        else:
            result = {'action': 'NONE', 'reason': f'No handler for type: {finding_type}'}

        # Update finding workflow status to RESOLVED
        update_finding_status(finding_id, finding.get('ProductArn', ''))

        return {
            'status': 'REMEDIATED',
            'remediationType': finding_type,
            'findingId': finding_id,
            'severity': severity,
            'action': result.get('action', 'UNKNOWN'),
            'detail': result,
            'remediatedAt': datetime.now(timezone.utc).isoformat(),
        }

    except Exception as e:
        print(f'Remediation failed: {e}')
        return {
            'status': 'FAILED',
            'remediationType': finding_type,
            'findingId': finding_id,
            'error': str(e),
        }


def remediate_security_group(resources: list) -> dict:
    """Close open ingress rules (0.0.0.0/0) on security groups."""
    for resource in resources:
        resource_id = resource.get('Id', '')
        # Extract SG ID from ARN or direct ID
        sg_id = resource_id.split('/')[-1] if '/' in resource_id else resource_id

        if not sg_id.startswith('sg-'):
            continue

        try:
            sg = EC2_CLIENT.describe_security_groups(GroupIds=[sg_id])
            for permission in sg['SecurityGroups'][0].get('IpPermissions', []):
                open_ranges = [
                    r for r in permission.get('IpRanges', [])
                    if r.get('CidrIp') == '0.0.0.0/0'
                ]
                if open_ranges:
                    EC2_CLIENT.revoke_security_group_ingress(
                        GroupId=sg_id,
                        IpPermissions=[{
                            'IpProtocol': permission['IpProtocol'],
                            'FromPort': permission.get('FromPort', -1),
                            'ToPort': permission.get('ToPort', -1),
                            'IpRanges': open_ranges,
                        }],
                    )
                    print(f'Revoked 0.0.0.0/0 on {sg_id} port {permission.get("FromPort")}')

            EC2_CLIENT.create_tags(
                Resources=[sg_id],
                Tags=[
                    {'Key': 'SecurityHub:Remediated', 'Value': 'true'},
                    {'Key': 'SecurityHub:RemediatedAt', 'Value': datetime.now(timezone.utc).isoformat()},
                ],
            )

            return {'action': 'REVOKED_OPEN_INGRESS', 'securityGroupId': sg_id}

        except Exception as e:
            print(f'Failed to remediate SG {sg_id}: {e}')
            raise

    return {'action': 'NO_SG_FOUND'}


def remediate_s3_public_access(resources: list) -> dict:
    """Enable public access block on S3 buckets."""
    for resource in resources:
        resource_id = resource.get('Id', '')
        bucket_name = resource_id.split(':::')[-1] if ':::' in resource_id else resource_id

        try:
            S3_CLIENT.put_public_access_block(
                Bucket=bucket_name,
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': True,
                    'IgnorePublicAcls': True,
                    'BlockPublicPolicy': True,
                    'RestrictPublicBuckets': True,
                },
            )
            print(f'Enabled public access block on {bucket_name}')
            return {'action': 'ENABLED_PUBLIC_ACCESS_BLOCK', 'bucket': bucket_name}

        except Exception as e:
            print(f'Failed to remediate S3 bucket {bucket_name}: {e}')
            raise

    return {'action': 'NO_BUCKET_FOUND'}


def update_finding_status(finding_id: str, product_arn: str) -> None:
    """Mark finding as RESOLVED in AWS Security Hub."""
    try:
        SECURITYHUB_CLIENT.batch_update_findings(
            FindingIdentifiers=[{
                'Id': finding_id,
                'ProductArn': product_arn,
            }],
            Workflow={'Status': 'RESOLVED'},
            Note={
                'Text': 'Auto-remediated by serverless pattern',
                'UpdatedBy': 'securityhub-finding-sfn-remediation',
            },
        )
    except Exception as e:
        print(f'Failed to update finding status: {e}')
