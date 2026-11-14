import json
import boto3
import os
from tempfile import gettempdir
from contextlib import closing

# Get the s3 client
s3 = boto3.client("s3")
#  Create a client to use Polly
polly_client = boto3.client("polly")

def lambda_handler(event, context):
    """
    Get invoked from S3 trigger. Reads the text file from S3 and invokes polly for audio conversion.
    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format
        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
    context: object, required
        Lambda Context runtime methods and attributes
        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict
        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    # Get the s3 bucket name
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    # Get the file name
    file_name = event["Records"][0]["s3"]["object"]["key"]
    # Get the file object
    file_obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    # Read the file
    file_content = file_obj["Body"].read().decode("utf-8")

    # Call the Polly API to convert the text to speech
    response = polly_client.synthesize_speech(Text=file_content, OutputFormat="mp3", VoiceId="Joanna")
    print(response)
    # Get the audio file
    audio_file = response["AudioStream"]
    # Save the audio file to the s3 bucket
    audio_file_name = file_name.split(".")[0] + ".mp3"
    print(audio_file_name)
    with closing(audio_file) as stream:
        s3.put_object(Key=audio_file_name, Body=stream.read(),  Bucket=bucket_name)
    ##s3.put_object(Bucket=bucket_name, Key=audio_file_name, Body=file)
    ##with open(audio_file, 'rb') as data:
    ##    s3.upload_fileobj(data, bucket_name, audio_file_name)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Converted the text to speech"
        }),
    }
