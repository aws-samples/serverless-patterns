import boto3
import urllib.parse
import os
import tempfile
from docx import Document

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['detail']['bucket']['name']
    source_key = event['detail']['object']['key']

    try:
        # Download the Word document from S3
        response = s3.get_object(Bucket=bucket, Key=source_key)
        word_content = response['Body'].read()

        # Create a temporary file from the Word document content
        with tempfile.TemporaryFile() as temp_file:
            temp_file.write(word_content)
            temp_file.seek(0)  # Move the file pointer to the beginning

            # Open the temporary file using the python-docx library
            doc = Document(temp_file)
            text = ''
            for para in doc.paragraphs:
                text += para.text + "\n"

        # Remove the 'raw/' prefix from the object key
        object_name = os.path.basename(source_key)

        # Write the text to a text file in the 'cleaned' prefix
        next_key = os.path.join(os.environ['NextPrefix'], object_name + "_text.txt")
        s3.put_object(Bucket=bucket, Key=next_key, Body=text.encode('utf-8'))

        print(f"Text extracted from Word document and written to {next_key} in bucket {bucket}")
    except Exception as e:
        print(f"Error: {e}")
        raise e

    return {
        'statusCode': 200,
        'body': f'File {source_key} processed and written to {next_key}',
        'next_key': next_key,
        'bucket': bucket
    }