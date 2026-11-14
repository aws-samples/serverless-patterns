# lambda handler
import boto3
import json
import os



def callRekognition(bucket_name,file_name):
    rekog_client = boto3.client('rekognition')
    response = rekog_client.detect_protective_equipment(
    Image={
        'S3Object': {
            'Bucket': bucket_name,
            'Name': file_name,
        }
    },
    SummarizationAttributes={
        'MinConfidence': float(os.environ['MIN_CONFIDENCE']),
        'RequiredEquipmentTypes': json.loads(os.environ['REQUIRED_PPE'])
    }
)
        
         
    return response


# publish a message to the IoT Topic
def writeIoT():
    iot_client = boto3.client('iot-data')
    iot_client.publish(topic = os.environ['TOPIC'],payload=json.dumps({"message":os.environ['MESSAGE']}))

# Check if anyone in the frame is not wearing the right PPE
def checkViolations(response):
    return response["Summary"]["PersonsWithoutRequiredEquipment"]

def lambda_handler(event, context):
    # S3 event
    s3_event = event['Records'][0]['s3']
    bucket_name = s3_event['bucket']['name']
    file_name = s3_event['object']['key']
    response = callRekognition(bucket_name,file_name)
    if(checkViolations(response)):
        writeIoT()

