import json
import boto3
from urllib.parse import unquote_plus

# import requests


def getTitanEmbeddingFromText(content):
    modelId = "amazon.titan-embed-text-v1"
    contentType = "application/json"
    accept = "*/*"
    body = json.dumps({"inputText": json.dumps(content)})
    bedrock_client = boto3.client("bedrock-runtime")

    response = bedrock_client.invoke_model(
        modelId=modelId, contentType=contentType, accept=accept, body=body
    )

    # print(response)
    response_body = json.loads(response.get("body").read())
    # print(response_body)
    return response_body


# def main():

#    text = 'sample text'
#    txt_response = getTitanEmbeddingFromText(text)


# if __name__ == "__main__":
#    main()


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
        file_obj = event["Records"][0]
        bucketname = str(file_obj["s3"]["bucket"]["name"])
        filename = unquote_plus(str(file_obj["s3"]["object"]["key"]))
        print("Filename: ", filename)

        file_content = readFile(bucketname, filename)
        print(file_content)

        txt_response = getTitanEmbeddingFromText(file_content)
        print("Response:")
        print(txt_response)

    return {"statusCode": 200, "body": json.dumps(txt_response)}
