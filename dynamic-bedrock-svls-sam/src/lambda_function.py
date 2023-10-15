import json
import sys
import base64
from pip._internal import main

main(['install', '-I', '-q', 'boto3', '--target', '/tmp/', '--no-cache-dir', '--disable-pip-version-check'])
sys.path.insert(0,'/tmp/')


region = 'us-east-1'

import boto3
print(boto3.__version__)

#initialize boto3 client
bedrock = boto3.client(service_name='bedrock-runtime', region_name=region)

def isbase64(payload):
    try:
        # Attempt to decode the payload as Base64
        decoded_payload = base64.b64decode(payload)
        # If decoding is successful, it's Base64 encoded
        return True
    except Exception as e:
        # If decoding raises an exception, it's not Base64 encoded
        return False


def lambda_handler(event, context):
    #fetch the resouce/model name
    resource = event['resource']
    
    prompt = event['body']
    
    #check if payload is base64 encoded or not 
    if isbase64(prompt) :
        base64_bytes = prompt.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        prompt = sample_string_bytes.decode("ascii")
    
    
    #select invoke model based on the resource/model from the request path
    if resource == '/text/model_ai21_j2grande' :
        kwargs = {
          "modelId": "ai21.j2-mid-v1",
          "contentType": "application/json",
          "accept": "*/*",
          "body": "{\"prompt\":\"" + prompt +"\",\"maxTokens\":200,\"temperature\":0.7,\"topP\":1,\"stopSequences\":[],\"countPenalty\":{\"scale\":0},\"presencePenalty\":{\"scale\":0},\"frequencyPenalty\":{\"scale\":0}}"
        }

    elif resource == '/text/model_ai21_j2jumbo' :
        kwargs = {
          "modelId": "ai21.j2-ultra-v1",
          "contentType": "application/json",
          "accept": "*/*",
          "body": "{\"prompt\":\"" + prompt +"\",\"maxTokens\":200,\"temperature\":0.7,\"topP\":1,\"stopSequences\":[],\"countPenalty\":{\"scale\":0},\"presencePenalty\":{\"scale\":0},\"frequencyPenalty\":{\"scale\":0}}"
        }

    elif resource == '/text/model_anthropic_claudeinstant' :
      #  prompt = prompt.encode('unicode_escape').decode('utf-8')
        kwargs = {
          "modelId": "anthropic.claude-instant-v1",
          "contentType": "application/json",
          "accept": "*/*",
          "body": "{\"prompt\":\"Human: "+ prompt +"\\nAssistant:\",\"max_tokens_to_sample\":300,\"temperature\":1,\"top_k\":250,\"top_p\":0.999,\"stop_sequences\":[\"\\n\\nHuman:\"],\"anthropic_version\":\"bedrock-2023-05-31\"}"
        }
        
    elif resource == '/text/model_anthropic_claudev2' :
        kwargs = {
          "modelId": "anthropic.claude-v2",
          "contentType": "application/json",
          "accept": "*/*",
          "body": "{\"prompt\":\"Human: "+ prompt +"\\nAssistant:\",\"max_tokens_to_sample\":300,\"temperature\":1,\"top_k\":250,\"top_p\":0.999,\"stop_sequences\":[\"\\n\\nHuman:\"],\"anthropic_version\":\"bedrock-2023-05-31\"}"
        }

    elif resource == '/image' :
        kwargs = {
          "modelId": "stability.stable-diffusion-xl-v0",
          "contentType": "application/json",
          "accept": "application/json",
          "body": "{\"text_prompts\":[{\"text\":\""+ prompt +"\"}],\"cfg_scale\":10,\"seed\":0,\"steps\":50}"
        }
    else :
        print("Invalid path")
        return {
            'statusCode': 404,
            'body': "Incorrect path"
        }

    #place invoke call to bedrock model to get response
    response = bedrock.invoke_model(**kwargs)
    print(response)
    response_body = json.loads(response.get('body').read())
    print(response_body)
    
    #image output
    if resource == '/image':
        final_resp = response_body['artifacts'][0]['base64']
        
        # Set the appropriate content type for your image
        response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "image/png",  
        },
        "isBase64Encoded": True,
        "body": final_resp
        }
        return response
        
    
    #anthropic output
    elif resource == '/text/model_anthropic_claudeinstant' or resource == '/text/model_anthropic_claudev2' :
        final_resp = response_body['completion']
        
    #ai21 output
    else :
        final_resp = response_body['completions'][0]['data']['text']
    
    #print(final_resp)
    
    return {
        'statusCode': 200,
        'body': final_resp
    }
