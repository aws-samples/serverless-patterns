import boto3
import json
import os
s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
        
def handler(event, context):
            # Extract bucket and key from the EventBridge event
            detail = event['detail']
            bucket = detail['bucket']['name']
            key = detail['object']['key']
            
            # Call Rekognition to detect document text
            response = rekognition.detect_text(
                Image={
                    'S3Object': {
                        'Bucket': bucket,
                        'Name': key
                    }
                }
            )
            
            # Write the Rekognition output to the output bucket
            output_key = f"rekognition-output-{key}"
            output_key = output_key[:output_key.rfind('.')]
            output_key = output_key + ".json"
            print(output_key)
            
            textDetections=response['TextDetections']
            print(response)
            
            s3.put_object(
                Bucket=os.environ['OUTPUT_BUCKET'],
                Key=output_key,
                Body=json.dumps(textDetections)
            )
            
            return {
                'statusCode': 200,
                'body': json.dumps('Text Detection successfully')
            }