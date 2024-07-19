import json
import os
import boto3


s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

def lambda_handler(event, context):
    
    caseid = event['caseid']
    bucket = event['casedetail']['bucket']['name']
    key = event['casebuck']['Payload']['SourcePath']



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

    key1 = caseid+'/summary'

    s3_resource.Object(bucket, key1).put(Body=summary)
    print('Summary written to s3 bucket')
            
    return {
        'statusCode': 200,
        "SummaryBucketName": bucket,
        "SummaryPath": key1,
        "Summary":summary,
        'body': json.dumps('Successfully uploaded to S3!')
    }


#function to read from S3 bucket and key as input
def read_s3_file(bucket, key):
    obj = s3_client.get_object(Bucket=bucket, Key=key)
    return obj['Body'].read().decode('utf-8')
