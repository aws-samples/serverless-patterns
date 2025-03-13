import json
import boto3 

modelId = "anthropic.claude-3-5-sonnet-20240620-v1:0"

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
            'anthropic_version': 'bedrock-2023-05-31',
            'messages': [
                {'role': 'user', 'content': prompt_data}
            ],
            'max_tokens': 1024,
            'temperature': 1,
            'top_p': 0.999,
            'stop_sequences': ['\n\nHuman:']
        })


        client = boto3.client('bedrock-runtime')
        response = client.invoke_model(
            body=body, modelId=modelId,  contentType="application/json",
            accept= "*/*"

        )
        response_body = json.loads(response.get('body').read())
        print(response_body)
        body = response_body.get('content')[0].get('text')

        print(body)




