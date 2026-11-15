# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: MIT-0

import boto3
import json
import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

app = FastAPI() #specified in run.sh
bedrock = boto3.client('bedrock-runtime')


@app.post("/story")
async def api_story(request: Request):
    body = await request.json()
    topic = body.get("topic")
    print(f"Topic received: {topic}")
    return StreamingResponse(bedrock_stream(topic), media_type="text/html")


def bedrock_stream(topic: str):
    instruction = f"""
    You are a world class writer. Please write a sweet bedtime story about {topic}.
    """
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": instruction,
            }
        ],
    })

    response = bedrock.invoke_model_with_response_stream(
        modelId='global.anthropic.claude-sonnet-4-5-20250929-v1:0', #using Global CRIS Anthropic Claude Sonnet 4.5 on Bedrock
        body=body
    )

    stream = response.get('body')
    if stream:
        for event in stream:
            chunk = event.get('chunk')
            if chunk:
                message = json.loads(chunk.get("bytes").decode())
                if message['type'] == "content_block_delta":
                    yield message['delta']['text'] or ""
                elif message['type'] == "message_stop":
                    yield "\n"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", "8080"))) #port specified in run.sh