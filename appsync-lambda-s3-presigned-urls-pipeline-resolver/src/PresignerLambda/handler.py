import json
import os
import boto3
from botocore.exceptions import ClientError
from typing import Dict, Any
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
s3_client = boto3.client('s3', endpoint_url=f'https://s3.{os.environ.get("AWS_REGION")}.amazonaws.com')
dynamodb = boto3.resource('dynamodb')

# Environment variables to fetcht bucket and table names
BUCKET_NAME = os.environ['BUCKET_NAME']
TABLE_NAME = os.environ['TABLE_NAME']

# Presigned URL expiration time (in seconds)
# Both upload and download URLs will expire after 1 hour
UPLOAD_URL_EXPIRATION = 3600
DOWNLOAD_URL_EXPIRATION = 3600


def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Main Lambda handler for S3 operations.
    
    Supports two operations:
    1. generateUploadUrl: Creates a presigned URL for uploading files to S3
    2. generateDownloadUrl: Creates a presigned URL for downloading files from S3
    """
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        
        operation = event.get('operation')
        
        if operation == 'generateUploadUrl':
            return generate_upload_url(event)
        elif operation == 'generateDownloadUrl':
            return generate_download_url(event)
        else:
            raise ValueError(f"Unknown operation: {operation}")
            
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}", exc_info=True)
        return {
            'error': str(e),
            'message': 'Failed to process request'
        }


def generate_upload_url(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate a presigned URL for uploading a file to S3.
    
    Args:
        event: Contains 'noteId' and optional 'fileName'
        
    Returns:
        Dict containing 'uploadUrl' and 'attachmentKey'
    """
    note_id = event.get('noteId')
    file_name = event.get('fileName', 'attachment')
    
    if not note_id:
        raise ValueError("noteId is required")
    
    # Sanitize filename and create S3 key
    sanitized_filename = sanitize_filename(file_name)
    attachment_key = f"notes/{note_id}/{sanitized_filename}"
    
    try:
        # Generate presigned URL for PUT operation
        upload_url = s3_client.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': BUCKET_NAME,
                'Key': attachment_key,
                'ContentType': get_content_type(sanitized_filename),
            },
            ExpiresIn=UPLOAD_URL_EXPIRATION,
            HttpMethod='PUT'
        )
        
        logger.info(f"Generated upload URL for note {note_id}, key: {attachment_key}")
        
        return {
            'uploadUrl': upload_url,
            'attachmentKey': attachment_key,
            'expiresIn': UPLOAD_URL_EXPIRATION
        }
        
    except ClientError as e:
        logger.error(f"Error generating upload URL: {str(e)}")
        raise Exception(f"Failed to generate upload URL: {str(e)}")


def generate_download_url(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate a presigned URL for downloading a file from S3.
    
    Args:
        event: Contains 'attachmentKey'
        
    Returns:
        Dict containing 'downloadUrl' if attachment exists, empty dict otherwise
    """
    attachment_key = event.get('attachmentKey')
    
    # If no attachment key, return empty result (note has no attachment)
    if not attachment_key:
        logger.info("No attachment key provided, skipping download URL generation")
        return {}
    
    try:
        # Check if object exists
        try:
            s3_client.head_object(Bucket=BUCKET_NAME, Key=attachment_key)
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                logger.warning(f"Attachment not found: {attachment_key}")
                return {}
            raise
        
        # Generate presigned URL for GET operation
        download_url = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': BUCKET_NAME,
                'Key': attachment_key,
            },
            ExpiresIn=DOWNLOAD_URL_EXPIRATION,
            HttpMethod='GET'
        )
        
        logger.info(f"Generated download URL for key: {attachment_key}")
        
        return {
            'downloadUrl': download_url,
            'expiresIn': DOWNLOAD_URL_EXPIRATION
        }
        
    except ClientError as e:
        logger.error(f"Error generating download URL: {str(e)}")
        raise Exception(f"Failed to generate download URL: {str(e)}")


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename to prevent path traversal and invalid characters.
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename safe for S3
    """
    # Remove path components
    filename = os.path.basename(filename)
    
    # Replace spaces with underscores
    filename = filename.replace(' ', '_')
    
    # Remove any potentially dangerous characters
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.')
    filename = ''.join(c for c in filename if c in allowed_chars)
    
    # Ensure filename is not empty
    if not filename:
        filename = 'attachment'
    
    return filename


def get_content_type(filename: str) -> str:
    """
    Determine content type based on file extension.
    
    Args:
        filename: Name of the file
        
    Returns:
        MIME type string
    """
    extension = filename.lower().split('.')[-1] if '.' in filename else ''
    
    content_types = {
        'txt': 'text/plain',
        'pdf': 'application/pdf',
        'png': 'image/png',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'gif': 'image/gif',
        'json': 'application/json',
        'csv': 'text/csv',
        'doc': 'application/msword',
        'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'xls': 'application/vnd.ms-excel',
        'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    }
    
    return content_types.get(extension, 'application/octet-stream')