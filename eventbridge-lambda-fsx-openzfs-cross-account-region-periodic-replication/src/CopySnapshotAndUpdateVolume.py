import json
import os
import time
import datetime
import boto3
import botocore

print("boto3 version: " + boto3.__version__)
print("botocore version: " + botocore.__version__)

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
        print("Examining OpenZFS volume snapshot " + snapshot['Name'] + " with Sanpshot ID = " + snapshot_id)
        if delta.days > retain_days:
            fsx_client.delete_snapshot(SnapshotId=snapshot_id)
            print("Deleted FSx for OpenZFS volume snapshot " + snapshot['Name'] + " with Sanpshot ID = " + snapshot_id)
        else:
            print("Skipping (retaining) FSx for OpenZFS volume " + snapshot['Name'] + " with Sanpshot ID = " + snapshot_id)
    except Exception as e:
        print("The error is: ", e)

def deleteSnapshots(retain_days, snapshot_name):
    print ("deleting snapshots")

    # query the FSx API for existing snapshots
    print ("Getting snapshots for volume id = " + volId)
    snapshots = fsx_client.describe_snapshots(
            Filters=[{'Name': 'volume-id', 'Values': [volId]}],
            MaxResults=20
        )
    print(snapshots)

    # loop thru the results, checking the snapshot date-time and call Fsx API to remove those older than x hours/days
    print("Starting purge of snapshots older than " + str(retain_days) + " days for volume " + volId)
    for snapshot in snapshots['Snapshots']:
        if snapshot['Name'].startswith(snapshot_name):
            deleteSnapshotIfOlderThanRetention(snapshot, retain_days)

def lambda_handler(event, context):
    print(event)
    src_snapshot_arn = event["src_snapshot_ResourceARN"]
    retain_days = event["snapshot_retain_days"]
    snapshot_name = event["snapshot_name"]

    rspJson = {}
    try:
        print ("Starting copy snapshot operation ...")
        options_string = os.environ.get("OPTIONS")
        options = [] if len(options_string) == 0 else list(options_string.split(", "))
        option_list = []
        for item in options:
            option_list.append(item.strip())
        print ("CopySnapshotAndUpdateVolume Options: ")
        print (option_list)

        response = fsx_client.copy_snapshot_and_update_volume(
                VolumeId=volId,
                SourceSnapshotARN=src_snapshot_arn,
                Options=option_list,
                CopyStrategy=os.environ.get("COPY_STRATEGY")
            )
        print (response)
        msg = "Started CopySnapshotAndUpdateVolume operation\n\n"
        msg += "Destination Volume ID : " + os.environ.get("DEST_VOLUME_ID") + "\n"
        msg += "Source Snapshot ARN : " + src_snapshot_arn
        print (msg)
        rspJson["Message"] = msg
        rspJson["Subject"] = 'Success Notification: CopySnapshotAndUpdateVolume'

    except Exception as e:
        print("The error is: ", e)
        msg = "Error while initiating CopySnapshotAndUpdateVolume operation\n\n"
        msg += "Destination Volume ID = " + os.environ.get("DEST_VOLUME_ID") + "\n"
        msg += "Source Snapshot ARN = " + src_snapshot_arn + "\n" + str(e)
        print (msg)
        rspJson["Message"] = msg
        rspJson["Subject"] = 'Error Notification: CopySnapshotAndUpdateVolume'

    print (rspJson)
    deleteSnapshots(retain_days, snapshot_name)
    print ("function completed")
    return rspJson