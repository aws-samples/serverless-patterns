#! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: MIT-0
import time
import boto3

client = boto3.client('athena')

def lambda_handler(event, context):
    start_query_response = client.start_query_execution(
        QueryString=event['dbQuery'],
        QueryExecutionContext={'Database': event['dbName']},
        ResultConfiguration={'OutputLocation': event['s3OutputLocation']}
        )
    print(start_query_response)
    #Added sleep to wait till the execution is fully completed
    time.sleep(2)
    get_query_results_response = client.get_query_results(QueryExecutionId=start_query_response['QueryExecutionId'])
    print(get_query_results_response)
    return {
        'statusCode': 200,
        'body': 'OK'
    }