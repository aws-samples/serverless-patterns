"""Custom Resource handler for OpenSearch Serverless NextGen Collection Group.

CloudFormation doesn't yet support the 'Generation' parameter on
AWS::OpenSearchServerless::CollectionGroup. This custom resource uses
the boto3 API directly to create/delete NextGen collection groups.

Properties:
    Name: Collection group name (3-32 chars, lowercase alphanumeric + hyphens)
    Description: Optional description
    MaxIndexingCapacityInOCU: Max indexing OCUs (default: 2)
    MaxSearchCapacityInOCU: Max search OCUs (default: 2)
"""

from __future__ import annotations

import re

import boto3
from crhelper import CfnResource

helper = CfnResource(json_logging=True, log_level="INFO", sleep_on_delete=30)
client = boto3.client("opensearchserverless")


@helper.create
def on_create(event, context):
    """Create a NextGen collection group."""
    props = event["ResourceProperties"]
    name = props["Name"]
    description = props.get("Description", "")
    max_indexing = int(props.get("MaxIndexingCapacityInOCU", 2))
    max_search = int(props.get("MaxSearchCapacityInOCU", 2))

    resp = client.create_collection_group(
        name=name,
        standbyReplicas="ENABLED",
        generation="NEXTGEN",
        description=description,
        capacityLimits={
            "maxIndexingCapacityInOCU": max_indexing,
            "maxSearchCapacityInOCU": max_search,
        },
    )

    detail = resp["createCollectionGroupDetail"]
    helper.Data["Id"] = detail["id"]
    helper.Data["Arn"] = detail["arn"]
    helper.Data["Name"] = detail["name"]
    helper.Data["Generation"] = "NEXTGEN"

    return detail["id"]


@helper.update
def on_update(event, context):
    """Update the collection group capacity limits."""
    props = event["ResourceProperties"]
    physical_id = event["PhysicalResourceId"]
    max_indexing = int(props.get("MaxIndexingCapacityInOCU", 2))
    max_search = int(props.get("MaxSearchCapacityInOCU", 2))
    description = props.get("Description", "")

    client.update_collection_group(
        id=physical_id,
        description=description,
        capacityLimits={
            "maxIndexingCapacityInOCU": max_indexing,
            "maxSearchCapacityInOCU": max_search,
        },
    )

    helper.Data["Id"] = physical_id
    helper.Data["Name"] = props["Name"]
    helper.Data["Generation"] = "NEXTGEN"

    return physical_id


@helper.delete
def on_delete(event, context):
    """Delete the collection group."""
    physical_id = event["PhysicalResourceId"]

    # If the create failed, the physical ID will be the CFN logical ID
    # rather than a valid collection group ID (lowercase alphanumeric, 3-40 chars)
    if not re.match(r'^[a-z0-9]{3,40}$', physical_id):
        return

    try:
        client.delete_collection_group(id=physical_id)
    except client.exceptions.ResourceNotFoundException:
        pass


def lambda_handler(event, context):
    """Main Lambda handler — delegates to crhelper."""
    helper(event, context)
