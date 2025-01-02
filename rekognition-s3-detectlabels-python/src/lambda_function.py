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
            
            # Call Rekognition to detect faces
            response = rekognition.detect_labels(
                Image={
                    'S3Object': {
                        'Bucket': bucket,
                        'Name': key
                    }
                },
                MaxLabels=15
            )
            
            # Write the Rekognition output to the output bucket
            output_key = f"rekognition-output-{key}"
            output_key = output_key[:output_key.rfind('.')]
            output_key = output_key + ".json"
            print(output_key)
            
            labelDetection=response['Labels']
            print(response)
            
            s3.put_object(
                Bucket=os.environ['OUTPUT_BUCKET'],
                Key=output_key,
                Body=json.dumps(labelDetection)
            )
            
            return {
                'statusCode': 200,
                'body': json.dumps('Label detection successfully')
            }