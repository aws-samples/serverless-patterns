import json
import boto3
import base64
from urllib.parse import unquote_plus
import logging
import os

# Configure logging to ensure CloudWatch visibility
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s',
    force=True
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Constants
SUPPORTED_EXTENSIONS = ['jpg', 'jpeg', 'png']
NOVA_MODEL_ID = os.environ.get('NOVA_MODEL_ID', 'amazon.nova-lite-v1:0')
AWS_REGION = os.environ.get('AWS_REGION_CUSTOM', 'us-east-1')

def lambda_handler(event, context):
    """
    Lambda handler for processing image uploads using Amazon Nova Lite
    """
    try:
        # Extract S3 information
        record = event["Records"][0]
        bucket_name = str(record["s3"]["bucket"]["name"])
        file_key = unquote_plus(str(record["s3"]["object"]["key"]))
        
        # Check file extension
        file_extension = file_key.lower().split('.')[-1]
        if file_extension not in SUPPORTED_EXTENSIONS:
            print(f"SKIPPED: {file_key} - Unsupported file type: {file_extension}")
            return {"statusCode": 200, "body": "File type not supported"}
        
        # Process the image
        image_bytes = read_s3_image(bucket_name, file_key)
        tags = analyze_image_with_nova(image_bytes, file_key)
        applied_tags = apply_tags_to_s3_object(bucket_name, file_key, tags)
        
        # Success log
        print(f"SUCCESS: {file_key} | Model: {NOVA_MODEL_ID} | Nova Response: {', '.join(tags)} | Tags Applied: {len(applied_tags)}")
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "processed": True,
                "file": file_key,
                "model": NOVA_MODEL_ID,
                "tags_count": len(applied_tags)
            })
        }
        
    except Exception as e:
        file_key = "unknown"
        try:
            file_key = unquote_plus(str(event["Records"][0]["s3"]["object"]["key"]))
        except:
            pass
            
        print(f"FAILED: {file_key} | Model: {NOVA_MODEL_ID} | Error: {str(e)}")
        
        return {
            "statusCode": 500,
            "body": json.dumps({
                "processed": False,
                "file": file_key,
                "error": str(e)
            })
        }


def determine_image_format(filename):
    """Determine image format based on file extension"""
    extension = filename.lower().split('.')[-1]
    format_mapping = {'jpg': 'jpeg', 'jpeg': 'jpeg', 'png': 'png'}
    return format_mapping.get(extension, 'jpeg')


def analyze_image_with_nova(image_bytes, filename):
    """Use Amazon Nova Lite to analyze image and return descriptive tags"""
    try:
        bedrock_runtime = boto3.client("bedrock-runtime", region_name=AWS_REGION)
        
        # Prepare request
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        image_format = determine_image_format(filename)
        
        nova_request = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "image": {
                                "format": image_format,
                                "source": {"bytes": image_base64}
                            }
                        },
                        {
                            "text": "Analyze this image and provide exactly 10 descriptive single words that best describe what you see. Return only the words separated by commas, no explanations."
                        }
                    ]
                }
            ],
            "inferenceConfig": {
                "maxTokens": 100,
                "temperature": 0.1
            }
        }
        
        # Call Nova Lite
        response = bedrock_runtime.invoke_model(
            modelId=NOVA_MODEL_ID,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(nova_request)
        )
        
        # Parse response
        response_data = json.loads(response.get("body").read())
        
        if ("output" in response_data and 
            "message" in response_data["output"] and 
            "content" in response_data["output"]["message"] and 
            response_data["output"]["message"]["content"]):
            
            content = response_data["output"]["message"]["content"]
            if isinstance(content, list) and len(content) > 0:
                analysis_text = content[0].get("text", "")
            else:
                analysis_text = str(content)
            
            # Process into clean tags
            tags = [word.strip().lower() for word in analysis_text.split(",")]
            tags = [tag for tag in tags if tag and len(tag) > 0 and tag.replace('-', '').replace('_', '').isalnum()]
            return tags[:10]
        
        return get_fallback_tags()
        
    except Exception:
        return get_fallback_tags()


def get_fallback_tags():
    """Return fallback tags when Nova fails"""
    return ["image", "photo", "content", "visual", "media", "file", "upload", "data", "picture", "object"]


def read_s3_image(bucket, key):
    """Read image file from S3 bucket"""
    s3_client = boto3.client("s3")
    s3_object = s3_client.get_object(Bucket=bucket, Key=key)
    return s3_object["Body"].read()


def apply_tags_to_s3_object(bucket, key, tag_words):
    """Apply AI-generated tags to S3 object"""
    s3_client = boto3.client("s3")
    
    # Create S3 tag set
    tag_set = []
    for i, word in enumerate(tag_words[:10]):
        clean_word = ''.join(c for c in word if c.isalnum() or c in ['-', '_']).strip()
        if clean_word:
            tag_set.append({
                'Key': f'ai-tag-{i+1}',
                'Value': clean_word[:256]
            })
    
    if tag_set:
        s3_client.put_object_tagging(
            Bucket=bucket,
            Key=key,
            Tagging={'TagSet': tag_set}
        )
    
    return tag_set