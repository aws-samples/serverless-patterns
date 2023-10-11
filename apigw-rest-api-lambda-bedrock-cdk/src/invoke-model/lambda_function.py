import boto3
import json
import traceback

bedrock_client = boto3.client("bedrock-runtime")
modelId = "anthropic.claude-v2"


def lambda_handler(event, context):

    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    try:

        prompt_data = json.loads(event["body"])["prompt"]
        request = json.dumps({
            'prompt': f'Human:{prompt_data}\n\nAssistant:',
            'max_tokens_to_sample': 1028,
            'temperature': 1,
            'top_k': 250,
            'top_p': 0.999,
            'stop_sequences': ['\n\nHuman:']
        })

        bedrock_response = bedrock_client.invoke_model(
            modelId=modelId,
            body=request,
        )

        response['body'] = bedrock_response["body"].read().decode("utf-8")

    except:
        traceback.print_exc()

        response['body'] = "Oops! Something is not working"

    return response