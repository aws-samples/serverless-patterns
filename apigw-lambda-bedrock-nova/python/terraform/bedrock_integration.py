import json
import boto3
import botocore

# Create Bedrock Runtime client
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1',
    endpoint_url='https://bedrock-runtime.us-east-1.amazonaws.com' 
)

def lambda_handler(event, context):
    try:
        # Handle both direct Lambda invocation and API Gateway requests
        if isinstance(event, dict):
            if 'body' in event:
                body = json.loads(event["body"])
            else:
                body = event
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'error': 'Invalid input format'
                })
            }

        # Extract the prompt
        prompt = body.get("prompt")
        if not prompt:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'error': 'Prompt is required'
                })
            }

        print("Prompt = " + prompt)

        # Create the request body for Nova Micro
        request_body = json.dumps({
            "system": [
                {
                    "text": "You are a helpful AI assistant that provides accurate and concise information."
                }
            ],
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            "inferenceConfig": {
                "maxTokens": 1024,
                "temperature": 0.7,
                "topP": 0.9,
                "topK": 50,
                "stopSequences": []
            }
        })

        # Invoke Bedrock API with Nova Micro model
        try:
            response = bedrock.invoke_model(
                body=request_body,
                modelId='amazon.nova-micro-v1:0',
                accept='application/json',
                contentType='application/json'
            )
            
            # Parse the response body
            response_body = json.loads(response['body'].read())
            print("Nova Micro Response:", response_body)

            # Extract text from the nested response structure
            generated_text = response_body.get('output', {}).get('message', {}).get('content', [{}])[0].get('text', '')

            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'generated-text': generated_text
                })
            }

        except botocore.exceptions.ClientError as e:
            print(f"Bedrock API Error: {str(e)}")
            return {
                'statusCode': 500,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'error': f"Bedrock API Error: {str(e)}"
                })
            }

    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e),
                'traceback': traceback.format_exc()
            })
        }
