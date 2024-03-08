import boto3
import base64
import json
from botocore.exceptions import ClientError
import os
from fpdf import FPDF

s3 = boto3.client('s3')

# Create a client for Amazon Bedrock
bedrock = boto3.client('bedrock-runtime')

def lambda_handler(event, context):

  input_bucket = os.environ['S3_BUCKET_INPUT'] 
  key = event['Records'][0]['s3']['object']['key']

  try:
    # Download JPEG image from S3
    image = s3.get_object(Bucket=input_bucket, Key=key)['Body'].read()

    # Convert to base64 encoding
    image_base64 = base64.b64encode(image).decode('utf-8')

    print(image_base64)

    # # Body for Claude v3 Sonnet
    body = json.dumps({
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 10000,
    "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "image",
              "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": image_base64
              }
            },
            {
              "type": "text",
              "text": "Can you create a blog based on this image? The blog should be explained well so that anyone having basic knowledge on AWS Services can understand it. Please start by saying 'Draft blog based on your image:'. Please include Title, Introduction, Conclusion sections along with any other sections required for the blog."
            }
          ]
        }
      ]
    })
    # Parameters for Claude V3 sonnet
    model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'
    accept = 'application/json'
    content_type = 'application/json'

    # Invoke Bedrock API
    response = bedrock.invoke_model(body=body, modelId=model_id, accept=accept, contentType=content_type)

    # Parse the response body
    response_body = json.loads(response.get('body').read())
    print(response_body)

    # Extract text
    text = response_body['content'][0]['text']

    # Create PDF
    pdf = FPDF() 
    pdf.add_page()

    pdf.set_font("Arial", size = 15)
    pdf.write(8, text)
    pdf.output("/tmp/draft-blog.pdf", "F")

    # Upload to S3
    output_bucket = os.environ['S3_BUCKET_OUTPUT'] 
    s3.upload_file('/tmp/draft-blog.pdf', output_bucket, 'draft-blog.pdf')

  except ClientError as e:
    print(e)
    return {
      'statusCode': 500,
      'body': 'Error generating the blog'
    }

  return {
    'statusCode': 200,
    'body': json.dumps({
        'generated-text': response_body
    })
}