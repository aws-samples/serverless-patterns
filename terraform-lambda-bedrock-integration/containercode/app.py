import json
import boto3
import sys
import os
import time
import logging
import logging.config

boto3_invoke_bedrock = boto3.client('bedrock-runtime')

def handler(event, context):

  env = os.getenv("ENV")
  organization = os.getenv("ORGANIZATION")
  log_level = logging.getLevelName(os.getenv("LOGGING_LEVEL"))
  bedrock_foundation_model = os.getenv("BEDROCK_FOUNDATION_MODEL")

  logging.basicConfig(
    format="%(asctime)s : %(levelname)s : %(message)s", level=log_level, force=True
  )
  logs = ""

  try:
    logging.info("Lambda Function Started in " + env + " environment" + " for " + organization + "utilizing foundation model : " + bedrock_foundation_model)

    if 'prompt_data' in event:
      prompt_data_text = event['prompt_data']
    else:  
      prompt_data_text = "Tell me Something about AWS"

    #Formatting the prompt before it is passed to the model
    body = json.dumps({"prompt": "Human:"+prompt_data_text+"\nAssistant:", "max_tokens_to_sample":600})
    
    #Define the model info
    modelId=bedrock_foundation_model
    accept = 'application/json'
    contentType = 'application/json'
    
    #Use boto3 to invoke the model with the prompt and print the response
    response = boto3_invoke_bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    logging.info("Prompt provided by user : " + prompt_data_text)
    logging.info("")
    print(response_body)

    return {
      'statusCode': 200,
    }

  except:
    logs = logs + str(sys.exc_info()[1])
    print(logs)