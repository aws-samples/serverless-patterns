import json
import boto3
import os
import subprocess
import zipfile
import cfnresponse

ASSET_BUCKET_NAME = os.getenv('ASSET_BUCKET_NAME')

# Get the service client.
s3_client = boto3.client('s3')

#--------------------------------------------------
# function: create_recordings_folder
#--------------------------------------------------
def create_recordings_folder():

    status = ''
    error = ''

    try:
        # Create a 'recordings' folder in the bucket.
        s3_client.put_object(Bucket=ASSET_BUCKET_NAME, Key='recordings/')
        status = cfnresponse.SUCCESS
    except Exception as e:
        error = str(e)
        status = cfnresponse.FAILED

    return status, error

#--------------------------------------------------
# function: lambda_handler
#--------------------------------------------------
def lambda_handler(event, context):

    print(json.dumps(event, default=str))

    if event['RequestType'] == 'Create':

        status = ''
        error = ''

        #--------------------------------------------------
        # Create the recordings folder in the S3 bucket.
        #--------------------------------------------------
        status, error = create_recordings_folder()

        if status == cfnresponse.SUCCESS:
            status, error = create_recordings_folder()
        else:
            cfnresponse.send(event, context, cfnresponse.FAILED, {"error" : error})


    cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
