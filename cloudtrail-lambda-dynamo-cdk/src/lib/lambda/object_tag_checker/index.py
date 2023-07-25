import boto3
import os
from objects_db import Objects
from Event import Event
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
s3_client = boto3.client('s3')
table_name = os.environ['TABLE_NAME']

def resources_items():
    db_instance = Objects(dynamodb, table_name)
    response = db_instance.scan_objects()

    return response

def pass_items(items):
    objects_to_check = []
    for s3_object in items['Items']:
        s3_object = Event(**s3_object)
        objects_to_check.append(s3_object)
    
    return objects_to_check

def add_toSet(tags: list):
    tags_set = set()
    for value in tags:
        tags_set.add(value["Key"].strip())  
    return tags_set

def update_keys(item):
    resource_instance = Objects(dynamodb, table_name)
    attributes = {'is_compliant': item.is_compliant}
    resource_instance.add_key(item, attributes)

def check_compliance(objects):
    required_keys = {"Key1", "Key2", "Key3", "Key4"} # replace with required resource keys 
    for i in objects:
        try:
            tags_set = set()
        
            response = s3_client.get_object_tagging(Bucket=i.bucket_name, Key=i.object_key)
            
            tags = response['TagSet']
            print
            if tags:
                tags_set = add_toSet(tags)

            i.tags = tags_set    
            is_not_compliant = i.validate_compliance(required_keys = required_keys)
            
            if is_not_compliant or not i.tags:

                # further action may be taken here if not compliant (EX: notify admins using SNS)
                
                i.is_compliant = False
                print(i.object_key, 'is not compliant')
            else:
                i.is_compliant = True
                update_keys(i)
                print(i.object_key, 'is now compliant')
                
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