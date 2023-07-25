import boto3
from botocore.exceptions import ClientError
import gzip
import json
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    
    items_to_add = []
    cloudtrail_bucket = os.environ['CLOUDTRAIL_BUCKET_NAME']
    
    for record in event['Records']:
        try:
            bucket_name = record['s3']['bucket']['name']
            
            if bucket_name != cloudtrail_bucket:
                continue
            
            object_key = record['s3']['object']['key']
            response = s3_client.get_object(Bucket=cloudtrail_bucket, Key=object_key)
            log_data = gzip.decompress(response['Body'].read()).decode('utf-8')
            cloudtrail_logs = json.loads(log_data)['Records']
            
            for log in cloudtrail_logs:
                event_name = log['eventName']
                user_identity = log['userIdentity']
                
                if (user_identity.get('type') == 'AWSService' and user_identity.get('invokedBy') == 'cloudtrail.amazonaws.com'):
                    continue
                
                if event_name == 'PutObject':
                    bucket_name = log['requestParameters']['bucketName']
                    key = log['requestParameters']['key']
                    object_arn = f'arn:aws:s3:::{bucket_name}/{key}'
                    item = {
                        'object_arn': object_arn,
                        'object_key': key,
                        'bucket_name': bucket_name,
                        'is_compliant': False
                    }
                    items_to_add.append(item)
        except ClientError as err:
            print(err)
            
    if items_to_add:
        with table.batch_writer() as batch:
            for item in items_to_add:
                batch.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }