# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import boto3
import os
from contextlib import closing

# Get the aws translate client
translate_client = boto3.client('translate')
# Get the aws s3 client
s3_client = boto3.client("s3")
# Get the aws polly client
polly_client = boto3.client("polly")

def lambda_handler(event, context):
    # Fetch the message body and request timestamp from the request event
    req_body = json.loads(event['body'])
    timestamp = event['requestContext']['requestTimeEpoch']
    bucket_name = os.environ['S3_BUCKET_NAME']

    try:
        # Call translate_text API with the text and language given in the request body
        translate_response = translate_client.translate_text(
            Text=req_body["OriginalText"],
            SourceLanguageCode='auto',
            TargetLanguageCode=req_body["TranslateToLanguage"]
        )
        print(req_body)

        # Get the translated text from the response
        response_text = translate_response['TranslatedText']
        
        # Call the Polly API to convert translated text to speech
        response = polly_client.synthesize_speech(Text=response_text, OutputFormat="mp3", VoiceId="Lucia")
        
        # Get the audio file from the response
        audio_file = response["AudioStream"]
        
        # Create s3 filename using request timestamp
        audio_file_name = str(timestamp) + ".mp3"
        print(audio_file_name)
        
        # Save the audio file to the s3 bucket that was created during stack creation
        with closing(audio_file) as stream:
            s3_client.put_object(Key=audio_file_name, Body=stream.read(),  Bucket=bucket_name)
        
        # create response object
        response_json =  { 
            "TranslatedText": response_text, 
            "AudioFile": "s3://" + bucket_name + "/" + audio_file_name
        }
        
    except Exception as errormessage:
        # Get the error messages if translation fails
        response_json = str(errormessage)

    # return translated text or error response if translation fails
    return {
        'statusCode': 200,
        'body': json.dumps(response_json)
    }
