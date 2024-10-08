import logging
import os
import json
import boto3
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create required clients
ec2_client = boto3.client("ec2")
rbin_client = boto3.client("rbin")

resource_tag_key = os.getenv("RECYCLE_BIN_TAG_KEY", "Project")
resource_tag_value = os.getenv("RECYCLE_BIN_TAG_VALUE", "Test-Retention")

# Create required tags for the resources
def manage_tags(imageid, snapshotid):
    # Add snapshot id to the image
    ec2_tag_response = ec2_client.create_tags(
        Resources=[imageid],
        Tags=[
            {"Key": "SnapshotId", "Value": snapshotid},
        ],
    )

    # Before deleting the snapshot verify that the snapshot has the tags matching the recycle bin rule
    # AMIs are already filtered by the required tag name
    # Add image id to the snapshot
    snapshots = ec2_client.describe_tags(
        Filters=[
            {"Name": "resource-id", "Values": [snapshotid]},
            {"Name": "tag:" + resource_tag_key, "Values": [resource_tag_value]},
            {"Name": "resource-type", "Values": ["snapshot"]},
        ]
    )

    snapshot_tags = [{"Key": "ImageId", "Value": imageid}]
    # If the response list is empty, add required tags to the snapshot
    if not snapshots["Tags"]:
        snapshot_name_tag = {"Key": resource_tag_key, "Value": resource_tag_value}
        snapshot_tags.append(snapshot_name_tag)
    
    # Add image id to the snapshot
    snapshot_tag_response = ec2_client.create_tags(Resources=[snapshotid], Tags=snapshot_tags)
    return ec2_tag_response, snapshot_tag_response



# Deregister the obsolete AMIs and delete the associated snapshots
def deregister_amis(obsolete_amis):
    logger.info(f"AMIs to deregister {obsolete_amis}")
    for item in obsolete_amis:
        ec2_tag_response, snapshot_tag_response = manage_tags(item["ImageId"], item["SnapshotId"])
        # Proceed with deregistration only if the tags are added to the resources
        if (
            ec2_tag_response["ResponseMetadata"]["HTTPStatusCode"]
            == snapshot_tag_response["ResponseMetadata"]["HTTPStatusCode"]
            == 200
        ):
            logger.info(f"Successfully added tags to {item['ImageId']} and {item['SnapshotId']}")
            logger.info("Deregistering Image and deleting associated snapshot")
            ec2_client.deregister_image(ImageId=item["ImageId"])
            ec2_client.delete_snapshot(SnapshotId=item["SnapshotId"])
        else:
            logger.info("Failed to add tags to the resources. Cannot proceed with AMI cleanup")


# Verify the required recycle bin rules are present
def list_recycle_bin_rules(resource_type):
    rbin_rule_present = False
    resource_tags = [{"ResourceTagKey": resource_tag_key, "ResourceTagValue": resource_tag_value}]
    rbin_rules = rbin_client.list_rules(ResourceType=resource_type, ResourceTags=resource_tags)
    if rbin_rules["Rules"]:
        rbin_rule_present = True
    return rbin_rule_present


def lambda_handler(event, context):
    try:
        logger.info("Verifying the recycle bin rules")
        ebs_rule_exists = list_recycle_bin_rules("EBS_SNAPSHOT")
        ami_rule_exists = list_recycle_bin_rules("EC2_IMAGE")

        if not ebs_rule_exists or not ami_rule_exists:
            logger.info("One or more required recycle bin rules does not exists. Cannot proceed with AMI cleanup")
            return
        
        logger.info("Recycle bin rules present. Starting AMI cleanup")

        # Filter AMIs having the 'Expire-After' tag and 'Name' tag matching the recycle bin rule
        # The Expire-After tag can be added to the AMI during the vending process as per the lifecycle rule to retain AMI
        response = ec2_client.describe_images(
            Owners=["self"],
            Filters=[
                {"Name": "tag-key", "Values": ["Expire-After"]},
                {"Name": "tag:" + resource_tag_key, "Values": [resource_tag_value]},
            ],
        )

        # Get today's date in Zulu format
        zulu_format = "%Y-%m-%dT%H:%M:%SZ"
        today = datetime.strptime((datetime.now()).strftime(zulu_format), (zulu_format))

        if len(response["Images"]) == 0:
            logger.info("No AMIs found for cleanup. Exiting...")

        obsolete_amis = []
        for item in response["Images"]:
            ami_expiry = None
            if "Tags" in item:
                for tag in item["Tags"]:
                    if tag["Key"] == "Expire-After":
                        ami_expiry = datetime.strptime((tag["Value"]), zulu_format)
                        ami_expiration_in_days = (today - ami_expiry).days
                        break

            if ami_expiry and ami_expiration_in_days >= 0:
                    deregister_object = {
                        "ImageId": item["ImageId"],
                        "SnapshotId": item["BlockDeviceMappings"][0]["Ebs"]["SnapshotId"],
                    }
                    obsolete_amis.append(deregister_object)

        if len(obsolete_amis) > 0:
            deregister_amis(obsolete_amis)

    except Exception as e:
        logger.info(e)






