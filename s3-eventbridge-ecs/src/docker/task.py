import sys
import os
from datetime import datetime
from datetime import date
import boto3

now = date.today()
processing_date = now.strftime("%m-%d-%Y")

s3Client = boto3.client('s3')


s3Bucket = os.environ['BUCKET_NAME']
s3ObjectKey = os.environ['OBJECT_KEY']
print(s3Bucket)
print(s3ObjectKey)

try:
    s3Response = s3Client.get_object(Bucket=s3Bucket,Key=s3ObjectKey)
    data = s3Response['Body'].read().decode('utf-8').splitlines(True)
    
    #implement business logic to process file

    result = {
        "status": "Success",
        "data": data,
        "processing_date": processing_date
    }
    print(result)
    

except Exception as e:
    result = {
        "status": "Failure",
        "data": data,
        "processing_date": processing_date
    }
    
    print(result)

    


    