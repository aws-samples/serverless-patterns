import logging
import json
import time
import os
import io
from time import sleep
from pathlib import Path
import yaml
from yaml.loader import SafeLoader
import boto3


session = boto3.Session()
logger = logging.getLogger()
session = boto3.Session()


if 'log_level' in os.environ:
    logger.setLevel(os.environ['log_level'])
    logger.info("Log level set to %s" % logger.getEffectiveLevel())
else:
    logger.setLevel(logging.INFO)



def read_yaml(tag_file):
    print(tag_file)
    try:
        file = open(tag_file,'r')
        yaml_data = yaml.load(file, Loader=SafeLoader)
        return yaml_data
    except Exception as e:
        print("Cannot load the file")
        exit(1)
    
def update_resource_tags(account):
    print(account)
    ResourceId = str(account['id'])
    try:
        cross_account_role_name = os.getenv("CROSS_ACC_ROLE_NAME")
        ct_account_info = os.getenv("AFT_CT_ACCOUNT")
        role_arn = f"arn:aws:iam::{ct_account_info}:role/{cross_account_role_name}"
        stsMaster = boto3.client("sts")
        logger.info("Assume CT Session")

        assumeRoleResult  = stsMaster.assume_role (
            RoleArn=role_arn,
            RoleSessionName="AWSAFT-Session"
        )

        sessionAccount = boto3.Session (
            aws_access_key_id=assumeRoleResult["Credentials"]["AccessKeyId"],
            aws_secret_access_key=assumeRoleResult["Credentials"]["SecretAccessKey"],
            aws_session_token=assumeRoleResult["Credentials"]["SessionToken"],
            region_name=os.getenv("REGION"),
        )

        SourceOrgIdclient = sessionAccount.client(service_name='organizations', region_name=os.getenv("REGION"))

        response = SourceOrgIdclient.untag_resource(
            ResourceId= ResourceId,
            TagKeys=[
                'accountName',
                'company',
                'department'
            ]
        )        


        response = SourceOrgIdclient.tag_resource(
            ResourceId= ResourceId,
            Tags= account['tags'])

    except Exception as e:
        print(e)
        print("Could not update tags for account {}".format(ResourceId))
        

def lambda_handler(event, context):
        
        try:
              tag_file = Path("/opt/tag-data.yaml")


              if tag_file.is_file():
                print("File exists")
              else:
                print("File does not exists")
                exit(1)

              contents = read_yaml(tag_file)

              for account in contents['Accounts']:
                    update_resource_tags(account)

        except Exception as e:
                    return e