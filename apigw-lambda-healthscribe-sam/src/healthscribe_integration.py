import os
import boto3
from botocore.exceptions import ClientError
# import time
import uuid
import json

transcribe = boto3.client('transcribe')
# job_name = "my-first-medical-scribe-job"
# job_uri = "s3://healthscribe-conversation/conversation.mp3"
# output_bucket = "healthscribe-conversation"   


def lambda_handler(event, context):
    
    bucket = os.environ['BUCKET_NAME']
    transcribe_service_role = os.environ['TRANSCRIBE_SERVICE_ROLE']
    job_uri = "s3://" + bucket + "/conversation.mp3"
    print (job_uri)

    try:
        response = transcribe.start_medical_scribe_job(
            MedicalScribeJobName = str(uuid.uuid4()),
            Media = {
            'MediaFileUri': job_uri
            },
            OutputBucketName = bucket,
            DataAccessRoleArn = transcribe_service_role,
            Settings = {
            'ShowSpeakerLabels': False,
            'ChannelIdentification': True
            },
            ChannelDefinitions = [
            {
                'ChannelId': 0, 
                'ParticipantRole': 'CLINICIAN'
            }, {
                'ChannelId': 1, 
                'ParticipantRole': 'PATIENT'
            }
            ]
        )
        print(response)

    except ClientError as e:
        print(e)
        return {
            'statusCode': 500,
            'body': 'Error starting Transcribe job'
        }
    payload = {
    "jobStatus": "IN_PROGRESS",
    "jobName": f"{response['MedicalScribeJob']['MedicalScribeJobName']}"
    }
    return {
        'statusCode': 200,
        'body': json.dumps(payload)
    }
