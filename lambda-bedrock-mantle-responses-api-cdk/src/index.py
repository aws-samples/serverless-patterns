import os
import json
from openai import OpenAI

client = OpenAI(
    base_url=os.environ['OPENAI_BASE_URL'],
    api_key=os.environ['OPENAI_API_KEY'],
)


def handler(event, context):
    body = json.loads(event.get('body', '{}'))
    prompt = body.get('prompt', 'What is Amazon Bedrock?')
    model = body.get('model', 'openai.gpt-oss-120b')

    try:
        response = client.responses.create(
            model=model,
            input=[{'role': 'user', 'content': prompt}],
        )
        return {
            'statusCode': 200,
            'body': json.dumps({
                'response': response.output_text,
                'model': model,
                'id': response.id,
            }),
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
        }
