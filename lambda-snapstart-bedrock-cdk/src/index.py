import json
import os
import boto3

bedrock = boto3.client("bedrock-runtime")
MODEL_ID = os.environ["MODEL_ID"]


def handler(event, context):
    prompt = event.get("prompt", "What are the benefits of Lambda SnapStart?")

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        contentType="application/json",
        accept="application/json",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": prompt}],
        }),
    )

    body = json.loads(response["body"].read())

    return {
        "statusCode": 200,
        "body": json.dumps({
            "prompt": prompt,
            "response": body["content"][0]["text"],
            "model": MODEL_ID,
            "usage": body["usage"],
        }),
    }
