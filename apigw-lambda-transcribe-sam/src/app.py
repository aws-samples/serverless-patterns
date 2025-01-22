import json
import boto3
import os
import uuid
from datetime import datetime
from typing import Dict, Any

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    try:
        request_body = json.loads(event['body'])
        s3_url = request_body['audio_url']
        
        transcribe = boto3.client('transcribe')
        job_name = f"transcribe-{uuid.uuid4()}"
        
        response = transcribe.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={'MediaFileUri': s3_url},
            MediaFormat='mp3',  # Adjust based on your needs
            LanguageCode='en-US'  # Adjust based on your needs
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'job_name': job_name,
                'status': 'IN_PROGRESS'
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }