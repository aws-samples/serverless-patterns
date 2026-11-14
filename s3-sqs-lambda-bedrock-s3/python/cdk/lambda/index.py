import json
import os
import boto3


s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

def lambda_handler(event, context):

    print(event)

    #sqs message body from event
    message = json.loads(event['Records'][0]['body'])

    # Get the bucket name and object from the sqs event
    bucket = message['Records'][0]['s3']['bucket']['name']
    key = message['Records'][0]['s3']['object']['key']


    with open('prompt_template.txt', "r") as file:
        template_String = file.read()

    data = {
        'transcript' : read_s3_file(bucket, key)
    }


    prompt = template_String.replace('{{transcript}}', data['transcript'])
    

    bedrock_runtime = boto3.client('bedrock-runtime')

    kwargs = {
        "modelId" : "amazon.titan-text-express-v1",
        "contentType" : "application/json",
        "accept": "*/*",
        "body": json.dumps({
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 512,
                "temperature" : 0,
                "topP" : 0.9
            }
        })
    }

    response = bedrock_runtime.invoke_model(**kwargs)

    response_body = json.loads(response.get('body').read())

    summary = response_body['results'][0]['outputText']

    print(summary)

    #write summary to s3 bucket
    # Get BUCKET_SUMMARY from environment variables
    bucket_summary = os.environ['BUCKET_SUMMARY']

    s3_resource.Object(bucket_summary, key).put(Body=summary)
    print('Summary written to s3 bucket')
            
    return 'Successfully processed SQS messages'


#function to read from S3 bucket and key as input
def read_s3_file(bucket, key):
    obj = s3.get_object(Bucket=bucket, Key=key)
    return obj['Body'].read().decode('utf-8')
