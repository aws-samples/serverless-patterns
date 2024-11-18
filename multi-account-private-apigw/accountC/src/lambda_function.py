import json
import boto3
import os
import logging
from botocore.exceptions import ClientError
import base64

logger = logging.getLogger()
logger.setLevel("INFO")

def lambda_handler(event, context):
    try:
        
        body = event.get('body')
        
        if not body:
            return {
                'statusCode': 400,
                "headers": {
                    "Content-Type": "application/json",
                },
                "isBase64Encoded": False,
                'body': json.dumps({"message": "Empty body!! Please pass a prompt in the request body."})
            }
        try:
            prompt = base64.b64decode(body).decode('utf-8')
            logger.info("Body was Base64-encoded. Decoded successfully.")
        except (base64.binascii.Error, UnicodeDecodeError):
            prompt = body
            logger.info("Body is a plain string. No decoding needed.")    

        image_base64 = generate_image(prompt=prompt)
        
        return {
            'statusCode': 200,
            "headers": {
                "Content-Type": "image/jpeg", 
            },
            "isBase64Encoded": True,
            'body': image_base64 
        }
    except Exception as e:
        logger.error("Failed to generate image: %s", e)
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",  
            },
            "isBase64Encoded": False,
            "body": json.dumps({"message": "Oops! Something went wrong. Please try again later."})
        }

def generate_image(prompt):
    """
    Generates an image using Amazon Titan Image Generator G1 model.
    
    Args:
        prompt (str): The text prompt for generating the image.
        
    Returns:
        str: Base64-encoded image data.
    
    Raises:
        ValueError: If the image generation fails.
    """
    region= os.environ.get('region')
    bedrock = boto3.client(service_name='bedrock-runtime', region_name=region)
    
    model_id = 'amazon.titan-image-generator-v2:0'
    body = json.dumps({
        "taskType": "TEXT_IMAGE",
        "textToImageParams": {
            "text": prompt
        },
        "imageGenerationConfig": {
            "numberOfImages": 1,
            "height": 1024,
            "width": 1024,
            "cfgScale": 8.0,
            "seed": 0
        }
    })

    try:
        logger.info("Generating image with model %s", model_id)
        response = bedrock.invoke_model(
            body=body,
            modelId=model_id,
            accept="application/json",
            contentType="application/json"
        )
        response_body = json.loads(response['body'].read())
        
        # Check for error in response
        if "error" in response_body:
            raise ValueError(f"Image generation failed: {response_body['error']}")
        
        base64_image = response_body["images"][0]
        logger.info("Image generated successfully with model %s", model_id)
        
        return base64_image  # Base64 string ready for direct return
    
    except ClientError as e:
        logger.error("AWS ClientError: %s", e)
        raise ValueError("Error invoking image generation model")
    except ValueError as e:
        logger.error("Image generation error: %s", e)
        raise
