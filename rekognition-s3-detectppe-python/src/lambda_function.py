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
            
            # Call Rekognition to detect the protective equipment
            response = rekognition.detect_protective_equipment(
                Image={
                    'S3Object': {
                        'Bucket': bucket,
                        'Name': key
                    }
                },
                SummarizationAttributes={
                    'MinConfidence': 90,
                    'RequiredEquipmentTypes': [
                        'FACE_COVER',
                        'HEAD_COVER',
                        'HAND_COVER',
            ]
        }
            )
            
            # Write the Rekognition output to the output bucket
            output_key = f"rekognition-output-{key}"
            output_key = output_key[:output_key.rfind('.')]
            output_key = output_key + ".json"
            print(output_key)
            print(response)
            ppe=response['Summary']
            
            s3.put_object(
                Bucket=os.environ['OUTPUT_BUCKET'],
                Key=output_key,
                Body=json.dumps(ppe)
            )
            
            return {
                'statusCode': 200,
                'body': json.dumps('Protective Equipments detected successfully')
            }