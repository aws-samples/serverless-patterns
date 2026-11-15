import os
import sys
import subprocess
import boto3
import zipfile
import json
from datetime import datetime
import cfnresponse
boto3_bucket = os.environ['BOTO3_BUCKET']

def upload_file_to_s3(file_path, bucket, key):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket, key)
    print(f"Upload successful. {file_path} uploaded to {bucket}/{key}")

def make_zip_filename():
    now = datetime.now()
    timestamp = now.strftime('%Y%m%d_%H%M%S')
    filename = f'BedrockBoto3SDK_{timestamp}.zip'
    return filename

def zipdir(path, zipname):
    zipf = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file),
                        os.path.relpath(os.path.join(root, file), 
                                        os.path.join(path, '..')))
    zipf.close()

def deleteObject(existingZip):
    print(f'Deleting Existing Zip: {existingZip}')
    s3_client = boto3.client('s3')
    s3_client.delete_object(Bucket=existingZip["Bucket"], Key=existingZip["Key"])
    return

def lambda_handler(event, context):
    print("Event: ", json.dumps(event))
    physicalResourceId = event.get("PhysicalResourceId", None)
    existingZip = None
    if physicalResourceId:
        try:
            existingZip = json.loads(physicalResourceId)
        except:
            existingZip = ""
    responseData={}
    reason=""
    status = cfnresponse.SUCCESS
    try: 
        if event['RequestType'] != 'Delete':
            os.chdir('/tmp')
            print(f"running pip install boto3==1.28.57")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "boto3==1.28.57", "-t", "python" ])
            boto3_zip_name = make_zip_filename()
            zipdir("python",boto3_zip_name)
            print(f"uploading {boto3_zip_name} to s3 bucket {boto3_bucket}")
            upload_file_to_s3(boto3_zip_name, boto3_bucket, boto3_zip_name)
            responseData = {"Bucket": boto3_bucket, "Key": boto3_zip_name}
            physicalResourceId = json.dumps(responseData)
        else:
            print(f"RequestType is: {event['RequestType']}")
    except Exception as e:
        print(e)
        status = cfnresponse.FAILED
        reason = f"Exception thrown: {e}"
    # delete any previously created zip file (during update or delete), so that bucket can be deleted
    if existingZip:
        deleteObject(existingZip)
    cfnresponse.send(event, context, status, responseData, reason=reason, physicalResourceId=physicalResourceId)