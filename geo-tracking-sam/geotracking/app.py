# Function to retrieve all device positions using AWS Location service.
import boto3
import json
import datetime
import os
from dateutil import parser
from decimal import Decimal

client = boto3.client('location')

# dt_now = datetime.datetime.now()
# currentdatetime = dt_now.strftime('%m/%d/%Y %H:%M:%S')
currentdatetime = datetime.datetime.utcnow().strftime('%F %T.%f')[:-3]
# print ('Currentdatetime: ', currentdatetime)

def serialize_datetime(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    raise TypeError("Type not serializable")

def lambda_handler(event, context):
    # table_name = 'get-location-device-position'
    table_name = os.environ.get('TableName')
    # print ('Table Name: ', table_name)
    dynamodb = boto3.resource('dynamodb')
    # print ('Event Info: ', json.dumps(event))
    # print ('Tracker Name: ', event['detail']['requestParameters']['TrackerName'])
    table = dynamodb.Table(table_name)
    trackername = event['detail']['requestParameters']['TrackerName']
    deviceInfo = event['detail']['requestParameters']['Updates']
    for trackerdevice in deviceInfo:
        deviceId = trackerdevice['DeviceId']
        response = client.get_device_position(
            DeviceId=deviceId,
            TrackerName=trackername
        )
        # print ('Device Position: ', json.dumps(response, default=serialize_datetime))
        # print ('Tracker Position: ', response['Position'])
        # print ('RequestId: ', response['ResponseMetadata']['RequestId'])
        # print ('latitude: ', response['Position'][0])
        # print ('longitude: ', response['Position'][1])
        # print ('Currentdatetime: ', currentdatetime)
        dynamodb_response = table.put_item(
            TableName=table_name,
            Item={
                'id': response['ResponseMetadata']['RequestId'],
                'deviceId': response['DeviceId'],
                'longitude': json.loads(json.dumps(response['Position'][0]), parse_float=Decimal),
                'latitude': json.loads(json.dumps(response['Position'][1]), parse_float=Decimal),
                # 'latitude': response['Position'][0],
                # 'longitude': response['Position'][1],
                'CreatedAt': currentdatetime
            }            
        )        
        
        
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
