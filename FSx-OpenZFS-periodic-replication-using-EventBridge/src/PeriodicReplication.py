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
sns_client = boto3.client('sns')

sns_notification = os.environ.get('SUCCESS_NOTIFICATION', "No") == 'Yes'
retain_days = int(os.environ.get('SNAPSHOT_RETAIN_DAYS'))

def send_sns_notification(msg, subject):
    sns_client.publish(
        TopicArn=os.environ.get("SNS_TOPIC_ARN"),
        Subject=subject,
        Message=msg
    )

def deleteSnapshotIfOlderThanRetention(snapshot):
    snapshot_id = snapshot['SnapshotId']
    created = snapshot['CreationTime']
    created_date = created.date()
    now_date = datetime.datetime.now().date()
    delta = now_date - created_date

    if delta.days > retain_days:
        fsx_client.delete_snapshot(SnapshotId=snapshot_id)
        print("Deleted FSx for OpenZFS volume snapshot " + snapshot_id)
    else:
        print("Skipping (retaining) FSx for OpenZFS volume snapshot " + snapshot_id)

def deleteSnapshots():
    print ("deleting snapshots")
    volume_ids = [os.environ.get("SRC_VOLUME_ID"), os.environ.get("DEST_VOLUME_ID")]

    # query the FSx API for existing snapshots
    for volId in volume_ids:
        print ("Getting snapshots for volume id = " + volId)
        snapshots = fsx_client.describe_snapshots(
                Filters=[{'Name': 'volume-id', 'Values': [volId]}],
                MaxResults=20
            )
        print(snapshots)

        # loop thru the results, checking the snapshot date-time and call Fsx API to remove those older than x hours/days
        print("Starting purge of snapshots older than " + str(retain_days) + " days for volume " + volId)
        for snapshot in snapshots['Snapshots']:
            response = fsx_client.list_tags_for_resource(ResourceARN=snapshot['ResourceARN'])
            #print (response)
            for tag in response['Tags']:
                if tag['Key'] == 'CreatedBy' and tag['Value'] == os.environ.get("SNAPSHOT_TAG_VALUE"):
                    deleteSnapshotIfOlderThanRetention(snapshot)


def lambda_handler(event, context):
    try:
        # call the FSx snapshot API
        print ("Creating a snapshot for the volume = " + os.environ.get("SRC_VOLUME_ID"))
        response = fsx_client.create_snapshot(
            # append datetime to ensure snap name is unique
            Name=os.environ.get("SNAPSHOT_NAME") + datetime.datetime.utcnow().strftime("_%Y-%m-%d_%H:%M:%S.%f")[:-3],
            VolumeId=os.environ.get("SRC_VOLUME_ID"),
            Tags=[{'Key': 'CreatedBy','Value': os.environ.get("SNAPSHOT_TAG_VALUE") },]
        )
        print(response)
        src_snapshot = response["Snapshot"]
        if sns_notification:
            print ("Sending SNS notification for successful snapshot creation")
            msg = "Snapshot Created Successfully\n\n"
            msg += "Snapshot ID : " + src_snapshot["SnapshotId"] + "\n"
            msg += "ResourceARN : " + src_snapshot["ResourceARN"] + "\n"
            msg += "Snapshot Name : " + src_snapshot["Name"] + "\n"
            msg += "Snapshot Tags : " + json.dumps(src_snapshot["Tags"]) + "\n"
            msg += "Snapshot Lifecycle : " + src_snapshot["Lifecycle"]
            send_sns_notification (msg, 'Success Notification: CreateSnapshot')

    except Exception as e:
        print("The error is: ", e)
        errMessage = "Error while creating a snapshot from the Source VolumeId = " + os.environ.get("SRC_VOLUME_ID") + "\n"
        errMessage += "Error = " + str(e)
        send_sns_notification (errMessage, 'Error Notification: CreateSnapshot')
        deleteSnapshots()
        return

    # call the FSx describe snapshot API to confirm created snapshot is in AVAILABLE state
    copy_snapshot = False
    for i in range(1, 10):
        time.sleep(10)
        print ("Describe Snapshot - Attept=" + str(i))
        ret = fsx_client.describe_snapshots(SnapshotIds=[src_snapshot["SnapshotId"]])
        print("Snapshot = " + src_snapshot["SnapshotId"] + " is in " + ret["Snapshots"][0]["Lifecycle"] +" state.")
        if ret["Snapshots"][0]["Lifecycle"] == "AVAILABLE":
            copy_snapshot = True
            break

    if copy_snapshot:
        try:
            print ("Starting copy snapshot operation ...")
            options = list(os.environ.get("OPTIONS").split(", "))
            option_list = []
            for item in options:
                option_list.append(item.strip())
            print (option_list)
            response = fsx_client.copy_snapshot_and_update_volume(
                    VolumeId=os.environ.get("DEST_VOLUME_ID"),
                    SourceSnapshotARN=src_snapshot["ResourceARN"],
                    Options=option_list,
                    CopyStrategy=os.environ.get("COPY_STRATEGY")
                )
            print (response)
            msg = "Started CopySnapshotAndUpdateVolume operation\n\n"
            msg += "Destination Volume ID : " + os.environ.get("DEST_VOLUME_ID") + "\n"
            msg += "Source Snapshot ARN : " + src_snapshot["ResourceARN"] 
            send_sns_notification (msg, 'Success Notification: CopySnapshotAndUpdateVolume')

        except Exception as e:
            print("The error is: ", e)
            errMessage = "Error while initiating CopySnapshotAndUpdateVolume operation\n\n"
            errMessage += "Destination Volume ID = " + os.environ.get("DEST_VOLUME_ID") + "\n"
            errMessage += "Source Snapshot ARN = " + src_snapshot["ResourceARN"] + "\n" + str(e)
            send_sns_notification (errMessage, 'Error Notification: CopySnapshotAndUpdateVolume')

    deleteSnapshots()
    print ("function completed")

