import json
import boto3
import os
import io
from tempfile import gettempdir
from contextlib import closing

# Get the s3 client
s3 = boto3.client("s3")
#  Create a client to use Polly
translate_client = boto3.client("translate")

output_bucket = os.environ['DESTINATION_BUCKET']

def lambda_handler(event, context):
    
    print(event)
    
    # Get the s3 bucket name
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    # Get the file name
    file_name = event["Records"][0]["s3"]["object"]["key"]
    # Get the file object
    file_obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    # Read the file
    file_content = file_obj["Body"].read().decode("utf-8")
    print(file_content)
    # Call the Polly API to convert the text to speech
    response = translate_client.translate_text(
            Text=file_content,
            SourceLanguageCode='auto',
            TargetLanguageCode='te'
        )
    print(response)
    # Get the audio file
    # Get the translated text from the response
    response_text = io.BytesIO(response['TranslatedText'].encode('utf-8'))
    txt_file_name = file_name.split(".")[0] + ".txt"
    s3.put_object(Key=txt_file_name, Body=response_text,  Bucket=output_bucket)
    return {
        'statusCode': 200,
        'body': json.dumps(response_text)
    }
