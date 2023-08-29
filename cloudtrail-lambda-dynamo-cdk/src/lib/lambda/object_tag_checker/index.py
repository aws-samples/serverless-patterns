import boto3
import os
import logging
from objects_db import Objects
from Event import Event
from botocore.exceptions import ClientError
from boto3.dynamodb.types import TypeDeserializer

logger = logging.getLogger()
logger.setLevel(logging.INFO)

deserializer = TypeDeserializer()
dynamodb = boto3.resource("dynamodb")
s3_client = boto3.client("s3")
table_name = os.environ["TABLE_NAME"]


def pass_items(event):
    objects_to_check = []

    for record in event["Records"]:
        new_image = record["dynamodb"].get("NewImage")
        python_data = new_image
        print(python_data)
        for key, value in python_data.items():
            if "S" in value:
                python_data[key] = value["S"]
            elif "BOOL" in value:
                python_data[key] = value["BOOL"]

        python_data = Event(**python_data)

        objects_to_check.append(python_data)

    return objects_to_check


def add_to_set(tags: list):
    tags_set = set()
    for value in tags:
        tags_set.add(value["Key"].strip())
    return tags_set


def update_keys(item):
    resource_instance = Objects(dynamodb, table_name)
    attributes = {"is_compliant": item.is_compliant}
    resource_instance.add_key(item, attributes)


def check_compliance(objects):
    required_keys = {
        "Key1",
        "Key2",
        "Key3",
        "Key4",
    }  # replace with required object keys
    for i in objects:
        try:
            tags_set = set()
            print(i.bucket_name)

            response = s3_client.get_object_tagging(
                Bucket=i.bucket_name, Key=i.object_key
            )

            tags = response["TagSet"]

            if tags:
                tags_set = add_to_set(tags)

            i.tags = tags_set
            is_not_compliant = i.validate_compliance(required_keys=required_keys)

            if is_not_compliant or not i.tags:
                # further action may be taken here if not compliant (EX: notify admins using SNS)

                i.is_compliant = False
                print(i.object_key, "is not compliant")
            else:
                i.is_compliant = True
                update_keys(i)
                print(i.object_key, "is now compliant")

        except ClientError as err:
            if err.response["Error"]["Code"] == "NoSuchTagSet":
                print(i.resource_name, "has no tags or does not exist")
            else:
                print(err)
        except Exception as err:
            print(err)


def lambda_handler(event, context):
    objects = pass_items(event)
    return check_compliance(objects)