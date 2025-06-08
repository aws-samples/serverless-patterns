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

    # Create the request body using the messaging API format for Claude 3.5
    request_body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 200,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.5,
        "top_p": 1,
        "top_k": 250
    })

    # Set the model id and other parameters required to invoke the model
    model_id = 'anthropic.claude-3-5-sonnet-20240620-v1:0'
    accept = 'application/json'
    content_type = 'application/json'

    # Invoke Bedrock API
    response = bedrock.invoke_model(body=request_body, modelId=model_id, accept=accept, contentType=content_type)
    
    # Parse the response body
    response_body = json.loads(response.get('body').read())
    print(response_body)
    
    # Extract the completion from the messaging API response format
    completion = response_body.get('content', [{}])[0].get('text', '')
    stop_reason = response_body.get('stop_reason', '')
    
    # Format the response to maintain backward compatibility with the existing API
    formatted_response = {
        'completion': completion,
        'stop_reason': stop_reason
    }

    return {
        'statusCode': 200,
        'body': json.dumps({
            'generated-text': formatted_response
        })
    }