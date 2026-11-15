# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import os
import json
import pymysql
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

session = boto3.session.Session()
client = session.client('secretsmanager')

host = os.environ['DB_ENDPOINT']
database = os.environ['DB_NAME']
secret_name = os.environ['SECRET_ARN']

def get_secret():
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = json.loads(get_secret_value_response['SecretString'])
            logger.info(f"value of password: {secret['password']}")
            return secret['username'], secret['password']

def lambda_handler(event, context):
    username, password = get_secret()
    
    try:
        # Attempt database connection
        conn = pymysql.connect(
            host=host,
            user=username,
            password=password,
            database=database,
            connect_timeout=5
        )
        
        # Execute simple test query
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
        
        conn.close()
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Successfully connected to the database',
                'database': database,
                'host': host
            })
        }
        
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Failed to connect to database',
                'error': str(e)
            })
        }
