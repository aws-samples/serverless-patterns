import os
import logging

import boto3

bedrock_runtime = boto3.client('bedrock-runtime')

ENV = os.getenv("ENV")
ORGANIZATION = os.getenv("ORGANIZATION")
MODEL_ID = os.getenv("BEDROCK_MODEL_ID")

logging.basicConfig(
  format="%(asctime)s : %(levelname)s : %(message)s",
  level=logging.getLevelName(os.getenv("LOGGING_LEVEL", "INFO")),
  force=True,
)


def handler(event, context):
  logging.info("Lambda function started in %s environment for %s using model %s", ENV, ORGANIZATION, MODEL_ID)

  prompt = event.get('prompt_data', "Tell me something about AWS")
  logging.info("Prompt provided by user : %s", prompt)

  # The Converse API uses the same request shape for every model that supports it
  response = bedrock_runtime.converse(
    modelId=MODEL_ID,
    messages=[{"role": "user", "content": [{"text": prompt}]}],
    inferenceConfig={"maxTokens": 600},
  )

  answer = "".join(
    block["text"] for block in response["output"]["message"]["content"] if "text" in block
  )
  logging.info("Model response : %s", answer)

  return {
    'statusCode': 200,
    'body': answer,
  }
