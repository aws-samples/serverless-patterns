import json
import boto3
from botocore.exceptions import ClientError
import os

sts_client = boto3.client('sts')
EXTERNAL_ROLE_ARN = os.environ['EXTERNAL_ROLE_ARN']
AMI_TABLE_NAME = os.environ['AMI_TABLE_NAME']
MAPPING_TABLE_NAME = os.environ['MAPPING_TABLE_NAME']
EXTERNAL_ROLE_SESSION_NAME = 'test-dynamodb-session'
sts_session = sts_client.assume_role(RoleArn=EXTERNAL_ROLE_ARN, RoleSessionName=EXTERNAL_ROLE_SESSION_NAME)
region = os.environ['AWS_REGION']

KEY_ID = sts_session['Credentials']['AccessKeyId']
ACCESS_KEY = sts_session['Credentials']['SecretAccessKey']
TOKEN = sts_session['Credentials']['SessionToken']

dynamodb = boto3.resource('dynamodb',
                            region_name=region,
                            aws_access_key_id=KEY_ID,
                            aws_secret_access_key=ACCESS_KEY,
                            aws_session_token=TOKEN)

ami_table = dynamodb.Table(AMI_TABLE_NAME)

dynamodb_current = boto3.resource('dynamodb',region_name=region)
mapping_table = dynamodb_current.Table(MAPPING_TABLE_NAME)

def update_new_entry_in_dynamodb_(record,image_id,account_id,used_by,id):
    if used_by == 'launch_template':
        if 'launch_template_id' in record:
            record['launch_template_id'].append(id)
        else:
            record['launch_template_id'] = [id]
        record['launch_template_id'] = list(set(record['launch_template_id']))
        response = ami_table.update_item(
        Key={
            'image_id': image_id,
            'shared_entitiy_id': account_id
        },
        UpdateExpression="set  launch_template_id=:lt_id",
        ExpressionAttributeValues={
            ':lt_id': record['launch_template_id']
        },
        ReturnValues="UPDATED_NEW"
        )
    elif used_by == 'instance':
        if 'instance_id' in record:
            record['instance_id'].append(id)
        else:
            record['instance_id'] = [id]
        record['instance_id'] = list(set(record['instance_id']))
        response = ami_table.update_item(
        Key={
            'image_id': image_id,
            'shared_entitiy_id': account_id
        },
        UpdateExpression="set instance_id=:lt_id",
        ExpressionAttributeValues={
            ':lt_id': record['instance_id']
        },
        ReturnValues="UPDATED_NEW"
        )


