import json
import boto3

client = boto3.client('bedrock-runtime')

def handler(event, context):

    body = json.loads(event.get('body', '{}'))
    #setting defult prompt if none provided
    prompt = body.get('prompt', 'Write a text to be posted on my social media channels about how Amazon Bedrock works')
    
    body = json.dumps({
        'prompt': "\n\nHuman:" + prompt + "\n\nAssistant:",
        "temperature": 0.5,
        "top_p": 1,
        "top_k": 250,
        "max_tokens_to_sample": 200,
        "stop_sequences": ["\n\nHuman:"]
    }) #all parameters (except for prompt) are set to default values

    modelId = 'anthropic.claude-v2'
    accept = 'application/json'
    contentType = 'application/json'

    response = client.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())

    return {
        'statusCode': 200,
        'body': json.dumps({
            'generated-text': response_body
        })
    }