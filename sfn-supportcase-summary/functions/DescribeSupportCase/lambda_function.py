import json
import boto3

support_client = boto3.client('support')
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

def lambda_handler(event, context):
    # TODO implement
    caseid = event['caseid']
    bucketname = event['casedetail']['bucket']['name']
    data = support_client.describe_cases(
    displayId=caseid)
    
    communication_bodies = []
    if 'cases' in data and data['cases']:
        for case in data['cases']:
            if 'recentCommunications' in case and case['recentCommunications']:
                for communication in case['recentCommunications']['communications']:
                    communication_bodies.append(communication['body'])


    desc = ''
    i=0
    for body in communication_bodies:
        desc+=body
        i+=1
        print(i)
        
    print("desc"+desc)
    
    s3_path = caseid+'/desc'
    s3_resource.Bucket(bucketname).put_object(Key=s3_path, Body=desc)
    
    print('Summary written to s3 bucket')
    
    return {
        'statusCode': 200,
        "SourceBucketName": bucketname,
        "SourcePath": s3_path,
        'body': json.dumps('Hello from Lambda!')
    }
