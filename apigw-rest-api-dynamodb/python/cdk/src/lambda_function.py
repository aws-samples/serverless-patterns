# A simple request-based authorizer example to demonstrate how to use request
# parameters to allow or deny a request. In this example, a request is
# authorized if the client-supplied headerauth1 header, QueryString1
# query parameter, and stage variable of StageVar1 all match
# specified values of 'headerValue1', 'queryValue1', and 'stageValue1',
# respectively.

import json
import jwt
import boto3

apigateway_client = boto3.client('apigateway')

def lambda_handler(event, context):
    # Retrieve request parameters from the Lambda function input:
    headers = event['headers']
    # queryStringParameters = event['queryStringParameters']
    # pathParameters = event['pathParameters']
    # stageVariables = event['stageVariables']

    # Parse the input for the parameter values
    tmp = event['methodArn'].split(':')
    apiGatewayArnTmp = tmp[5].split('/')
    awsAccountId = tmp[4]
    region = tmp[3]
    restApiId = apiGatewayArnTmp[0]
    stage = apiGatewayArnTmp[1]
    method = apiGatewayArnTmp[2]
    resource = '/'

    if (apiGatewayArnTmp[3]):
        resource += apiGatewayArnTmp[3]

    # Perform authorization to return the Allow policy for correct parameters
    # and the 'Unauthorized' error, otherwise.

    authResponse = {}
    condition = {}
    condition['IpAddress'] = {}
    id_token = json.dumps(event['headers']['Authorization'])
    try:
        token = id_token.split()[1].strip('"')
        decoded = jwt.decode(token, options={"verify_signature": False})
        groups = decoded['cognito:groups']
        for group in groups:
            if 'Group-' in group:
                # api_key = get_api_key_value(f'ApiKey-{group.split('-')[1]}')
                api_key = get_api_key(f'ApiKey-{group.split('-')[1]}')
                response = generateAllow('me', event['methodArn'], api_key)
                print('authorized')
                return json.loads(response)
            else:
                print('unauthorized')
                response = generateDeny('me', event['methodArn'], api_key)
                return json.loads(response)

    except:
        token = None
        api_key = None
        response = generateDeny('me', event['methodArn'], api_key)
        return json.loads(response)
    

    # Help function to generate IAM policy

def generatePolicy(principalId, effect, resource, api_key):
    authResponse = {}
    authResponse['principalId'] = principalId
    if (effect and resource):
        policyDocument = {}
        policyDocument['Version'] = '2012-10-17'
        policyDocument['Statement'] = []
        statementOne = {}
        statementOne['Action'] = 'execute-api:Invoke'
        statementOne['Effect'] = effect
        statementOne['Resource'] = resource
        policyDocument['Statement'] = [statementOne]
        authResponse['policyDocument'] = policyDocument
        authResponse['usageIdentifierKey'] = api_key


    authResponse_JSON = json.dumps(authResponse)
    print(authResponse_JSON)

    return authResponse_JSON


def generateAllow(principalId, resource, api_key):
    return generatePolicy(principalId, 'Allow', resource, api_key)


def generateDeny(principalId, resource, api_key):
    return generatePolicy(principalId, 'Deny', resource, api_key)


def get_api_key(key_name):
    try:
        response = apigateway_client.get_api_keys(nameQuery=key_name, includeValues=True)
        api_keys = response['items']
        if api_keys:
            return api_keys[0]['value']
        return None
    except ClientError as e:
        print(e)
        return None