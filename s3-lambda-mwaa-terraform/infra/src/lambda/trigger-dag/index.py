import os
import boto3
import http.client
import base64
import ast
import logging
import json

# Logger
logger = logging.getLogger()
logger.setLevel(os.environ['LOG_LEVEL'])

# MWAA Environment Name
mwaa_env_name = os.environ['MWAA_ENV_NAME']

# DAG name
dag_id = 'hello-world-dag'

# Command to trigger DAG
mwaa_cli_command = 'dags trigger'

# S3 Client
s3 = boto3.client('s3')

# DynamoDB Client
dynamodb = boto3.client('dynamodb')

# MWAA Client
mwaa = boto3.client('mwaa')

def lambda_handler(event, context):
    """
    Lambda handler method to trigger DAG
    """
    try:
        logger.info(f'Received Event: {json.dumps(event)}')
        paramsList = __generate_dag_params(event)
        logger.debug(f'params: {json.dumps(paramsList)}')
    except Exception as e:
        logger.error(e)
        raise e

    for params in paramsList:
        try:
            __trigger_dag(params)
        except Exception as e:
            ########################
            # RETRY LOGIC GOES HERE
            ########################
            logger.error(e)
            raise e

def __trigger_dag(params):
    # get web token
    mwaa_cli_token = mwaa.create_cli_token(
        Name=mwaa_env_name
    )
    conn = http.client.HTTPSConnection(mwaa_cli_token['WebServerHostname'])
    payload = "{0} {1} --conf '{2}'".format(mwaa_cli_command, dag_id, json.dumps(params))
    logger.info(f'DAG trigger payload: {payload}')
    headers = {
      'Authorization': 'Bearer ' + mwaa_cli_token['CliToken'],
      'Content-Type': 'text/plain'
    }
    conn.request("POST", "/aws_mwaa/cli", payload, headers)
    res = conn.getresponse()
    data = res.read()
    dict_str = data.decode("UTF-8")
    logger.info(f'Response: {dict_str}')
    mydata = ast.literal_eval(dict_str)
    if(mydata['stderr']):
        message = f'Attempt to trigger DAG {dag_id} was unsuccessful. '\
            f'Error received: {base64.b64decode(mydata["stderr"])}'
        raise Exception(message)
    logger.info(f'Success: DAG {dag_id} was triggered successfuly')
    logger.debug(f'Output:{base64.b64decode(mydata["stdout"])}')
    return base64.b64decode(mydata['stdout'])

def __generate_dag_params(event):
    return __process_s3_event(event)

def __process_s3_event(event):
    s3ObjList = []
    if 'Records' in event and len(event['Records']) > 0:
        for record in event['Records']:
            s3ObjList.append(
                {
                    's3SourceBucket': record['s3']['bucket']['name'],
                    's3SourceBucketKey': record['s3']['object']['key']
                }
            )
    return s3ObjList
