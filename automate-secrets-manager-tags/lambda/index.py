import json
import boto3

secrets_manager_client = boto3.client('secretsmanager')
    
def lambda_handler(event, context):
    # Extract user info from the EventBridge event 
    try:
        principalId = event['detail']['userIdentity']['principalId']
        print(f'principalId:{principalId}')
        user_name = principalId.split(":")[1]
        
    except KeyError:
        print("Error: Could not extract user name from event")
        return

    secret_name = event['detail']['requestParameters']['name']

    try:
        # Apply a tag to the secret
        secrets_manager_client.tag_resource(
            SecretId=secret_name,
            Tags=[
                {
                    'Key': 'LoginUserName',
                    'Value': user_name
                }
            ]
        )
        print(f"Successfully tagged secret {secret_name} with username {user_name}")
    except Exception as e:
        print(f"Error tagging secret: {str(e)}")
        raise e
