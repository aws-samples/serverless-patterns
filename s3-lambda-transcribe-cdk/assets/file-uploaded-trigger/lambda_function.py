import json
import boto3
import os
import random

transcribe = boto3.client('transcribe')

output_bucket = os.environ['DESTINATION_BUCKET']

def lambda_handler(event, context):
    try:
        for record in event['Records']:

            # Get S3 Object Info
            bucket_name = record['s3']['bucket']['name']
            key = record['s3']['object']['key']

            job_name = key.split('.')[0]
            rand_id = random.randint(0, 1000000)
            job_name = job_name + str(rand_id)
            job_name = job_name[0:199] if len(job_name) >= 200 else job_name

            # Start Transcription Job
            response = transcribe.start_transcription_job(
                TranscriptionJobName=job_name,
                IdentifyLanguage=True,
                Media={
                    'MediaFileUri': 's3://' + bucket_name + '/' + key,
                    'RedactedMediaFileUri': 's3://' + bucket_name + '/' + key
                },
                OutputBucketName=output_bucket,
                OutputKey=job_name + '.json'
            )

        return {
            'statusCode': 200,
            'body': json.dumps(response['TranscriptionJob']['TranscriptionJobName'])
        }

    except Exception as e:
        print('Error')
        print(str(e))
        return {
            'statusCode': 500,
            'body': str(e)
        }
