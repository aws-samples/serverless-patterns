import json
import boto3

# Get list of available foundational models using the 'bedrock' client.
# This allows the application to interact with the service configuratoin.
bedrock = boto3.client('bedrock')
models = str(bedrock.list_foundation_models())

# 'bedrock_runtime' is the client to consume the Bedrock service
bedrock_runtime = boto3.client('bedrock-runtime')

def handler(event, context):
    model_id = event['model_id']
    request_body = event['request_body']
    # Attempt Bedrock invocation
    try:
        body = json.loads(bedrock_runtime.invoke_model(body=json.dumps(
            request_body), modelId=model_id)['body'].read().decode('utf-8'))
        statusCode = 200
    # If any error occurs return the error and list of avaiable foundational models
    except Exception as e:
        body = {
            "error":str(e),
            "request_body":request_body,
            "models":models
        }
        statusCode = 500
    # Bedrock invocation sucessful, alongside the modela response, return model_id and execution time to help evaluate models performances
    return {
        'statusCode': statusCode,
        'model_id': model_id,
        'execution_time': 50000-context.get_remaining_time_in_millis(),
        'body': json.dumps(body)
    }