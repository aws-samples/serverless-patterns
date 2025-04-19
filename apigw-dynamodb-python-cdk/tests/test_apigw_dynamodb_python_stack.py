import pytest
import requests
import boto3
from botocore.exceptions import ClientError

def get_stack_outputs(stack_name):
    client = boto3.client('cloudformation')
    response = client.describe_stacks(StackName=stack_name)
    outputs = response['Stacks'][0]['Outputs']
    
    return {output['OutputKey']: output['OutputValue'] for output in outputs}

@pytest.fixture(scope="module")
def config():
    stack_name = "ApigwDynamodbPythonStack"  
    output = get_stack_outputs(stack_name)
    return output

def get_api_key_value(apiKey):
    client = boto3.client('apigateway')
    response = client.get_api_key(
        apiKey=apiKey,
        includeValue=True
    )
    return response['value']

def create_cognito_user(username, password, client_id, pool_id, group_name):
    client = boto3.client('cognito-idp')
    
    try:
        response = client.admin_create_user(
            UserPoolId=pool_id,
            Username=username,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': username
                }
            ],
            # TemporaryPassword=password,
            MessageAction='SUPPRESS'
        )
        response = client.admin_set_user_password(
            UserPoolId=pool_id,
            Username=username,
            Password=password,
            Permanent=True
        )
        client.admin_add_user_to_group(
            UserPoolId=pool_id,
            Username=username,
            GroupName=group_name
        )
        return response
    except ClientError as e:
        print(f"Error creating user: {e}")
        return None

# Function to authenticate user and retrieve token
def authenticate_user(username, password, client_id):
    client = boto3.client('cognito-idp')
    
    try:
        response = client.initiate_auth(
            ClientId=client_id,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password,
            }
        )
        return response['AuthenticationResult']['IdToken']
    except ClientError as e:
        print(f"Error authenticating user: {e}")
        return None

# Function to delete a user from Cognito
def delete_cognito_user(username, pool_id):
    client = boto3.client('cognito-idp')
    
    try:
        client.admin_delete_user(
            UserPoolId=pool_id,
            Username=username
        )
    except ClientError as e:
        print(f"Error deleting user: {e}")

@pytest.fixture(scope="module")
def token(config):
    usernameBasic = 'testuser@mail.com'  # Choose a unique username
    usernameFree = "testuser1@mail.com"
    password = 'TestPassword123!'  # Ensure this meets Cognito password policy
    client_id=config['CognitoClientId']
    pool_id=config['CognitoUserPoolId']
    # Create user
    create_cognito_user(usernameFree, password, client_id, pool_id, "Group-FreeTier")
    create_cognito_user(usernameBasic, password, client_id, pool_id, "Group-BasicUsagePlan")
    
    # Authenticate user and get token
    user_token_free = authenticate_user(usernameFree, password, client_id)
    user_token_basic = authenticate_user(usernameBasic, password, client_id)


    # Finalizer to delete user after tests
    yield user_token_free, user_token_basic  # This is where the test will use the token
    delete_cognito_user(usernameFree, pool_id)  # This will run after the test is done
    delete_cognito_user(usernameBasic, pool_id)


def test_put_authorized(token, config):
    api_url = config['ApiUrl']
    api_url = f"{api_url}/put"  
    token_data = token[1]
    headers = {'Authorization': f'Bearer {token_data}', 'Content-Type': 'application/json'}
    payload = {"ID": "aa", "FirstName": "test", "Age": 22}  
    response = requests.post(api_url, headers=headers, json=payload)
    
    assert response.status_code == 200
    assert response.json()['body'] == {"message": "Item Added Successfully"}  

def test_put_unauthorized(config):
    api_url = config['ApiUrl']
    api_url = f"{api_url}/put"  
    headers = {'Authorization': f'Bearer invalid_token', 'Content-Type': 'application/json'}
    payload = {"ID": "aa", "FirstName": "test", "Age": 22}  

    response = requests.post(api_url, headers=headers, json=payload)
    
    assert response.status_code == 403  

def test_get_with_api_key(config):
    api_url = config['ApiUrl']
    api_url = f"{api_url}/get"  
    api_key_value = get_api_key_value(config['ApiKeyId0'])
    headers = {'x-api-key': api_key_value, 'Content-Type': 'application/json'}

    response = requests.get(api_url, headers=headers)

    assert response.status_code == 200
    assert response.json()['body'] == {"ID": "aa", "FirstName": "test", "Age": '22'}

def test_get_without_api_key(config):
    api_url = config['ApiUrl']
    api_url = f"{api_url}/get"  
    headers = {'Content-Type': 'application/json'}

    response = requests.get(api_url, headers=headers)
    print(response.text)

    assert response.status_code == 403
    assert response.json() == {'message': 'Forbidden'}

def test_delete_item_authorized(token, config):
    api_url = config['ApiUrl']
    api_url = f"{api_url}/delete/aa"  
    headers = {'Authorization': f'Bearer {token[0]}', 'Content-Type': 'application/json'}
    payload = {'ID': {'S': 'aa'}, 'FirstName': {'S': 'test'}}

    response = requests.post(api_url, headers=headers, json=payload)
    assert response.status_code == 200
