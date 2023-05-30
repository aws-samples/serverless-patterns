import boto3
import os
import json
import gzip
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    items_to_add = []
    bucket_name = os.environ['BUCKET_NAME']
    
    for record in event['Records']:
        try:
            if record['s3']['bucket']['name'] != bucket_name:
                continue
            
            object_key = record['s3']['object']['key']
            
            response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
            log_data = gzip.decompress(response['Body'].read()).decode('utf-8')
            cloudtrail_logs = json.loads(log_data)['Records']
            
            for log in cloudtrail_logs:
                event_name = log['eventName']
                event_id = log['eventID']
                event_source = log['eventSource']
                    
                if event_name == 'CreateBucket':
                    bucket_name = log['requestParameters']['bucketName']
                    bucket_arn = f'arn:aws:s3:::{bucket_name}'
                            
                    item = {
                        'resource_arn': bucket_arn,
                        'event_id': event_id,
                        'event_source': event_source,
                        'resource_name': bucket_name,
                        'is_compliant': False
                    }
                    items_to_add.append(item)
                    
                if event_name == 'CreateCluster':
                    cluster_arn = log['responseElements']['cluster']['clusterArn']
                    cluster_name = log['requestParameters']['clusterName']
                        
                    item = {
                        'resource_arn': cluster_arn,
                        'event_id': event_id,
                        'event_source': event_source,
                        'resource_name': cluster_name,
                        'is_compliant': False
                    }
                    items_to_add.append(item)
                    
                if event_name.startswith('CreateFunction'):
                    function_name = log['requestParameters']['functionName']
                    region = log['awsRegion']
                    account_id = log['userIdentity']['accountId']
                    function_arn = f'arn:aws:lambda:{region}:{account_id}:function:{function_name}'
                        
                        
                    item = {
                        'resource_arn': function_arn,
                        'event_id': event_id,
                        'event_source': event_source,
                        'resource_name': function_name,
                        'is_compliant': False
                    }
                        
                    if not any(i['resource_arn'] == function_arn for i in items_to_add):
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