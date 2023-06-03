import json
import boto3
import os

def lambda_handler(event, context):
    kendra = boto3.client('kendra')
    query_text = event['query']
    index_id = os.getenv('KENDRA_INDEX_ID')

    response = kendra.query(
        QueryText=query_text,
        IndexId=index_id
    )
    
    # Process the response
    results = []
    for result in response['ResultItems']:
        if result['Type'] == 'ANSWER':
            # Prepare the result item
            result_item = {
                'AnswerText': result['DocumentExcerpt']['Text'],
            }
            
            # Add the result item to the results
            results.append(result_item)

    # Return the results
    return {
        'Results': results
    }