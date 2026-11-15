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
sns_client = boto3.client('sns')

sns_notification = os.environ.get('SUCCESS_NOTIFICATION', "No") == 'Yes'
retain_days = int(os.environ.get('SNAPSHOT_RETAIN_DAYS'))
snapshot_name = os.environ.get('SNAPSHOT_NAME')

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

    try:
        logger.info("Examining OpenZFS volume snapshot " + snapshot['Name'] + " with Sanpshot ID = " + snapshot_id)
        if delta.days > retain_days:
            fsx_client.delete_snapshot(SnapshotId=snapshot_id)
            logger.info("Deleted FSx for OpenZFS volume snapshot " + snapshot['Name'] + " with Sanpshot ID = " + snapshot_id)
        else:
            logger.info("Skipping (retaining) FSx for OpenZFS volume " + snapshot['Name'] + " with Sanpshot ID = " + snapshot_id)
    except Exception as e:
        logger.info("The error is: %s", str(e))

def deleteSnapshots():
    logger.info ("deleting snapshots")
    volId = os.environ.get("SRC_VOLUME_ID")

    # query the FSx API for existing snapshots
    logger.info ("Getting snapshots for volume id = " + volId)
    next_token = None
    while True:
        # Prepare the base request parameters
        params = {
            'Filters':[{'Name': 'volume-id', 'Values': [volId]}],
            'MaxResults': 20  # 20 snapshots per API call
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
                deleteSnapshotIfOlderThanRetention(snapshot)

        # Check if there are more results
        next_token = response.get('NextToken')
        if not next_token:
            break

def lambda_handler(event, context):
    try:
        # call the FSx snapshot API
        logger.info ("Creating a snapshot for the volume = " + os.environ.get("SRC_VOLUME_ID"))
        response = fsx_client.create_snapshot(
            # append datetime to ensure snap name is unique
            Name=os.environ.get("SNAPSHOT_NAME") + datetime.datetime.utcnow().strftime("_%Y-%m-%d_%H:%M:%S.%f")[:-3],
            VolumeId=os.environ.get("SRC_VOLUME_ID"),
            Tags=[{'Key': 'CreatedBy','Value': os.environ.get("SNAPSHOT_TAG_VALUE") },]
        )
        logger.info(response)
        src_snapshot = response["Snapshot"]
        if sns_notification:
            logger.info ("Sending SNS notification for successful snapshot creation")
            msg = "Snapshot Created Successfully\n\n"
            msg += "Snapshot ID : " + src_snapshot["SnapshotId"] + "\n"
            msg += "ResourceARN : " + src_snapshot["ResourceARN"] + "\n"
            msg += "Snapshot Name : " + src_snapshot["Name"] + "\n"
            msg += "Snapshot Tags : " + json.dumps(src_snapshot["Tags"]) + "\n"
            msg += "Snapshot Lifecycle : " + src_snapshot["Lifecycle"]
            send_sns_notification (msg, 'Success Notification: CreateSnapshot')

    except Exception as e:
        logger.info("The error is: " + str(e))
        errMessage = "Error while creating a snapshot from the Source VolumeId = " + os.environ.get("SRC_VOLUME_ID") + "\n"
        errMessage += "Error = " + str(e)
        send_sns_notification (errMessage, 'Error Notification: CreateSnapshot')
        deleteSnapshots()
        return

    # call the FSx describe snapshot API to confirm created snapshot is in AVAILABLE state
    copy_snapshot = False
    for i in range(1, 10):
        time.sleep(10)
        logger.info ("Describe Snapshot - Attempt=" + str(i))
        ret = fsx_client.describe_snapshots(SnapshotIds=[src_snapshot["SnapshotId"]])
        logger.info("Snapshot = " + src_snapshot["SnapshotId"] + " is in " + ret["Snapshots"][0]["Lifecycle"] +" state.")
        if ret["Snapshots"][0]["Lifecycle"] == "AVAILABLE":
            copy_snapshot = True
            break

    if not copy_snapshot:
        logger.info ("ERROR - The snapshot does not transition to AVAILABLE state for some reason - Snapshot ID : " + src_snapshot["SnapshotId"])
        msg = "ERROR - The snapshot does not transition to AVAILABLE state for some reason !!\n\n"
        msg += "Snapshot ID : " + src_snapshot["SnapshotId"] + "\n"
        msg += "Snapshot Name : " + src_snapshot["Name"] + "\n"
        send_sns_notification (msg, 'Error Notification: CreateSnapshot')
    else:
        try:
            logger.info ("Assuming role in target ...")
            sts_connection = boto3.client('sts')
            target_role = sts_connection.assume_role(
                RoleArn=os.environ.get("DEST_IAM_ROLE"),
                RoleSessionName="target_lambda_role"
            )

            # create a lambda client using the assumed role credentials
            lambda_client = boto3.client(
                'lambda',
                region_name=os.environ.get("DEST_LAMBDA_REGION"),
                aws_access_key_id=target_role['Credentials']['AccessKeyId'],
                aws_secret_access_key=target_role['Credentials']['SecretAccessKey'],
                aws_session_token=target_role['Credentials']['SessionToken'],
            )

            # prepare payload to invoke the target/destination lambda function
            payload = {
                "src_snapshot_ResourceARN": src_snapshot["ResourceARN"],
                "snapshot_retain_days":retain_days,
                "snapshot_name":snapshot_name
            }
            payload = json.dumps(payload)

            logger.info ("Invoking target lambda function ...")
            response = lambda_client.invoke(
                FunctionName=os.environ.get("DEST_LAMBDA_ARN"),
                InvocationType='RequestResponse',
                Payload=payload
            )

            logger.info ("Received response from a target lambda function ...")
            lambda_rsp = json.load(response["Payload"])
            logger.info(lambda_rsp)
            send_sns_notification (lambda_rsp["Message"], lambda_rsp["Subject"])

        except Exception as e:
            logger.info("The error is: " + str(e))
            errMessage = "Error while invoking target lambda function\n\n"
            errMessage += "Source Snapshot ARN = " + src_snapshot["ResourceARN"] + "\n" + str(e)
            logger.info(errMessage)
            send_sns_notification (errMessage, 'Error Notification: Invoke Lambda Function')

    deleteSnapshots()
    logger.info ("function completed")
