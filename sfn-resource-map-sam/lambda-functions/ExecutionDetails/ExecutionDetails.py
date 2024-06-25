import boto3
import csv
from io import StringIO
import os
from datetime import datetime, timedelta

def fetch_arns_and_names_from_s3(bucket_name, key):
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=bucket_name, Key=key)
    csv_data = response['Body'].read().decode('utf-8')
    csv_reader = csv.DictReader(StringIO(csv_data))

    state_machines_info = list(csv_reader)
    return state_machines_info

def get_execution_errors_and_throttles(cloudwatch_client, arn, start_time, end_time):
    throttles_metric = cloudwatch_client.get_metric_statistics(
        Namespace='AWS/States',
        MetricName='ExecutionThrottled',
        Dimensions=[
            {
                'Name': 'StateMachineArn',
                'Value': arn
            },
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=86400,  # 1 day
        Statistics=['Sum']
    )

    errors_metric = cloudwatch_client.get_metric_statistics(
        Namespace='AWS/States',
        MetricName='ExecutionsFailed',
        Dimensions=[
            {
                'Name': 'StateMachineArn',
                'Value': arn
            },
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=86400,  # 1 day
        Statistics=['Sum']
    )

    throttles = sum(data_point['Sum'] for data_point in throttles_metric['Datapoints'])
    errors = sum(data_point['Sum'] for data_point in errors_metric['Datapoints'])

    return int(errors), int(throttles)

def update_csv_with_errors_and_throttles(bucket_name, key):
    cloudwatch_client = boto3.client('cloudwatch')
    end_time = datetime.now()
    start_time = end_time - timedelta(days=7)

    state_machines_info = fetch_arns_and_names_from_s3(bucket_name, key)

    for state_machine in state_machines_info:
        arn = state_machine['ARN']
        errors, throttles = get_execution_errors_and_throttles(cloudwatch_client, arn, start_time, end_time)
        state_machine['Errors'] = errors
        state_machine['Throttles'] = throttles

    csv_data = generate_csv(state_machines_info)
    s3_client = boto3.client('s3')
    s3_client.put_object(
        Body=csv_data,
        Bucket=bucket_name,
        Key=key
    )

def generate_csv(state_machines_info):
    csv_data = StringIO()
    fieldnames = ['Name', 'ARN', 'Resources', 'Errors', 'Throttles']
    writer = csv.DictWriter(csv_data, fieldnames=fieldnames)
    writer.writeheader()
    for state_machine in state_machines_info:
        writer.writerow(state_machine)
    return csv_data.getvalue()

def lambda_handler(event, context):
    bucket_name = os.environ['S3BucketName']
    key = 'state-machines.csv'
    update_csv_with_errors_and_throttles(bucket_name, key)
    return {
        'Status':'Success'
    }
