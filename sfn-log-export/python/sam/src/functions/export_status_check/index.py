import boto3

log_client = boto3.client('logs')


def handler(event, context):
    task_id = event['taskId']
    result = log_client.describe_export_tasks(taskId=task_id)

    # per documentation, only one export can run at a time per account,
    # therefore ensure none are running in this account
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.describe_export_tasks
    # result = log_client.describe_export_tasks(statusCode='CANCELLED' | 'PENDING' | 'PENDING_CANCEL' | 'RUNNING')
    status = 'RUNNING'

    task_status = result.get('exportTasks')
    if len(task_status) != 0:
        task_status = task_status[0].get('status').get('code')

    if task_status not in ['PENDING', 'PENDING_CANCEL', 'RUNNING']:
        status = 'NOT_RUNNING'

    return {"Status": status}