def get_data_from_dynamodb(image_id,account_id):
    try:
        response = ami_table.get_item(
            Key={'image_id': image_id,
            'shared_entitiy_id': account_id
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        if 'Item' in response:
            return response['Item']
        else:
            return None

def update_mapping(id,image_id):
    response = mapping_table.update_item(
            Key={
                'id': id
            },
            UpdateExpression="set image_id=:image_id",
            ExpressionAttributeValues={
                ':image_id':image_id
            },
            ReturnValues="UPDATED_NEW"
            )


def  used_in_launch_template(event,account_id):
    request_parameters = event['requestParameters']
    if event['eventName'] == 'CreateLaunchTemplate':
        lt_id = event['responseElements']['CreateLaunchTemplateResponse']['launchTemplate']['launchTemplateId']
        launch_template_data =  request_parameters['CreateLaunchTemplateRequest']['LaunchTemplateData']
    elif event['eventName'] == 'CreateLaunchTemplateVersion':
        lt_id = event['responseElements']['CreateLaunchTemplateVersionResponse']['launchTemplateVersion']['launchTemplateId']
        launch_template_data =  request_parameters['CreateLaunchTemplateVersionRequest']['LaunchTemplateData']
        version_number = event['responseElements']['CreateLaunchTemplateVersionResponse']['launchTemplateVersion']['versionNumber']
        lt_id = lt_id + '_v' + str(version_number)

    image_id = launch_template_data['ImageId']

    update_mapping(lt_id,image_id)
    record = get_data_from_dynamodb(image_id, account_id)
    if record:
        update_new_entry_in_dynamodb_(record,image_id,account_id,'launch_template',lt_id)
    else:
        print("Data not present in DDB")

def used_in_run_instance(event,account_id):
    response_elements = event['responseElements']
    instances =  response_elements['instancesSet']['items']
    for i in instances:
        image_id = i['imageId']
        instance_id = i['instanceId']
        update_mapping(instance_id,image_id)
        record = get_data_from_dynamodb(image_id, account_id)
        if record:
            update_new_entry_in_dynamodb_(record,image_id,account_id,'instance',instance_id)
        else:
            print("Data not present in DDB")

def remove_entry_from_dynamodb(record,image_id,account_id,used_by,id):
    if used_by == 'launch_template':
        if 'launch_template_id' in record:
            if id in record['launch_template_id']:
                record['launch_template_id'].remove(id)
        record['launch_template_id'] = list(set(record['launch_template_id']))
        response = ami_table.update_item(
        Key={
            'image_id': image_id,
            'shared_entitiy_id': account_id
        },
        UpdateExpression="set launch_template_id=:lt_id",
        ExpressionAttributeValues={
            ':lt_id': record['launch_template_id']
        },
        ReturnValues="UPDATED_NEW"
        )
    elif used_by == 'instance':
        if 'instance_id' in record:
            if id in record['instance_id']:
                record['instance_id'].remove(id)
        record['instance_id'] = list(set(record['instance_id']))
        response = ami_table.update_item(
        Key={
            'image_id': image_id,
            'shared_entitiy_id': account_id
        },
        UpdateExpression="set instance_id=:lt_id",
        ExpressionAttributeValues={
            ':lt_id': record['instance_id']
        },
        ReturnValues="UPDATED_NEW"
        )


def get_image_id(id):
    try:
        response = mapping_table.get_item(
            Key={'id': id})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        if 'Item' in response:
            return response['Item']['image_id']
        else:
            return None

def remove_entry_from_mapping(lt_id):
    try:
        response = mapping_table.delete_item(
            Key={
                'id': lt_id
            }
        )
    except ClientError as e:
        print(e)

def remove_from_launch_template(event,account_id):
    requestParameters = event['requestParameters']
    latest_version = 1
    if event['eventName'] == 'DeleteLaunchTemplate':
        lt_id = requestParameters['DeleteLaunchTemplateRequest']['LaunchTemplateId']
        latest_version = event['responseElements']['DeleteLaunchTemplateResponse']['launchTemplate']['latestVersionNumber']
        default_version = event['responseElements']['DeleteLaunchTemplateResponse']['launchTemplate']['defaultVersionNumber']
        if default_version != 1:
            lt_id = lt_id + '_v' + str(default_version)
    elif  event['eventName'] == 'DeleteLaunchTemplateVersions':
        lt_id = requestParameters['DeleteLaunchTemplateVersionsRequest']['LaunchTemplateId']
        version_number = event['responseElements']['DeleteLaunchTemplateVersionsResponse']['successfullyDeletedLaunchTemplateVersionSet']['item']['versionNumber']
        if version_number != 1:
            lt_id = lt_id + '_v' + str(version_number)
    image_id = get_image_id(lt_id)
    record = get_data_from_dynamodb(image_id,account_id)
    if record:
        for i in range(2,(latest_version+1)):
            new_lt_id = lt_id + '_v' + str(latest_version)
            remove_entry_from_dynamodb(record,image_id,account_id,'launch_template',new_lt_id)
        remove_entry_from_dynamodb(record,image_id,account_id,'launch_template',lt_id)
    else:
        print("Data not present in DDB")
    remove_entry_from_mapping(lt_id)

def remove_from_run_instance(event,account_id):
    responseElements = event['responseElements']
    instnaces =  responseElements['instancesSet']['items']
    for i in instnaces:
        instance_id = i['instanceId']
        image_id = get_image_id(instance_id)
        record = get_data_from_dynamodb(image_id,account_id)
        if record:
            remove_entry_from_dynamodb(record,image_id,account_id,'instance',instance_id)
        else:
            print("Data not present in DDB")
        remove_entry_from_mapping(instance_id)


def lambda_handler(event, context):
    event = event['detail']
    account_id = event['userIdentity']['accountId']
    if event['eventName'] == 'CreateLaunchTemplate' or event['eventName'] == 'CreateLaunchTemplateVersion':
        used_in_launch_template(event,account_id)
    elif event['eventName'] == 'RunInstances':
        used_in_run_instance(event,account_id)
    elif event['eventName'] == 'DeleteLaunchTemplate' or event['eventName'] == 'DeleteLaunchTemplateVersions':
        remove_from_launch_template(event,account_id)
    elif event['eventName'] == 'TerminateInstances':
        remove_from_run_instance(event,account_id)
    else:
        print("Invalid")