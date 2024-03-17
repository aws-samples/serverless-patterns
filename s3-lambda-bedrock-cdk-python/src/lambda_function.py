import boto3
import json

def lambda_handler(event, context):

    print("S3 Put Event Detected")

    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name'] 
    key = event['Records'][0]['s3']['object']['key']

    # Print a message
    print(f"File uploaded to bucket {bucket} with key {key}")

    inputContent = read_s3_file(bucket, key)

    embedding, token_count = generate_embeddings(inputContent)

    #print embedding and token count
    print(f"Embedding: {embedding}, Token Count: {token_count}")

    #return status code 200 with json text in body
    return {
        'statusCode': 200,
        'body': embedding}

#function to read from S3 bucket and key as input
def read_s3_file(bucket, key):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket, Key=key)
    return obj['Body'].read().decode('utf-8')

#function embeddings form input text using bedrock-runtime and amazon.titan-embed-text-v1 modelID
def generate_embeddings(text):

  bedrock = boto3.client('bedrock-runtime')

  body = json.dumps({
    "inputText": text
  })

  response = bedrock.invoke_model(
    body=body,
    modelId='amazon.titan-embed-text-v1',
    accept='application/json', 
    contentType='application/json'
  )

  response_body = json.loads(response['body'].read())

  embedding = response_body['embedding']
  token_count = response_body['inputTextTokenCount']

  return embedding, token_count
