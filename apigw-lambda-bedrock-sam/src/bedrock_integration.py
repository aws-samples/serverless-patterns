import json
import boto3

# Create a client for Amazon Bedrock
bedrock = boto3.client('bedrock-runtime')

def lambda_handler(event, context):

    # Extract the request body from the event object
    body = json.loads(event["body"])

    # Extract the prompt string from the request body
    prompt = body["prompt"]
    print("Prompt = " + prompt)

    # Create the body
    body = json.dumps({
        'prompt': "\n\nHuman:" + prompt + "\n\nAssistant:",
        "temperature": 0.5,
        "top_p": 1,
        "top_k": 250,
        "max_tokens_to_sample": 200,
        "stop_sequences": ["\n\nHuman:"]
    })

    # Set the model id and other parameters required to invoke the model
    model_id = 'anthropic.claude-v2'
    accept = 'application/json'
    content_type = 'application/json'

    # Invoke Bedrock API
    response = bedrock.invoke_model(body=body, modelId=model_id, accept=accept, contentType=content_type)
    print(response)

    # Parse the response body
    response_body = json.loads(response.get('body').read())
    print(response_body)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'generated-text': response_body
        })
    }