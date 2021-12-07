from datetime import datetime, timedelta, date
import os
import boto3

log_client = boto3.client('logs')

ARCHIVE_BUCKET = os.environ['ARCHIVE_BUCKET']
BUCKET_PREFIX = os.environ['BUCKET_PREFIX']


def get_snapshot_range_stamps():
    today = date.today()
    delta = timedelta(milliseconds=1)

    # end of the last day of previous month
    last = datetime(today.year, today.month, 1, 0, 0, 0, 0) - delta
    # midnight of the first day of previous month
    first = datetime(last.year, last.month, 1, 0, 0, 0, 0)

    # get timestamps in milliseconds.
    start = first.timestamp() * 1000
    end = last.timestamp() * 1000

    return int(start), int(end)


def handler(event, context):
    start, end = get_snapshot_range_stamps()
    log_group_name = event.get('name')

    destination_prefix = "{}{}".format(BUCKET_PREFIX, log_group_name)

    result = log_client.create_export_task(
        # strip arn prefix to derive only the log group name
        logGroupName=log_group_name,
        fromTime=start,
        to=end,
        destination=ARCHIVE_BUCKET,
        destinationPrefix=destination_prefix
    )

    return {"taskId": result['taskId']}
