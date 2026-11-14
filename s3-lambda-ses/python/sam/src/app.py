import boto3
from botocore.exceptions import ClientError
import os

s3 = boto3.client('s3')
ses = boto3.client('ses')

def lambda_handler(event, context):

  bucket = os.environ['S3_BUCKET'] 
  key = event['Records'][0]['s3']['object']['key']
  sender_email = os.environ['SENDER_EMAIL']
  recipient_email = os.environ['RECIPIENT_EMAIL']

  try:
    url = s3.generate_presigned_url('get_object',
                                    Params={'Bucket': bucket, 'Key': key},
                                    ExpiresIn=3600)

    body = f"A new object was uploaded to S3. You can access it with this pre-signed URL. The URL will expire in one hour: {url}"

    ses.send_email(
      Source=sender_email,
      Destination={
        'ToAddresses': [
          recipient_email
        ]
      },
      Message={
        'Subject': {
          'Data': 'New Amazon S3 object uploaded'
        },
        'Body': {
          'Text': {
            'Data': body
          }
        }
      }
    )

  except ClientError as e:
    print(e)
    return {
      'statusCode': 500,
      'body': 'Error generating pre-signed URL or sending email'
    }

  return {
    'statusCode': 200,
    'body': 'Email sent successfully'
  }