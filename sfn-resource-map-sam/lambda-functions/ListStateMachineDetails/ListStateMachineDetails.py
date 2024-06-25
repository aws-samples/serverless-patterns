import boto3
import json
import csv
import os
from io import StringIO

def get_state_machine_definition(sfn_client, state_machine_arn):
    response = sfn_client.describe_state_machine(
        stateMachineArn=state_machine_arn
    )
    return response['definition']

def list_state_machines_and_resources(sfn_client):
    state_machines_info = []
    paginator = sfn_client.get_paginator('list_state_machines')
    for page in paginator.paginate():
        for state_machine in page['stateMachines']:
            state_machine_arn = state_machine['stateMachineArn']
            state_machine_name = state_machine['name']
            definition = get_state_machine_definition(sfn_client, state_machine_arn)
            definition_json = json.loads(definition)

            resources = set()
            for state in definition_json['States'].values():
                if 'Resource' in state:
                    resource_arn = state['Resource']
                    resources.add(resource_arn)

            state_machines_info.append({
                'Name': state_machine_name,
                'ARN': state_machine_arn,
                'Resources': list(resources)
            })

    return state_machines_info

def generate_csv(state_machines_info):
    csv_data = StringIO()
    writer = csv.writer(csv_data)
    writer.writerow(['Name', 'ARN', 'Resources'])
    for state_machine in state_machines_info:
        resources = ', '.join(state_machine['Resources'])
        writer.writerow([state_machine['Name'], state_machine['ARN'], resources])
    return csv_data.getvalue()

def upload_to_s3(csv_data, bucket_name, key):
    s3_client = boto3.client('s3')
    s3_client.put_object(
        Body=csv_data,
        Bucket=bucket_name,
        Key=key
    )

def lambda_handler(event, context):
    sfn_client = boto3.client('stepfunctions')
    state_machines_info = list_state_machines_and_resources(sfn_client)
    csv_data = generate_csv(state_machines_info)
    bucket_name = os.environ['S3BucketName']
    key = 'state-machines.csv'
    upload_to_s3(csv_data, bucket_name, key)
    return {
        'Status':'Success'
    }