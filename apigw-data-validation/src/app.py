import json

def lambda_handler(event, context):
    try:
        # Parse the incoming JSON body
        body = json.loads(event['body'])
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Data validation succeeded',
                'data': body
            })
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Invalid request body'
            })
        }