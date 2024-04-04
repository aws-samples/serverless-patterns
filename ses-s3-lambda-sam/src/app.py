import boto3
import email
from email.header import decode_header
import mimetypes

s3 = boto3.client('s3')

def lambda_handler(event, context):

    # Get the S3 bucket and object key from the event 
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Get the email object from S3
    obj = s3.get_object(Bucket=bucket, Key=key)
    msg = email.message_from_bytes(obj['Body'].read())

    # Process the email here
    print(f"Received email from {msg['From']}")

    # Print subject, body, attachments etc.
    print(f"Subject: {msg['Subject']}")
    
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            try:
                # Get the email body
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    print(f"Body: {part.get_payload(decode=True)}")
                # Get the attachments 
                if "attachment" in content_disposition:
                    filename = part.get_filename()
                    print(f"Attachment: {filename}")
            except:
                pass
    else:
        # Extract content type of email
        content_type = msg.get_content_type()
        # Get the email body
        print(f"Body: {msg.get_payload(decode=True)}")
