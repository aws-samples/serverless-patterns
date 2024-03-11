import boto3
import urllib.parse
import os
import tempfile
from pdf2image import convert_from_path
from PyPDF2 import PdfReader

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['detail']['bucket']['name']
    source_key = event['detail']['object']['key']

    try:
        # Download the PDF file from S3
        response = s3.get_object(Bucket=bucket, Key=source_key)
        pdf_content = response['Body'].read()

        # Create a temporary file from the PDF content
        with tempfile.TemporaryFile() as temp_file:
            temp_file.write(pdf_content)
            temp_file.seek(0)  # Move the file pointer to the beginning

            # Extract text from the PDF file
            pdf_reader = PdfReader(temp_file)
            text = ''
            for page in range(len(pdf_reader.pages)):
                text += pdf_reader.pages[page].extract_text()

        # Remove the 'raw/' prefix from the object key
        object_name = os.path.basename(source_key)

        # Write the text to a text file in the 'stage' prefix
        next_key = os.path.join(os.environ['NextPrefix'], object_name + "_text.txt")
        s3.put_object(Bucket=bucket, Key=next_key, Body=text.encode('utf-8'))

        print(f"Text extracted from PDF and written to {next_key} in bucket {bucket}")
    except Exception as e:
        print(f"Error: {e}")
        raise e

    return {
        'statusCode': 200,
        'body': f'File {source_key} processed and written to {next_key}',
        'next_key': next_key,
        'bucket': bucket
    }