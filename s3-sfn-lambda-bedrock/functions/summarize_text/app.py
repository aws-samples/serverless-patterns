import json
import boto3
import os
from urllib.parse import unquote_plus
from datetime import datetime

def getSummaryFromText(content):
    modelId = "anthropic.claude-v2:1"
    contentType = "application/json"
    accept = "*/*"
    
    body = json.dumps({
    "prompt": "\n\nHuman: " + os.environ['BedrockPrompt'] + " \n " +content+ "\n\nAssistant:",
    "max_tokens_to_sample": 300,
    "temperature": 0.1,
    "top_p": 0.9,
})

    
    bedrock_client = boto3.client("bedrock-runtime")

    response = bedrock_client.invoke_model(
        modelId=modelId, contentType=contentType, accept=accept, body=body
    )

    response_body = json.loads(response.get("body").read())
    return response_body["completion"]


def readFile(bucket, key):
    s3_client = boto3.client("s3")
    fileObj = s3_client.get_object(Bucket=bucket, Key=key)
    file_content = fileObj["Body"].read().decode("utf-8")
    return file_content


def lambda_handler(event, context):
    txt_response = ""
    s3 = boto3.client("s3")
    if event:
        print("event", event)
        
        # Get the staged key and bucket name from the Step Functions event
        source_key = event["SourceKey"]
        
        # Check if the 'detail' key exists in the event
        bucketname = event["Bucket"]
        
        file_content = readFile(bucketname, source_key)
        print(file_content)

        txt_response = getSummaryFromText(file_content)
        print("Response:")
        print(txt_response)

        # Write output file to S3 bucket
        output_data = {
            "original_content": file_content,
            "summary": txt_response,
            "model": "anthropic.claude-v2:1",
            "datetime": str(datetime.now())
        }

        output_key = os.environ['NextPrefix'] + f"{source_key.split('/')[-1]}.json"
        s3.put_object(
            Body=json.dumps(output_data),
            Bucket=bucketname,
            Key=output_key
        )

    return {"statusCode": 200, "body": "File summary generated and uploaded to S3"}