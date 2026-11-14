import os


def lambda_handler(event, context):

    cognito_region = os.environ.get('cognito_region')   
    user_pools_id  = os.environ.get('user_pools_id')  
    user_pools_web_client_id = os.environ.get('user_pools_web_client_id')  
    print("Cognito Region: ",cognito_region)
    print("Cognito User Pool Id: ", user_pools_id)
    print("Cognito User Pool Client ID: ", user_pools_web_client_id)

   
    return {
        "statusCode": 200,
        'headers': {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    },
        "body": "OK"
    }
