import json
import boto3 

modelId = "anthropic.claude-v2"

def lambda_handler(event, context):
    # TODO implement
    # prompt_data =f"""
    # You are a world class writer. Write me a blog about teaching 8 yearl old boy.
    # """

    for record in event['Records']:
        print(record)
        request=json.loads(record["body"])
        print(request)
        prompt_data = request["prompt"]
        body = json.dumps({
            'prompt': f'Human:{prompt_data}\n\nAssistant:', 
            'max_tokens_to_sample': 1028,
            'temperature': 1,
            'top_k': 250,
            'top_p': 0.999,
            'stop_sequences': ['\n\nHuman:']
        })


        client = boto3.client('bedrock-runtime')
        response = client.invoke_model(
            body=body, modelId=modelId,  contentType="application/json",
            accept= "*/*"

        )
        body = json.loads(response["body"].read().decode("utf-8"))

        print(body)

        #### Publish response to websocket, IoT Core topic


