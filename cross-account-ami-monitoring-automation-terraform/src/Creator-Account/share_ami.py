import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
import os
import copy

region = os.environ['AWS_REGION']
DYNAMODB_TABLE_NAME = os.environ['DYNAMODB_TABLE_NAME']
SSM_PREFIX = os.environ['SSM_PREFIX']

dynamodb = boto3.resource('dynamodb',region_name=region)
ami_table = dynamodb.Table(DYNAMODB_TABLE_NAME)
ssm_client = boto3.client('ssm')

def insert_dynamodb(image_id,shared_account_id,shared_org_ou):

    entity_list = shared_account_id + shared_org_ou

    for entity_id in entity_list:
        response = ami_table.put_item(
            # Data to be inserted
            Item={
                'image_id': image_id,
                'shared_entitiy_id': entity_id,
                'AMI_share_status': 'AMI Shared'
            }
        )

def update_dynamodb(record,image_id,shared_account_id,shared_org_ou):
    for r in record['shared_account_id']:
        shared_account_id.append(r)
    for r in record['shared_org_ou']:
        shared_org_ou.append(r)
    shared_account_id = list(set(shared_account_id))
    shared_org_ou = list(set(shared_org_ou))

    response = ami_table.update_item(
    Key={
        'image_id': image_id
    },
    UpdateExpression="set shared_account_id=:shared_account_id ,shared_org_ou=:shared_org_ou",
    ExpressionAttributeValues={
        ':shared_account_id': shared_account_id,
        ':shared_org_ou': shared_org_ou
    },
    ReturnValues="UPDATED_NEW"
    )

def delete_dynamodb_record(image_id):
    response = ami_table.delete_item(
        Key={
            'image_id': image_id
        }
    )

    status_code = response['ResponseMetadata']['HTTPStatusCode']


def get_account_ids(image_id):
    response = ami_table.query(KeyConditionExpression=Key('image_id').eq(image_id)
    )
    print(response['Items'])
    account_ids=[]
    for rec in response['Items']:
        account_ids.append(rec['shared_entitiy_id'])
    return account_ids


def update_dynamodb_remove(image_id,entity_id,status):
    response = ami_table.update_item(
    Key={
        'image_id': image_id,
        'shared_entitiy_id': entity_id
    },
    UpdateExpression="set AMI_share_status=:status",
    ExpressionAttributeValues={
        ':status':  status
    },
    ReturnValues="UPDATED_NEW"
    )

def get_data_from_dynamodb(image_id,entity_id):
    try:
        response = ami_table.get_item(
            Key={
                'image_id': image_id,
                'shared_entitiy_id': entity_id
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        if 'Item' in response:
            return response['Item']
        else:
            return None

def check_shared_entry(record):
    instance_id = record.get('instance_id',[])
    launch_template_id = record.get('launch_template_id',[])
    return launch_template_id,instance_id

def check_ami_usage(record):
    still_in_use_acc_id = []
    acc_id = record.get('account_id',[])
    org_id = record.get('shared_org_ou',[])
    instance_id = record.get('instance_id',[])
    launch_template_id = record.get('launch_template_id',[])
    for acc in acc_id:
        still_in_use_acc_id.append(acc)
    for org in org_id:
        still_in_use_acc_id.append(acc)
    return still_in_use_acc_id,launch_template_id,instance_id

def notify_email(account, image_id,used_lt_id,used_instance_id):
        parameter = ssm_client.get_parameter(Name=SSM_PREFIX+"/"+account, WithDecryption=True)
        print(parameter['Parameter']['Value'])
        value = parameter['Parameter']['Value']
        SENDER = value
        RECIPIENT = [value]
        SUBJECT = f'[Action Required]: AMI issue alert in AWS Account {account}'
        BODY_HTML = BODY_HTML = f"""
        <html>
            <body>
                <h>Greetings from AWS Cross Account AMI Monitoring,</h><br>
                <p>There is an AMI deregistration happened that might effect which may likely impact your resources. Here are the details:<br><br>
                <b>Account:</b> {account}<br>
                <b>Region:</b> {region}<br>
                <b>Image Id:</b> {image_id}<br>
                <b>Still used in Launch templates:</b> {used_lt_id}<br>
                <b>Still used in EC2 Instance:</b> {used_instance_id}<br>
                Please connect with AMI Admin account owner to know more details about it.<br><br>
                Thanks, <br><br>Cross Account AMI Monitoring Team
                </p>
            </body>
        </html>
    """
        client = boto3.client('ses', region_name=region)
        response = client.send_email(
            Source=SENDER,
            Destination={
                'ToAddresses': RECIPIENT
            },
            Message={
                'Body': {
                    'Html': {
                        'Data': BODY_HTML
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': SUBJECT,
                },
            },
        )


def lambda_handler(event, context):
    requestParameters = event['detail']['requestParameters']
    event_name = event['detail']['eventName']
    image_id = requestParameters['imageId']
    if event_name == 'ModifyImageAttribute':
        if 'add' in requestParameters['launchPermission']:
            action = 'add'
        elif 'remove' in requestParameters['launchPermission']:
            action = 'remove'
        else:
            print("Invalid Action")
            raise
    elif event_name == 'DeregisterImage':
        action = 'delete'
    else:
        raise

    shared_account_id = []
    shared_org_ou = []
    if action != 'delete':
        for record in requestParameters['launchPermission'][action]['items']:
            if 'userId' in record:
                shared_account_id.append(record['userId'])
            elif 'organizationalUnitArn' in record:
                shared_org_ou.append(record['organizationalUnitArn'])

    if action == 'add':
        insert_dynamodb(image_id,shared_account_id,shared_org_ou)
    elif action == 'remove':
        for acc in shared_account_id:
            record = get_data_from_dynamodb(image_id,acc)
            used_lt_id,used_instance_id = check_shared_entry(record)
            if used_lt_id or used_instance_id:
                notify_email(acc,image_id,used_lt_id,used_instance_id)
            update_dynamodb_remove(image_id,acc,"AMI Sharing removed")
    elif action == 'delete':
        account_ids = get_account_ids(image_id)
        for acc in account_ids:
            record = get_data_from_dynamodb(image_id,acc)
            used_lt_id,used_instance_id = check_shared_entry(record)

            if used_lt_id or used_instance_id:
                print(f'still used in account ids {acc}')
                notify_email(acc,image_id,used_lt_id,used_instance_id)
            update_dynamodb_remove(image_id,acc,"AMI Deregistered")
    else:
        print("Error")
        raise Exception