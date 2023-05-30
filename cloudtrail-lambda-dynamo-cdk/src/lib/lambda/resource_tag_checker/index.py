import boto3
import os
from resources_db import Resources
from Event import Event
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
s3_client = boto3.client('s3')
dax_client = boto3.client('dax')
lambda_client = boto3.client('lambda')
table_name = os.environ['TABLE_NAME']

def resources_items():
    db_instance = Resources(dynamodb, table_name)
    response = db_instance.scan_resources()

    return response

def pass_items(items):
    resources_to_check = []
    for resource in items['Items']:
        resource = Event(**resource)
        print(resource)
        resources_to_check.append(resource)
    
    return resources_to_check

def add_toSet(tags: list):
    tags_set = set()
    for value in tags:
        tags_set.add(value["Key"].strip())  
    return tags_set

def update_keys(item):
    resource_instance = Resources(dynamodb, table_name)
    attributes = {'is_compliant': item.is_compliant}
    resource_instance.add_key(item, attributes)

def check_compliance(objects):
    required_keys = {"Key1", "Key2", "Key3", "Key4"} # replace with required resource keys 
    for i in objects:
        try:
            tags_set = set()
            if i.service == 's3':
                response = s3_client.get_bucket_tagging(Bucket=i.resource_name)               
                tags = response['TagSet']
                if tags:
                    tags_set = add_toSet(tags)
            elif i.service == 'dax': 
                response = dax_client.list_tags(ResourceName=i.resource_arn)
                tags = response['Tags'] 
                if tags:
                    tags_set = add_toSet(tags)
            elif i.service == 'lambda':
                response = lambda_client.list_tags(Resource=i.resource_arn)
                tags = response['Tags']
                if tags:
                    for value in tags:
                        tags_set.add(value.strip()) 
            i.tags = tags_set    
            is_not_compliant = i.validate_compliance(required_keys = required_keys)
            if is_not_compliant or not i.tags:
                # further action may be taken here if not compliant (EX: notify admins using SNS)
                i.is_compliant = False
                print(i.resource_name, 'is not compliant')
            else:
                i.is_compliant = True
                update_keys(i)
                print(i.resource_name, 'is now compliant')
                
        except ClientError as err:
            if err.response['Error']['Code'] == 'NoSuchTagSet':
                print(i.resource_name,'has no tags or does not exist')
            else:
                print(err)
        except Exception as err:
            print(err)  

def lambda_handler(event=None, context=None):
    items = resources_items() 
    objects = pass_items(items) 
    return check_compliance(objects)


print(lambda_handler())