import json
import os
import time
import datetime
import boto3
import botocore
import logging
logger = logging.getLogger()
logger.setLevel("INFO")

logger.info("boto3 version: " + boto3.__version__)
logger.info("botocore version: " + botocore.__version__)

session = boto3.session.Session()
fsx_client = session.client(service_name='fsx')
volId = os.environ.get("DEST_VOLUME_ID")

def deleteSnapshotIfOlderThanRetention(snapshot, retain_days):
    snapshot_id = snapshot['SnapshotId']
    created = snapshot['CreationTime']
    created_date = created.date()
    now_date = datetime.datetime.now().date()
    delta = now_date - created_date

    try:
        logger.info("Examining OpenZFS volume snapshot " + snapshot['Name'] + " with Sanpshot ID = " + snapshot_id)
        if delta.days > retain_days:
            fsx_client.delete_snapshot(SnapshotId=snapshot_id)
            logger.info("Deleted FSx for OpenZFS volume snapshot " + snapshot['Name'] + " with Sanpshot ID = " + snapshot_id)
        else:
            logger.info("Skipping (retaining) FSx for OpenZFS volume " + snapshot['Name'] + " with Sanpshot ID = " + snapshot_id)
    except Exception as e:
        logger.info("The error is: " + str(e))

def deleteSnapshots(retain_days, snapshot_name):
    logger.info ("deleting snapshots")
    
    # query the FSx API for existing snapshots
    logger.info ("Getting snapshots for volume id = " + volId)
    next_token = None
    while True:
        # Prepare the base request parameters
        params = {
            'Filters':[{'Name': 'volume-id', 'Values': [volId]}],
            'MaxResults': 2  # 20 snapshots per API call
        }

        # Add NextToken if it exists
        if next_token:
            params['NextToken'] = next_token

        # Make the API call
        response = fsx_client.describe_snapshots(**params)
        
        # Process snapshots in current response
        snapshots = response.get('Snapshots', [])
        logger.info(snapshots)

        # loop thru the results, checking the snapshot date-time and call Fsx API to remove those older than x hours/days
        logger.info("Starting purge of snapshots older than " + str(retain_days) + " days for volume " + volId)
    
        for snapshot in snapshots:
            if snapshot['Name'].startswith(snapshot_name):
                deleteSnapshotIfOlderThanRetention(snapshot, retain_days)

        # Check if there are more results
        next_token = response.get('NextToken')
        if not next_token:
            break

def lambda_handler(event, context):
    logger.info(event)
    src_snapshot_arn = event["src_snapshot_ResourceARN"]
    retain_days = event["snapshot_retain_days"]
    snapshot_name = event["snapshot_name"]

    rspJson = {}
    try:
        logger.info ("Starting copy snapshot operation ...")
        options_string = os.environ.get("OPTIONS")
        options = [] if len(options_string) == 0 else list(options_string.split(", "))
        option_list = []
        for item in options:
            option_list.append(item.strip())
        logger.info ("CopySnapshotAndUpdateVolume Options: ")
        logger.info (option_list)

        response = fsx_client.copy_snapshot_and_update_volume(
                VolumeId=volId,
                SourceSnapshotARN=src_snapshot_arn,
                Options=option_list,
                CopyStrategy=os.environ.get("COPY_STRATEGY")
            )
        logger.info (response)
        msg = "Started CopySnapshotAndUpdateVolume operation\n\n"
        msg += "Destination Volume ID : " + os.environ.get("DEST_VOLUME_ID") + "\n"
        msg += "Source Snapshot ARN : " + src_snapshot_arn
        logger.info (msg)
        rspJson["Message"] = msg
        rspJson["Subject"] = 'Success Notification: CopySnapshotAndUpdateVolume'

    except Exception as e:
        logger.info("The error is: " +  str(e))
        msg = "Error while initiating CopySnapshotAndUpdateVolume operation\n\n"
        msg += "Destination Volume ID = " + os.environ.get("DEST_VOLUME_ID") + "\n"
        msg += "Source Snapshot ARN = " + src_snapshot_arn + "\n" + str(e)
        logger.info (msg)
        rspJson["Message"] = msg
        rspJson["Subject"] = 'Error Notification: CopySnapshotAndUpdateVolume'

    logger.info (rspJson)
    deleteSnapshots(retain_days, snapshot_name)
    logger.info ("function completed")
    return rspJson